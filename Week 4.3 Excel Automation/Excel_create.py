from openpyxl import Workbook

wb = Workbook()
sheet = wb.active
sheet.title = "Sheet1"

sheet.append(["Data", "Product", "qty", "Price"])
sheet.append(["24-01-01", "Apple", 2, 10])
sheet.append(["24-01-02", "Banana", 5, 3])

wb.save("sales.xlsx")

print("sales.xlsx created")
