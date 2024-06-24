"""
    Viết hàm nhận 1 tham số đầu vào là 1 số tự nhiên n
    In ra kết quả là tích các thừa số nguyên tố của số đó
    Ví dụ, với n = 100
    Kết quả in ra màn hình là:
        100 = 2 x 2 x 5 x 5
"""


def get_string(n):
    factors = []
    # start from min prime number
    divisor = 2

    while n > 1:
        while n % divisor == 0:
            factors.append(divisor)
            n //= divisor
        divisor += 1

    factors_str = ' x '.join(map(str, factors))
    print(f"{original_n} = {factors_str}")

original_n = int(input("Please enter a natural number: "))
get_string(original_n)
