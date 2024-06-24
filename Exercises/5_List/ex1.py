"""
    Viết 1 hàm nhận 2 tham số đầu vào:
    1. 1 list bao gồm các số bất kì
    2. 1 số tự nhiên k
    Trả về kết quả là 1 list, trong đó các phần tử bị dịch sang trái k đơn vị
    Ví dụ:
    Input:
        array = [1, 2, 3, 4, 5]
        k = 2
    Output:
        array = [3, 4, 5, 1, 2]
"""


def shift_array(array, k):
    shift_array = array[k:] + array[:k] # Shift the list
    return shift_array

print(shift_array([1, 2, 3, 4, 5], 1))
