import os
import csv

#assign path to csv

csvpath = os.path.join("Pybank", "Resources", "budget_data.csv")

#open csv file via path & assign rows to variables

with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvreader)
    total_months = []
    profit_loss_net = []
    pl_change = []
  
    print("Financial Analysis")
    print("-------------------------------------------")

#Set loop for row counter (total_months) and sum of profit_loss_net 
    for row in csvreader:
        
        total_months.append(row[0])

        profit_loss_net.append(int(row[1]))
    
#Set loop to find month to month pl_change

    for x in range(1,len(profit_loss_net)):
        pl_change.append(int(profit_loss_net[x])-int(profit_loss_net[x-1])) 

 #Calculate avg_pl and find greatest_increase (max) and greatest_decrease (min)
      
    avg_pl = sum(pl_change)/(len(total_months)-1)
    greatest_increase = max(pl_change)
    greatest_decrease = min(pl_change)
    
#Find month_row index of max and min values

    max_month_index = int(pl_change.index(greatest_increase))
    min_month_index = int(pl_change.index(greatest_decrease))

#Print findings
   
    print(f"Total Months: {len(total_months)}")
    print(f"Total: ${sum(profit_loss_net)}")
    print(f"Average Change: ${round(avg_pl,2)}")
    print(f"Greatest Increase in Profits: {total_months[max_month_index+1]} (${greatest_increase})")
    print(f"Greatest Decrease in Profits: {total_months[min_month_index+1]} (${greatest_decrease})")


#Text_file.write values to analysis.txt 

file_to_save = os.path.join("Pybank", "analysis.txt")
with open(file_to_save, "w") as text_file:
    text_file.write(f"Total Months: {len(total_months)}")
    text_file.write(f"Total: ${sum(profit_loss_net)}")
    text_file.write(f"Average Change: ${round(avg_pl,2)}")
    text_file.write(f"Greatest Increase in Profits: {total_months[max_month_index+1]} (${greatest_increase})")
    text_file.write(f"Greatest Decrease in Profits: {total_months[min_month_index+1]} (${greatest_decrease})")
