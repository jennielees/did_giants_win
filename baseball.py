import requests

mlb_stats = 'http://gd2.mlb.com/components/game/mlb/year_2014/postseason_scoreboard.json'
response = requests.get(mlb_stats)
result  = response.json()


def who_won(result):
    h = int(result['home'])
    a = int(result['away'])
    if h > a:
        return 'home'
    else:
        return 'away'

def did_giants_win():
    total_giants_wins = 0
    total_royals_wins = 0
    wins_needed = 4

    for game in result['games']:
        if game['description'][:12] == 'World Series':

            linescore = game.get('linescore')

            if linescore == None:
                # This game hasn't happened yet!
                continue

            outcome = linescore['r']
            winner = who_won(outcome)

            mykey = 'away_team_name'
            if game[mykey] == 'Giants':
                print "Giants away, Royals home"
                if winner == 'away':
                    print "Away team won, they were Giants"
                    total_giants_wins += 1
                else:
                    print "Home team won, not the Giants :("
                    total_royals_wins += 1
            elif game['home_team_name'] == 'Giants':
                print "Giants home, Royals away"
                if winner == 'home':
                    print "Home team won, they were Giants"
                    total_giants_wins += 1
                else:
                    print "Away team won, not the Giants :("
                    total_royals_wins += 1

    print "The Giants have won {} games so far. {} total needed!!!".format(total_giants_wins, wins_needed)
    print "The Royals have won {} games so far. {} total needed!!!".format(total_royals_wins, wins_needed)


    if total_giants_wins == wins_needed:
        print "THEY WON!!!!!"
        return "YES"
    elif total_royals_wins == wins_needed:
        print "THEY DIDN'T WIN :( :("
        return "NO"
    else:
        print "Not over yet! Still could happen!"
        return "check back later!"


if __name__=="__main__":
    they_won = did_giants_win()
    print they_won