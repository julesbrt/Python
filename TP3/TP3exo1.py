def a():
    n=int(input("entrer la valeur de n : "))
    N=0
    for x in range(1, n+1):
        N+=x
    print(N)


def b():
    x = 0
    while x != 100:
        x = int(input("entrer la valeur de x : "))


def c():
    nums = []
    for i in range(10):
        while i in range(10):
            try:
                prompt = float(input(f"Entrez un nombre entre 0 et 20 ({i + 1}): "))
                if prompt in range(21):
                    nums.append(prompt)
                    break
            except ValueError:
                continue

            print("Valeur invalide, veuillez entrer une nouvelle valeur entre 0 et 20 : ")
            continue

    inferieur10 = 0
    range1015 = 0
    superieur15 = 0
    for i in nums:
        if i < 10:
            inferieur10 += 1
        elif i in range(10, 15):
            range1015 += 1
        else:
            superieur15 += 1

    print(f"{inferieur10} nb strictement inférieurs à 10.\n"
          f"{range1015} nb supérieur à 10 et inférieur strictement à 15.\n"
          f"{superieur15} nb supérieur à 15.\n")


def d():
    entree = int(input("Entrez un nombre: "))
    temp = 0
    N = 0
    while temp <= entree:
        N += 1
        temp += N

    print(f"N={N - 1}")

d()