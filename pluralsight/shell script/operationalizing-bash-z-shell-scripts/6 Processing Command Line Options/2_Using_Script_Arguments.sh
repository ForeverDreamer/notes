#!/bin/bash
printf "The script is: %s\n" "$0"
printf "The number of arguments is: %d\n" "$#"
printf "The arguments list is: %s\n" "$*"
printf "The arguments as an array are: %s\n" "$@"
fname="$1"
lname="$2"
printf "First: %s Last: %s\n" "$fname" "$lname"