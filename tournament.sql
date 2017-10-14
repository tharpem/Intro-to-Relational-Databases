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
Name TEXT NOT NULL,
Team TEXT);

CREATE TABLE match (
  /*Lists winners of matches*/
match serial PRIMARY KEY,
player1_id SMALLINT,
player2_id SMALLINT,
winner SMALLINT);

CREATE TABLE Player_Stats (
  /*Lists individual player stats*/
  id TEXT,
  name TEXT,
  wins SMALLINT default 0,
  matches SMALLINT default 0,
  ranks SMALLINT);

CREATE TABLE Swiss_Pairs(
  /*Lists next sets of Swiss pairs*/
  id1 SMALLINT,
  name1 TEXT,
  id2 SMALLINT,
  name2 TEXT);
