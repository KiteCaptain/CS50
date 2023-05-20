import csv


phonebook = {
    "Kite": "0114338374",
    "Eugine": "0115638423",
    "Captain": "0115786235",
}

with open("phonebook.csv", "a", newline="") as file:
    writer = csv.writer(file)
    if phonebook:
        for name, number in phonebook.items():
            writer.writerow([name, number])

    file = open("phonebook.csv", "a")
    name = str(input("Name: "))
    number = str(input("Number: "))
    writer = csv.writer(file)
    writer.writerow([name, number])
# file.close()