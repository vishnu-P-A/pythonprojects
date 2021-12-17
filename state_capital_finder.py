import random


def random_state_capital():
    thisdict = {
        "goa": "panaji",
        "karnataka": "banglore",
        "kerala": "tvm",
        "tamilnadu": "chennai",
        "punjab": "chandigrah",
    }
    print(random.choice(list(thisdict.items())))


if __name__ == "__main__":
    random_state_capital()
