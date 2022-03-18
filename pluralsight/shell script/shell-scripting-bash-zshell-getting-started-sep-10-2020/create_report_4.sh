#!/bin/bash

# 语法：if testcode; then successcode; else failcode; fi
# 查看比较选项：man test

if [[ ! $input_file ]]; then
    echo "Error: Input file not configured"
    # return 1
    exit 1
fi

if [[ -e $input_file ]]; then
    echo "Error: Input file $input_file does not exist"
    exit 1
fi

if [[ ! $1 ]]; then
    echo "Error: missing parameter: container name"
    exit
fi
container="$1"

if [[ $2 ]]; then
    directory="$2"
else
    directory="$HOME/reports"
fi
output_file="$directory/${container}_report.csv"

mkdir -p -- "$directory"
if grep -- "$container" "$input_file" > "$output_file"; then
    echo "Wrote report $output_file"
else
    echo "container $container not found"
fi
