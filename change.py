import csv

input_file = "Data/du_lieu.csv"
output_file = "Data/data.csv"

with open(input_file, "r") as file:
    reader = csv.reader(file)
    next(reader)
    rows = []
    for row in reader:
        year = row[0]
        month = row[1]
        day = row[2]
        date = f"{year}-{month.zfill(2)}-{day.zfill(2)}"
        new_row = [date] + row[3:]
        rows.append(new_row)

with open(output_file, "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["date", "meantemp", "humidity", "meanpressure", "wind_speed"])  
    writer.writerows(rows)

print("Đã định dạng thành công.")