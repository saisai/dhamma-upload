#/bin/bash

sudo apt-get update
sudo apt-get upgrade -y
sudo apt-get install build-essential -y
sudo apt-get install libxslt1-dev libxslt1.1 libxml2-dev libxml2 libssl-dev libffi-dev python-dev -y
sudo apt-get install curl git vim -y

sudo apt-get install mysql-server mysql-client -y
sudo aptitude install apache2 apache2-doc -y
sudo aptitude install php5 php5-mysql libapache2-mod-php5 -y
sudo apt-get install php5-mcrypt php5-gd -y
sudo a2enmod rewrite
sudo apt-get install postgresql -y
sudo apt-get install php5-pgsql -y
sudo apt-get install postgresql-contrib -y
sudo apt-get install python-psycopg2 -y # python
sudo apt-get install libpq-dev -y #for python psycopg2
sudo service apache2 restart
sudo apt-get install apache2-mpm-prefork apache2-prefork-dev -y
sudo apt-get install libcurl4-openssl-dev
sudo apt-get install libmysqlclient-dev
sudo apt-get install software-properties-common python-software-properties -y
#http://www.pontikis.net/blog/postgresql-9-debian-7-wheezy

#sh: phpize: command not found    
#ERROR: 'phpize' failed

sudo apt-get install php5-dev

# access control lists
sudo apt-get install acl
sudo apt-get install -y python-nfqueue
# ack tool
# http://beyondgrep.com/install/
curl http://beyondgrep.com/ack-2.14-single-file > ack
sudo cp /usr/local/bin/
sudo chmod 0755 /usr/local/bin/ack

sudo apt-get install python-virtualenv -y
sudo apt-get install python-mysqldb -y
sudo apt-get install tcpdump -y
#https://github.com/amix/vimrc
git clone git://github.com/amix/vimrc.git ~/.vim_runtime 
sh ~/.vim_runtime/install_basic_vimrc.sh

# get pip
wget https://bootstrap.pypa.io/get-pip.py
sudo python get-pip.py

sudo pip install scrapy beautifulsoup4 lxml html5lib sqlalchemy
sudo pip install service_identity
sudo pip install scapy
# download composer and move to /usr/local/bin
# https://getcomposer.org/doc/00-intro.md
curl -sS https://getcomposer.org/installer | php
sudo mv composer.phar /usr/local/bin/composer

#
sudo cp /etc/apache2/sites-available/default /etc/apache2/sites-available/default.bak
sudo rm -rf /etc/apache2/sites-available/default
sudo cp default /etc/apache2/sites-available/
sudo service apache2 reload


# https://community.runabove.com/kb/en/instances/how-to-relay-postfix-mails-via-smtp.gmail.com-on-ubuntu-14.04.html
# How To Relay Postfix mails via smtp.gmail.com
sudo apt-get install postfix mailutils libsasl2-2 ca-certificates libsasl2-modules nano -y
'''
sudo nano -w /etc/postfix/main.cf

relayhost = [smtp.gmail.com]:587
smtp_sasl_auth_enable = yes
smtp_sasl_password_maps = hash:/etc/postfix/sasl/sasl_passwd
smtp_sasl_security_options = noanonymous
smtp_tls_CAfile = /etc/postfix/cacert.pem
smtp_use_tls = yes

sudo cat /etc/ssl/certs/Thawte_Premium_Server_CA.pem | sudo tee -a /etc/postfix/cacert.pem 
sudo nano -w /etc/postfix/sasl/sasl_passwd
[smtp.gmail.com]:587 USERNAME@gmail.com:PASSWORD
sudo chmod 400 /etc/postfix/sasl/sasl_passwd
sudo postmap /etc/postfix/sasl/sasl_passwd
sudo /usr/sbin/postfix reload
'''
#http://nbviewer.ipython.org/gist/giotta/5556234

# how to install ruby, ruby on rails


sudo apt-get install -y gawk libreadline6-dev libyaml-dev libsqlite3-dev sqlite3 autoconf libgdbm-dev libncurses5-dev automake libtool bison pkg-config

gpg --keyserver hkp://keys.gnupg.net --recv-keys 409B6B1796C275462A1703113804BB82D39DC0E3

\curl -sSL https://get.rvm.io | bash -s stable

source /home/vagrant/.rvm/scripts/rvm

\curl -sSL https://get.rvm.io | bash -s stable --ruby

# To start using RVM you need to run `source /home/vagrant/.rvm/scripts/rvm`
#  in all your open shell windows, in rare cases you need to reopen all shell windows.

source /home/vagrant/.rvm/scripts/rvm

\curl -sSL https://get.rvm.io | bash -s stable --rails

#sudo rm -rf /etc/apache2/sites-available/default
#sudo cp default /etc/apache2/sites-available/
#sudo service apache2 reload
#sudo tail -f /var/log/apache2/error.log
#check modules loaded
#sudo apachectl -M

#cron checker http://www.cronchecker.net/
# will execute every 30th minute of every hour every day.  
#*/30 * * * * /bin/bash /vagrant/www/laravel-5-jobs/run_scrapy.sh

# debian extra size
#http://www.extellisys.com/articles/python-on-debian-wheezy

#https://github.com/mongodb/mongo-php-driver
## how to install php-mongodb driver
#Libraries have been installed in:
#   /vagrant/mongodb/mongo-php-driver/modules

#If you ever happen to want to link against installed libraries
#in a given directory, LIBDIR, you must either use libtool, and
#specify the full pathname of the library, or use the `-LLIBDIR'
#flag during linking and do at least one of the following:
#   - add LIBDIR to the `LD_LIBRARY_PATH' environment variable
#     during execution
#   - add LIBDIR to the `LD_RUN_PATH' environment variable
#     during linking
#   - use the `-Wl,-rpath -Wl,LIBDIR' linker flag
#   - have your system administrator add LIBDIR to `/etc/ld.so.conf'
#See any operating system documentation about shared libraries for
#more information, such as the ld(1) and ld.so(8) manual pages.

# how to install php-mongo driver
# http://wptrafficanalyzer.in/blog/installing-and-configuring-php-mongo-driver-with-apache-in-ubuntu-12-04-lts/
sudo apt-get install php-pear
sudo pecl install mongo

#Open the file “/etc/php5/apache2/php.ini” and add the given below line
#extension=mongo.so

#http://tech.enekochan.com/en/2013/10/22/install-mongodb-in-ubuntu-12-04-with-php-driver/