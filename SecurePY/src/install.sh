#!/bin/bash
clear
apt-get install figlet
clear
figlet -f slant SecurePy
sleep 1
echo ""
echo "Press Enter to continue"
read touch
case $touch in
*)      echo ""
        ;;
esac

echo " [ * ]  -=  Installation will begin, please wait.  =-  [ * ]"
echo ""
echo "                    Made By PyR3Q"
echo ""
echo "  [INSTAGRAM]: @pyr3q"
echo "  [WebSite]: pyr3q.github.io"
echo "  [YouTube]: PyR3Q"
echo ""
sleep 1
n=20
for x in `seq $n`
do
    for i in `seq $x`; do echo -n "#"; done
    echo -en "\r"
    sleep 0.3
done
echo ""
sleep 3

apt-get install git
apt-get install proxychains
git clone https://github.com/Und3rf10w/kali-anonsurf
cd kali-anonsurf
chmod +x installer.sh
./installer.sh
figlet -f slant Install Done.
echo ""
echo "[ * ]  -=  Install Done, Press a Enter to exit.  =-  [ * ]"
read touch
case $touch in
*)      echo ""
        ;;
esac