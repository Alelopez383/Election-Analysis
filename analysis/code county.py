# -*- coding: utf-8 -*-
"""
Created on Thu Aug 11 18:33:03 2022

@author: alelo
"""

import csv
import os

file_to_load = os.path.join ('..','Resources', 'election_results.csv')
file_to_save = os.path.join ('..','analysis', 'election_analysis.txt')

total_votes = 0
county_options = []
county_votes = {}

winning_county = ""
winning_count = 0
winning_percentage = 0


with open (file_to_load) as election_data:
    file_reader = csv.reader (election_data)
    header = next(file_reader)
    
    for row in file_reader:
        total_votes += 1
        county_name = row [1]
        
        if county_name not in county_options:
            county_options.append(county_name)
            county_votes [county_name] = 0
        
        county_votes [county_name] += 1

for county_name in county_votes:
    votes = county_votes [county_name]
    vote_percentage = float(votes) / float (total_votes) * 100
    
    print(f"{county_name}: {vote_percentage:.1f}% ({votes:,})\n") 
    
    if (votes > winning_count) and  (vote_percentage > winning_percentage):
        winning_count = votes
        winning_percentage = vote_percentage
        winning_county = county_name
    
winning_county_summary = (
            f"-------------------------\n"
            f"Winner: {winning_county}\n"
            f"Winning Vote Count: {winning_count:,}\n"
            f"Winning Percentage: {winning_percentage:.1f}%\n"
            f"-------------------------\n")
        
print(winning_county_summary)
    
print (winning_county)
    
print (f'{county_name}: received {vote_percentage:.1f}% of the vote.')
    
print(total_votes)
    