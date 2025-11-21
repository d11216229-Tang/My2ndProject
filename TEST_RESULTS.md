# Safe Division 單元測試結果

## 專案說明
此專案實作了一個 `safe_division(a, b)` 函式，能夠安全地進行除法運算並防止除以零的錯誤。

## 檔案結構
- `safe_division.py` - 包含 safe_division 函式的主要模組
- `test_safe_division.py` - 完整的單元測試套件
- `safe_division_test.py` - 原始的範例檔案（保留作為參考）

## 測試結果

### 綠燈場景（測試通過）✅

當 `safe_division` 函式正確處理除以零的情況時：

**程式碼狀態：**
```python
except ZeroDivisionError:
    return "Error: Division by zero is not allowed."
```

**測試執行結果：**
```
test_boundary_values ... ok
test_division_by_one ... ok
test_division_by_same_number ... ok
test_division_by_zero ... ok
test_division_with_result_fraction ... ok
test_negative_division ... ok
test_normal_division ... ok
test_zero_divided_by_number ... ok

----------------------------------------------------------------------
Ran 8 tests in 0.000s

OK
```

✅ **所有 8 個測試案例都通過**，包括：
- 正常的數值相除
- 負數相除
- 邊界值相除
- 除以零的處理

### 紅燈場景（測試失敗）❌

當「處理除以零」的程式碼被註解掉後：

**程式碼狀態：**
```python
except ZeroDivisionError:
    # return "Error: Division by zero is not allowed."
    pass
```

**測試執行結果：**
```
test_boundary_values ... ok
test_division_by_one ... ok
test_division_by_same_number ... ok
test_division_by_zero ... ERROR
test_division_with_result_fraction ... ok
test_negative_division ... ok
test_normal_division ... ok
test_zero_divided_by_number ... ok

======================================================================
ERROR: test_division_by_zero
----------------------------------------------------------------------
Traceback (most recent call last):
  File "test_safe_division.py", line 36, in test_division_by_zero
    result = safe_division(10, 0)
UnboundLocalError: cannot access local variable 'result' where it is not associated with a value

----------------------------------------------------------------------
Ran 8 tests in 0.001s

FAILED (errors=1)
```

❌ **測試失敗**：針對除以零的單元測試出現錯誤，因為程式無法妥善處理 ZeroDivisionError。

## 結論

此測試驗證了：
1. **綠燈**：當 safe_division 函式正確實作除以零的例外處理時，所有測試都能通過
2. **紅燈**：當移除例外處理的程式碼後，針對除以零的測試會失敗，證明該處理機制是必要的

這展示了單元測試在確保程式碼品質和功能正確性方面的重要性。
