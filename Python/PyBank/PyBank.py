import os
import csv

budget1_csv = os.path.join("budget_data_1.csv")

revenue_1 = []
date_1 = []
revenue_change1 = []

with open(budget1_csv, 'r') as csvfile:
    csv_reader1 = csv.reader(csvfile, delimiter=",")
    next(csv_reader1, None)
    for row in csv_reader1:
        revenue_1.append(float(row[1]))
        date_1.append(row[0])
        total_months1 = len(date_1)
        total_revenue1 = sum(revenue_1)
        avg_rev_change1 = round(total_revenue1/total_months1, 0)
        
          
    for i in range(1, len(revenue_1)):
        revenue_change1.append(revenue_1[i] - revenue_1[i-1])
        inc_rev_change1 = max(revenue_change1)
        dec_rev_change1 = min(revenue_change1)
        inc_date1 = str(date_1[revenue_change1.index(max(revenue_change1))])
        dec_date1 = str(date_1[revenue_change1.index(min(revenue_change1))])
  
budget2_csv = os.path.join("budget_data_2.csv")

revenue_2 = []
date_2 = []
revenue_change2 = []
with open(budget2_csv, 'r') as csvfile:
    csv_reader2 = csv.reader(csvfile, delimiter=",")
    next(csv_reader2, None)
    for row in csv_reader2:
        revenue_2.append(float(row[1]))
        date_2.append(row[0])
        total_months2 = len(date_2)
        total_revenue2 = sum(revenue_2)
        avg_rev_change2 = round(total_revenue2/total_months2, 0)

    for i in range(1, len(revenue_2)):
        revenue_change2.append(revenue_2[i] - revenue_2[i-1])
        inc_rev_change2 = max(revenue_change2)
        dec_rev_change2 = min(revenue_change2)
        inc_date2 = str(date_2[revenue_change2.index(max(revenue_change2))])
        dec_date2 = str(date_2[revenue_change2.index(min(revenue_change2))])

    total_months = total_months1 + total_months2
    total_revenue = (total_revenue1) + (total_revenue2)
    avg_rev_change = total_revenue/total_months
    
    if inc_rev_change1 >= inc_rev_change2:
        inc_rev_change = inc_rev_change1
        inc_date = inc_date1
    else:
        inc_rev_change = inc_rev_change2
        inc_date = inc_date2
        Financial_Analysis.append(inc_date + inc_rev_change)
    if dec_rev_change1 <= dec_rev_change2:
        dec_rev_change = dec_rev_change1
        dec_date = dec_date1
    else: 
        dec_rev_change = dec_rev_change2
        dec_date = dec_date1
    print("Financial Analysis")
    print("----------------------------")
    print("Total Months: " + str(total_months))
    print("Total Revenue: $" + str(int(total_revenue)))
    print("Average Change in Revenue: $" + str(int(avg_rev_change)))
    print("Greatest Increase in Revenue: " + inc_date + " ($" + str(int(inc_rev_change)) + ")")
    print("Greatest Decrease in Revenue: " + dec_date + " ($" + str(int(dec_rev_change)) + ")")

Financial_Analysis = os.path.join("FinancialAnalysis.csv")
with open(Financial_Analysis, 'w', newline="") as datafile:
    csvWriter = csv.writer(datafile)
    csvWriter.writerow(["Financial Analysis"])
    csvWriter.writerow(["----------------------------"])
    csvWriter.writerow(["Total Months: " + str(total_months)])
    csvWriter.writerow(["Total Revenue: $" + str(int(total_revenue))])
    csvWriter.writerow(["Average Revenue Change: $" + str(int(avg_rev_change))])
    csvWriter.writerow(["Greatest Increase in Revenue: " + str(inc_date) + " " + "($" + str(int(inc_rev_change)) + ")"])
    csvWriter.writerow(["Greatest Decrease in Revenue: " + str(dec_date) + " " + "($" + str(int(dec_rev_change)) + ")"])

    












