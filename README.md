# Election-Analysis
Election auditing of the tabulated results for US Congressional precint of Colorado using Python and Spyder Code Editor.


##**Overview of Election Audit:** 
The purpose of the study in question is to audit the votes of the US Congressional precint of Colorado election. With this analysis, we want to confirm and give certainty of the results, regardless of the winner.

In addition, we seek to find a simple and effective way to count votes with a high level of confidence in the results; for this, a code is ought that can be replicated in other parliamentary elections.

##**Election-Audit Results:**
Using a bulleted list, address the following election outcomes. Use images or examples of your code as support where necessary.

-How many votes were cast in this congressional election?

-Provide a breakdown of the number of votes and the percentage of total votes for each county in the precinct.

-Which county had the largest number of votes?

-Provide a breakdown of the number of votes and the percentage of the total votes each candidate received.

-Which candidate won the election, what was their vote count, and what was their percentage of the total votes?

**Election-Audit Summary:**
In a summary statement, provide a business proposal to the election commission on how this script can be used—with some modifications—for any -election. Give at least two examples of how this script can be modified to be used for other elections.
One of the purposes of the work carried out in this electoral audit is that it can be replicated in other congresses in other states. Before showing the general code, it is necessary to specify certain rules to follow. First of all, it is very important to know the directory of the file where the information to be audited is located. Second, Python has the advantage of reading almost any kind of database, just checking that we have the command to download it, if not, we can just import the library to our code editor. Thrid, 
Now, the code model:
### Add our dependencies/libraries to open the files, if neccessary.
### Add file_variables to load and to save the file. For that we need to know the path (directly or indirectly)
file_to_load = os.path.join("..", "..", "file.csv")
file_to_save = os.path.join("..","..", "file.txt")

###Declare all the variables, with this is not neccessary to know the names of the candidates or the counties.
total_votes = 0
candidate_options = []
candidate_votes = {}
winning_candidate = ""
winning_count = 0
winning_percentage = 0


### Read the csv and convert it into a list of dictionaries
#So any dataset will be easy to access
with open(file_to_load) as election_data:
     reader = csv.reader(election_data)
     header = next(reader)
     for row in reader:
        total_votes += 1
        candidate_name = row['index number for the position of the candidate name in the list']

        # Loop to go throught all the rows and extract the information
        if candidate_name not in candidate_options:
            candidate_options.append(candidate_name)
            candidate_votes[candidate_name] = 0
        candidate_votes[candidate_name] += 1

### Save the results to our text file.
with open(file_to_save, "w") as txt_file:

    # Print the final vote count (to terminal)
     election_results = (
        f"\nElection Results\n"
        f"-------------------------\n"
        f"Total Votes: {total_votes:,}\n"
        f"-------------------------\n\n")
    
     print(election_results, end="")

     txt_file.write(election_results)

    # Save the final candidate vote count to the text file.
     for candidate_name in candidate_votes:

        # Retrieve vote count and percentage
        votes = candidate_votes.get(candidate_name)
        vote_percentage = float(votes) / float(total_votes) * 100
        candidate_results = (
            f'\n'
            f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")

        print(candidate_results)
        #  Save the candidate results to our text file.
        txt_file.write(candidate_results)

        # Determine winning vote count, winning percentage, and candidate.
        if (votes > winning_count) and (vote_percentage > winning_percentage):
            winning_count = votes
            winning_candidate = candidate_name
            winning_percentage = vote_percentage

    # Print the winning candidate (to terminal)
     winning_candidate_summary = (
        f"-------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"Winning Vote Count: {winning_count:,}\n"
        f"Winning Percentage: {winning_percentage:.1f}%\n"
        f"-------------------------\n")
     print(winning_candidate_summary)

    # Save the winning candidate's name to the text file
     txt_file.write(winning_candidate_summary)

