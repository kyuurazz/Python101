while True:
    try:
        n = 0
        a = int(input("Masukan Bilangan : "))
        if n < a:
            n = a

        elif a == 0:
            print("Program Selesai\n")
            break
    except:
        print("Bilangan Tidak Boleh Kosong!")