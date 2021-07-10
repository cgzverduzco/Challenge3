# -*- coding: UTF-8 -*-
"""PyPoll Homework Challenge Solution."""

# Add our dependencies.
from collections import Counter
import csv
import os

# **********************      Modification 1 uncomment line 10
# It can read other cvs, and generate the analysis about this information. It's has to be in the Resorces folder.
# name_file = input("Enter the name of the csv: ")

# Add a variable to load a file from a path. For Modification 1. Comment line 13
file_to_load = os.path.join("Resources", "election_results.csv")

# ********************** Modification 1 uncomment line 17
#file_to_load = os.path.join("Resources", name_file)

# Add a variable to save the file to a path.
file_to_save = os.path.join("analysis", "election_analysis.txt")

# Initialize a total vote counter.
total_votes = 0

# Candidate Options and candidate votes.
candidate_options = []
candidate_votes = {}

# 1: Create a county list and county votes dictionary.
# This list hold the names of the counties
county_list = []
# This Dictionary hold the county as the key and the votes cast for each county as the values
county_votes = {}

# Track the winning candidate, vote count and percentage
winning_candidate = ""
winning_count = 0
winning_percentage = 0

# 2: Track the largest county and county voter turnout.
# String that hold the county name for the county with the largest turnout.
turnout_county = ""
# Integer that hold the number of votes of the county that had the largest turnout.
turnout_votes = 0
turnout_percentage = 0

""" # ********************** Modification 2 ----------------------------------------------------------- Lines 47 to 74
# Create list for get the uniques values in the colummns in the file
election_options = []   
# Create string for asking
ask_election = "Select election: "
# get de header and uniques string
with open(file_to_load) as election_data:
    reader = csv.reader(election_data)
    # Get the header
    header = next(reader)
# For each row in the CSV file.
    for row in reader:
        election_name = row [3]
        # if the election does not match any existing election in the election options.
        if election_name not in election_options:
            # Add the existing county to the list of counties.
            election_options.append(election_name)
    # Generate the string for the options
    for i in range (0, len(election_options)):
        ask_election = ask_election + "[" + f"{(i+1)}" +"] for " + election_options[i] + " "
# Print the option on console
print (f"\n-------------------------\n"
       f"{ask_election}" )   
# Ask for the option 
election_define = input("Define an election: ")
election_define = election_options[int(election_define)-1]
print (f"-------------------------\n")
# - """


# Read the csv and convert it into a list of dictionaries
with open(file_to_load) as election_data:
    reader = csv.reader(election_data)

    # Read the header
    header = next(reader)

    # For each row in the CSV file.
    for row in reader:

        # ********************** Modification 2
        # Extract the election from each row.
        # election = row [3]

        # Add to the total vote count    
        total_votes = total_votes + 1

        # ********************** Modification 2 - Comment line 92, uncommment 95-96. Indent the lines from 98 to 128 (1 tab)
        # if election == election_define :
        #    total_votes = total_votes + 1

        # Get the candidate name from each row.
        candidate_name = row[2]

        # 3: Extract the county name from each row.
        county_name = row [1]
        
        # If the candidate does not match any existing candidate add it to
        # the candidate list
        if candidate_name not in candidate_options:

            # Add the candidate name to the candidate list.
            candidate_options.append(candidate_name)

            # And begin tracking that candidate's voter count.
            candidate_votes[candidate_name] = 0 

        # Add a vote to that candidate's count
        candidate_votes[candidate_name] += 1

        # 4a: Write an if statement that checks that the
        # county does not match any existing county in the county list.
        if county_name not in county_list:

            # 4b: Add the existing county to the list of counties.
            county_list.append(county_name)

            # 4c: Begin tracking the county's vote count.
            county_votes[county_name] = 0

        # 5: Add a vote to that county's vote count.
        county_votes[county_name] += 1

# Save the results to our text file.
with open(file_to_save, "w") as txt_file:

    # Print the final vote count (to terminal)
    election_results = (
        f"\nElection Results\n"
        
        # ********************** Modification 2
        # f"\n{election_define} Election Results\n"
        
        f"-------------------------\n"
        f"Total Votes: {total_votes:,}\n"
        f"-------------------------\n\n"
        f"County Votes:\n")
    print(election_results, end="")

    txt_file.write(election_results)

    # 6a: Write a for loop to get the county from the county dictionary.
    for county_name in county_votes:
        # 6b: Retrieve the county vote count.
        votes = county_votes.get(county_name)
        # 6c: Calculate the percentage of votes for the county.
        vote_percentage = float(votes) / float(total_votes) * 100

         # 6d: Print the county results to the terminal.
        county_results = (
            f"{county_name}: {vote_percentage:.1f}% ({votes:,})\n")
        print(county_results)

         # 6e: Save the county votes to a text file.
        txt_file.write(county_results)

         # 6f: Write an if statement to determine the winning county and get its vote count.
        if (votes > turnout_votes) and (vote_percentage > turnout_percentage):
            turnout_votes = votes
            turnout_county = county_name
            turnout_percentage = vote_percentage

    # 7: Print the county with the largest turnout to the terminal.
    large_county = (f"\n-------------------------\n"
          f"Largest County Turnout: {turnout_county}\n"
          f"-------------------------\n")
    print(large_county)

    # 8: Save the county with the largest turnout to a text file.
    txt_file.write(large_county)

    # Save the final candidate vote count to the text file.
    for candidate_name in candidate_votes:

        # Retrieve vote count and percentage
        votes = candidate_votes.get(candidate_name)
        vote_percentage = float(votes) / float(total_votes) * 100
        candidate_results = (
            f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")

        # Print each candidate's voter count and percentage to the
        # terminal.
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
