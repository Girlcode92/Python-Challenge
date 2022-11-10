import os
import csv

candidates = {}

#start counter at zero
total_votes = 0
most_votes_count = 0
most_votes_candidate = ""

csvpath = os.path.join("PyPoll/Resources/election_data 2.csv")

with open(csvpath,'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvreader)

    
    for row in csvreader:
    
#Start candidate tally and accumulate vote count data
        
        candidate_name = row[2]
        total_votes = total_votes + 1
        
        if candidate_name in candidates:
            candidates[candidate_name] = candidates[candidate_name] + 1
        else:
            candidates[candidate_name] = 1

#Print "Election results" and output total_votes count            

with open('analysis_election.txt', 'w') as text_file:
    print ("\n" + "Election Results")
    print('--------------------------------' + "\n")
    output = ("Total Votes: " + str(total_votes) + "\n")
    print(output)
    text_file.write(output)
    print("--------------------------------" + "\n")
 
 #Set parameters and rules for finding the winner via vote_counts, candidate percentage of votes
    for candidate_name, candidate_votes in candidates.items():
        if candidate_votes > most_votes_count:
            most_votes_candidate = candidate_name
            most_votes_count = candidate_votes
        candidates_percent = round((candidate_votes/total_votes)*100,3)
        
 #Print results and text_file       
        output = candidate_name + ":" + str(candidates_percent) + '% ' + '(' + str(candidate_votes) + ')'
        print(output)
        text_file.write(output + '\n')
  

    print(f"----------------------------------------\nWinner: {most_votes_candidate}\n----------------------------------------" + '\n')
    text_file.write(f'----------------------------------------\nWinner: {most_votes_candidate}\n----------------------------------------' + "\n")