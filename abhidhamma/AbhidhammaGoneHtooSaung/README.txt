for i in `ls -v *.pdf`; do c=`basename $i .pdf`; echo $i; convert -geometry 1000x1000 -density 200x200 -quality 100 $i images/$c.jpg; done
