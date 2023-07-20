import os
import csv

election_data_csv = os.path. join(".","Resources","election_data.csv")

with open(election_data_csv, newline ='') as csvfile:
    csv_reader= csv.reader(csvfile, delimiter=",")
    csv_header= next(csv_reader)   #header row is skipped using the  the next()function.
    
    

    # Setting up the variables 
    total_votes = 0             # keeps track of number of votes. 
    candidates_count = {}       # create empty dictionary to store the vote counts for each candidate.The keys of this dictionary are the candidate names, and the values are vote counts.
    
    #iterates over each row in csv file
    for row in csv_reader:
        # in each iteration total votes = increament by 1
        total_votes += 1
        
        # candidate name is used as key in the candidate_count dictionary
        candidate_name = row[2]
        
        # used to count votes for each candidate in the dictionary(candidates_count).
        if candidate_name in candidates_count:             
            candidates_count[candidate_name] += 1          # The if condition is used to check if candidate_name already exist in the dictionary if yes then the increment of 1 using +=1.
        else:                                              # The else condition is used when the candidate_name doesnt exist in the dictionary so a new key:value is added with initial count 1
            candidates_count[candidate_name] = 1
    
    # finding the winner from the data
    winner = max(candidates_count, key=candidates_count.get)   # The max() function with get() is used to returns the candidate name (key) with the maximum vote count (value) from the candidates_count dictionary.
                                                               
    
    
    # Calculate the percentage of votes for each candidate using (dictionary comprehension.{key:value for (key,value) in dict.items()}
    # A new key-value pair is created in the percentages dictionary. The key (candidate's name), and the value is calculated as (votes / total_votes) * 100.
    percentages = {candidate: (votes / total_votes) * 100 for candidate, votes in candidates_count.items()}
    
    # Format the analysis results
   # Print the results
    print("Election Results")
    print("-------------------------")
    print(f"Total Votes: {total_votes}")
    print("-------------------------")
    for candidate, votes in candidates_count.items():                               #The loop iterates through the candidates_count dictionary.
        print(f"{candidate}: {percentages[candidate]:.3f}% ({votes})")
    print("-------------------------")
    print(f"Winner: {winner}")
    print("-------------------------")
   
    # Export the results to a text file
with open('election_results.txt', 'w') as output_file:
    output_file.write("Election Results\n")
    output_file.write("-------------------------\n")
    output_file.write(f"Total Votes: {total_votes}\n")
    output_file.write("-------------------------\n")
    for candidate, votes in candidates_count.items():
        output_file.write(f"{candidate}: {percentages[candidate]:.3f}% ({votes})\n")
    output_file.write("-------------------------\n")
    output_file.write(f"Winner: {winner}\n")
    output_file.write("-------------------------\n")
        
