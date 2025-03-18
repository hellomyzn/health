import abc


class SingletonMeta(abc.ABCMeta):
    """シングルトン用メタクラス。
    このメタクラスを利用することで、対象クラスは常に1つのインスタンスのみ生成される。
    """

    def __init__(cls, name, bases, dict_):
        """
        メタクラスの初期化メソッド。

        Args:
            cls: 対象となるクラス自身
            name (str): クラス名
            bases (tuple): クラスの基底クラスのタプル
            dict_ (dict): クラス定義に含まれる属性やメソッドの辞書

        処理内容:
            - この段階で、クラスごとに _instance 属性を None に初期化する。
              これにより、まだインスタンスが生成されていない状態を示す。
        """
        cls._instance = None  # 各クラスごとにシングルトンインスタンスの格納先を準備
        super().__init__(name, bases, dict_)

    def __call__(cls, *args, **kwargs):
        """
        クラスのインスタンス生成時に呼び出されるメソッド。

        Args:
            *args: コンストラクタに渡される位置引数
            **kwargs: コンストラクタに渡されるキーワード引数

        処理内容:
            - もしまだインスタンスが生成されていなければ、super().__call__(*args, **kwargs)
              を呼び出して新たなインスタンスを生成し、それを cls._instance に保持する。
            - すでにインスタンスが存在する場合は、既存のインスタンスを返す。
            - これにより、複数回呼ばれても同じインスタンスが再利用され、__init__ の再実行も防げる。
        """
        if cls._instance is None:
            cls._instance = super().__call__(*args, **kwargs)
        return cls._instance
