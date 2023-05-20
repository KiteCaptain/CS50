import csv 

titles = dict()

with open("favourites.csv", "r") as file:
    reader = csv.DictReader(file)
    for row in reader:
        title = row["title"].strip().lower()
        if title not in titles:
            titles[title] = 1
        titles[title] += 1  
             
for title in sorted(titles, key=lambda title: titles[title], reverse=True):
    print(title, titles[title])
    
title = input("Title: ").strip().lower()
with open("favourites.csv", "r") as file:
    reader = csv.DictReader(file)
    counter = 0
    for row in reader:
        if row["title"].strip().lower() == title:
            counter += 1
print(counter)