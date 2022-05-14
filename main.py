# print("Hello world")
# x = 3
# y = 4
# if x < y:
#     print("Hello")
# for i in range(0, 101, 10):
#     print(i)
# for i in range(50, -1, -1):
#     print(i)
# -------------------------------------------------
# from PTL import Image, ImageFilter

# before = Image.open("123.jpg")
# after = before.filter(ImageFilter.BoxBlur(1))
# after.save("out.jpg")
# ------------------------------------------------------
# answer = input("Name?")
# print(f"hello,{answer}")
# -----------------------------------------------------
# import cs50
# from cs50 import get_int
# x=get_int("x: ")
# y=get_int("y: ")
# ----------------------------------------------------------
# x = int(input("x:"))
# y = int(input("y:"))
# # print(x + y)
# # print(x / y)
# if x < y:
#     print("x меньше y")
# elif x > y:
#     print("y меньше x")
# else:
#     print("y = x")
# ---------------------------------------------------------
# import cs50

# s = cs50.get_string("Вы согласны?")
# if s == "Да" or s == "да":
#     print("Вы согласны")
# elif s == "Нет" or s == "нет":
#     print("не согласны")
# -----------------------------------------------------------

# def meow():
#     print("meow")

# for i in range(3):
#   meow()
# --------------------------------------------------------
# def main():
#     meow(3)

# def meow(n):
#     for i in range(n):
#         print("meow")

# main()
# -------------------------------------------------------------
# from cs50 import get_int

# def main():
#     i = get_positive_int()
#     print(i)

# def get_positive_int():
#     while True:
#         n = get_int("positive_int :")
#         if n > 0:
#             break
#     return n

# main()
# -----------------------------------------------------------------
# for i in range(3):
#    # print("?", end="")
#     print("?"*2)
# print()
# -----------------------------------------------------------------
# for i in range(5):
#   for j in range(31):
#     print("?", end="")
#   print()
# --------------------------------------------------------------------
# scores = {72, 73, 33}

# print("Average: " + str(sum(scores) / len(scores)))
# print(f"Average:{sum(scores)/len(scores)}")
# --------------------------------------------------------------------
# scores = []
# for i in range(3):
#     scores.append(int(input("Score: ")))

# print(scores)
# --------------------------------------------------------------------
# s=input("Before: ")
# print("After: ",end="")
# for c in s:
#   print(c.upper(),end="")
# print()
# --------------------------------------------------------------------
# s = input("Before: ")
# s = s.upper()
# print("After: " + s)
# --------------------------------------------------------------------
# import sys

# if len(sys.argv) != 2:
#     print("отсутствует")
#     sys.exit(1)

# print("helllo," + sys.argv[1])
# sys.exit(0)
# --------------------------------------------------------------------
# import sys

# number = [4, 6, 8, 6, 8, 10, 3]

# if 0 in number:
#     print("found")
#     sys.exit(0)

# print("not found")
# sys.exit(1)
# --------------------------------------------------------------------
# import sys

# names = ["qwe", "asd", "zxc", "rfv", "tgb", "yhn", "ikm"]

# if "rqwe" in names:
#     print("found")
#     sys.exit(0)

# print("not found")
# sys.exit(1)
# --------------------------------------------------------------------
# set
# import sys

# people = {
#     "Harry": "+324234234234",
#     "Tom": "+3424234234234",
#     "Vasek": "+312312323123",
#     "Petr": "+312424234233",
#     "Sem": "+31242424234343"
# }
# name=input("Name: ")
# if name in people:
#   print("Number: "+people[name])
# --------------------------------------------------------------------
x=1
y=2
