-- Create tournament database and connect to it.
DROP DATABASE IF EXISTS tournament;
CREATE DATABASE tournament;
\c tournament

-- Create players table.
CREATE TABLE players (
    id serial primary key,
    name text
);

-- Create matches table.
CREATE TABLE matches (
    id serial primary key,
    winner integer references players(id),
    loser integer references players(id)
);

-- Create view for finding number of wins per player.
CREATE VIEW player_wins AS
SELECT players.id, COUNT(matches.winner) AS wins
FROM players LEFT JOIN matches
ON players.id = matches.winner
GROUP BY players.id;

-- Create view for finding number of matches per player.
CREATE VIEW player_matches AS
SELECT players.id, COUNT(matches.winner) AS matches
FROM players LEFT JOIN matches
ON players.id = matches.winner OR players.id = matches.loser
GROUP BY players.id;
