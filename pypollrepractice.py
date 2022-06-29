import csv 
import os
                            # Assign a variable to load a file from a path
                            # to load file and read file
                            # file_to_load = 'resources/election_results.csv'

file_to_load = os.path.join("resources", "election_results.csv")

                            # Assign a variable to save the file to a path
                            # to write a file and save a file ("w" meand write to file, "r" to read, etc.)
file_to_save = os.path.join("analysis","election_practice.txt")

                            #open the election results and read the file
with open (file_to_load) as election_data:
    
    file_reader=csv.reader(election_data)
    headers = next(file_reader)
    print(headers)



#for row in file=reader:
    #print(row)

#with open(file_to_save, "w") as txt_file:
   # txt_file.write("Hello Bootcamp,\n ")
    #txt_file.write("Practice make perfect!,\n ")
    #txt_file.write("We will have to write the codes several times,\n ")
    #----------- \n = new line



