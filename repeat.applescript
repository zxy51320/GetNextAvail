repeat
	do shell script "caffeinate -dimsu &> /dev/null &"
    do shell script "/usr/local/bin/python3 /Users/lizhidi/Downloads/GetNextAvail.py"
    delay 1800 -- ��λΪ�룬��ʾ�ӳ�30����
end repeat