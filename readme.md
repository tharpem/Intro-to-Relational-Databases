<h1>Swiss Tournament - Final Project for Intro to Relational Databases Course</h1>.

This project developed a database and tables to enable registration, scorekeeping, ranking, and swiss pairing of players for a tournament. All players are to play 4 rounds matched with players of similar winning success.

<h2>DATABASE:</h2> tournament
<h2>TABLES</h2>:
  <ul>players (registration)</ul>
  <ul>match (record of match)</ul>
  <ul>Player_Stats (individual registrants winning and ranking stats)</ul>
  <ul>SwissPairs (pairing of individual players for a match determined by Player_Stats ranks)</ul>

<h2>BUILT WITH:</h2>
  Atom Text Editor
  Pyschopg2 PostgreSQL Adaptor
  python

<h2>MATCHING STEPS:</h2>
<li>Player is registered via registerPlayer function.</li>
  <ul>(Automatically via inputPlayerStandings function) Player is automatically added to Player_Stats table</ul>

<li>When match is reported via reportMatch function:</li>
   <ul>the match, winner and loser is input into the match table</ul>
   <ul>(Automatically via the adjustWinnerStats function run once with winner and once with loser) the win/loss/addition of match played updates Player_Stats table.</ul>

<li>Players are matched via swissPairings function.</li>
  <ul>Ranking is checked</ul>
  <ul>Players are added in that order to a list called pair_list.</ul>
  <ul>The Swiss_Pairs table is populated from this list</ul>

Other functions included:
  countPlayers (which counts the number of registered players and is used in denominator for matching pairs)
  seeRegisteredPlayers (which lists the registered players)
  deleteSwissPairs to delete the data in Swiss_Pairs table
  deletePlayers to delete data in players and Player_Stats tables
  deleteMatches to delete data in matches table
  show_Swiss_Pairs to list the Swiss Pairs

<h2>TESTING</h2>
  Tests were performed via the tournament_test.py file provided by the Udacity Intro to Relational Databases course.  Tested for:
  Correct deletion of data when prompted
  Correct listing of players and data in tables
  Correct matching of players

<h2>Authors</h2>
  Maji Tharpe
