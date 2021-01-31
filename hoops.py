#import random function to randomly choose teams
import random as rand

#create dictionary for teams
dic = {}
#create team dictionary for total of wins
win = {}
#variable for teams
teams = ["Celtics", "Bulls", "Raptors", "Bucks", "Magic", "76ers", "Lakers"]
#variable for team's skill level
skill_level =[96, 83, 88, 94, 82, 91, 98]

#assigning key and value to dictionary
for num in range(len(teams)):
    dic[teams[num]]=skill_level[num]
#assigned value of 0 for each team in win dictionary
    win[teams[num]]=0
print(win)
print(dic)

#randomly choosing 7 games - 2 teams play each other
for i in range(8):

    team1 = rand.choice(list(dic.keys()))
    team2 = rand.choice(list(dic.keys()))

#if a team is chosen twice, it will randomly choose another combination of teams
    while team1 == team2:
        team1 = rand.choice(list(dic.keys()))
        team2 = rand.choice(list(dic.keys()))


    print("Todays Match: " + team1 + " vs " + team2)

#comparing team's skill value to see who wins game
    if dic[team1] > dic[team2]:
        print(team1 + " wins the game!")
#Add 1 to team 1's win score in win dictionary
        win[team1]+=1
    else:
#Increment 1 to team 2's win score in win dictionary
        print(team2 + " wins the game!")
        win[team2]+=1

#creating list of values for team wins [values]
win_values = list(win.values())
#creating list of team names for teams [keys]
win_keys = list(win.keys())
print(win_values)
#find highest number of wins from list of teams
max_value = max(win_values)
#print out team name [key] that won the most games
print(win_keys[win_values.index(max_value)] + " won the most games out of all other teams!")
#print(win_values.index(max_value))
    





        


#print("Upcoming Games: \n")

#for home_team in teams:
    #for away_team in teams:
       # if home_team != away_team:
            #print(home_team + " vs " + away_team)

