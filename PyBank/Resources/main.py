import os
import csv

budget_data_csv = os.path.join(".","Resources","budget_data.csv")

#Initializing the variablea before iterating the rows .

total_months = 0
net_total = 0
previous_list = 0                 #previous_list is initialized to zero as there is no preceding row before the first row.
profit_loss_changes = []          # profit_loss_changes is initially empty to store the changes in profit/loss values.
greatest_increase = ['', 0]       # both the variables are initialized as empty strings '' for the dates and zero 0 for the amounts. 
greatest_decrease = ['', 0]
   


with open(budget_data_csv, newline='') as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')


    # Read the header row first (skip this step if there is no header)
    csv_header = next(csvreader)
    

    
    # Iterate through the rows
    for row in csvreader:
        # Count the number of months
        total_months += 1
        
        # Get the profit/loss for the current row
        current_list = int(row[1])                       #inside the loop ,current_list is assigned with the value of the profit/loss from row[1].
        
        # Calculate the net total
        net_total += current_list
        
        # Calculate the change in profit/loss
        profit_loss_change = current_list- previous_list  
        
        profit_loss_changes.append(profit_loss_change)        # The calculated change is then appended to profit_loss_changes list.
        
        # Update the previous_data for the next iteration 
        previous_list = current_list
        
        # checks if the change is larger than the greatest increase or smaller than the current greatest decrease and are changed with the new date and amount.
        if profit_loss_change > greatest_increase[1]:
            greatest_increase = [row[0], profit_loss_change]
        elif profit_loss_change < greatest_decrease[1]:
            greatest_decrease = [row[0], profit_loss_change]
        
        # Calculate the average change  
    total_change = sum(profit_loss_changes) - profit_loss_changes[0]        # we subtract profit_loss_changes[0] from the list as there is no preceding month to calculate.
average_change = total_change / (total_months - 1)                   # (total_month -1)= number of months excluding the first month because there is no change to calculate for the first month.
       
       
        # Print the final result.
analysis_results = f'''
    Financial Analysis
    -------------------------
    Total Months: {total_months}
    Total: ${net_total}
    Average Change: ${average_change:.2f}
    Greatest Increase in Profits: {greatest_increase[0]} (${greatest_increase[1]})
    Greatest Decrease in Profits: {greatest_decrease[0]} (${greatest_decrease[1]})
    '''
print(analysis_results)
    
    # Export the results to a text file
with open('financial_analysis.txt', 'w') as output_file:
        output_file.write(analysis_results)