def factoral(num):
    if num == 1:
        return 1
    else:
        return num * factoral(num - 1)


print(factoral(3))
