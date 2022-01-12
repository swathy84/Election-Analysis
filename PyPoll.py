#Add our denpendencies. 
import os
import csv

#assign vairalbe toload a file from a path 
file_to_load = os.path.join("Resources","election_results.csv")
#assign a vairable to save the file to a path. 
file_to_save = os.path.join("analysis","election_analysis.txt")

#open the ealection results and read a file . 
with open(file_to_load) as election_data:
    #to do : read and analyze the data here.
    #read the file objects with a reader function 
    file_reader = csv.reader(election_data)

    #Print the header row 
   # headers = next(file_reader)
   # print(headers)


    #print each row in the csv file .
   for row in file_reader:
       print(row)
