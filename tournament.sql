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

DECLARE Ranks float =  COUNT(match.winner WHERE match.winner=players.id)/COUNT(match.winner WHERE (match.winner=players.id OR match.loser=players.id)

CREATE VIEW Player_Stats (Id, Name, Wins, Matches, Ranking)
  /*Lists individual player stats*/
  AS Select players.id, players.name, COUNT(match.winner WHERE match.winner=players.id), COUNT(match.winner WHERE match.winner=players.id OR match.loser=players.id), Ranks
  FROM players JOIN match ON players.id = match.winner and players.id=match.loser
  ORDER BY Ranking;

--Shows next pairing for matches
CREATE VIEW Swiss_Pairs (id1, name1, id2, name2)


-- CREATE TABLE Swiss_Pairs(
--   /*Lists next sets of Swiss pairs*/
--   id1 SMALLINT,
--   name1 TEXT,
--   id2 SMALLINT,
--   name2 TEXT);
