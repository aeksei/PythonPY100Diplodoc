src = not True or (True and not True)
# result = not True or (True and not True)
# result = not True or (True and False)
# result = not True or False
# result = False or False
result = False

print(src == result)
