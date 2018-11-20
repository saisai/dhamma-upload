tcpdump -i eth0 -nl -w- dst 'port 34306' | strings -n8 > /home/user/log/09-1.2014.txt
tcpdump -i eth0 -nl -w- dst 'port 80' | strings -n8 >> port80log_09_1_2014.txt