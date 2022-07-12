#!/bin/bash
case $USER in
    doer )
        echo "You are cool"
        ;;
    root )
        echo "You are the boss"
        ;;
esac

declare -l month
month=$(date +%b)
case $month in
    dec | jan | feb )
        echo "Winter";;
    mar | apr | may )
        echo "Spring";;
    jun | jul | aug )
        echo "Summer";;
    sep | oct | nov )
        echo "Autumn"
esac
