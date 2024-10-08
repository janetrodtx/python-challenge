# Import necessary modules
import csv
import os
print(os.path.realpath(__file__))
os.chdir(os.path.dirname(os.path.realpath(__file__)))
# Set the input and output file paths
INPUT_PATH = os.path.join("Resources", "election_data.csv")  # Input file path
OUTPUT_PATH = os.path.join("analysis", "election_analysis.txt")  # Output file path

# Initialize variables to track the election data
total_votes = 0
votes_for_candidates = {}
winning_votes = 0
winner = ""

# Open the CSV file in read mode
with open(INPUT_PATH, 'r') as csvfile:
    # Create a CSV reader object
    csv_reader = csv.reader(csvfile)

    # Skip the header row (if present)
    next(csv_reader)

    for row in csv_reader:
        if row:  # Check if the row is not empty
            if len(row) > 2:  # Ensure there are enough columns
                candidate = row[2]
                total_votes += 1
                
                # Count votes for each candidate
                if candidate in votes_for_candidates:
                    votes_for_candidates[candidate] += 1
                else:
                    votes_for_candidates[candidate] = 1
            else:
                print("Row does not have enough columns:", row)
# Print out the results
print(f"-------------------------------------------")
print(f"Election Results")
print(f"-------------------------------------------")
print(f"Total Votes: {total_votes:,}")
print(f"-------------------------------------------")           

# Determine the winner based on popular vote
if votes_for_candidates:  # Check if the dictionary is not empty
    winner = max(votes_for_candidates, key=votes_for_candidates.get)

# Prepare the output string
output = (
    "Election Results\n"
    "-------------------------\n"
    f"Total Votes: {total_votes}\n"
    "-------------------------\n"
)

# Iterate through the candidates to calculate percentages and build the output
for candidate, votes in votes_for_candidates.items():
    percentage = (votes / total_votes) * 100
    output += f"{candidate}: {percentage:.3f}% ({votes})\n"

# Determine the winner based on popular vote
if votes_for_candidates:  # Check if the dictionary is not empty
    winner = max(votes_for_candidates, key=votes_for_candidates.get)

output += (
    "-------------------------\n"
    f"Winner: {winner}\n"
    "-------------------------\n"
)

# Print the results
print(output)

# Write the results to a text file
with open(OUTPUT_PATH, 'w') as text_file:
    text_file.write(output)