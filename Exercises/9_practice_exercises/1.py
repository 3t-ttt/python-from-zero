"""
Yêu cầu người dùng nhập vào 1 số nguyên dương.
Viết 1 hàm nhận tham số đầu vào là 1 số nguyên dương.
Hàm này trả về hiệu số giữa số lớn nhất và số nhỏ nhất có thể tạo thành từ các chữ số của tham số đầu vào
Ví dụ, nếu tham số đầu vào là 314, thì giá trị trả về của hàm số là 297, vì 297 = 431 - 134
"""

# def max_difference(number):
#     digits = list(number)
#     max_number = int(''.join(sorted(digits, reverse=True)))
#     min_number = int(''.join(sorted(digits)))
#     print(min_number)
#     print(max_number)
#     return max_number - min_number

# # Example usage:
# input_number = input("Enter a positive integer: ")
# result = max_difference(input_number)
# print(f"The difference is: {result}")

######################################################################################
"""
    Pascal's triangle
    Yêu cầu người dùng nhập vào 1 số nguyên dương n.
    Viết 1 hàm nhận tham số đầu vào là số nguyên dương n.
    Hàm này tạo ra tam giác pascal cho tới hàng thứ n
    Ví dụ nếu n = 4 thì hàm sẽ in ra kết quả sau:
        1
        1 1
        1 2 1
        1 3 3 1
        1 4 6 4 1
    
    """
    
# def generate_pascals_triangle(num_rows):
#     triangle = []

#     for i in range(num_rows + 1):
#         row = [1] * (i + 1)
#         for j in range(1, i):
#             row[j] = triangle[i - 1][j - 1] + triangle[i - 1][j]
#         triangle.append(row)
#         print(row)
#     return triangle


# n = int(input("Enter a positive integer n: "))
# pascals_triangle = generate_pascals_triangle(n)


######################################################################################
"""
Viết 1 hàm nhận dãy số này là tham số đầu vào, và trả lại giá trị bị khuyết

"""

# def find_missing_value(array):
#     input_sum = sum(array)
#     n = len(array) + 1
#     full_sum = n * (n + 1) // 2
#     return full_sum - input_sum

# array = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 12, 13, 14, 15, 16]
# missing_value = find_missing_value(array)
# print(missing_value)

######################################################################################
"""
    Viết 1 hàm kiểm tra xem 1 mảng 2 chiều (nested list) có phải là magic square (ma phương) hay không?
    Hàm nhận tham số đầu vào là 1 nested List, và trả về True nếu đó là ma phương, hoặc False nếu không phải
    Định nghĩa:
        một ma trận kì ảo bậc n (còn gọi là ma phương) là một cách sắp xếp n→ số, là các số nguyên phân biệt,
        trong một bảng vuông sao cho tổng n số trên mỗi hàng, cột, và đường chéo đều bằng nhau.
    
"""

def is_magic_square(matrix):
    n = len(matrix)
    sum = 0
    for i in range(n**2 + 1):
        sum += i
    sum //= n
    
    #check sum of each row
    for row in range(n):
        if sum(matrix[row]) != sum:
            return False
    
    #check sum of each column
    for col in range(n):
        col_sum = 0
        for row in range(n):
            col_sum += matrix[row][col]
        if col_sum != sum:
            return False
            
    # Check diagonals
    if sum(matrix[i][i] for i in range(n)) != sum:  # Check main diagonal
        return False
    if sum(matrix[i][n-1-i] for i in range(n)) != sum:  # Check secondary diagonal
        return False

    # Check if all numbers are unique and in the range 1 to n^2
    unique_numbers = {num for row in matrix for num in row}
    if unique_numbers != set(range(1, n*n + 1)):
        return False

    return True

# Test case
matrix = [
    [2, 7, 6],
    [9, 5, 1],
    [4, 3, 8]
]
print(is_magic_square(matrix))  # Output: True

