#!/bin/bash

while true
do
#read door latch sensor until door is open(or left open)
sudo python hall_effect.py
mutt -s " The door is open!" 4086562329@txt.att.net < nada.txt
done