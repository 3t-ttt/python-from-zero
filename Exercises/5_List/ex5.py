"""
    Yêu cầu người dùng nhập vào 1 số nguyên dương
    Kiểm tra xem số đó có phải là 1 số may mắn hay không

    Số may mắn là số được định nghĩa theo quá trình sau: bắt đầu với số nguyên dương x
    và tính tổng bình phương y các chữ số của x, sau đó tiếp tục tính tổng bình phương
    các chữ số của y. Quá trình này lặp đi lặp lại cho đến khi thu được kết quả là 1
    thì dừng (tổng bình phương các chữ số của số 1 chính là 1) hoặc quá trình sẽ kéo dài vô tận.
    Số mà quá trình tính này kết thúc bằng 1 gọi là số may mắn.
    Số có quá trình tính kéo dài vô tận là số không may mắn hay còn gọi là số đen đủi
    Ví dụ: 19 là số may mắn vì
    1^2 + 9^2 = 82
    8^2 + 2^2 = 68
    6^2 + 8^2 = 100
    1^2 + 0^2 + 0^2 = 1 (End)

    Some happy numbers are: 1, 7, 13, 19, 23, 28, 44, 49, 68, 79, 129, 133, 139, 167, 188, 226, 236, 239, 338, 
    356, 367, 368, 379, 446, 469, 478, 556, 566, 888, 899
"""

def is_happy_number(n):
    # Function to calculate the sum of squares of digits of a number
    def sum_of_squares(num):
        return sum(int(digit) ** 2 for digit in str(num))

    # Initialize an empty set to keep track of seen numbers
    seen_numbers = set()

    original_number = n  # Store the original number for the final output message

    while n != 1 and n not in seen_numbers:
        # Add the current number to the set of seen numbers
        seen_numbers.add(n)
        # Update n to be the sum of the squares of its digits
        n = sum_of_squares(n)

    # Check the final value of n to determine if it's a happy number
    if n == 1:
        return f"{original_number} is a happy number"
    else:
        return f"{original_number} is an unhappy number"

# Example usage
user_input = int(input("Please enter a positive integer: "))
print(is_happy_number(user_input))

