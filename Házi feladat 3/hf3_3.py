gender = input("Kérem adja meg hogy fiú-e vagy lány: ")

if gender == "lány":

    age = input("Kérem adja meg életkorát: ")
    try:
        number = int(age)
        if number >= 10 and number <= 12:
            print("Játszhat a csapatban.")
        else:
            print("Nem felel meg az életkor, ezért nem játszhat a csapatban.")

    except ValueError:
        print("Az életkor nem felel meg.")

if gender == "fiú":
    print("Nem játszhat a csapatban.")