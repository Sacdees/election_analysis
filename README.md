## Overview of Election Audit

Our objective for this data is to assist a Colorado Board of Elections employee, Tom, to tabulate results for U.S Congressional precinct in Colorado.  The target audit is to report the total number of votes cast, the total number of votes for each candidate, the percentage of votes for each candidate and the winner of the election based on the popular vote.  The process is typically performed in Excel, but Toms manager tasked him with automating the process using Python and to make it adaptable to future election audits.

Tom's manager, Seth, would like him to become familiar with the command line, which will be used to make updates to the GitHub repository, access local files and folders, and write and run Python programming scripts and allow Seth to check on Tom's progress on the projects and aid when needed. Seth will run the Python files from the command line and is only concerned about the results displayed.  

# Colorado Congressional District Data
# Election Audit Detail Include: 

- Total number of votes cast in the election: 369,711
- Votes by county:
  - Jefferson: 10.51%, (38,855)
  - Denver: 82.78%, (306,055)
  - Arapahoe: 6.71%, (24,801)
- County with most votes: Denver
- Votes by candidate:
  - Charles Casper Stockham: 23.0% (85,213)
  - Diana DeGette: 73.8% (272,892)
  - Raymon Anthony Doane: 3.1% (11,606)
- Election winner: Diana DeGette
  - Total votes received: 272,892
  - Percentage of votes: 73.8%

## Python Election Analysis Code Summary
The overall result was a successful audit using Python as requested by Toms manager.  Since we were able to successfully automate using Python, Tom can now be able to use the code to audit not only other congressional district, but he can also expand it to many other elections.  By simply manipulating Python code functions, importing other csv data file and exporting or generating new output files, Tom can successfully use the code for Senatorial districts and even local district races such as mayoral or city council elections. The code will continue to be able to support mail-in ballots, punch cards and direct recording machines for all future needs.

