"""
    A.
    Viết hàm is_member() nhận 2 tham số đầu vào:
    1. 1 giá trị (số, chuỗi ký tự, bool, ...)
    2. 1 List chứa các giá trị bất kì
    Hàm kiểm tra xem giá trị có xuất hiện trong List hay không
    (Không dùng toán tử in)

    B.
    Viết hàm overlapping() nhận 2 tham số đầu vào là 2 List
    Hàm trả về danh sách các phần tử nằm ở cả 2 List
    Gợi ý: Sử dụng hàm is_member()
"""
#A
def is_member(value, list_of_values):
    for item in list_of_values:
        if item == value:
            return True
    return False

#B
def overlapping(list_1, list_2):
    overlapping_list = []
    for item in list_1:
        if is_member(item, list_2) is True:
            overlapping_list.append(item)
    return overlapping_list

print(is_member("monday", ["rose", 5, True, "monday", "tuesday", -5.5]))
print(overlapping(["rose", 5, True, "monday"], ["rose", 5, False, "monday", "tuesday", -5.5]))
