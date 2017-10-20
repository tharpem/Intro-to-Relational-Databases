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

# def inputPlayerStandings(playername, getPlayerID):
#     cur.execute("INSERT INTO Player_Stats (id, name) VALUES ('" + getPlayerID + "', '"+ playername + "')")
#     cnx.commit()
#     return getPlayerID
unplayedMatch = []

# def pullMatchedId():
#     cur.execute("""SELECT player1_id FROM match WHERE winner=Null""")
#     matchedrows=cur.fetchall()
#     for row in matchedrows:
#         unplayedMatch.append()
#     cur.execute("""SELECT player2_id FROM match WHERE winner=Null""")
#     matched2rows=cur.fetchall()
#     for row in matched2rows:
#         unplayedMatch.append()
#     return unplayedMatch

# def inputFirstMatch(getPlayerID):
#     pullMatchedId()
#     for items in unplayedMatch:
#         if getPlayerID NOT IN unplayedMatch:
#         pair_List.append()
#     cur.execute("INSERT INTO Player_Stats (id, name) VALUES ('" + getPlayerID + "', '"+ playername + "')")
#     cnx.commit()
#     return getPlayerID


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
    # inputFirstMatch(getPlayerID)
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
    # cur.execute("SELECT matchID FROM match WHERE (winner = player1_id or winner = player2_ID) AND (loser = player1_id or loser = player2_id)")
    # reportMatchID=cur.fetchone()
    # print (reportMatchID)
    input_match_SQL = "INSERT INTO match (winner, loser) VALUES (%s, %s)"
    # WHERE matchID=(%s)"
    data=(winner, loser)
    cur.execute(input_match_SQL, data)
    cnx.commit()
    # adjustWinnerStats(winner)
    # adjustWinnerStats(loser)
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
# def deleteSwissPairs():
#     delete_Swiss_SQL = """DELETE FROM Swiss_Pairs"""
#     cur.execute(delete_Swiss_SQL)
#     cnx.commit()

#helper function for swissPairings to add names from players table to Swiss_Pairs table
def addingNames():
    add_Name1_SQL="INSERT INTO match (player1_id) VALUES (%s) FROM players WHERE match.player1_id = players.id "
    data = players.name
    cur.execute(add_Name1_SQL, data)
    cnx.commit()
    add_Name2_SQL = "INSERT INTO match (player2_id) VALUES (%s) FROM players WHERE match.player2_id = players.id "
    data =players.name
    cur.execute(add_Name2_SQL, data)
    cnx.commit()

    # add_Name1_SQL = """UPDATE Swiss_Pairs SET name1 = players.name FROM players WHERE Swiss_Pairs.id1 = players.id"""
    # cur.execute(add_Name1_SQL)
    # cnx.commit()
    # add_Name2_SQL = """UPDATE Swiss_Pairs SET name2 = players.name FROM players WHERE Swiss_Pairs.id2= players.id"""
    # cur.execute(add_Name2_SQL)
    # cnx.commit()

#helper function for swissPairings to show pairings from Swiss_Pairs
# def show_Swiss_Pairs():
#     swissListSQL = """SELECT * FROM match WHERE winner=null"""
#     cur.execute(swissListSQL)
#     rows = cur.fetchall()
#     for row in rows:
#         print (row)
#     return rows

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
            print (id1)
            id2 = pair_List[index+1]
            print (id2)
            newPair.append([id1, id2])
            print (newPair)
            index +=2
            pair_count +=1
    print(newPair)
    print("finished createSwiss")
    return newPair

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
        print (name1)
        getNameSQLID2="SELECT name FROM players WHERE id=%s"
        data = (id2,)
        cur.execute(getNameSQLID1, data)
        name2=cur.fetchone()
        newPair[index]=[newPair[index][0], name1, newPair[index][1], name2]
        print (newPair[index])
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

#
# def testCount():
#     """
#     Test for initial player count,
#              player count after 1 and 2 players registered,
#              player count after players deleted.
#     """
#     deleteMatches()
#     print("Passed test count deleteMatches")
#     deletePlayers()
#     c = countPlayers()
#     if c == '0':
#         raise TypeError(
#             "countPlayers should return numeric zero, not string '0'.")
#     if c != 0:
#         raise ValueError("After deletion, countPlayers should return zero.")
#     print ("1. countPlayers() returns 0 after initial deletePlayers() execution.")
#     registerPlayer("Chandra Nalaar")
#     c = countPlayers()
#     if c != 1:
#         raise ValueError(
#             "After one player registers, countPlayers() should be 1. Got {c}".format(c=c))
#     print ("2. countPlayers() returns 1 after one player is registered.")
#     print("Passed first registration")
#     registerPlayer("Jace Beleren")
#     c = countPlayers()
#     if c != 2:
#         raise ValueError(
#             "After two players register, countPlayers() should be 2. Got {c}".format(c=c))
#     print ("3. countPlayers() returns 2 after two players are registered.")
#     print("Passed second registration")
#
#     deletePlayers()
#     c = countPlayers()
#     if c != 0:
#         raise ValueError(
#             "After deletion, countPlayers should return zero.")
#     print ("4. countPlayers() returns zero after registered players are deleted.\n5. Player records successfully deleted.")
# testCount()
#
# def testStandingsBeforeMatches():
#     """
#     Test to ensure players are properly represented in standings prior
#     to any matches being reported.
#     """
#     deleteMatches()
#     deletePlayers()
#     registerPlayer("Melpomene Murray")
#     registerPlayer("Randy Schwartz")
#     standings = playerStandings()
#     if len(standings) < 2:
#         raise ValueError("Players should appear in playerStandings even before "
#                          "they have played any matches.")
#     elif len(standings) > 2:
#         raise ValueError("Only registered players should appear in standings.")
#     if len(standings[0]) != 4:
#         raise ValueError("Each playerStandings row should have four columns.")
#     [(id1, name1, wins1, matches1), (id2, name2, wins2, matches2)] = standings
#     if matches1 != 0 or matches2 != 0 or wins1 != 0 or wins2 != 0:
#         raise ValueError(
#             "Newly registered players should have no matches or wins.")
#     if set([name1, name2]) != set(["Melpomene Murray", "Randy Schwartz"]):
#         raise ValueError("Registered players' names should appear in standings, "
#                          "even if they have no matches played.")
#     print ("6. Newly registered players appear in the standings with no matches.")
#
# testStandingsBeforeMatches()

# def testReportMatches():
#     """
#     Test that matches are reported properly.
#     Test to confirm matches are deleted properly.
#     """
#     deleteMatches()
#     deletePlayers()
#     registerPlayer("Bruno Walton")
#     registerPlayer("Boots O'Neal")
#     registerPlayer("Cathy Burton")
#     registerPlayer("Diane Grant")
#     standings = playerStandings()
#     [id1, id2, id3, id4] = [row[0] for row in standings]
#     reportMatch(id1, id2)
#     reportMatch(id3, id4)
#     standings = playerStandings()
#     for (i, n, w, m) in standings:
#         if m != 1:
#             raise ValueError("Each player should have one match recorded.")
#         if i in (id1, id3) and w != 1:
#             raise ValueError("Each match winner should have one win recorded.")
#         elif i in (id2, id4) and w != 0:
#             raise ValueError("Each match loser should have zero wins recorded.")
#     print ("7. After a match, players have updated standings.")
#     deleteMatches()
#     standings = playerStandings()
#     if len(standings) != 4:
#         raise ValueError("Match deletion should not change number of players in standings.")
#     for (i, n, w, m) in standings:
#         if m != 0:
#             raise ValueError("After deleting matches, players should have zero matches recorded.")
#         if w != 0:
#             raise ValueError("After deleting matches, players should have zero wins recorded.")
#     print ("8. After match deletion, player standings are properly reset.\n9. Matches are properly deleted.")
#
# testReportMatches()

def testPairings():
    """
    Test that pairings are generated properly both before and after match reporting.
    """
    deleteMatches()
    deletePlayers()
    registerPlayer("Twilight Sparkle")
    registerPlayer("Fluttershy")
    registerPlayer("Applejack")
    registerPlayer("Pinkie Pie")
    registerPlayer("Rarity")
    registerPlayer("Rainbow Dash")
    registerPlayer("Princess Celestia")
    registerPlayer("Princess Luna")
    standings = playerStandings()
    [id1, id2, id3, id4, id5, id6, id7, id8] = [row[0] for row in standings]
    print("startSwiss")
    pairings = swissPairings()
    if len(pairings) != 4:
        raise ValueError(
            "For eight players, swissPairings should return 4 pairs. Got {pairs}".format(pairs=len(pairings)))
    reportMatch(id1, id2)
    reportMatch(id3, id4)
    reportMatch(id5, id6)
    reportMatch(id7, id8)
    pairings = swissPairings()
    if len(pairings) != 4:
        raise ValueError(
            "For eight players, swissPairings should return 4 pairs. Got {pairs}".format(pairs=len(pairings)))
    [(pid1, pname1, pid2, pname2), (pid3, pname3, pid4, pname4), (pid5, pname5, pid6, pname6), (pid7, pname7, pid8, pname8)] = pairings
    possible_pairs = set([frozenset([id1, id3]), frozenset([id1, id5]),
                          frozenset([id1, id7]), frozenset([id3, id5]),
                          frozenset([id3, id7]), frozenset([id5, id7]),
                          frozenset([id2, id4]), frozenset([id2, id6]),
                          frozenset([id2, id8]), frozenset([id4, id6]),
                          frozenset([id4, id8]), frozenset([id6, id8])
                          ])
    actual_pairs = set([frozenset([pid1, pid2]), frozenset([pid3, pid4]), frozenset([pid5, pid6]), frozenset([pid7, pid8])])
    for pair in actual_pairs:
        if pair not in possible_pairs:
            raise ValueError(
                "After one match, players with one win should be paired.")
    print ("10. After one match, players with one win are properly paired.")

testPairings()


cur.close()
cnx.close()
