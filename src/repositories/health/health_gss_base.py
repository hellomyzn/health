# src/repositories/health/health_gss_base.py

import datetime
import time
import gspread
from repositories.gss_base import GSSBase
from common.config import Config
from common.log import info, warn, debug

CONFIG = Config().config


def get_spreadsheet_key_by_year(year: int) -> str:
    """
    設定ファイルの GSS セクションから、年ごとの Spreadsheet Key を取得する。
    例:
        [GSS]
        DEFAULT_SHEET_KEY = <default_key>
        SHEET_KEY_2025 = <2025用のキー>
        SHEET_KEY_2026 = <2026用のキー>
    該当するキーが存在しない場合は、UNKNOWN_KEY（またはデフォルトキー）を返す。
    """
    return CONFIG["GSS"].get(f"SHEET_KEY_{year}", CONFIG["GSS"]["UNKNOWN_KEY"])


class HealthGssBase(GSSBase):
    """
    Health 用の Google Spreadsheet リポジトリのベースクラス

    渡されたレコードデータは list[Model, ] 型で、各 Model オブジェクトの
    "start_date" フィールドに基づいて年ごとにグループ化し、対応する Spreadsheet
    に対して、複数行を一括で追加します。

    子クラスでは、BASE_SHEET_NAME、header、adapter（および必要に応じて model_cls）
    などを設定してください。
    """
    # Spreadsheet 内のシート名（例："BodyMass" など）
    BASE_SHEET_NAME = "default"

    def add(self, data: list) -> None:
        """
        複数の Model オブジェクトからデータをまとめ、年ごとに対応する Spreadsheet に
        一括して複数行を追加する。

        Args:
            data (list[Model, ]): 追加するデータのリスト。各 Model は to_dict() で辞書変換可能。
                                  なお、変換は adapter の from_model_to_list() を用います。
        """
        # 年ごとに Model オブジェクトをグループ化
        records_by_year = {}
        for model in data:
            record = model.to_dict(without_none_field=True)
            start_date = record.get("start_date")
            if isinstance(start_date, str):
                try:
                    dt = datetime.datetime.strptime(start_date, "%Y-%m-%d %H:%M:%S %z")
                    year = dt.year
                except Exception:
                    warn("Invalid start_date format: {}. Using 'unknown'", start_date)
                    year = "unknown"
            elif isinstance(start_date, datetime.datetime):
                year = start_date.year
            else:
                year = "unknown"
            records_by_year.setdefault(year, []).append(model)

        # 年ごとにSpreadsheetへ一括追加
        for year, models in records_by_year.items():
            sheet_key = get_spreadsheet_key_by_year(year)
            sheet_name = self.sheet_name

            # 指定された Spreadsheet に接続
            self.update_spreadsheet(sheet_key, sheet_name)

            # 各 Model を adapter を使ってリスト形式に変換
            rows = []
            # id 列がある場合、取得しておく（header の先頭に "id" がある前提）
            if "id" in self.columns:
                id_index = self.columns.index("id")
                next_id = self.__get_next_id()
            for model in models:
                row = self.adapter.from_model_to_list(model)
                # id 列が空なら次の id をセット
                if "id" in self.columns:
                    if not row[id_index]:
                        row[id_index] = next_id
                        next_id += 1
                rows.append(row)

            row_num = self.__find_next_available_row()
            try:
                debug("Inserting {} rows at row {} for year {}: {}", len(rows), row_num, year, rows)
                # 複数行（リストのリスト）を一括で挿入
                self.worksheet.insert_rows(rows, row_num)
            except gspread.exceptions.APIError as exc:
                err_status = exc.response.json()["error"]["status"]
                is_sheet_size_err = (err_status == "INVALID_ARGUMENT")
                is_request_limit = (err_status == "RESOURCE_EXHAUSTED")
                if is_sheet_size_err:
                    warn("Sheet size is not enough for year {}. {}: {}", year, exc.__class__.__name__, exc)
                    rows_to_add = 1000
                    self.worksheet.add_rows(rows_to_add)
                    info("Added {} rows to sheet {} for year {}", rows_to_add, sheet_name, year)
                    raise exc
                if is_request_limit:
                    warn("Request quota exceeded for year {}. {}: {}", year, exc.__class__.__name__, exc)
                    raise exc
                warn("Gspread API error for year {}: {}: {}", year, exc.__class__.__name__, exc)
                raise exc
            info("Added {} rows to spreadsheet (key: {}) at row {} for year {}", len(rows), sheet_key, row_num, year)

    def update_spreadsheet(self, sheet_key: str, sheet_name: str):
        """
        指定された Spreadsheet キーで Spreadsheet を開き、指定のシート名に接続する。
        ヘッダーのチェックは初回のみ実施します（_columns_checked フラグで管理）。

        Args:
            sheet_key (str): Spreadsheet のキー
            sheet_name (str): Spreadsheet 内のシート名
        """
        workbook = self.gss.connection.open_by_key(sheet_key)
        try:
            self.worksheet = workbook.worksheet(sheet_name)
        except gspread.exceptions.WorksheetNotFound as exp:
            warn("Sheet '{}' not found in spreadsheet with key: {}", sheet_name, sheet_key)
            raise exp

        if not getattr(self, "_columns_checked", False):
            if not self.__has_columns():
                self.__write_columns()
            self._columns_checked = True

    def __find_next_available_row(self) -> int:
        first_column_data = list(filter(None, self.worksheet.col_values(1)))
        time.sleep(1)
        return len(first_column_data) + 1

    def __has_columns(self) -> bool:
        columns = self.worksheet.row_values(1)
        time.sleep(1)
        return bool(columns == self.columns)

    def __write_columns(self) -> None:
        self.worksheet.insert_row(self.columns, index=1)
        info("Added columns in spreadsheet (sheet: {}). Columns: {}", self.sheet_name, self.columns)
        time.sleep(1)

    def __get_next_id(self) -> int:
        """
        シートの 1 列目（"id" 列）のデータを取得し、最新の id の次の番号を返す。
        ヘッダー行は除外する。
        """
        values = self.worksheet.col_values(1)
        # ヘッダーのみの場合は 1 を返す
        if len(values) <= 1:
            return 1
        int_values = []
        # 2 行目以降の値を数値に変換
        for val in values[1:]:
            try:
                int_values.append(int(val))
            except ValueError:
                continue
        if int_values:
            return max(int_values) + 1
        return 1
