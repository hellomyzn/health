# src/repositories/health/health_csv_base.py

import os
import csv
from repositories.csv_base import CsvBase
from common.log import info
from utils.datetime_parser import DatetimeParser


class HealthCsvBase(CsvBase):
    """
    Health 用の CSV リポジトリのベースクラス

    渡されたレコードデータ（dict）から startDate を元に年別のディレクトリを作成し、
    その年ごとのCSVファイル（FILE_NAME）に追記する。
    子クラスでは FILE_NAME や header, adapter を設定する。
    """
    BASE_PATH = "/opt/work/src/csv/health"
    FILE_NAME = "default.csv"  # 子クラスで上書きする

    def add(self, data: list) -> None:
        """
        data は辞書形式で、少なくとも "startDate" キー（"%Y-%m-%d %H:%M:%S %z"形式の文字列）を持つものとする。
        その年のディレクトリに CSV を追記する。
        """

        records_by_year = {}
        for model in data:
            start_date = model.start_date
            year = DatetimeParser.extract_year(start_date)
            records_by_year.setdefault(year, []).append(model)

        for year, models in records_by_year.items():
            # 年別ディレクトリを作成
            directory = os.path.join(self.BASE_PATH, str(year))
            os.makedirs(directory, exist_ok=True)
            self.path = os.path.join(directory, self.FILE_NAME)

            all_data = self.all()
            if len(all_data) <= 1:
                next_id = 1
            else:
                next_id = int(all_data[-1]["id"]) + 1
                if next_id == "":
                    raise Exception("previous data's id is empty")

            with open(file=self.path, mode="a", encoding="utf-8", newline="") as f:
                writer = csv.DictWriter(f, fieldnames=self.header)
                for model in models:
                    model.id = next_id
                    dict_ = self.adapter.from_model(model)
                    writer.writerow(dict_)
                    next_id += 1

        info("Added data to CSV file: {0}", self.path)
