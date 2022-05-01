#!/bin/bash -x
case $1 in
    on )
        # 只对子进程有效，shell父进程无效
        export WINDOWS_HOST=`cat /etc/resolv.conf|grep nameserver|awk '{print $2}'`
        export ALL_PROXY=socks5://$WINDOWS_HOST:10808
        export HTTP_PROXY=$ALL_PROXY
        export HTTPS_PROXY=$ALL_PROXY
        git config --global proxy.https $ALL_PROXY
        echo "代理开启"
        ;;
    off )
        unset WINDOWS_HOST
        unset ALL_PROXY
        unset HTTP_PROXY
        unset HTTPS_PROXY
        git config --global --unset http.proxy
        echo "代理关闭"
        ;;
    * )
        echo "参数只支持(on|off)"
        exit 1
        ;;
esac