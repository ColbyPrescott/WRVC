i = 0
while i < 100000:
    # print(chr(i), end="")
    print(chr(i).encode("utf-8", "ignore").decode("utf-8"), end="")
    i += 1