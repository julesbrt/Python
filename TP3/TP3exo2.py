import time


def ffor():
    nb = int(input("Entrez un nombre (for): "))
    for i in range(nb + 1):
        print(nb - i)
        time.sleep(0.1)


def fwhile():
    nb = int(input("Entrez un nombre (while): "))
    temp = 0
    while temp <= nb:
        print(nb - temp)
        temp += 1
        time.sleep(0.1)

ffor()
fwhile()