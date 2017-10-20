-- Tables and Views for Intro-to-Relational-Databases final Tournament Project
--Database purpose is to show players, record stats and allow swiss matching of players.

CREATE DATABASE tournament;

CREATE TABLE players (
  /*Registered players of tournament*/
Id serial PRIMARY KEY,
Name TEXT NOT NULL);

CREATE TABLE match (
  /*Lists winners of matches*/
matchID serial PRIMARY KEY,
winner SMALLINT,
loser SMALLINT);

/*Helper view for Player_Stats view*/
CREATE VIEW playerTotalMatches AS SELECT players.id AS ID, COUNT(match.matchID) AS Count FROM players LEFT JOIN match on players.id=match.winner OR players.id=match.loser
GROUP BY players.id;

/*Helper view for Player_Stats view*/
CREATE VIEW playerTotalWins AS SELECT players.id AS ID, COUNT(match.winner) As Wins FROM players LEFT JOIN match
ON match.winner=players.id
GROUP BY players.id;

/*Helper view for Player_Stats view*/
CREATE VIEW playerRanks AS SELECT players.id AS ID, playerTotalWins.Wins/NULLIF(playerTotalMatches.Count,0) AS Ranking
FROM players
LEFT JOIN playerTotalWins ON players.id=playerTotalWins.ID
INNER JOIN playerTotalMatches ON players.id=playerTotalMatches.ID
ORDER BY Ranking;


CREATE VIEW Player_Stats (Id, Name, Wins, Matches, Ranking)
  /*Lists individual player stats*/
  AS Select players.id AS ID, players.name AS NAme, playerTotalWins.Wins AS Wins, playerTotalMatches.Count AS Matches, playerRanks.Ranking AS Ranking
  From players LEFT OUTER JOIN playerTotalWins ON players.id=playerTotalWins.ID
  INNER JOIN playerTotalMatches ON players.id=playerTotalMatches.ID
  INNER JOIN playerRanks on players.id=playerRanks.ID
  ORDER BY Ranking DESC;
