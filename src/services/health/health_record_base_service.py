from abc import ABC, abstractmethod


class HealthRecordBaseService(ABC):
    """
    HealthRecord 用の共通処理をまとめたサービスのベースクラス

    Attributes:
        model_cls: 対応するモデルクラス（from_dict メソッドを持つ）
        gss_repo: Google Sheets 用のリポジトリ
        csv_repo: CSV 用のリポジトリ
    """

    def __init__(self, model_cls, gss_repo, csv_repo):
        self.model_cls = model_cls
        self.gss_repo = gss_repo
        self.csv_repo = csv_repo

    def process(self, records: list[dict]):
        """
        複数のレコード（辞書のリスト）を処理して、モデル化し、
        Google Sheets と CSV に保存する共通の処理

        Args:
            records (list[dict]): 各レコードの属性情報が入った辞書のリスト
        """
        # 各辞書からモデルインスタンスを生成
        model_instances = [self.model_cls.from_dict(data) for data in records]

        # 例：Google Sheets に一括で保存
        self.gss_repo.add(model_instances)

        # CSV への保存は、各レコードごとに行う（リポジトリ側でバッチ処理に変更することも可能）
        for instance in model_instances:
            self.csv_repo.add(instance.to_dict(without_none_field=True))
