from setuptools import setup
from setuptools import find_packages

setup(
    name="regex_generator",  # パッケージ名（pip listで表示される）
    version="0.0.1",  # バージョン
    description="sample of minimum package",  # 説明
    author="tw",  # 作者名
    packages=find_packages(),  # 使うモジュール一覧を指定する
    license="MIT",  # ライセンス
)
