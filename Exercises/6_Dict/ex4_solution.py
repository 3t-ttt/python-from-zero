"""
    Viết chương trình kết hợp 2 dictionary vào làm 1.
    Nếu key xuất hiện ở cả 2 dictionary thì cộng 2 value
    tương ứng lại
"""

dict1 = {'a': 100, 'b': 200, 'c': 300}
dict2 = {'a': 300, 'b': 200, 'd': 400}

# for key, value in dict1.items():
#     if key in dict2.keys():
#         dict2[key] += value
#     else:
#         dict2[key] = value
# print(dict2)

for key in dict2:
    if key in dict1:
        dict1[key] += dict2[key]
    else:
        dict1[key] = dict2[key]
print(dict1)


