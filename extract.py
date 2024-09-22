import csv
csv_file = "meets/37th_Early_Bird_Open_Mens_5000_Meters_HS_Open_5K_24.csv"
femalecsv_file = "meets/37th_Early_Bird_Open_Womens_5000_Meters_HS_Open_5K_24.csv"
output_file = "earlyBird.html"

with open(malecsv_file, newline='', encoding='utf-8') as file:
    reader = csv.reader(file)
    maledata = list(reader) 

with open(femalecsv_file, newline='', encoding='utf-8') as file:
    reader = csv.reader(file)
    femaledata = list(reader) 

meet_name = maledata[0][0]
meet_date = maledata[1][0]
male_link = maledata[2][0]
female_link = femaledata[2][0]
malemeet_description = ''.join(maledata[3][:])
femalemeet_description = ''.join(femaledata[3][:])

male_teamRank = maledata[7][1]
female_teamRank = femaledata[7][1]

maleteams = maledata[7:25]
femaleteams = femaledata[7:21]

for team in maleteams: 
    maleteam_place = team[0]
    maleteam_name = team[1]
    maleteam_score = team[2]
    print(team)

for team in femaleteams: 
    femaleteam_place = team[0]
    femaleteam_name = team[1]
    femaleteam_score = team[2]
    print(team)