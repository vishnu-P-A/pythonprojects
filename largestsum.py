inputnum = str(input("enter the number:"))


def numconcat(num1, num2, num3):

    num1 = str(num1)
    num2 = str(num2)
    num3 = str(num3)

    num1 = num1 + num2 + num3

    return int(num1)


def largest_number(inum):
    firstno = 0
    for i in range(1, len(inum) - 2):
        number = numconcat(inum[i], inum[i + 1], inum[i + 2])
        if number > firstno:
            firstno = number
        else:
            continue
    return firstno


if __name__ == "__main__":
    print(largest_number(inputnum))
