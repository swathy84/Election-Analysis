#Add our dependencies. 

import csv
import os


# Assign variable to load a file from a path 
file_to_load = os.path.join("Resources","election_results.csv")

# Assign a variable to save the file to a path. 
file_to_save = os.path.join("analysis","election_analysis.txt")

#creating a total_votes variable to increment by 1 each time as the row been read. 
total_votes = 0 

#Declaring a new empty list to retreive the candidate names 
candidate_options = []

# Declaring a new empty dictionary to retreive each candidates total vote 
candidate_votes={}

# Declare a variable that holds an empty string for the winning candidate 
winning_candidate = " " 

#declare a variavle for hte winning count and assign to 0 
winning_count = 0

#declare a winning percentage 
winning_percentage = 0

# Open the election results and read a file. 
with open(file_to_load) as election_data:
    #to do : read and analyze the data here.
    #read the file objects with a reader function 
    file_reader = csv.reader(election_data)
    
    # Read and Print the header row 
    headers = next(file_reader)
    # print(headers)

    #print each row in the csv file .
    for row in file_reader:
        #print(row) would print the entire data from the .csv file 
        #print(row)

        #Add to the total vote count
        total_votes += 1
       
        # print the candidate name from the 3rd column (index = 2) for each row 
        candidate_name = row[2]

      
         
        #if the candidate does not match any exisitig candidate 
        if candidate_name not in candidate_options:
            
            #Add the candidate name to candidate list.
            candidate_options.append(candidate_name)


            #Begin tracking the candidates vote count.
            candidate_votes[candidate_name] = 0

        #Add a vote to that candidate's count
        candidate_votes[candidate_name] += 1  



        #determine the percentage of votes for each candidate by looping throguh the counts 
        #iterate through the candidate list 
    for candidate_name in candidate_votes:
        
        #retrieve vote count of a candidate 
        votes = candidate_votes[candidate_name]
        
        #calculate the percentage votes
        vote_percentage = float(votes)/float(total_votes)*100

        #Print the candidate name and percentage of votes .
        print(f'{candidate_name}: received {vote_percentage: .1F}% of the votes.')
           
        #determining  winning vote count and candidate 
        #determine if the votes are greater than the winning count
        if (votes > winning_count) and (vote_percentage > winning_percentage):
                
            #if true then set winning_count = votes and winning_percent = vote_percentage
            winning_count = votes
                
            winning_percentage = vote_percentage
                
            #set the winning_candidate equal to the candidate's name 
            winning_candidate = candidate_name
    
        #print the  each candidates name, vote count and percentage votes
        print(f'{candidate_name}: {vote_percentage: .1F}% ({votes: ,})\n ')     

    #print the Winning candidate  summary 
    winning_candidate_summary = (
                                f' ----------------------------------\n'
                                f' Winner: {winning_candidate}\n'
                                f' Winning Vote Count: {winning_count: ,}\n'
                                f' Winning Percentage : {winning_percentage: .1F}%\n'
                                f' --------------------------------------------\n'
                                )
    print(winning_candidate_summary)
                      

# Print the total_votes should be equal to the total numbers of rows  in elections_results.csv without header 369711
#print(total_votes)  

#print candidate list.
#print(candidate_options)

#print the candidate vote dictionary 
#print(candidate_votes)



