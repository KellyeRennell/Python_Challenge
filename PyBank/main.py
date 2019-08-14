import os
import csv

csvpath = os.path.join("Resources/budget_data.csv")


with open(csvpath, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    header = next(csvreader)
    
    total_number_months = []
    total_budget_data_profit = []
    monthly_change_budget_data = []
    
    
    
    for row in csvreader:
        total_number_months.append(row[0])
        total_budget_data_profit.append(int(row[1]))
        
                    
    for i in range(len(total_budget_data_profit)-1):
        
        monthly_change_budget_data.append(total_budget_data_profit[i+1]-total_budget_data_profit[i])
        
        
    max_increase = max(monthly_change_budget_data)
    max_decrease = min(monthly_change_budget_data)
        
    monthly_max_increase = monthly_change_budget_data.index(max(monthly_change_budget_data)) + 1
    monthly_max_decrease = monthly_change_budget_data.index(min(monthly_change_budget_data)) + 1     
        
    # Print out results
    print("Budget Data Analysis")
    print("------------------------")
    print(f"Total Months:{len(total_number_months)}")
    print(f"Total: ${sum(total_budget_data_profit)}")
    print(f"Average Change: {round(sum(monthly_change_budget_data)/len(monthly_change_budget_data),2)}")
    print(f"Greatest Increase in Profits: {total_number_months[monthly_max_increase]} (${(str(max_increase))})")
    print(f"Greatest Decrease in Profits: {total_number_months[monthly_max_decrease]} (${(str(max_decrease))})")             
    

#Output files
output_path = os.path.join(".", 'output.txt')   

with open(output_path, 'w') as txt:
#write methods to print to Budget_Data_Analysis_Summary   
    txt.write("Budget Analysis Summary")
    txt.write("\n")
    txt.write("----------------------------")
    txt.write("\n")
    txt.write(f"Total Months: {len(total_number_months)}")
    txt.write("\n")
    txt.write(f"Total: ${sum(total_budget_data_profit)}")
    txt.write("\n")
    txt.write(f"Average Change: {round(sum(monthly_change_budget_data)/len(monthly_change_budget_data),2)}")
    txt.write("\n")
    txt.write(f"Greatest Increase in Profits: {total_number_months[monthly_max_increase]} (${(str(max_increase))})")
    txt.write("\n")
    txt.write(f"Greatest Decrease in Profits: {total_number_months[monthly_max_decrease]} (${(str(max_decrease))})")
