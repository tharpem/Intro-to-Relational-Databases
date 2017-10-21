#!/usr/bin/env python
#.
# tournament.py -- implementation of a Swiss-system tournament
#
import psycopg2
import sys

cnx = psycopg2.connect("dbname='tournament'")
cur = cnx.cursor()

def connect():
#     """Connect to the PostgreSQL database.  Returns a database connection."""
    return psycopg2.connect("dbname='tournament'")


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


def registerPlayer (playername):
    """Adds a player to the tournament database.
    The database assigns a unique serial id number for the player.  (This
    should be handled by your SQL database schema, not in your Python code.)

    Args:
      name: the player's full name (need not be unique).
    """
    #register player in players
    registerSQL = ("INSERT INTO players (name) VALUES (%s);")
    data = (playername,)
    cur.execute(registerSQL, data)
    cnx.commit()
    cur.execute("SELECT Id FROM players ORDER By ID Desc LIMIT 1")#get latest registree Id
    getPlayerID= cur.fetchone()
    getPlayerID = getPlayerID[0]
    getPlayerID = str(getPlayerID)
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
    seePlayerStandingsSQL = """SELECT Player_Stats.id AS ID, Player_Stats.name AS Name, Player_Stats.wins as Wins, Player_Stats.matches AS Matches FROM Player_Stats ORDER BY ranking DESC"""
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
    input_match_SQL = "INSERT INTO match (winner, loser) VALUES (%s, %s)"
    data=(winner, loser)
    cur.execute(input_match_SQL, data)
    cnx.commit()
    return winner



#helper function for swissPairings() to generate list of ID pairs
def createSwissIDPairs(newPair):
    index = 0
    pair_count = 0
    pair_List = []
    ranked_ID_SQL = """SELECT id FROM Player_Stats ORDER BY Ranking DESC"""
    cur.execute(ranked_ID_SQL)
    rows=cur.fetchall()
    #add to pair_list
    for row in rows:
        pair_List.append(row[0])
    for items in pair_List:
        while pair_count <= (len(pair_List)/2)-1:
            id1 = pair_List[index]
            id2 = pair_List[index+1]
            newPair.append([id1, id2])
            index +=2
            pair_count +=1
    return newPair

#helper function for swissPairings() to populat names in list of ID pairs
def addNameSwissIDPairs(newPair):
    pullNamesIDSQL = """SELECT id, name FROM players""" #pull table snapshot of names & inputPlayerStandings
    cur.execute(pullNamesIDSQL)
    rows=cur.fetchall()
    index=0
    for items in newPair:
        id1=newPair[index][0]
        id2=newPair[index][1]
        getNameSQLID1="SELECT name FROM players WHERE id=%s"
        data = (id1,)
        cur.execute(getNameSQLID1, data)
        name1=cur.fetchone()
        getNameSQLID2="SELECT name FROM players WHERE id=%s"
        data = (id2,)
        cur.execute(getNameSQLID1, data)
        name2=cur.fetchone()
        newPair[index]=[newPair[index][0], name1, newPair[index][1], name2]
        index +=1
    return newPair

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
    newPair=[]
    createSwissIDPairs(newPair) #create list of id's
    addNameSwissIDPairs(newPair)    # add names to list and print
    return newPair
