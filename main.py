from bs4 import BeautifulSoup
import requests
import csv

URL = "https://www.nba.com/stats"
response = requests.get(URL)

soup = BeautifulSoup(response.content, 'html.parser')


player_name_tags = soup.find_all('a', class_='Anchor_anchor__cSc3P LeaderBoardPlayerCard_lbpcTableLink__MDNgL')

# Extract the text from each tag
all_stats = [tag.text for tag in player_name_tags]

most_points_stats = all_stats[:10]

most_points_yesterday = []

for players in most_points_stats:
    most_points_yesterday.append(players)
    
player_names_most_points = [name for name in most_points_yesterday if not name.isdigit()]
most_points = [point for point in most_points_yesterday if  point.isdigit()]
players_data = zip(player_names_most_points, most_points)

filename = "stats_last_game.csv"

with open(filename, "w", newline='') as csv_file:
    csv_writer = csv.writer(csv_file)
    csv_writer.writerow(["Player", "Points"])
    for player in players_data:
        csv_writer.writerow([player[0], player[1]])
    