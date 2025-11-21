# 請用 Python 寫一個 safe_division(a, b) 函式，能防止除以零，並將程式碼上傳至 GitHub
def safe_division(a, b):
    try:
        result = a / b
    except ZeroDivisionError:
        return "Error: Division by zero is not allowed."
    return result
# 範例使用
print(safe_division(10, 2))  # 輸出: 5.0
print(safe_division(10, 0))  # 輸出: Error: Division by zero is not allowed.
print(safe_division(10, 3))  # 輸出: 3.3333333333333335
print(safe_division(10, 10))    # 輸出: 1.0
print(safe_division(10, 1)) # 輸出: 10.0