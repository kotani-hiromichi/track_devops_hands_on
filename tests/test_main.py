import sys
from pathlib import Path

# src ディレクトリをパスに追加
sys.path.insert(0, str(Path(__file__).parent.parent / "src"))

from main import add


def test_add_integers():
    """整数の加算をテスト"""
    assert add(2, 3) == 5


def test_add_floats():
    """浮動小数点数の加算をテスト（整数に変換）"""
    assert add(1.2, 3.5) == 4
