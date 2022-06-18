import csv
import string

# csv file name
filename = "crimes-19.csv"

# initializing the titles and rows list
fields = []
rows = []

print("Reading")

# reading csv file
with open(filename, 'r') as csvfile:
    # creating a csv reader object
    csvreader = csv.reader(csvfile)

    # extracting field names through first row
    fields = next(csvreader)

    # extracting each data row one by one
    for row in csvreader:

        # Format
        # Location Description
        if row[7] == "Residence":
            ld = 1
        elif row[7] == "Apartment":
            ld = 2
        elif row[7] == "Sidewalk" or row[7] == "Street":
            ld = 3
        elif row[7] == "Bank":
            ld = 4
        else:
            ld = 0

        # Arrest
        if row[8] == "false":
            a = 1
        else:
            a = 0

            # Domestic
        if row[9] == "false":
            d = 1
        else:
            d = 0

        rows.append([''.join([c for c in row[4] if c.isdigit()]), ld, a, d, row[10], row[11], row[12], row[13], row[17]])

print("Writing....")

filename = "crimes-19-m.csv"

# writing to csv file
with open(filename, 'w') as csvfile:
    # creating a csv writer object
    csvwriter = csv.writer(csvfile)

    # writing the fields
    csvwriter.writerow([fields[4], fields[7], fields[8], fields[9], fields[10], fields[11], fields[12], fields[13], fields[17]])

    # writing the data rows
    csvwriter.writerows(rows)

print("Done")
# %%
