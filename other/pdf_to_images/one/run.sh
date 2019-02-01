rm -rfv pages
rm -rfv a.pdf
#wget -O a.pdf http://dhammadownload.com/File-Library/DawKhinHlaTin/DawKhinHlaTin-AbhidhaLevel1Note.pdf; 
#wget -O a.pdf http://dhammadownload.com/File-Library/DawKhinHlaTin/DhammaByuhar-AbhidhammaYoYo-2ndLevel-Notes.pdf
#wget -O a.pdf http://dhammadownload.com/File-Library/DawKhinHlaTin/DhammaByuhar-AhChayKhanAhBiDhammaThinTan-3rdLevel-Notes.pdf
#wget -O a.pdf http://dhammadownload.com/File-Library/DawKhinHlaTin/DawKhinHlaTin-WiThoatDiMagNoteLevel1.pdf
#wget -O a.pdf http://dhammadownload.com/File-Library/DawKhinHlaTin/DawKhinHlaTin-WiThoatDiMagNoteLevel2.pdf
#wget -O a.pdf http://dhammadownload.com/File-Library/DawKhinHlaTin/DawKhinHlaTin-WiThoatDiMagNoteLevel3.pdf
#wget -O a.pdf http://dhammadownload.com/File-Library/DawKhinHlaTin/DawKhinHlaTin-AbhidhammaGoneHtooSaung-Level1.pdf
#wget -O a.pdf http://dhammadownload.com/File-Library/DawKhinHlaTin/DawKhinHlaTin-AbhidhammaGoneHtooSaung-Level2.pdf
#wget -O a.pdf dhammadownload.com/File-Library/DawKhinHlaTin/DawKhinHlaTin-AbhidhammaGoneHtooSaung-Level3.pdf
#wget -O a.pdf http://dhammadownload.com/File-Library/DawKhinHlaTin/DawKhinHlaTin-BasicPahtanClassNote.pdf
#wget -O a.pdf http://dhammadownload.com/File-Library/DawKhinHlaTin/DawKhinHlaTin-MahaThatiPaHtarNaThotSummary.pdf
#wget -O a.pdf http://dhammadownload.com/File-Library/DawKhinHlaTin/DawKhinHlaTin-YinKyayMuKyintWutSubject.pdf
#wget -O a.pdf http://dhammadownload.com/File-Library/DawKhinHlaTin/DawKhinHlaTin-Payatekyi11.pdf
#wget -O a.pdf http://dhammadownload.com/File-Library/DawKhinHlaTin/DawKhinHlaTin-AHNatTaLatKhaNaSuta.pdf
#wget -O a.pdf http://dhammadownload.com/File-Library/DawKhinHlaTin/DawKhinHlaTin-MahaThatiPaHtarNaThotSummary.pdf
#wget -O a.pdf http://dhammadownload.com/File-Library/DawKhinHlaTin/DawKhinHlaTin-GaYuDhammaTheLa.pdf
#wget -O a.pdf http://dhammadownload.com/File-Library/DawKhinHlaTin/DawKhinHlaTin-Myitta%20Suta.pdf
#wget -O a.pdf http://dhammadownload.com/File-Library/DawKhinHlaTin/DawKhinHlaTin-ParRaMeePoneYate.pdf
#wget -O a.pdf http://dhammadownload.com/File-Library/DawKhinHlaTin/DawKhinHlaTin-MaHaThaRaNaGoneTawKyi.pdf
#wget -O a.pdf http://dhammadownload.com/File-Library/DawKhinHlaTin/DawKhinHlaTin-DhammaCekkaSuta.pdf
#wget -O a.pdf http://dhammadownload.com/File-Library/other/BuddhaBarTharKongTaYork.pdf
#wget -O a.pdf http://dhammadownload.com/File-Library/The-Ministry-Of-Religious-Affairs/TheMinistryOfReligiousAffairs-BuddhaBartharLatSwalKyann-1.pdf
#wget -O a.pdf "http://dhammadownload.com/File-Library/The-Ministry-Of-Religious-Affairs/TheMinistryOfReligiousAffairs-BuddhaBartharLatSwalKyann-part-1(1993).pdf"
wget -O a.pdf "http://dhammadownload.com/File-Library/The-Ministry-Of-Religious-Affairs/TheMinistryOfReligiousAffairs-BuddhaBartharLatSwalKyann-part-2(1996).pdf"
python3 aa.py
cd pages;
rm -rfv images; mkdir images; for i in `ls -v *.pdf`; do c=`basename $i .pdf`; echo $i; convert -geometry 1000x1000 -density 200x200 -quality 100 $i images/$c.jpg; done