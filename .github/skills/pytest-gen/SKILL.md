---
name: pytest-gen
description: 生成全面的 pytest 測試 - 適用於生成測試、建立測試套件或測試 Python 程式碼
---

# Pytest 生成技能

生成測試時，請遵循以下結構。

## 測試組織

- 依受測函式分組測試
- 多組輸入使用 `@pytest.mark.parametrize`
- 共用設置使用 fixtures
- 遵循 arrange/act/assert（安排／執行／斷言）模式

## 涵蓋需求

- 正常路徑（預期用法）
- 邊界情況（空字串、None、邊界值）
- 錯誤情況（無效輸入、找不到檔案、錯誤型別）
- 整合測試（函式協同運作）

## 範本

```python
import pytest
from module_under_test import function_to_test


@pytest.fixture
def sample_data():
    """Provide shared test data."""
    return {"key": "value"}


class TestFunctionName:
    """Tests for function_name."""

    def test_happy_path(self, sample_data):
        result = function_to_test(valid_input)
        assert result == expected_output

    def test_empty_input(self):
        result = function_to_test("")
        assert result == expected_for_empty

    @pytest.mark.parametrize("input_val,expected", [
        ("valid", True),
        ("", False),
        (None, False),
    ])
    def test_various_inputs(self, input_val, expected):
        assert function_to_test(input_val) == expected
```
