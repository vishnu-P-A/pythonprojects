import sys


def findoddoreve():
    if any(i.isdigit() for i in sys.argv):
        if int(sys.argv[1]) % 2 == 0:
            print("even number")
        else:
            print("odd number")
    else:
        print("string")


if __name__ == "__main__":
    findoddoreve()
