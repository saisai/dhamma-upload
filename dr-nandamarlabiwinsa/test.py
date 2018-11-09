import subprocess
import os

#len( os.popen( "ps -aef | grep -i 'myprocess' | grep -v 'grep' | awk '{ print $3 }'" ).read().strip().split( '\n' ) ) > 1:
#len( os.popen( "ps -aef | grep -i '/usr/bin/youtube-upload' | awk '{ print $3 }'" ).read().strip().split( '\n' ) ) > 1:
#result = os.popen( "ps -aef | grep -i '/usr/bin/youtube-upload' | awk '{ print $3 }'" ).read().strip().split( '\n' )
#ps -aef | grep -i '/usr/bin/youtube-upload' | grep -v 'grep' | awk '{ print $3 }'
#result = os.popen( "ps -aef | grep -i '/usr/bin/youtube-upload'" ).read().strip().split( '\n' )

#result = os.popen( "ps -aef | grep -i '/usr/bin/youtube-upload' | awk '{ print $3 }'" ).read().strip().split( '\n' )
# result = ['6905', '6908', '6909'] output

#result = os.popen( "ps -aef | grep -i '/usr/bin/youtube-upload' | awk '{ print $3 }'" ).read().strip().split( '\n' )
# termux on android
result = os.popen( "ps -aef | grep -i '/data/data/com.termux/files/usr/bin/youtube-upload' | awk '{ print $3 }'" ).read().strip().split( '\n' )
if len(result) > 2:
    print(result)
    print(result)
    print(len(result))
    print(type(result))
'''
if len(os.popen( "ps -aef | grep -i '/usr/bin/youtube-upload' | awk '{ print $3 }'" ).read().strip().split( '\n' ) ) > 3:
    #result = os.popen( "ps -aef | grep -i '/usr/bin/youtube-upload'" ).read().strip().split( '\n' )
    result = os.popen( "ps -aef | grep -i '/usr/bin/youtube-upload' | awk '{ print $3 }'" ).read().strip().split( '\n' )
    print(result)
'''
'''
p1_command = ['ps', '-eaf']
p2_command = ['grep', '"/usr/bin/youtube-upload"']
p1 = subprocess.Popen(p1_command, stdout=subprocess.PIPE)
p2 = subprocess.Popen(p2_command, stdin=p1.stdout, stdout=subprocess.PIPE)
'''
#print(p2.stdout)
#p1.stdout.close()
#print(p2.communicate())

