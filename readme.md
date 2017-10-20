#Swiss Tournament - Final Project for Intro to Relational Databases Course.

This project developed a database and tables and lists to enable registration, scorekeeping, ranking, and swiss pairing of players for a tournament. All players are to play 4 rounds matched with players of similar winning success.

##DATABASE:
  tournament
##TABLES:
  * players (registration)
  * match (record of match)

##VIEWS:

  * Player_Stats (individual registrants winning and ranking stats)
    Helper Views:
  * playerTotalMatches - totals number of matches in which they have played
  * playerTotalWins - totals number of wins they have had
  * playerRanks - provides their ranking based on wins/matches


##LISTS:

  * SwissPairs (pairing of individual players for a match determined by Player_Stats ranks)

##BUILT WITH:
  Atom Text Editor
  Pyschopg2 PostgreSQL Adaptor
  python

##MATCHING STEPS:
1. Player is registered via registerPlayer function.
  * Player is automatically added to Player_Stats view

2. When match is reported via reportMatch function:
  * the winner and loser is input into the match table
  * Automatically the Player_Stats view and helper views are updated.

3. Players are matched via swissPairings function.
  * Players are added in ranking order to a list called pair_List.
  * The Swiss_Pairs list newPair is populated from this list.

Other functions included:
  countPlayers (which counts the number of registered players and is used in denominator for matching pairs)
  seeRegisteredPlayers (which lists the registered players)
  deletePlayers to delete data in players table
  deleteMatches to delete data in matches table

##TESTING
  Tests were performed via the tournament_test.py file provided by the Udacity Intro to Relational Databases course.  Tested for:
  * Correct deletion of data when prompted
  * Correct listing of players and data in tables
  * Correct matching of players

##Authors
  Maji Tharpe
