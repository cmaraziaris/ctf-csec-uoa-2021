

import requests
import sys


# s = []
# s.append('curl -v localhost:8000/ultimate.html -X POST -H "Host: localhost:8000" -H "Connection: keep-alive" ')
# s.append('curl ')


# -H "Cache-Control: max-age=0" -H "sec-ch-ua: \" Not A;Brand";v=\"99\", \"Chromium\";v=\"90\", \"Google Chrome\";v=\"90\"" -H "sec-ch-ua-mobile: ?0" \
# -H "Upgrade-Insecure-Requests: 1" \
# -H "User-Agent: Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36" \
# -H "Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9" \
# -H "Sec-Fetch-Site: none" \
# -H "Sec-Fetch-Mode: navigate" \
# -H "Sec-Fetch-User: ?1" \
# -H "Sec-Fetch-Dest: document" \
# -H "Accept-Encoding: gzip, deflate, br" \
# -H "Accept-Language: en-US,en;q=0.9" \
# -H "Content-Length: 15" \
# -u test:test \
# --data-binary @payload.bin
# '''

# print(s)

headers = {
	'Authorization' : 'Basic dGVzdDp0ZXN0',
	'Host': 'localhost:8000',
	'Connection' : 'keep-alive',
	'Cache-Control' : 'max-age=0',
	'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="90", "Google Chrome";v="90"',
	'sec-ch-ua-mobile' : '?0',
	'Upgrade-Insecure-Requests' : '1',
	'User-Agent' : 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36',
	'Accept' : 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
	'Sec-Fetch-Site' : 'none',
	'Sec-Fetch-Mode' : 'navigate',
	'Sec-Fetch-User' : '?1',
	'Sec-Fetch-Dest' : 'document',
	'Accept-Encoding' : 'gzip, deflate, br',
	'Accept-Language' : 'en-US,en;q=0.9'
}

if sys.argv[1] == '1':
	headers['Authorization'] = 'Basic YWRtaW46Ym9iJ3MgeW91ciB1bmNsZQ=='



payload = None
with open("payload.bin", "rb") as f:
	payload = f.read()
print(payload)

url = 'http://localhost:8000/ultimate.html'

# response = requests.post(url, headers=headers, data=payload)
# print(response)
# print(response.text)


s = requests.Session()

req = requests.Request('POST', url, headers=headers)
prepped = req.prepare()
prepped.headers['Content-Length'] = 15
prepped.body = b"?admin_pwd=" + payload

print(prepped.body)


try:
	resp = s.send(prepped)

	print(resp.status_code)
	print(resp.text)

except requests.exceptions.RequestException as e:
	print(e)

