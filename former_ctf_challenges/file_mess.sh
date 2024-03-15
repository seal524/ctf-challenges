#!/bin/bash

for a in {a..z}
do
	echo "$a"
	for b in {a..z}
	do
		echo "$b"
		for c in {a..z}
		do
			for d in {a..z}
			do
				echo "$d" > ./$a/$b/$c/$d.txt
			done
		done
	done
done
