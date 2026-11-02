"""冒烟测试：确认包可导入、版本号存在。"""

import contest_team


def test_package_importable() -> None:
    assert contest_team.__version__ == "0.1.0"