import csv

with open('one.csv', 'r') as csv_f:
    reader_guy = csv.DictReader(csv_f)

    with open('new.csv', 'w', newline="") as new_file:
        fieldnames = ['first', 'second']
        writer_guy = csv.DictWriter(
            new_file, fieldnames=fieldnames)
        writer_guy.writeheader()

        for line in reader_guy:
            writer_guy.writerow(line)
