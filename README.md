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

Clone the repository to your local system, then launch the VM:
```
git clone http://github.com/richgieg/TournamentResults
cd TournamentResults/vagrant
vagrant up
```

*It may take several minutes for the VM to spin up when you're launching it for
the first time, since the VM image is being fetched and the one-time
configuration must take place. Please be patient. Once the process is complete,
your terminal prompt will be returned, thus allowing you to execute the next
steps.*

Connect to the VM via SSH, create the database, then run the test suite:
```
vagrant ssh
cd /vagrant/tournament
psql -f tournament.sql
python tournament_test.py
```

*If all tests were successfully executed, the last line of output should be
"Success!  All tests pass!" If that is not the case, then examine the output to
determine which unit test failed. With this vital information, you should be
able to easily track down the problem in the code.*

Exit the SSH session and shutdown the VM:
```
exit
vagrant halt
```
