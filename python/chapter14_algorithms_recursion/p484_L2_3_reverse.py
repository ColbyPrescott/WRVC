def reverse(str):
    if str == "":
        return str
    return reverse(str[1:]) + str[0]