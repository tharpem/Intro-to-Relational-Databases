<h1>Swiss Tournament - Final Project for Intro to Relational Databases Course</h1>.

This project developed a database and tables and lists to enable registration, scorekeeping, ranking, and swiss pairing of players for a tournament. All players are to play 4 rounds matched with players of similar winning success.

<h2>DATABASE:</h2> tournament
<h2>TABLES</h2>:
  <ul>players (registration)</ul>
  <ul>match (record of match)</ul>

<h2>VIEWS:</h2>
  <ul>Player_Stats (individual registrants winning and ranking stats)</ul>
  Helper Views:
  <ul>playerTotalMatches - totals number of matches in which they have played</ul>
  <ul>playerTotalWins - totals number of wins they have had</ul>
  <ul>playerRanks - provides their ranking based on wins/matches</ul>

<h2>LISTS:</h2>
<ul>SwissPairs (pairing of individual players for a match determined by Player_Stats ranks)</ul>

<h2>BUILT WITH:</h2>
  Atom Text Editor
  Pyschopg2 PostgreSQL Adaptor
  python

<h2>MATCHING STEPS:</h2>
<li>Player is registered via registerPlayer function.</li>
  <ul> Player is automatically added to Player_Stats view</ul>

<li>When match is reported via reportMatch function:</li>
   <ul>the winner and loser is input into the match table</ul>
   <ul>Automatically the Player_Stats view and helper views are updated.</ul>

<li>Players are matched via swissPairings function.</li>
  <ul>Players are added in ranking order to a list called pair_List.</ul>
  <ul>The Swiss_Pairs list newPair is populated from this list</ul>

Other functions included:
  countPlayers (which counts the number of registered players and is used in denominator for matching pairs)
  seeRegisteredPlayers (which lists the registered players)
  deletePlayers to delete data in players table
  deleteMatches to delete data in matches table

<h2>TESTING</h2>
  Tests were performed via the tournament_test.py file provided by the Udacity Intro to Relational Databases course.  Tested for:
  Correct deletion of data when prompted
  Correct listing of players and data in tables
  Correct matching of players

<h2>Authors</h2>
  Maji Tharpe
