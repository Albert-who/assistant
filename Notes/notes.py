import csv

NOTES = "notes.csv"

def readNotes():
    i = []
    with open(NOTES, newline="") as file:
        reader = csv.reader(file)
        for row in reader:
            i.append(row)
    return i

def writeNotes(note: str):
    print(note)
    with open(NOTES, 'a') as file:
        file.write(note)