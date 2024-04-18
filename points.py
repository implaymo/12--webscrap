from bs4 import BeautifulSoup
import requests
import csv

URL = "https://www.nba.com/stats"
response = requests.get(URL)

soup = BeautifulSoup(response.content, 'html.parser')


def yesterday_results(list, list2):
    for player in list:
        list2.append(player)


player_name_tags = soup.find_all('a', class_='Anchor_anchor__cSc3P LeaderBoardPlayerCard_lbpcTableLink__MDNgL')

all_stats = [tag.text for tag in player_name_tags]


## Player Points
most_points_stats = all_stats[:10]

most_points_yesterday = []

yesterday_results(list=most_points_stats, list2=most_points_yesterday)
    
player_names_most_points = [name for name in most_points_yesterday if not name.isdigit()]
most_points = [point for point in most_points_yesterday if  point.isdigit()]


## Player Rebounds    
most_rebound_stats = all_stats[10:20]

most_rebound_yesterday = []

yesterday_results(list=most_rebound_stats, list2=most_rebound_yesterday)

player_names_most_rebounds = [name for name in most_rebound_yesterday if not name.isdigit()]
most_rebounds = [point for point in most_rebound_stats if point.isdigit()]
players_data = zip(player_names_most_points, most_points, player_names_most_rebounds, most_rebounds)

filename = "stats_last_game.csv"

with open(filename, "w", newline='') as csv_file:
    csv_writer = csv.writer(csv_file)
    csv_writer.writerow(["Most Points", "Total Points", "Most Rebounds", "Total Rebounds"])
    for player in players_data:
        csv_writer.writerow([player[0], player[1], player[2], player[3]])
    
    

