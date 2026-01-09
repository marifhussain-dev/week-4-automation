import csv

def read_sales():
    with open("sales.csv", newline="") as f:
        reader = csv.reader(f)
        header = next(reader)
        rows = list(reader)
        clean_row = []
        skipped = 0
        seen = set()

        for row in rows:
            try:
                date = row[0].strip()
                product = row[1]
                qty = int(row[2])
                price = float(row[3])
            except (ValueError, IndexError):
                skipped += 1
                continue

            if qty <= 0 or price <= 0:
                skipped += 1
                continue

            key = (date, product, qty, price)
            if key in seen:
                skipped += 1
                continue
            seen.add(key)

            clean_row.append([date, product, qty, price])
    print ("clean rows: ", len(clean_row))
    print("skipped rows:", skipped)

    return header, clean_row

    
def calculate_revenue(clean_row):
    total_revenue = 0.0

    for row in clean_row:
        date = row[0]
        product = row[1]
        qty = int(row[2])
        price = float(row[3])

        revenue = qty*price
        total_revenue += revenue
        print(product, "revenue: ", round(revenue, 2))
    print("Total Revenue:", round(total_revenue, 2))
    
    return total_revenue
    
def write_summary(clean_row, total_revenue):
    revenue_by_product = {}
    for row in clean_row:
        product = row[1]
        qty = int(row[2])
        price = float(row[3])
        revenue = qty * price

        revenue_by_product[product] = revenue_by_product.get(product, 0)+revenue

    with open("summary.csv", "w", newline = "") as f:
        writer = csv.writer(f)
        writer.writerow(["product", "total_revenue"])

        for product, revenue in revenue_by_product.items():
            writer.writerow([product, round(revenue, 2)])
        writer.writerow([])
        writer.writerow(["TOTAL", round(total_revenue, 2)])
    print("Summary written to summary.csv")
    

def main():
    header, clean_row = read_sales()
    print("Header: ", header)
    print("Rows: ")
    
    total_revenue = calculate_revenue(clean_row)
    write_summary(clean_row, total_revenue)

if __name__ == "__main__":
    main()


