# Tournament Results

This is the second project in my pursuit of my Full-Stack Web Developer
Nanodegree from Udacity. Following is Udacity's description for this project:

"In this project, you’ll be writing a Python module that uses the PostgreSQL
database to keep track of players and matches in a game tournament. The game
tournament will use the Swiss system for pairing up players in each round:
players are not eliminated, and each player should be paired with another player
with the same number of wins, or as close as possible. This project has two
parts: defining the database schema (SQL table definitions), and writing the
code that will use it."

----
## Install VirtualBox


## Install Vagrant


## Run the Test Suite
Use a command line terminal for the following steps.

Clone the repository to your local system:

```
git clone http://github.com/richgieg/TournamentResults
```

Launch the VM:

```
cd TournamentResults/vagrant
vagrant up
```

Connect to the VM via SSH:

```
vagrant ssh
```

Create the tournament database:

```
cd /vagrant/tournament
psql -f tournament.sql
```

Run the tournament test suite:

```
python tournament_test.py
```

Exit the SSH session and shutdown the VM:

```
exit
vagrant halt
```
