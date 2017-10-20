-- Table definitions for the tournament project.
--
-- Put your SQL 'create table' statements in this file; also 'create view'
-- statements if you choose to use it.
--
-- You can write comments in this file by starting them with two dashes, like
-- these lines here.

CREATE DATABASE tournament;

CREATE TABLE players (
  /*Registered players of tournament*/
Id serial PRIMARY KEY,
Name TEXT NOT NULL);

CREATE TABLE match (
  /*Lists winners of matches*/
matchID serial PRIMARY KEY,
player1_id SMALLINT,
player2_id SMALLINT,
winner SMALLINT,
loser SMALLINT);

-- CREATE FUNCTION countMatches(match)
--   RETURNS BIGINT AS
-- $func$
--     SELECT COUNT(match.matchID)
--     FROM   match JOIN players ON match.player1_id=players.id OR match.player2_id=players.id;
-- $func$ LANGUAGE SQL VOLATILE;

-- CREATE FUNCTION showRank(match)
--   RETURNS FLOAT AS
-- $func$
--     SELECT COUNT(match.winner)/countMatches(match)
--     FROM   match JOIN players ON  match.player1_id=players.id OR match.player2_id=players.id;
-- $func$ LANGUAGE SQL VOLATILE;

-- CREATE VIEW playerTotalMatches AS SELECT players.id, COUNT (match.matchID)
-- FROM match JOIN players ON  match.player1_id=players.id OR match.player2_id=players.id
-- WHERE players.id=match.player1_id OR players.id=match.player2_id;

CREATE VIEW playerTotalMatches AS SELECT players.id AS ID, COUNT(match.matchID) AS Count FROM players LEFT JOIN match on players.id=match.winner OR players.id=match.loser
GROUP BY players.id;

CREATE VIEW playerTotalWins AS SELECT players.id AS ID, COUNT(match.winner) As Wins FROM players LEFT JOIN match
ON match.winner=players.id
GROUP BY players.id;

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



--Shows next pairing for matches
CREATE VIEW Swiss_Pairs (id1, name1, id2, name2)


-- CREATE TABLE Swiss_Pairs(
--   /*Lists next sets of Swiss pairs*/
--   id1 SMALLINT,
--   name1 TEXT,
--   id2 SMALLINT,
--   name2 TEXT);
