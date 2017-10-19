#!/usr/bin/env python
#.
# tournament.py -- implementation of a Swiss-system tournament
#
import psycopg2
import sys

def connect():
#     """Connect to the PostgreSQL database.  Returns a database connection."""
    return psycopg2.connect("dbname='tournament'")

connect()
cnx = psycopg2.connect("dbname='tournament'")
cur = cnx.cursor()

def deletePlayers():
    """Remove all the player records from the database."""
    deletePlayersSQL = "DELETE FROM players"
    cur.execute(deletePlayersSQL)
    cnx.commit()
    return deletePlayersSQL

def deleteMatches():
    """Remove all the match records from the database."""
    deleteMatchesSQL = "DELETE FROM match"
    cur.execute(deleteMatchesSQL)
    cnx.commit()
    return deleteMatchesSQL


def seeRegisteredPlayers():
    cur.execute("SELECT * FROM players")
    rows = cur.fetchall()
    for row in rows:
        print (row)

# #helper function for registerPlayer to input registered player into the playerStandings table
# #default wins and matches of 0
def inputPlayerStandings(playername, getPlayerID):
    cur.execute("INSERT INTO Player_Stats (id, name) VALUES ('" + getPlayerID + "', '"+ playername + "')")
    cnx.commit()
    return getPlayerID

def registerPlayer (playername):
    """Adds a player to the tournament database.
    The database assigns a unique serial id number for the player.  (This
    should be handled by your SQL database schema, not in your Python code.)

    Args:
      name: the player's full name (need not be unique).
    """
    #register player in players
    registerSQL = ("INSERT INTO players (name) VALUES('" + playername +"')")
    cur.execute(registerSQL)
    cnx.commit()
    cur.execute("SELECT Id FROM players ORDER By ID Desc LIMIT 1")#get latest registree Id
    getPlayerID= cur.fetchone()
    getPlayerID = getPlayerID[0]
    getPlayerID = str(getPlayerID)
    inputPlayerStandings(playername, getPlayerID)
    cnx.commit()
    return registerSQL

def countPlayers():
    """Returns the number of players currently registered."""
    countPlayersSQL = 'SELECT COUNT(name) FROM players'
    cur.execute(countPlayersSQL)
    rows = cur.fetchone()
    for row in rows:
        print (rows[0])
    playerCount = rows[0]
    return playerCount

def playerStandings():
    """Returns a list of the players and their win records, sorted by wins.
    The first entry in the list should be the player in first place, or a player
    tied for first place if there is currently a tie.

    Returns:
      A list of tuples, each of which contains (id, name, wins, matches):
        id: the player's unique id (assigned by the database)
        name: the player's full name (as registered)
        wins: the number of matches the player has won
        matches: the number of matches the player has played
    """
    seePlayerStandingsSQL = """SELECT Player_Stats.id AS ID, Player_Stats.name AS Name, Player_Stats.wins as Wins, Player_Stats.matches AS Matches FROM Player_Stats ORDER BY ranks DESC"""
    cur.execute(seePlayerStandingsSQL)
    rows = cur.fetchall()
    for row in rows:
        print (row)
    return rows

def reportMatch(winner, loser):
    """Records the outcome of a single match between two players.

    Args:
      winner:  the id number of the player who won
      loser:  the id number of the player who lost
    """
    winner = str(winner)
    loser = str(loser)
    input_match_SQL = """INSERT INTO match (winner, loser) VALUES ('""" + winner + """', '""" + loser + """')"""
    cur.execute(input_match_SQL)
    cnx.commit()
    adjustWinnerStats(winner)
    adjustWinnerStats(loser)
    return winner

# def adjustWinnerStats(winner):
#     findWinSQL="""SELECT (wins, matches) FROM Player_Stats WHERE id = '""" + winner + """'"""
#     cur.execute(findWinSQL)
#     wins_Matches= cur.fetchone()
#     winner_Wins = wins_Matches[0][1]
#     winner_Wins = int(winner_Wins)
#     winner_Wins += 1
#     winner_Matches = wins_Matches[0][3]
#     winner_Matches = int(winner_Matches)
#     winner_Matches +=1
#     player_rank = winner_Matches/winner_Wins
#     player_rank = str(player_rank)
#     winner_Wins = str(winner_Wins)
#     winner_Matches = str(winner_Matches)
#     addWin = """UPDATE Player_Stats SET
#     wins = '"""+ winner_Wins + """', matches = '""" + winner_Matches + """', ranks = '""" + player_rank + """' WHERE id ='""" + winner + """'"""
#     cur.execute(addWin)
#     cnx.commit()
#
# def adjustWinnerStats(loser):
#     findWinSQL="""SELECT (wins, matches) FROM Player_Stats WHERE id = '""" + loser + """'"""
#     cur.execute(findWinSQL)
#     wins_Matches= cur.fetchone()
#     loser_Matches = wins_Matches[0][3]
#     loser_Matches = int(loser_Matches)
#     loser_Matches +=1
#     loser_Matches = str(loser_Matches)
#     addLose = """UPDATE Player_Stats SET matches = '""" + loser_Matches + """' WHERE id ='""" + loser + """'"""
#     cur.execute(addLose)
#     cnx.commit()

#helper function for swissPairings to clear prior data
def deleteSwissPairs():
    delete_Swiss_SQL = """DELETE FROM Swiss_Pairs"""
    cur.execute(delete_Swiss_SQL)
    cnx.commit()

#helper function for swissPairings to add names from players table to Swiss_Pairs table
def addingNames():
    add_Name1_SQL="""INSERT INTO match (player1_id) VALUES players.name FROM players WHERE match.player1_id = players.id """
    cur.execute(add_Name1_SQL)
    cnx.commit()
    add_Name2_SQL = """INSERT INTO match (player2_id) VALUES players.name FROM players WHERE match.player2_id = players.id """
    cur.execute(add_Name2_SQL)
    cnx.commit()

    # add_Name1_SQL = """UPDATE Swiss_Pairs SET name1 = players.name FROM players WHERE Swiss_Pairs.id1 = players.id"""
    # cur.execute(add_Name1_SQL)
    # cnx.commit()
    # add_Name2_SQL = """UPDATE Swiss_Pairs SET name2 = players.name FROM players WHERE Swiss_Pairs.id2= players.id"""
    # cur.execute(add_Name2_SQL)
    # cnx.commit()

#helper function for swissPairings to show pairings from Swiss_Pairs
def show_Swiss_Pairs():
    swissListSQL = """SELECT * FROM match WHERE winner=null"""
    cur.execute(swissListSQL)
    rows = cur.fetchall()
    for row in rows:
        print (row)
    return rows

def swissPairings():
    """Returns a list of pairs of players for the next round of a match.
    Assuming that there are an even number of players registered, each player
    appears exactly once in the pairings.  Each player is paired with another
    player with an equal or nearly-equal win record, that is, a player adjacent
    to him or her in the standings.

    Returns:
      A list of tuples, each of which contains (id1, name1, id2, name2)
        id1: the first player's unique id
        name1: the first player's name
        id2: the second player's unique id
        name2: the second player's name
     """
    index = 0
    pair_count = 0
    pair_List = []
    deleteSwissPairs()
    ranked_ID_SQL = """SELECT id FROM Player_Stats ORDER BY Ranks DESC"""
    cur.execute(ranked_ID_SQL)
    rows=cur.fetchall()
    #add to pair_list
    for row in rows:
        pair_List.append(row[0])
    while pair_count <= countPlayers()/2 - 2:
        id1 = pair_List[index]
        id2 = pair_List[index+1]
        swiss_Insertion_SQL = """INSERT INTO match (id1, id2) VALUES ('""" + id1 + """', '""" + id2 + """')"""
        cur.execute(swiss_Insertion_SQL)
        cnx.commit()
        index +=2
        pair_count +=1
    show_Swiss_Pairs()
    addingNames()
    return rows


cur.close()
cnx.close()
