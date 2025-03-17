# src/repositories/health/health_csv_base.py

import os
import csv
import datetime
from repositories.csv_base import CsvBase
from common.log import info


class HealthCsvBase(CsvBase):
    """
    Health 用の CSV リポジトリのベースクラス

    渡されたレコードデータ（dict）から startDate を元に年別のディレクトリを作成し、
    その年ごとのCSVファイル（FILE_NAME）に追記する。
    子クラスでは FILE_NAME や header, adapter を設定する。
    """
    BASE_PATH = "/opt/work/src/csv/health"
    FILE_NAME = "default.csv"  # 子クラスで上書きする

    def add(self, data: dict) -> None:
        """
        data は辞書形式で、少なくとも "startDate" キー（"%Y-%m-%d %H:%M:%S %z"形式の文字列）を持つものとする。
        その年のディレクトリに CSV を追記する。
        """
        start_date_str = data.get("startDate")
        if start_date_str:
            try:
                dt = datetime.datetime.strptime(start_date_str, "%Y-%m-%d %H:%M:%S %z")
                year = dt.year
            except Exception:
                year = "unknown"
        else:
            year = "unknown"

        # 年別ディレクトリを作成
        directory = os.path.join(self.BASE_PATH, str(year))
        os.makedirs(directory, exist_ok=True)
        file_path = os.path.join(directory, self.FILE_NAME)

        file_exists = os.path.isfile(file_path)
        with open(file_path, mode="a", encoding="utf-8", newline="") as f:
            writer = csv.DictWriter(f, fieldnames=self.header)
            if not file_exists:
                writer.writeheader()
            writer.writerow(data)

        info("Added data to CSV file: {0}", file_path)
