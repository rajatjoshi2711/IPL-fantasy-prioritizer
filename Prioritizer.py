import csv
import pandas as pd
import operator

with open('ipl.csv') as csvfile:
    reader = csv.reader(x.replace('\0', '') for x in csvfile)

df = pd.read_csv('ipl.csv', names=['Match_no', 'Team1', 'Team2', 'Date', 'Time', 'Venue', 'Stadium'])
# print(df)

dict_teams = {"CSK": 0, "DD": 0, "KKR": 0, "KXP": 0, "MI": 0, "RR": 0, "RCB": 0, "SRH": 0}
last_match_number = input("What was the match number of last match that took place?\nAns: ")
last_match_number_int = int(last_match_number)
next_match_int = int(last_match_number) + 1
next_match_str = str(next_match_int)

team_1 = df.iloc[next_match_int - 1, 1]
team_2 = df.iloc[next_match_int - 1, 2]

print("Next match is match number "+next_match_str+" between '"+team_1+"' and '"+team_2+"'.")

count = 10      # Number of next matches to be considered
i = 0

while i <= 10:
    team_1 = df.iloc[next_match_int - 1 + i, 1]
    team_2 = df.iloc[next_match_int - 1 + i, 2]
    dict_teams[team_1] += count
    dict_teams[team_2] += count
    count = count - 1
    i = i + 1

sorted_dict_teams = sorted(dict_teams.items(), key=operator.itemgetter(1))

print("\nPriorities: ")
print(sorted_dict_teams)
