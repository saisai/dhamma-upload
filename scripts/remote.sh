
ssh -i /cygdrive/d/hello/hello/ssh_keygen/this u0_a155@192.168.1.37 -p 8022 mkdir -vp /home/storage/downloads/ma_ha_si_saya_daw/ShifPhyarMagginNibbanwin

echo 'http://dhammadownload.com/MP3Library/MahasiSayadawUSobhanaMahathera/DVD-11/024-MahasiSayadawGyi-ShifPhyarMagginNibbanwin(1)-1338-DVD11.mp3
http://dhammadownload.com/MP3Library/MahasiSayadawUSobhanaMahathera/DVD-11/025-MahasiSayadawGyi-ShifPhyarMagginNibbanwin(2)-1338-DVD11.mp3
http://dhammadownload.com/MP3Library/MahasiSayadawUSobhanaMahathera/DVD-11/026-MahasiSayadawGyi-ShifPhyarMagginNibbanwin(3)-1338-DVD11.mp3
' | ssh -i /cygdrive/d/hello/hello/ssh_keygen/this u0_a155@192.168.1.37 -p 8022 "cat > /home/storage/downloads/ma_ha_si_saya_daw/ShifPhyarMagginNibbanwin/dl.txt"

echo 'SOURCE="${BASH_SOURCE[0]}"
while [ -h "$SOURCE" ] ; do SOURCE="$(readlink "$SOURCE")"; done
DIR="$( cd -P "$( dirname "$SOURCE" )" && pwd )"

# Change into that directory
echo $DIF
cd $DIR

for i in $(cat dl.txt);do echo $i; wget -c $i; done
' | ssh -i /cygdrive/d/hello/hello/ssh_keygen/this u0_a155@192.168.1.37 -p 8022 "cat > /home/storage/downloads/ma_ha_si_saya_daw/ShifPhyarMagginNibbanwin/dl.sh"

# download remotely
ssh -i /cygdrive/d/hello/hello/ssh_keygen/this u0_a155@192.168.1.37 -p 8022 bash /home/storage/downloads/ma_ha_si_saya_daw/ShifPhyarMagginNibbanwin/dl.sh
# sleep 1 second
echo "sleeping one second"
sleep 1
ssh -i /cygdrive/d/hello/hello/ssh_keygen/this u0_a155@192.168.1.37 -p 8022 ls /home/storage/downloads/ma_ha_si_saya_daw/ShifPhyarMagginNibbanwin/

# sleep 1 second 
echo "sleeping one second"
sleep 1 

# writing python file remotely as rename.py
printf "
import argparse
import os
import glob


dirpath = os.getcwd()
print('current directory is : ' + dirpath)
foldername = os.path.basename(dirpath)
print('Directory name is : ' + foldername)
scriptpath = os.path.realpath(__file__)
print('Script path is : ' + scriptpath)

# Go to the current directory of file name 
abspath = os.path.abspath(__file__)
dname = os.path.dirname(abspath)
os.chdir(dname)
dirpath = os.getcwd()
print('current directory', dirpath)

parser = argparse.ArgumentParser(description='Demo')
parser.add_argument('--show', '-s',
        action='store_true',
        help='show how to do')

parser.add_argument('--go', '-g',
                         action='store_true',
                         help='rename file')

args = parser.parse_args()


if args.show:
    i = 1
    for name in glob.glob('*.mp3'):
        print(name)
        print('{:03}'.format(i))
        i += 1
elif args.go:
    i = 1
    for name in glob.glob('*.mp3'):
        print(name)
        print('{:03}'.format(i))
        os.rename(name, '{:03}.mp3'.format(i))
        i += 1
" | ssh -i /cygdrive/d/hello/hello/ssh_keygen/this u0_a155@192.168.1.37 -p 8022 "cat > /home/storage/downloads/ma_ha_si_saya_daw/ShifPhyarMagginNibbanwin/rename.py"

# sleep 1 second 
echo "sleeping one second"
sleep 1 
# checking python file
ssh -i /cygdrive/d/hello/hello/ssh_keygen/this u0_a155@192.168.1.37 -p 8022 python /home/storage/downloads/ma_ha_si_saya_daw/ShifPhyarMagginNibbanwin/rename.py -h

# running python file to check 
ssh -i /cygdrive/d/hello/hello/ssh_keygen/this u0_a155@192.168.1.37 -p 8022 python /home/storage/downloads/ma_ha_si_saya_daw/ShifPhyarMagginNibbanwin/rename.py -s

# rename file
echo "renaming file..."
ssh -i /cygdrive/d/hello/hello/ssh_keygen/this u0_a155@192.168.1.37 -p 8022 python /home/storage/downloads/ma_ha_si_saya_daw/ShifPhyarMagginNibbanwin/rename.py -g

# sleep 1 second 
echo "sleeping one second"
sleep 1 
# checking python file
ssh -i /cygdrive/d/hello/hello/ssh_keygen/this u0_a155@192.168.1.37 -p 8022 ls -l /home/storage/downloads/ma_ha_si_saya_daw/ShifPhyarMagginNibbanwin/
#ssh -i /cygdrive/d/hello/hello/ssh_keygen/this u0_a155@192.168.1.37 -p 8022 -t cd "/home/storage/downloads/ma_ha_si_saya_daw/ShifPhyarMagginNibbanwin/; bash"
ssh -i /cygdrive/d/hello/hello/ssh_keygen/this u0_a155@192.168.1.37 -p 8022 ls -l /home/storage/downloads/ma_ha_si_saya_daw/
#ssh -i /cygdrive/d/hello/hello/ssh_keygen/this u0_a155@192.168.1.37 -p 8022 rm -rfv /home/storage/downloads/ma_ha_si_saya_daw/ShifPhyarMagginNibbanwin
