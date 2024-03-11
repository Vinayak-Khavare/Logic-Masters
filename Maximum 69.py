def maximum69Number (num: int):
    a = list(str(num))
    for i in range(len(a)):
        if a[i] == "6":
            a[i] = "9"
            break
    return int(''.join(a))
