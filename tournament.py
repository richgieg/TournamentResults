#!/usr/bin/env python
#
# tournament.py -- implementation of a Swiss-system tournament
#

import psycopg2


# Define the table names.
_PLAYER_TABLE = "players"
_MATCH_TABLE = "matches"


def connect():
    """Connect to the PostgreSQL database. Returns a database connection."""
    return psycopg2.connect("dbname=tournament")


def _query(query, values=(), commit=False):
    """Executes a query against the PostgreSQL database.

    This is an internal helper function that will execute a query against the
    PostgreSQL database. If the commit argument is False, then the function will
    return the results. Otherwise, the function will commit the changes to the
    database and return an empty list.

    Args:
        query: The query string to execute against the database.
        values: A tuple containing the values to substitute into the query
                string (OPTIONAL, default is an empty tuple).
        commit: If true, changes are committed (OPTIONAL, default is False).

    Returns:
        If the commit argument is False (default), then the function returns a
        list containing the resulting rows from the execution of the query.
        Otherwise, the function returns an empty list.
    """
    results = []
    db = connect()
    cursor = db.cursor()
    cursor.execute(query, values)
    if commit:
        db.commit()
    else:
        results = cursor.fetchall()
    db.close()
    return results


def _clearTable(table):
    """Remove all the records from a table.

    This is an internal helper function that will remove all the records from
    the table specified in the table argument.

    Args:
        table: The name of the table from which to remove all records.
    """
    _query("DELETE FROM " + table, commit=True)


def deleteMatches():
    """Remove all the match records from the database."""
    _clearTable(_MATCH_TABLE)


def deletePlayers():
    """Remove all the player records from the database."""
    _clearTable(_PLAYER_TABLE)


def countPlayers():
    """Returns the number of players currently registered."""
    result = _query("SELECT COUNT(*) FROM " + _PLAYER_TABLE)
    return int(result[0][0])


def registerPlayer(name):
    """Adds a player to the tournament database.

    The database assigns a unique serial id number for the player.  (This
    should be handled by your SQL database schema, not in your Python code.)

    Args:
        name: The player's full name (need not be unique).
    """
    values = (name,)
    _query("INSERT INTO players (name) VALUES (%s)", values, True)


def playerStandings():
    """Returns a list of the players and their win records, sorted by wins.

    The first entry in the list should be the player in first place, or a player
    tied for first place if there is currently a tie.

    Returns:
        A list of tuples, each of which contains (id, name, wins, matches):
            id: The player's unique id (assigned by the database).
            name: The player's full name (as registered).
            wins: The number of matches the player has won.
            matches: The number of matches the player has played.
    """


def reportMatch(winner, loser):
    """Records the outcome of a single match between two players.

    Args:
        winner: The id number of the player who won.
        loser: The id number of the player who lost.
    """


def swissPairings():
    """Returns a list of pairs of players for the next round of a match.

    Assuming that there are an even number of players registered, each player
    appears exactly once in the pairings. Each player is paired with another
    player with an equal or nearly-equal win record, that is, a player adjacent
    to him or her in the standings.

    Returns:
        A list of tuples, each of which contains (id1, name1, id2, name2).
            id1: The first player's unique id.
            name1: The first player's name.
            id2: The second player's unique id.
            name2: The second player's name.
    """


