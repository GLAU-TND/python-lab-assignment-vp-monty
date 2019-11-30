try:
    x = int(input())# if enter 0-9 number then no Exception generated but if not this so it show Exception
except Exception as e:
    print("ValueError",e)
try:
    x = 10
    y =input()
    z = x + y
    print(z)
except TypeError as e:
    print(e)

try:
    x = 10
    print(x.count)
except AttributeError as e:
    print(e)
