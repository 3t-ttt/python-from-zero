"""
    Yêu cầu người dùng nhập vào 1 số tự nhiên n bất kì
    Tạo ra 1 dictionary với key lần lượt là các số từ
    0 đến n, và value là bình phương của key
"""

n = int(input("Enter a number: "))
result = {}
for key in range(n+1):
    result[key] = key**2
print(result)