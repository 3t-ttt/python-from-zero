"""
    Yêu cầu người dùng nhập vào lượng nước tiêu thụ của 1 hộ gia đình
    Viết chương trình tính hóa đơn tiền nước cho gia đình đó,
    với quy tắc sau:
    Lượng nước (lít)                    Giá mỗi 1000 lít
    0-8000                                  5$
    8001-22000                              6$
    22001-30000                             7$
    30001+                                  10$
"""
liters = int(input("Enter volume of consumed water (liters): "))
if liters <= 8000:
    bill = 5 * liters / 1000
elif liters <= 22000:
    bill = 6 * liters / 1000
elif liters <= 30000:
    bill = 7 * liters / 1000
else:
    bill = 10 * liters / 1000
print("Amount to pay:", bill, "$")
