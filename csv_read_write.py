import csv

with open("one.csv", "r") as f:
    file_reader = csv.DictReader(f)

    with open("new.csv", "w", newline="") as w:
        fieldnames = ["first", "second"]
        file_writer = csv.DictWriter(w, fieldnames=fieldnames)
        file_writer.writeheader()

        for line in file_reader:
            file_writer.writerow(line)
