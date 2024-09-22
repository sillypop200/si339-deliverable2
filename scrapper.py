import csv

html_template = '''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset = "UTF-8"> 
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title> {meet_name} </title>
</head>
<body>
    <header> 
        <nav>
            <li><a href="index.html">Home</a></li>
            <li><a href="#meetSummary">Meet Summary</a></li>
            <li><a href="#meetPhotoBook">Meet Photo Book</a></li>
            <li><a href="#meetIndividualResults">Meet Individual Results</a></li>
        </nav>
        <h1>{meet_name}</h1>
        <h3>{meet_date}</h3>
    </header>
        <!-- Section for Meet Summary -->
        <section id = "meetSummary"> 
            <h1> Meet Summary </h1>
            <p> {meet_description}</p>
        </section>

        <!-- Section for Meet Photos -->
        <section id = "meetPhotoBook"> 
            <h1> Meet Photo Book </h1>
            <div id = "photoBook">
                <div class = "photo">
                    <img src = "earlybird/IMG_9043.jpg" alt= "Meet Photo 1">
                </div>
                <div class = "photo">
                    <img src = "earlybird/IMG_9049.jpg" alt= "Meet Photo 2">
                </div>
                <div class = "photo">
                    <img src = "earlybird/IMG_9051.jpg" alt= "Meet Photo 3">
                </div>
                <div class = "photo">
                    <img src = "earlybird/IMG_9037.jpg" alt= "Meet Photo 3">
                </div>
            </div>
        </section>

        <!-- Section for Team Results -->
        <section id = "meetTeamResults"> 
            <h1> Meet Team Results </h1>
            <table id = "meet-team-results">
                <thead>
                    <th>Place</th>
                    <th>Team Name</th>
                    <th>Score</th>
                </thead>
                <tbody>
                    {team_results}
                </tbody>
            </table>
        </section>

        <!-- Section for Individual Results -->
        <section id = "meetIndividualResults"> 
            <h1> Meet Individual Results </h1>
            <table id = "meet-individal-results">
                <thead>
                    <th>Place</th>
                    <th>Name</th>
                    <th>Time</th>
                    <th>Grade</th>
                    <th>Team</th>
                    <th>Athletic.Net Link</th>
                </thead>
                <tbody>
                    {individual_results}
                </tbody>
            </table>
        </section>
</body>
</html>
'''

# This function formats rows for teams
def format_team_row(team):
    return f'''
                    <tr class = "team-row">
                        <td class = "team-placing">{team[0]}</td>
                        <td class = "team-name">{team[1]}</td>
                        <td class = "team-score">{team[2]}</td>
                    </tr>
'''

# This function formats rows for individuals
def format_individual_row(athlete):
    return f'''
                    <tr class = "athlete-row">
                        <td class = "athlete-placing">{athlete[0]}</td>
                        <td class = "athlete-name">{athlete[2]}</td>
                        <td class = "athlete-time">{athlete[4]}</td>
                        <td class = "athlete-grade">{athlete[1]}</td>
                        <td class = "athlete-team">{athlete[5]}</td>
                        <td class = "athlete-link"><a href="{athlete[3]}">Link</a></td>
                    </tr>
'''

# Reading data from CSV and constructing the HTML page
def create_html_from_csv(csv_file, output_html):
    with open(csv_file, newline='', encoding='utf-8') as csvfile:
        reader = csv.reader(csvfile)
        rows = list(reader)

        # Assuming the CSV file contains headers and correct data
        meet_name = rows[0][0]
        meet_date = rows[1][0]
        meet_description = rows[3][0]
        
        # Dynamically find the start indices
        team_start_index = None
        individual_start_index = None
        for i, row in enumerate(rows):
            if row[:3] == ['Place', 'Team', 'Score']:
                team_start_index = i + 1
            if row[:8] == ['Place', 'Grade', 'Name', 'Athlete Link', 'Time', 'Team', 'Team Link', 'Profile Pic']:
                individual_start_index = i + 1
                break

        if team_start_index is None or individual_start_index is None:
            raise ValueError("Error: Could not find the required headers in the CSV.")

        team_results = rows[team_start_index:individual_start_index - 1]
        individual_results = rows[individual_start_index:]

        # Check if team row has exactly 3 columns
        team_results = [team for team in team_results if len(team) >= 3]
        # Check if individual row has exactly 8 columns
        individual_results = [individual for individual in individual_results if len(individual) >= 8]

        team_results_html = ''.join([format_team_row(team) for team in team_results])
        individual_results_html = ''.join([format_individual_row(individual) for individual in individual_results])

        html_content = html_template.format(
            meet_name=meet_name,
            meet_date=meet_date,
            meet_description=meet_description,
            team_results=team_results_html,
            individual_results=individual_results_html
        )

        with open(output_html, 'w', encoding='utf-8') as html_file:
            html_file.write(html_content)

# File paths
csv_file = 'meets/37th_Early_Bird_Open_Womens_5000_Meters_HS_Open_5K_24.csv'
output_html = '{meet_name}.html'

# Create the html file
create_html_from_csv(csv_file, output_html)