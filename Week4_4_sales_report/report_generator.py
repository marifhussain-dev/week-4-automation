"""
Sales Report Automation (Week 4.4)

INPUT:
- sales.csv (date,product,qty,price)

OUTPUT:
- output/sales_report.xlsx

FLOW:
1) Read sales.csv
2) Validate + clean rows (skip bad rows, qty/price <= 0)
3) Calculate revenue per row (qty * price)
4) Create Excel report:
- Sheet 1: Sales (all clean rows + Revenue column)
- Sheet 2: Summary (total revenue by product + grand total)
5) Save Excel report into output/ folder
"""


import csv
from openpyxl import Workbook
from openpyxl.styles import Font

def read_and_clean_csv(filename):
    clean_rows = []
    skipped = 0

    with open(filename, newline="") as f:
        reader = csv.reader(f)
        header = next(reader) #skip header

        for row in reader:
            try:
                date = row[0].strip()
                product = row[1].strip()
                qty = int(row[2])
                price = float(row[3])
            except (ValueError, IndexError):
                skipped += 1
                continue
            if qty <= 0 or price <= 0:
                skipped += 1
                continue
            revenue = qty * price
            clean_rows.append([date, product, qty, price, revenue])

    return clean_rows, skipped

def autosize_columns(sheet):
    for column in sheet.columns:
        max_length = 0
        col_letter = column[0].column_letter

        for cell in column:
            if cell.value is not None:
                max_length = max(max_length, len(str(cell.value)))

        sheet.column_dimensions[col_letter].width = max_length + 2

def write_sales_sheet(rows, output_file):
    wb = Workbook()
    sheet = wb.active
    sheet.title = "Sales"

    headers = ["Date", "Product", "Qty", "Price", "Revenue"]
    sheet.append(headers)

    for cell in sheet[1]:
        cell.font = Font(bold=True)

    for row in rows:
        sheet.append(row)

    summary = wb.create_sheet(title="Summary")
    summary.append(["Product", "Total Revenue"])

    for cell in summary[1]:
        cell.font = Font(bold=True)

    revenue_by_product = {}
    grand_total = 0

    for r in rows:
        product = r[1]
        revenue = r[4]
        revenue_by_product[product] = revenue_by_product.get(product, 0)+revenue
        grand_total += revenue

    for product, total_rev in revenue_by_product.items():
        summary.append([product, round(total_rev, 2)])

    summary.append([])
    summary.append(["Total", round(grand_total, 2)])

    wb.save(output_file)
    autosize_columns(sheet)
    autosize_columns(summary)
    


rows, skipped = read_and_clean_csv("sales.csv")
write_sales_sheet(rows, "output/sales_report.xlsx")
print("Report Created")
