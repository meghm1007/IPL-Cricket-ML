import pickle
import pandas as pd

teams = ['Sunrisers Hyderabad',
 'Mumbai Indians',
 'Royal Challengers Bangalore',
 'Kolkata Knight Riders',
 'Kings XI Punjab',
 'Chennai Super Kings',
 'Rajasthan Royals',
 'Delhi Capitals']

print('Sunrisers Hyderabad\n Mumbai Indians\n Royal Challengers Bangalore\nKolkata Knight Riders \n Kings XI Punjab\n Chennai Super Kings \n Rajasthan Royals \n Delhi Capitals')
choiceT = int(input("Enter Batting Team Number (1-8)"))
if choiceT>8 or choiceT<1:
    exit()

batting_team = teams[choiceT+1]

print('Sunrisers Hyderabad\nMumbai Indians\nRoyal Challengers Bangalore\nKolkata Knight Riders\nKings XI Punjab\nChennai Super Kings\nRajasthan Royals\nDelhi Capitals')
choiceT2 = int(input("Enter Bowling Team Number (1-8): "))

if choiceT2>8 or choiceT2<1:
    exit()

if choiceT==choiceT2:
    exit()

bowling_team = teams[choiceT+1]

print()
print()
cities = ['Hyderabad', 'Bangalore', 'Mumbai', 'Indore', 'Kolkata', 'Delhi',
       'Chandigarh', 'Jaipur', 'Chennai', 'Cape Town', 'Port Elizabeth',
       'Durban', 'Centurion', 'East London', 'Johannesburg', 'Kimberley',
       'Bloemfontein', 'Ahmedabad', 'Cuttack', 'Nagpur', 'Dharamsala',
       'Visakhapatnam', 'Pune', 'Raipur', 'Ranchi', 'Abu Dhabi',
       'Sharjah', 'Mohali', 'Bengaluru']

print('Hyderabad\nBangalore\nMumbai\nIndore\nKolkata\nDelhi\nChandigarh\nJaipur\nChennai\nCape Town\nPort Elizabeth\nDurban\nCenturion\nEast London\nJohannesburg\nKimberley\nBloemfontein\nAhmedabad\nCuttack\nNagpur\nDharamsala\nVisakhapatnam\nPune\nRaipur\nRanchi\nAbu Dhabi\nSharjah\nMohali\nBengaluru')
choiceC = (input("Enter City: "))
selected_city = choiceC
print()
print()
pipe = pickle.load(open('pipe.pkl','rb'))

target = int(input("Input the target:"))
score = int(input("Enter the score:"))
wickets = int(input("Enter the wickets out:"))
overs = float(input("Enter the number of overs:"))

runs_left = target - score
balls_left = 120 - (overs*6)
wickets = 10 - wickets
crr = score/overs
rrr = (runs_left*6)/balls_left

input_df = pd.DataFrame(
    {'batting_team': [batting_team], 'bowling_team': [bowling_team], 'city': [selected_city], 'runs_left': [runs_left],
     'balls_left': [balls_left], 'wickets': [wickets], 'total_runs_x': [target], 'crr': [crr], 'rrr': [rrr]})

result = pipe.predict_proba(input_df)
loss = result[0][0]
win = result[0][1]
print(batting_team + "- " + str(round(win*100)) + "%")
print(bowling_team + "- " + str(round(loss*100)) + "%")