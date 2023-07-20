import os
import csv

def election_analysis(file_path):
    # Initialize variables to store the analysis results
    total_votes = 0
    candidate_votes = {}
    candidate_list = []
    file_path = os.path.join('.', 'Resources', 'election_data.csv')
    
    with open(file_path, 'r') as csvfile:
        csvreader = csv.reader(csvfile)
        next(csvreader)

        for row in csvreader:
            # Extract the candidate name from the current row
            candidate = row[2]

            # Count the total number of votes
            total_votes += 1

            # Add the candidate to the candidate list if not present
            if candidate not in candidate_list:
                candidate_list.append(candidate)
                candidate_votes[candidate] = 0

            # Increment the candidate's vote count
            candidate_votes[candidate] += 1

    # Calculate the percentage of votes each candidate won
    candidate_percentage = {candidate: (votes / total_votes) * 100 for candidate, votes in candidate_votes.items()}

    # ref: Dictionary format to determine winner based on popular vote
    # myDict = {'a': 1, 'b': 2, 'c': 3}
    # print(max(myDict, key=myDict.get))
    # Find the winner based on popular vote
    election_winner = max(candidate_votes, key=candidate_votes.get)

    # Print the election analysis results
    print("Election Results")
    print("-------------------------")
    print(f"Total Votes: {total_votes}")
    print("-------------------------")
    for candidate in candidate_list:
        print(f"{candidate}: {candidate_percentage[candidate]:.3f}% ({candidate_votes[candidate]})")
    print("-------------------------")
    print(f"Winner: {election_winner}")
    print("-------------------------")

    # Export the election analysis results to a text file
    output_file = "analysis/election_analysis.txt"
    with open(output_file, 'w') as f:
        f.write("Election Results\n")
        f.write("-------------------------\n")
        f.write(f"Total Votes: {total_votes}\n")
        f.write("-------------------------\n")
        for candidate in candidate_list:
            f.write(f"{candidate}: {candidate_percentage[candidate]:.3f}% ({candidate_votes[candidate]})\n")
        f.write("-------------------------\n")
        f.write(f"Winner: {election_winner}\n")
        f.write("-------------------------\n")

# closing statement
if __name__ == "__main__":
    file_path = "election_data.csv"
    election_analysis(file_path)
