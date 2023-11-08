repeat
	do shell script "caffeinate -dimsu &> /dev/null &"
    do shell script "/usr/local/bin/python3 /Users/lizhidi/Downloads/GetNextAvail.py"
    delay 1800 -- 单位为秒，表示延迟30分钟
end repeat