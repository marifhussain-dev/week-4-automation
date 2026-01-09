import csv
from openpyxl import Workbook
from openpyxl.styles import Font

wb = Workbook()
sheet = wb.active
sheet.title = "Sales"

with open("sales.csv", newline="") as f:
    reader = csv.reader(f)
    for row in reader:
        sheet.append(row)

#Bold header row
for cell in sheet[1]:
    cell.font = Font(bold=True)

wb.save("sales_from_csv.xlsx")
print("Saved: sales_from_csv.xlsx")
