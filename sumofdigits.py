def findsum(no):
    sum = 0
    for i in no:
        sum = sum + int(i)g
    a = len(str(sum))
    if a > 1:
        print(sum)
        return findsum(str(sum))
    else:
        return sum


if __name__ == "__main__":
    num = input("enter the number:")
    print(findsum(num))
