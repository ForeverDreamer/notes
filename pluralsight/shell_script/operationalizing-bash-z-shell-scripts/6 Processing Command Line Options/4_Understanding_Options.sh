#!/bin/bash

while getopts ':cd' opt
do
  while (( "$#" )) ; do
    # ^-, '-'开头的正则表达式
    if ! [[ $1 =~ ^- ]] ; then
      username="$1"
    fi
    shift
  done
  case "$opt" in
    # -m, --create-home: Create the user's home directory if it does not exist
	  c) sudo useradd -m "$username"
      break ;;
    # -r, --remove: Files in the user's home directory will be removed along with the home directory itself and the user's mail spool
    d) sudo userdel -r "$username"
	    break ;;
    *) echo "Usage: $0 [-c|-d] -- <username>" ;;
  esac
done
