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