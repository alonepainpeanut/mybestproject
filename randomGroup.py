import random
dataKelasB = ["Zarir", "Adit", "Angga", "Aprilia", "Ovin", "Bagas", "Bobby", "Daru", "Defri", "Diaz", "Dita", "Elnad", 
              "Fabian", "Rima", "Hanif", "Heparia", "Jaisy", "Lasminanto", "Lintang", "Maranatha", "Afif", "Hafidz", 
              "Rizky Alief", "Wildan", "Musa", "Najwa", "Naufal", "Novia", "Oktavia", "Purwa", "Refa", "Ridwan", 
              "Risna", "Rizqi Haprab", "Ruth", "Seli", "Septian", "Tubagus", "Zahra", "Loay"]

kelompok = []
kelompok1 = []
kelompok2 = []
kelompok3 = []
kelompok4 = []
kelompok5 = []
kelompok6 = []
kelompok7 = []
kelompok8 = []
kelompok9 = []
kelompok10 = []
for i in range(4):
    randomKomputer = random.choice(dataKelasB)
    kelompok1.append(randomKomputer)
    dataKelasB.remove(randomKomputer)
    if len(kelompok1) == 4:
        for i in range(4):
            randomKomputer = random.choice(dataKelasB)
            kelompok2.append(randomKomputer)
            dataKelasB.remove(randomKomputer)
            if len(kelompok2) == 4:
                for i in range(4):
                    randomKomputer = random.choice(dataKelasB)
                    kelompok3.append(randomKomputer)
                    dataKelasB.remove(randomKomputer)
                    if len(kelompok3) == 4:
                        for i in range(4):
                            randomKomputer = random.choice(dataKelasB)
                            kelompok4.append(randomKomputer)
                            dataKelasB.remove(randomKomputer)
                            if len(kelompok4) == 4:
                                for i in range(4):
                                    randomKomputer = random.choice(dataKelasB)
                                    kelompok5.append(randomKomputer)
                                    dataKelasB.remove(randomKomputer)
                                    if len(kelompok5) == 4:
                                        for i in range(4):
                                            randomKomputer = random.choice(dataKelasB)
                                            kelompok6.append(randomKomputer)
                                            dataKelasB.remove(randomKomputer)
                                            if len(kelompok6) == 4:
                                                for i in range(4):
                                                    randomKomputer = random.choice(dataKelasB)
                                                    kelompok7.append(randomKomputer)
                                                    dataKelasB.remove(randomKomputer)
                                                    if len(kelompok7) == 4:
                                                        for i in range(4):
                                                            randomKomputer = random.choice(dataKelasB)
                                                            kelompok8.append(randomKomputer)
                                                            dataKelasB.remove(randomKomputer)
                                                            if len(kelompok8) == 4:
                                                                for i in range(4):
                                                                    randomKomputer = random.choice(dataKelasB)
                                                                    kelompok9.append(randomKomputer)
                                                                    dataKelasB.remove(randomKomputer)
                                                                    if len(kelompok9) == 4:
                                                                        for i in range(4):
                                                                            randomKomputer = random.choice(dataKelasB)
                                                                            kelompok10.append(randomKomputer)
                                                                            dataKelasB.remove(randomKomputer)



kelompok.append(kelompok1)
kelompok.append(kelompok2)
kelompok.append(kelompok3)
kelompok.append(kelompok4)
kelompok.append(kelompok5)
kelompok.append(kelompok6)
kelompok.append(kelompok7)
kelompok.append(kelompok8)
kelompok.append(kelompok9)
kelompok.append(kelompok10)
index = 0
for i in range(10):
    print("\nKelompok ke-" + str(i+1), ": ")
    for a in range(4):
        index += 1
        print(str(index)+ "." ,kelompok[i][a])






