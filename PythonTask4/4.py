def function(str1):
    str1 = str1.split('-')
    str2 = list(str1)
    str2.sort()
    s = '-'.join(str2)
    return s

print(function("a-b-c-d-y-e-r-d-g"))