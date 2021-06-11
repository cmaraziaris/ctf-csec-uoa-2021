
cp request.http temp_req
printf "$1" >> temp_req
cat temp_req
rm -f temp_req