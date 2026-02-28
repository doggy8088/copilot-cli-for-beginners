---
name: pytest-gen
description: Generate comprehensive pytest tests - use when generating tests, creating test suites, or testing Python code
---

# Pytest 測試產生技能

產生測試時，請遵循以下結構。

## 測試組織方式

- 依受測函式分組
- 多組輸入情境使用 `@pytest.mark.parametrize`
- 共用前置設定使用 fixtures
- 遵循「安排／執行／驗證（arrange/act/assert）」模式

## 覆蓋率要求

- 正常路徑（預期使用方式）
- 邊界情境（空字串、None、臨界值）
- 錯誤情境（無效輸入、找不到檔案、型別錯誤）
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
