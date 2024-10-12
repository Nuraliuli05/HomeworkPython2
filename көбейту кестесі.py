
def kobeitu_kestesi(n):
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            print(f"{i} x {j} = {i * j}", end="\t")
        print()


n = int(input("Көбейту кестесінің өлшемін енгізіңіз: "))
kobeitu_kestesi(n)