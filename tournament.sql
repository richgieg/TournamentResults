-- Create tournament database and connect to it.
DROP DATABASE IF EXISTS tournament;
CREATE DATABASE tournament;
\c tournament

-- Create players table.
CREATE TABLE players (
    id serial primary key,
    name text
);
