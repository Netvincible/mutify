#!/bin/bash
beta=$(ps aux | grep -c spotify)
delta=$((0))
# tau=$(pgrep source_linux.sh)
omega=0

while [ $beta -ge 2 ]
do	
	sleep 2
	alpha=$(playerctl --player=spotify metadata | grep -c Advertisement)
	gama=$(playerctl --player=spotify status | grep -c Playing)
	beta=$(ps aux | grep -c spotify)
	delta=$((delta + 1))

	if [ "$alpha" = 1 ] && [ "$gama" = 1 ]
	then
		playerctl --player=spotify volume 0
		sleep 31

		alpha=$(playerctl --player=spotify metadata | grep -c Advertisement)
		gama=$(playerctl --player=spotify status | grep -c Playing)

		if [ "$alpha" = 1 ] && [ "$gama" = 1 ]
		then
			sleep 30
			playerctl --player=spotify volume 1
		else
			playerctl --player=spotify volume 1
		fi
		omega=$((omega + 1))
		echo "$omega"
		

	else
		echo "$omega"

	fi
	

	# if [ $delta == 120 ]
	# then
	# 	delta=$((0))
	# 	clear
	# fi
done

#REMEMBER: always leave extra spaces while coding shell script, but here delta is an exception--> delta= $((0)) is invalid
