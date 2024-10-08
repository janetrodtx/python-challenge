# Dependencies
import csv
import os


os.chdir(os.path.dirname(os.path.realpath(__file__)))
# Files to load and output (update with correct file paths)
INPUT_PATH = os.path.join("Resources", "budget_data.csv") 
OUTPUT_PATH = os.path.join("analysis", "budget_analysis.txt") 
print(INPUT_PATH)

# Define variables to track the financial data
total_months = 0
total = 0
# Add more variables to track other necessary financial data
changes = []
months = []

# Open and read the csv
with open(INPUT_PATH) as file:
    csv_reader = csv.reader(file)
    # Skip the header row
    header = next(csv_reader)
    # Extract first row to avoid appending to net_change_list 
    first_row = next(csv_reader)
    previous_profit = int(first_row[1])
    for row in csv_reader:
        print(row)    
        months.append(row[0])
        current_profit = int(row[1])
        # Track the total
        total_months += 1
        total += current_profit
        # Track the total and net change
        net_change = current_profit - previous_profit
        changes.append(net_change)
        previous_profit = current_profit

print("Net changes:", changes)
print("Total:", total)

        # Calculate the greatest increase in profits (month and amount)
max_increase = max(changes)
max_increase_month = months[changes.index(max_increase)]

        # Calculate the greatest decrease in losses (month and amount)
max_decrease = min(changes)
max_decrease_month = months[changes.index(max_decrease)]


# Calculate the average net change across the months
average_change = sum(changes) / len(changes)


# Generate the output summary
output = (
    "Financial Analysis\n"
    "----------------------------\n"
    f"Total Months: {total_months}\n"
    f"Total: ${total}\n"
    f"Average Change: ${average_change:.2f}\n"
    f"Greatest Increase in Profits: {max_increase_month} (${max_increase})\n"
    f"Greatest Decrease in Profits: {max_decrease_month} (${max_decrease})\n"
)

print(output)
with open(OUTPUT_PATH, "w") as file:
    file.write(output)
print(f"Results have been written to {OUTPUT_PATH}")
