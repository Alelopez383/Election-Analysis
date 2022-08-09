# Th data we need to rertrieve
# 1. The total number of votes cast.
# 2. A complete list of candidates who received votes
# 3. The percentage of votes each candidate won.
# 4. The total number of votes each candidate won.
# 5. The winner of the election based on popular vote.


import csv

# Assign a variable for the file to load and the path.
file_to_load ='C:/Users/alelo/Documents/BootCamp Tec/Module 3_Python/Challenge 3/Election-Analysis/Resources/election_results.csv'

# Open the election results and read the file.
with open(file_to_load) as election_data:

# To do: perform analysis.
    print(election_data)

############################################################################

# When we dont know the direct path of the file that we want to read, we use 
# the Indirect path, usieng os() module

import os
print(dir(os))

dir(os.path)

#To declare a variable for the file to loa, connect the os.path with the join() fucntion
#Chaining:
# os.path.join()

import ntpath
print(dir(ntpath)) 

# Assign a variable for the file to load and the path.

file_to_load=ntpath.join('Resources','election_results.csv')
with open(file_to_load) as election_data:
     print(election_data)

import csv
import os
# Assign a variable for the file to load and the path. Checar subsecciones de archivos
file_to_load = os.path.join('..','Resources', 'election_results.csv')
# Open the election results and read the file.
with open(file_to_load) as election_data:

    # Print the file object.
     print(election_data)

############################################################################

# WRITE TO FILES: We create a filename variable to a direct or indirect path where the file is.
#Then we use open() with 'w' mode

# Create a filename variable to a direct or indirect path to the file.
file_to_save = os.path.join('..', "analysis", "election_analysis.txt")
# Using the open() function with the "w" mode we will write data to the file.
open(file_to_save, "w")

##########################################################################
#writing in the new folder 'election_analysis.txt'

# Create a filename variable to a direct or indirect path to the file.
file_to_save = os.path.join("..", "analysis", "election_analysis.txt")

# Use the open statement to open the file as a text file.
outfile = open(file_to_save, "w")
# Write some data to the file.
outfile.write("Hello World")
outfile.write('probando')

# Close the file
outfile.close()

#########################################################################

#Now we are doing the same as before but using with() statement instead of open an close functions

# Create a filename variable to a direct or indirect path to the file.
file_to_save = os.path.join("..", "analysis", "election_analysis.txt")

# Using the with statement open the file as a text file.
with open(file_to_save, "w") as txt_file:

    # Write some data to the file.
    txt_file.write("Hello World")

    txt_file.write("probando")

######################################################################

# Now we are going to add some more text: counties

 # Write three counties to the file.
file_to_save = os.path.join("..", "analysis", "election_analysis.txt")
with open(file_to_save, "w") as txt_file:
     txt_file.write("Arapahoe, ")
     txt_file.write("Denver, ")
     txt_file.write("Jefferson.")

#a simpler way to write the counties in one line, using separarte lines, spaces
file_to_save = os.path.join("..", "analysis", "election_analysis.txt")
with open(file_to_save, "w") as txt_file:
    txt_file.write("Counties in the Election\n-----------------\nArapahoe\nDenver\nJefferson")
    
##########################################################################
#Now we are going to read the election results. For taht we are using the .csv file

# 1. Add our dependencies.
import csv
import os

# 2.Assign a variable to load a file from a path.
file_to_load = os.path.join("..","Resources", "election_results.csv")

# 3. Assign a variable to save the file to a path.
file_to_save = os.path.join("..","analysis", "election_analysis.txt")

# 4.Open the election results and read the file. 
#Remember that after : we have to use indentaxion in the next line.
with open(file_to_load) as election_data:

    # 5. To read and analyze the data here with the function reader.
    file_reader = csv.reader(election_data)
    
    #6. To pull the data and print, we use  for method
    for row in file_reader:
        print(row)

        #the output is a list of rows of the csv file.

#Now, to retrieve the first item  from the output we can use:
file_to_load = os.path.join("..","Resources", "election_results.csv")  
file_to_save = os.path.join("..","analysis", "election_analysis.txt")
with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)
    for row in file_reader:
            print(row[0])

#Now, we want to skip the first row, the column headers. For that we use next(file_reader)
# Read the file object with the reader function.
file_to_load = os.path.join("..","Resources", "election_results.csv")  
file_to_save = os.path.join("..","analysis", "election_analysis.txt")
with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)

    # Print the header row, to verify that we are skipping the headers.
    headers = next(file_reader)
    print(headers)
    

#######################################################################

#Using election_results.csv file, get the total votes
# 1. Add the dependencies

import csv
import os

# 2. Assign a variable to load a file from a path

file_to_load=os.path.join("..","Resources", "election_results.csv")

# 3. Assign a variable to save the file to a path

file_to_save= os.path.join('..', 'analysis', 'election_analysis.txt')

# 4. Open the election results and read the file. 
# 4.1 Read the header row
# 4.2 Print each row in the csv file

with open (file_to_load) as election_data:
    file_reader =csv.reader(election_data)
    headers = next(file_reader)
    for row in file_reader:
        print(row)

#########################################################################
#To count up all the votes, we need to initialize a variable, called an accumulator.
# the accumalator will increment by 1 as we read each row in the for loop. 
#For convenience, we will initialize a variable called total_votes to zero.
# 1. Add the total vot counter before the with open () statement
# 2. Open the elections results and read the file with open () 
# 3. Increment the total_votes by 1 after the for() loop
# 4. Print out the total votes


import csv
import os

file_to_load= os.path.join("..","Resources", "election_results.csv")
file_to_save= os.path.join('..', 'analysis', 'election_analysis.txt')

total_votes = 0

with open (file_to_load) as election_data:
    file_reader =csv.reader(election_data)
    headers = next(file_reader)
    
    
    for row in file_reader:
        total_votes += 1
        
        print(total_votes)

##########################################################################
#To get the Candidate in the election, but only the unique candidate names. 
# For that we need to use an IF() statement with the 'not in' membership operator.
#With that, we will add to the list the candidate´s name one time only.
# The if statement has to be nested inside the for loop while iterating through each row

#Now we do it for candidates votes

# Add our dependencies.
import csv
import os
# Assign a variable to load a file from a path.
file_to_load = os.path.join("..","Resources", "election_results.csv")
# Assign a variable to save the file to a path.
file_to_save = os.path.join("..","analysis", "election_analysis.txt")

# Initialize a total vote counter.
total_votes = 0

# Candidate options and candidate votes
candidate_options = []

# 1. Declare the empty dictionary.
candidate_votes = {}

# Open the election results and read the file.
with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)

    # Read the header row.
    headers = next(file_reader)

    # Print each row in the CSV file.
    for row in file_reader:
        # Add to the total vote count.
        total_votes += 1

        # Print the candidate name from each row.
        candidate_name = row[2]

        if candidate_name not in candidate_options:
          # Add the candidate name to the candidate list.
            candidate_options.append(candidate_name)

           # 2. Begin tracking that candidate's vote count.
            candidate_votes[candidate_name] = 0
            
     # Add a vote to that candidate's count. We have to take it out of the if statement, but not from the for loop
        candidate_votes[candidate_name] += 1


# Print the candidate vote dictionary.
print(candidate_votes)
print( candidate_options)

# Determine the percentage of votes for each candidate by looping through the counts.
# 1. Iterate through the candidate list.
for candidate_name in candidate_votes:
    # 2. Retrieve vote count of a candidate.
    votes = candidate_votes[candidate_name]
    # 3. Calculate the percentage of votes.
    vote_percentage = float(votes) / float(total_votes) * 100
    # 4. Print the candidate name and percentage of votes.
    print(f"{candidate_name}: received {vote_percentage:.1f}% of the vote.")
    

# Winning Candidate and Winning Count Tracker
winning_candidate = ""
winning_count = 0
winning_percentage = 0

# Determine winning vote count and candidate
# 1. Determine if the votes are greater than the winning count.
if (votes > winning_count) and (vote_percentage > winning_percentage):
     # 2. If true then set winning_count = votes and winning_percent = vote_percentage.
        winning_count = votes
        winning_percentage = vote_percentage
     # 3. Set the winning_candidate equal to the candidate's name.
        winning_candidate = candidate_name

# Determine the percentage of votes for each candidate by looping through the counts.
# Iterate through the candidate list.
for candidate_name in candidate_votes:
    # Retrieve vote count of a candidate.
    votes = candidate_votes[candidate_name]
    # Calculate the percentage of votes.
    vote_percentage = float(votes) / float(total_votes) * 100

    # Determine winning vote count and candidate
    # Determine if the votes is greater than the winning count.
    if (votes > winning_count) and (vote_percentage > winning_percentage):
         # If true then set winning_count = votes and winning_percent =
         # vote_percentage.
         winning_count = votes
         winning_percentage = vote_percentage
         # And, set the winning_candidate equal to the candidate's name.
         winning_candidate = candidate_name

#  print out each candidate's name, vote count, and percentage of votes

print(f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")
winning_candidate_summary = (
    f"-------------------------\n"
    f"Winner: {winning_candidate}\n"
    f"Winning Vote Count: {winning_count:,}\n"
    f"Winning Percentage: {winning_percentage:.1f}%\n"
    f"-------------------------\n")
print(winning_candidate_summary)