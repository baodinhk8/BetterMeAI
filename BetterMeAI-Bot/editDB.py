import csv
import os


def addToDB(question, answer):
    with open("data.csv", "r") as f1:
        last_id = f1.readlines()[-1]
        last_id = (last_id.split(','))[0]
    new_id = int(last_id)+1

    fields = [str(new_id), question, answer]

    with open(r'data.csv', 'a') as f:
        writer = csv.writer(f)
        writer.writerow(fields)

    return str(new_id)


def exceptedAnswer(n_id, data):
    os.rename('data.csv', 'data.csv.bak')

    csv_in = open('data.csv.bak', 'r')
    csv_out = open('data.csv', 'w')

    writer = csv.writer(csv_out)

    for row in csv.reader(csv_in):
        if(row[0] == "id"):
            writer.writerow(row)
        elif(int(row[0]) == n_id):
            new_data = [row[0], row[1], row[2], data]
            writer.writerow(new_data)
        else:
            writer.writerow(row)
