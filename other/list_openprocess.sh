
#for i  in `tasklist | grep -v Image | grep -v = | awk '{print $1}'` ;do echo $i; done
for cmd in `tasklist | grep -v Image | grep -v = | awk '{print $1}'`
do
    if [ $cmd == "bash.exe" ]; then
        echo $cmd
        which $cmd
    fi
    
done
