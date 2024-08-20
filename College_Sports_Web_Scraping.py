import requests
from bs4 import BeautifulSoup
import pandas as pd

'''
This scrapes the sports that fall in one calendar year, i.e. 2016, 2017 etc
'''
# Define the list of years you want to scrape
years_to_scrape = list(range(2016, 2023))  # From 2016 to 2022

# Define a list of team names you want to scrape
teams_to_scrape = ["baseball", "cross-country", "football", "womens-soccer", "softball",
                   "womens-volleyball"]  # Add or remove team names as needed

# Create a dictionary to store team names, their data, and dates
team_data = {}

# Loop through the teams
for team in teams_to_scrape:
    # Create a list to store team data for this team
    team_info = []

    # Loop through the years
    for year in years_to_scrape:
        # Generate the URL for the specific year and team
        url = f"https://utahutes.com/sports/{team}/schedule/{year}"

        try:
            # Send a GET request to the URL
            response = requests.get(url)

            if response.status_code == 200:
                html = response.text
            else:
                print(f"Failed to retrieve the webpage for {year}-{team}")
                continue  # Skip to the next year if there's an issue

            soup = BeautifulSoup(html, 'html.parser')

            # Find all elements with the class "sidearm-schedule-game-opponent-name" (div or span)
            opponent_elements = soup.find_all(class_="sidearm-schedule-game-opponent-name")

            # Extract team names, dates, and URLs from each element
            game_data = []

            for element in opponent_elements:
                team_name = element.get_text(strip=True)
                anchor = element.find("a")
                if anchor:
                    date_label = anchor.get("aria-label")
                    if date_label:
                        date = date_label.split(" on ")[-1]  # Extract the date part
                        game_data.append((team_name, date, year))

            team_info.extend(game_data)
        except Exception as e:
            print(f"An error occurred for {year}-{team}: {e}")

    # Create a DataFrame for this team
    df = pd.DataFrame(team_info, columns=["Team Name", "Date", "Year"])

    # Remove duplicates that appear in consecutive rows
    df = df[df['Team Name'] != df['Team Name'].shift()]

    # Store the DataFrame for this team in the dictionary
    team_data[team] = df

# Create an Excel writer to save data to different tabs (worksheets)
excel_file = 'teams_single_year_data_with_dates.xlsx'
with pd.ExcelWriter(excel_file, engine='xlsxwriter') as writer:
    # Iterate through the team data and save each team's data in a separate worksheet
    for team, df in team_data.items():
        df.to_excel(writer, sheet_name=team, index=False)

print(f"Team data with dates has been exported to {excel_file}.")

'''
This scrapes the sports that fall across multiple calendar years, i.e. "2016-17", "2017-18" etc
'''

# Define the list of years to scrape
years_to_scrape = ["2016-17", "2017-18", "2018-19", "2019-20", "2020-21", "2021-22", "2022-23"]  # From 2016 to 2023

# Define a list of team names to scrape
teams_to_scrape = ["mens-basketball", "mens-golf", "womens-basketball", "womens-gymnastics", "mens-swimming-and-diving",
                   "womens-swimming-and-diving", "mens-tennis", "womens-tennis", "track-and-field"]  # Add or remove team names as needed

# Create a dictionary to store team names, their data, and dates
team_data = {}

# Loop through the teams
for team in teams_to_scrape:
    # Create a list to store team data for this team
    team_info = []

    # Loop through the years
    for year in years_to_scrape:
        # Generate the URL for the specific year and team
        url = f"https://utahutes.com/sports/{team}/schedule/{year}"

        try:
            # Send a GET request to the URL
            response = requests.get(url)

            if response.status_code == 200:
                html = response.text
            else:
                print(f"Failed to retrieve the webpage for {year}-{team}")
                continue  # Skip to the next year if there's an issue

            soup = BeautifulSoup(html, 'html.parser')

            # Find all elements with the class "sidearm-schedule-game-opponent-name" (div or span)
            opponent_elements = soup.find_all(class_="sidearm-schedule-game-opponent-name")

            # Extract team names, dates, and URLs from each element
            game_data = []

            for element in opponent_elements:
                team_name = element.get_text(strip=True)
                anchor = element.find("a")
                if anchor:
                    date_label = anchor.get("aria-label")
                    if date_label:
                        date = date_label.split(" on ")[-1]  # Extract the date part
                        game_data.append((team_name, date, year))

            team_info.extend(game_data)
        except Exception as e:
            print(f"An error occurred for {year}-{team}: {e}")

    # Create a DataFrame for this team
    df = pd.DataFrame(team_info, columns=["Team Name", "Date", "Year"])

    # Remove duplicates that appear in consecutive rows
    df = df[df['Team Name'] != df['Team Name'].shift()]

    # Store the DataFrame for this team in the dictionary
    team_data[team] = df

# Create an Excel writer to save data to different tabs (worksheets)
excel_file = 'teams_data_with_dates.xlsx'
with pd.ExcelWriter(excel_file, engine='xlsxwriter') as writer:
    # Iterate through the team data and save each team's data in a separate worksheet
    for team, df in team_data.items():
        df.to_excel(writer, sheet_name=team, index=False)

print(f"Team data with dates has been exported to {excel_file}.")

'''
This scrapes lacrosse schedule info which did not become a varsity sport until 2019
'''
# Define the list of years you want to scrape
lax_years_to_scrape = ["2019", "2020", "2021", "2022", "2023"]  # From 2016 to 2023

# Define a list of team names you want to scrape
teams_to_scrape = ["mens-lacrosse"]  # Add or remove team names as needed

# Create a dictionary to store team names, their data, and dates
team_data = {}

# Loop through the teams
for team in teams_to_scrape:
    # Create a list to store team data for this team
    team_info = []

    # Loop through the years
    for year in lax_years_to_scrape:
        # Generate the URL for the specific year and team
        url = f"https://utahutes.com/sports/{team}/schedule/{year}"

        try:
            # Send a GET request to the URL
            response = requests.get(url)

            if response.status_code == 200:
                html = response.text
            else:
                print(f"Failed to retrieve the webpage for {year}-{team}")
                continue  # Skip to the next year if there's an issue

            soup = BeautifulSoup(html, 'html.parser')

            # Find all elements with the class "sidearm-schedule-game-opponent-name" (div or span)
            opponent_elements = soup.find_all(class_="sidearm-schedule-game-opponent-name")

            # Extract team names, dates, and URLs from each element
            game_data = []

            for element in opponent_elements:
                team_name = element.get_text(strip=True)
                anchor = element.find("a")
                if anchor:
                    date_label = anchor.get("aria-label")
                    if date_label:
                        date = date_label.split(" on ")[-1]  # Extract the date part
                        game_data.append((team_name, date, year))

            team_info.extend(game_data)
        except Exception as e:
            print(f"An error occurred for {year}-{team}: {e}")

    # Create a DataFrame for this team
    df = pd.DataFrame(team_info, columns=["Team Name", "Date", "Year"])

    # Remove duplicates that appear in consecutive rows
    df = df[df['Team Name'] != df['Team Name'].shift()]

    # Store the DataFrame for this team in the dictionary
    team_data[team] = df

# Combine all lacrosse team data into one DataFrame
combined_df = pd.concat(team_data.values(), ignore_index=True)

# Create an Excel writer to save data for lacrosse
excel_file = 'lacrosse_data.xlsx'

# Save the combined DataFrame to the Excel file
combined_df.to_excel(excel_file, index=False)

print(f"Team data with dates has been exported to {excel_file}.")

'''
This scrapes beach volleyball schedule info, also did not become a varsity sport by 2016 start year
used to scrape other sports teams schedules
'''
# Define the list of years you want to scrape
w_vb_years_to_scrape = ["2017", "2018", "2019", "2020", "2021", "2022", "2023"]  # From 2016 to 2023

# Define a list of team names you want to scrape
teams_to_scrape = ["womens-beach-volleyball"]  # Add or remove team names as needed

# Create a dictionary to store team names, their data, and dates
team_data = {}

# Loop through the teams
for team in teams_to_scrape:
    # Create a list to store team data for this team
    team_info = []

    # Loop through the years
    for year in w_vb_years_to_scrape:
        # Generate the URL for the specific year and team
        url = f"https://utahutes.com/sports/{team}/schedule/{year}"

        try:
            # Send a GET request to the URL
            response = requests.get(url)

            if response.status_code == 200:
                html = response.text
            else:
                print(f"Failed to retrieve the webpage for {year}-{team}")
                continue  # Skip to the next year if there's an issue

            soup = BeautifulSoup(html, 'html.parser')

            # Find all elements with the class "sidearm-schedule-game-opponent-name" (div or span)
            opponent_elements = soup.find_all(class_="sidearm-schedule-game-opponent-name")

            # Extract team names, dates, and URLs from each element
            game_data = []

            for element in opponent_elements:
                team_name = element.get_text(strip=True)
                anchor = element.find("a")
                if anchor:
                    date_label = anchor.get("aria-label")
                    if date_label:
                        date = date_label.split(" on ")[-1]  # Extract the date part
                        game_data.append((team_name, date, year))

            team_info.extend(game_data)
        except Exception as e:
            print(f"An error occurred for {year}-{team}: {e}")

    # Create a DataFrame for this team
    df = pd.DataFrame(team_info, columns=["Team Name", "Date", "Year"])

    # Remove duplicates that appear in consecutive rows
    df = df[df['Team Name'] != df['Team Name'].shift()]

    # Store the DataFrame for this team in the dictionary
    team_data[team] = df

# Combine all beach vb team data into one DataFrame
vb_df = pd.concat(team_data.values(), ignore_index=True)

# Create an Excel writer to save data for lacrosse
excel_file = 'beach_vb_data.xlsx'

# Save the combined DataFrame to the Excel file
vb_df.to_excel(excel_file, index=False)

print(f"Team data with dates has been exported to {excel_file}.")

'''
This scrapes ski schedule info, had differing format of years present in the schedule webpages
'''
# Define the list of years you want to scrape
lax_years_to_scrape = ["2016-17", "2017-18", "2018-19", "2019-20", "2020-21", "2022"]  # From 2016 to 2023

# Define a list of team names you want to scrape
teams_to_scrape = ["alpine-skiing"]

# Create a dictionary to store team names, their data, and dates
team_data = {}

# Loop through the teams
for team in teams_to_scrape:
    # Create a list to store team data for this team
    team_info = []

    # Loop through the years
    for year in lax_years_to_scrape:
        # Generate the URL for the specific year and team
        url = f"https://utahutes.com/sports/{team}/schedule/{year}"

        try:
            # Send a GET request to the URL
            response = requests.get(url)

            if response.status_code == 200:
                html = response.text
            else:
                print(f"Failed to retrieve the webpage for {year}-{team}")
                continue  # Skip to the next year if there's an issue

            soup = BeautifulSoup(html, 'html.parser')

            # Find all elements with the class "sidearm-schedule-game-opponent-name" (div or span)
            opponent_elements = soup.find_all(class_="sidearm-schedule-game-opponent-name")

            # Extract team names, dates, and URLs from each element
            game_data = []

            for element in opponent_elements:
                team_name = element.get_text(strip=True)
                anchor = element.find("a")
                if anchor:
                    date_label = anchor.get("aria-label")
                    if date_label:
                        date = date_label.split(" on ")[-1]  # Extract the date part
                        game_data.append((team_name, date, year))

            team_info.extend(game_data)
        except Exception as e:
            print(f"An error occurred for {year}-{team}: {e}")

    # Create a DataFrame for this team
    df = pd.DataFrame(team_info, columns=["Team Name", "Date", "Year"])

    # Remove duplicates that appear in consecutive rows
    df = df[df['Team Name'] != df['Team Name'].shift()]

    # Store the DataFrame for this team in the dictionary
    team_data[team] = df

# Combine all ski team data into one DataFrame
ski_df = pd.concat(team_data.values(), ignore_index=True)

# Create an Excel writer to save data for lacrosse
excel_file = 'ski_data.xlsx'

# Save the combined DataFrame to the Excel file
ski_df.to_excel(excel_file, index=False)

print(f"Team data with dates has been exported to {excel_file}.")