import re

regex = "^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$"


def check(email):
    if re.search(regex, email):
        print("vaild")
    else:
        print("invalid")


if __name__ == "__main__":
    email = "vishnupa2000@gmail.com"
    check(email)
