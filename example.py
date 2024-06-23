# print("please input your name: ")
# name = input()
# print("name: ", name)
# print("type of input: ", type(name))


#===================================================================#
"""
    Yêu cầu người dùng nhập vào 1 số nguyên tương ứng với số giờ
    In ra số giây tương ứng
"""
# hours = int(input("Enter the hours: "))
# seconds = hours * 3600
# print(hours, "hours = ", seconds, "seconds")


#===================================================================#
"""
    Yêu cầu người dùng nhập vào 1 số nguyên n
    Tính và in ra tổng số đo các góc của đa giác đều n cạnh
"""
# n = int(input("Enter a positive integer n: "))

# # Check if n is a positive integer and n >= 3
# if n <= 2:
#     print("A polygon must have at least 3 sides.")
# else:
#     sum_of_angles = (n - 2) * 180
#     print(f"The sum of the interior angles of a regular {n}-sided polygon is {sum_of_angles} degrees.")


#===================================================================#
"""
    Nhập vào số giây bất kỳ t (t là số nguyên dương bất kỳ)
    In ra màn hình thời gian tương ứng trong ngày dưới dạng
    hh : mm : ss
"""
# t = int(input("Enter the seconds: "))
# hours = t // 3600
# minutes = ( t % 3600 ) // 60
# seconds = t % 60
# print(hours,":", minutes,":", seconds)


#===================================================================#
"""
    Yêu cầu người dùng nhập vào 1 số tự nhiên lớn hơn 1
    1. Kiểm tra xem đó có phải là số nguyên tố hay không
    2. In ra màn hình tất cả các số nguyên tố nhỏ hơn hoặc bằng n
"""
# n = int(input("Enter a number: "))
# for m in range(2, n + 1):
#     for i in range(2, int(m ** 0.5 + 1)):
#         if m % i == 0:
#             print(m, "is a composite number")
#             break
#     else:
#         print(m, "is a prime number")


#===================================================================#
"""
    Yêu cầu người dùng nhập vào 1 số tự nhiên n khác 0
    In ra n số Fibonacci đầu tiên
    Định nghĩa dãy Fibonacci: Dãy Fibonacci bắt đầu với 2 số 1
    Các số sau được xác định bẳng tồng của 2 số ngay trước nó.
    1 vài số Fibonacci đầu tiên trong dãy: 1, 1, 2, 3, 5, 8
"""
# num = int(input("Enter a number: "))
# n1, n2 = 1, 1
# count = 0
# while count < num:
#     print(n1)
#     new_n = n1 + n2
#     n1 = n2
#     n2 = new_n
#     count += 1


#===================================================================#
"""
    Yêu cầu người dùng nhập vào 1 số tự nhiên n khác 0
    In ra tất cả các số Armstrong nhỏ hơn hoặc bằng n
    Định nghĩa số Armstrong: 1 số n được gọi là số Armstrong nếu:
    Tổng các chữ số của số đó, với mỗi chữ số được lũy thừa với
    số mũ k bằng chính số đó, với k là số chữ số của n
    Ví dụ: 153 là số Amstrong vì:
    153 có 3 chữ số, và 153 = 1^3 + 5^3 + 3^3
"""

# n = input("Enter a number: ") # n is a string
# k = len(n)
# sum = 0
# for digit in n:               # digit is a string
#     sum += int(digit)**k      # digit must be a number
# if sum == int(n):             # n must be a number to compare
#     print(n, "is an Amstrong number")
# else:
#     print(n, "is not an Amstrong number")


#===================================================================#
"""
    Viết hàm tính và trả về khoảng cách giữa 2 điểm:
    - A(xa, ya, za)
    - B(xb, yb, zb)
    trong không gian 3 chiều
"""

from math import sqrt

# Method 1
def calculate_distance_1(a, b):
    distance = 0
    xa, ya, za = a
    xb, yb, zb = b
    distance = sqrt((xa-xb)**2 + (ya-yb)**2 + (za-zb)**2 )
    return distance



# Method 2
def calculate_distance_2(a, b):
    distance = 0
    for i in range(len(a)):
        distance += (a[i] - b[i]) ** 2
    distance = sqrt(distance)
    return distance

# Method 3
def calculate_distance(a, b):
    distance = 0
    for i, j in zip(a, b):
        distance += (i - j) ** 2
    distance = sqrt(distance)
    return distance

a = (1, 3, 6)
b = (2, 1, 3)

print("Distance_1 between 2 points is:", calculate_distance_1(a, b))

print("Distance_2 between 2 points is:", calculate_distance_2(a, b))

print("Distance_0 between 2 points is:", calculate_distance(a, b))