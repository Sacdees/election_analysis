import csv 
import os
                            # Assign a variable to load a file from a path
                            # to load file and read file
                            # file_to_load = 'resources/election_results.csv'

file_to_load = os.path.join("resources", "election_results.csv")

                            # Assign a variable to save the file to a path
                            # to write a file and save a file ("w" meand write to file, "r" to read, etc.)
file_to_save = os.path.join("analysis","election_practice.txt")

                            # Place above everything because we want to be 0 every time it runs
total_votes = 0
candidate_options = []
candidate_votes = {}
winning_candidate = ""                                                  #
winning_count = 0
winning_percentage = 0

                                                            #open the election results and read the file
with open (file_to_load) as election_data:
    
    file_reader=csv.reader(election_data)                   #open the election results and read file 
    headers = next(file_reader)                             #read the header row
    for row in file_reader:                                 #print each row in the CSV file
        total_votes += 1                                    #add the total vote count
        candidate_name = row[2]                             #print candidate name from each row
        if candidate_name not in candidate_options:
            candidate_options.append(candidate_name)        #add candidate name if not in list
            candidate_votes[candidate_name] = 0             #begin 
        candidate_votes[candidate_name] += 1                #add a vote to that candidates count (align with if or will only count '1')

                                    

for candidate_name in candidate_votes:                      #iterate through the candidate votes
    votes = candidate_votes[candidate_name]                 #retrieve vote count of a candidate
    vote_percentage = float(votes)/float(total_votes)*100       #calculate the percenatage of votes
       
    print(f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")    #TO DO print EACH name,count,% votes to the terminal
    
    
    if (votes > winning_count) and (vote_percentage > winning_percentage):      #determine if votes is > winning count
        winning_count = votes                                                   #if true then set to next two lines
        winning_percentage = vote_percentage
        winning_candidate = candidate_name                                      #set the winning candidate equal to candidates name 

winning_candidate_summary = (                                                   #TO DO print WINNING candidate, vote, %            
    f"-------------------------\n"
    f"Winner: {winning_candidate}\n"
    f"Winning Vote Count: {winning_count:,}\n"
    f"Winning Percentage: {winning_percentage:.1f}%\n"
    f"-------------------------\n")
print(winning_candidate_summary)                          







