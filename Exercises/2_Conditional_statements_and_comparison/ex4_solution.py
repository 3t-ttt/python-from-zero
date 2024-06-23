"""
    Quy đổi điểm từ thang điểm 100 sang thang điểm chữ theo quy tắc:
        Điểm                             Quy đổi
        > 90                                A
        > 80 và <=90                        B
        > 60 và <= 80                       C
        <= 60                               D
"""
score = int(input("Enter a score: "))
if score > 90:
    grade = "A"
elif score > 80:
    grade = "B"
elif score > 60:
    grade = "C"
else:
    grade = "D"
print("Grade:", grade)