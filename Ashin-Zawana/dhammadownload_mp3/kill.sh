
for val in $(tmux ls | awk '{ print $1 }' | cut -d '-' -f 1) then
do
	echo $val
	tmux kill-session -t $val
done

