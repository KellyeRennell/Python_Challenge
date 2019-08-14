import os
import csv

#where the election_data.csv is located
csv_path = os.path.join("Resources/election_data.csv")


candidates = []
vote_count = []
vote_count_winner = 0
total_number_votes = 0

with open(csv_path, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvfile)
    
# print(f"csv header: {csv_header}")
# csv header: Voter ID,County,Candidate
#reading/looping through each row of data after the header row

    for row in csvreader: 
        total_number_votes = total_number_votes + 1
     
        if row[2] not in candidates:
            candidates.append(row[2])
            vote_count.append(0)
           
            
        candidate_index = candidates.index(row[2])
        
        vote_count[candidate_index] =  vote_count[candidate_index] + 1
        
        
                
    print("Election Data Results")
    print("-------------------")
    print(f"Total votes: {total_number_votes}")  
    
    for x in range(len(candidates)):
        
        percentage_vote = round((vote_count[x]/total_number_votes)*100, 3)
        print(f"{candidates[x]}: {percentage_vote}% ({vote_count[x]})")
        
        if (vote_count_winner < vote_count[x]):
            vote_count_winner = vote_count[x]
            winner = candidates[x]
            
    print(f"Winner: {winner}")
        
#output files
output_path = os.path.join(".", 'output.txt') 
              
with open(output_path, "w") as txt:
    txt.write("Election Data Results")
    txt.write('\n')
    txt.write(f"Total votes: {total_number_votes}")
    txt.write('\n')
    txt.write(f"{candidates[x]}: {percentage_vote}% ({vote_count[x]})")
    txt.write('\n')
    txt.write(f"Winner: {winner}")
    