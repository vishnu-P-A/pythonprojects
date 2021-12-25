def findpower(num, power, method):
    if method == 0:
        x = pow(a, n)
        return x
    else:
        val = 1
        for i in range(power):
            val = val * num
        return val


if __name__ == "__main__":
    a = int(input("enter the number:"))
    n = int(input("enter the power:"))
    meth = int(input("enter the method:"))
    store = findpower(a, n, meth)
    print(store)
