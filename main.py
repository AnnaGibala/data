import csv

sales_data = open("sales_data_sample.csv", "r")

csv_sales_data = csv.reader(sales_data)

for r in range(7):
    print(next(csv_sales_data))


sales_data = open("sales_data_sample.csv", "r")
csv_sales_data = csv.reader(sales_data)

next(csv_sales_data)

total_revenue = 0

min_year = 100000
max_year = 0

for r in csv_sales_data:
    quantity = r[1]
    price = r[2]
    revenue = int(quantity) * float(price)
    total_revenue += revenue

    if int(r[9]) < min_year:
        min_year = int(r[9])

    if int(r[9]) > max_year:
        max_year = int(r[9])


print("Całkowity przychód wynosi: ", total_revenue)
print("Zakres lat : od ", min_year, "do ", max_year)


sales_sum = open("sales_sum.txt", "w")

sales_sum.write("Calkowity przychod wynosi: " + str(total_revenue) + "\n")
sales_sum.write("Zakres lat : od " + str(min_year) + "do " + str(max_year))

