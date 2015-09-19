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

To execute this project, please follow the steps in the sections below.

----
## Install VirtualBox 4.3
VirtualBox 4.3 is required for Vagrant to function. The steps for installing it
vary depending on your operating system. You can find the installer for many
operating systems [here](https://www.virtualbox.org/wiki/Download_Old_Builds_4_3).

If you happen to be using Ubuntu 15.04 (as I did for this project), you can try
this terminal command:
```
sudo apt-get install virtualbox-4.3
```

*This command will probably work for other versions of Ubuntu as well.*

----
## Install Vagrant
Vagrant is required to manage the virtual machine (VM) used for executing this
project. The VM image is automatically fetched by Vagrant when the VM is
powered up the first time. The VM comes preconfigured with Python and
PostgreSQL. The steps for installing Vagrant vary depending on your operating
system. You can find the installer for many operating systems
[here](https://www.vagrantup.com/downloads.html).

If you happen to be using Ubuntu 15.04 (as I did for this project), you can try
this terminal command:
```
sudo apt-get install vagrant
```

*This command will probably work for other versions of Ubuntu as well.*

----
## Run the Test Suite
Use a command line terminal for the following steps.

**Clone the repository to your local system, then launch the VM:**
```
git clone http://github.com/richgieg/TournamentResults.git
cd TournamentResults/vagrant
vagrant up
```

*It may take several minutes for the VM to spin up when you're launching it for
the first time, since the VM image is being fetched and the one-time
configuration must take place. Please be patient. Once the process is complete,
your terminal prompt will be returned, thus allowing you to execute the next
steps.*

**Connect to the VM via SSH, create the database, then run the test suite:**
```
vagrant ssh
cd /vagrant/tournament
psql -f tournament.sql
python tournament_test.py
```

*If all tests were successfully executed, the last line of output should be
"Success!  All tests pass!" If that is not the case, then the output can be
examined in order to determine which unit test failed. With this vital
information, one should be able to easily track down the problem in the code
(if a problem happened to be present).*

**Exit the SSH session and shutdown the VM:**
```
exit
vagrant halt
```
