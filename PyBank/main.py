import os
import csv

def financial_analysis(file_path):
    # Initialize variables to store the analysis results
    total_months = 0
    net_profit_losses = 0
    prev_profit_loss = 0
    total_change = 0
    greatest_inc = 0
    greatest_inc_date = ""
    greatest_dec = 0
    greatest_dec_date = ""
    file_path = os.path.join('.', 'Resources', 'budget_data.csv')

    with open(file_path, 'r') as csvfile:
        csvreader = csv.reader(csvfile)
        next(csvreader)

        for row in csvreader:
            # Extract date and profit/loss values from the current row
            date = row[0]
            profit_loss = int(row[1])

            # Calculate the total number of months
            total_months += 1

            # Calculate the net total amount of profit/loss
            net_profit_losses += profit_loss

            # Calculate the change in profit/loss from the previous month
            if total_months > 1:
                change = profit_loss - prev_profit_loss
                total_change += change

                # Check for the greatest increase and decrease in profit/loss
                if change > greatest_inc:
                    greatest_inc = change
                    greatest_inc_date = date
                elif change < greatest_dec:
                    greatest_dec = change
                    greatest_dec_date = date

            # Update the previous profit/loss for the next cycle
            prev_profit_loss = profit_loss

    # Calculate the average change in profit/loss
    average_change = total_change / (total_months - 1)

    # Print the analysis results
    print("Financial Analysis")
    print("------------------")
    print(f"Total Months: {total_months}")
    print(f"Total: ${net_profit_losses}")
    print(f"Average Change: ${average_change:.2f}")
    print(f"Greatest Increase in Profits: {greatest_inc_date} (${greatest_inc})")
    print(f"Greatest Decrease in Profits: {greatest_dec_date} (${greatest_dec})")

    # Export the analysis results to a text file
    output_file = "analysis/financial_analysis.txt"
    with open(output_file, 'w') as f:
        f.write("Financial Analysis\n")
        f.write("------------------\n")
        f.write(f"Total Months: {total_months}\n")
        f.write(f"Net Total: ${net_profit_losses}\n")
        f.write(f"Average Change: ${average_change:.2f}\n")
        f.write(f"Greatest Increase in Profits: {greatest_inc_date} (${greatest_inc})\n")
        f.write(f"Greatest Decrease in Profits: {greatest_dec_date} (${greatest_dec})\n")

# closing statement
if __name__ == "__main__":
    file_path = "budget_data.csv"
    financial_analysis(file_path)
