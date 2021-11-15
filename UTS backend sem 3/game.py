import random

print(" Selamat Datang di Permainan Batu, Gunting, Kertas")
print("--------------------------------------------------")

pilihan = ["","batu","gunting","kertas"]
kamu = None

while kamu != 0:
    print("Pilihan Kamu:")
    for x in range(1,4):
        print(f"{x}. {pilihan[x]}")
    print("0. berhenti")
    print("--------------------------------------------------")

    kamu = int(input("Masukkan Pilihanmu: "))
    kom = random.choice(["batu", "gunting", "kertas"])

    if kamu == 1:
        print("Kamu     : batu")
        print("komputer :", kom)
        if kom == "batu":
            print("                 SERI")
            print("--------------------------------------------------")
        elif kom == "gunting":
            print("                 Kamu MENANG")
            print("--------------------------------------------------")
        else :
            print("                 Kamu KALAH")
            print("--------------------------------------------------")
            
    elif kamu == 2:
        print("Kamu     : gunting")
        print("komputer :", kom)
        if kom == "gunting":
            print("                 SERI")
            print("--------------------------------------------------")
        elif kom == "kertas":
            print("                 Kamu MENANG")
            print("--------------------------------------------------")
        else :
            print("                 Kamu KALAH")
            print("--------------------------------------------------")
            
    elif kamu == 3:
        print("Kamu     : kertas")
        print("komputer :", kom)
        if kom == "kertas":
            print("                 SERI")
            print("--------------------------------------------------")
        elif kom == "batu":
            print("                 Kamu MENANG")
            print("--------------------------------------------------")
        else :
            print("                 Kamu KALAH")
            print("--------------------------------------------------")

    else:
        print("Bye - Bye")
print("--------------------------------------------------")