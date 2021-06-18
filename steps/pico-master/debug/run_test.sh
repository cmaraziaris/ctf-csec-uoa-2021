

echo $1, $2
python3 process_answer.py 1 $1 $2 && cat request_post_template.http > temp.http && cat payload.bin >> temp.http && cat temp.http | socat - TCP4:localhost:8000