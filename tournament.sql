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

-- Create view for player standings.
CREATE VIEW player_standings AS
SELECT players.id, players.name, player_wins.wins, player_matches.matches
FROM players, player_wins, player_matches
WHERE players.id = player_wins.id AND players.id = player_matches.id
ORDER BY player_wins.wins DESC;

-- Create view for next pairing.
CREATE VIEW next_pairing AS
SELECT a.id AS id1, b.id AS id2
FROM player_standings AS a, player_standings AS b
WHERE a.wins = b.wins AND a.id < b.id;
