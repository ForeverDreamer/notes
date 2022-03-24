#!/bin/bash
function create_directory() {
    # 函数内使用declare定义的变量只在函数内有效
    declare -l directory
    # -r: raw, 忽略转义符, -p: prompt
    read -rp "Enter a directory name: " directory
    mkdir "$directory"
}

while true; do
    clear
    echo "Choose 1 2 or 3"
    echo "1: list users"
    echo "2: create directory"
    echo "3: quit"
    # -s: silent, -n1: 只接受1个字符
    read -sn1
    case "$REPLY" in
        1) who;;
        2) create_directory;;
        3) exit 0;;
    esac
    read -n1 -p "Press any key to continue"
done