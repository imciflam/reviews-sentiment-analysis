from nbc import nbc
from lstm import lstm


def inpStr(model): 
    if model == "nbc":
        review = input("enter a review: ") 
        nbc(review)
    elif model == "lstm":
        lstm()

def main():
    print("[1] use nbc")
    print("[2] use lstm")
    print("[0] exit")
    cmd = input("enter a command: ")
    while cmd != "Exit":
        if cmd == "1":
            inpStr("nbc")
        elif cmd == "2":
            inpStr("lstm")
        elif cmd == "0":
            exit()
        else:
            print("wrong command")
        cmd = input("enter a command: ")
    return


main()