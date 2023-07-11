# Personalization 

Automated sending personalized documents to a long list of recepeints on a weekly basis.

## Content
- personalization.csv
- personalization.py

## Description
1. `personalization.py` script reads csv file from the first argument and generates personalization for each row. 
2. `personalization-done.csv` is then created with all the details of the personalization.

## Installation
Replace `<token>` with your personal Turtl token inside `personalization.py`

## Steps to follow

1. Marketing team will be sending us the file with the list of names and emails for personalization on a weekly basis.

2. Please download the file and run the command inside terminal.

```sh
python3 personalization.py personalization.csv
```
3. Send `personalization-done.csv` back to Marketing team.
