
import base64
from hashlib import sha256


def encode_to_b64(str):
	b = str.encode('ascii')
	b64_b = base64.b64encode(b)
	b64_str = b64_b.decode('ascii')
	return b64_str

def encode_to_sha256(str):
	b = str.encode('ascii')
	sha256_str = sha256(b).hexdigest()
	return sha256_str

if __name__ == '__main__':
	code = input()
	code_sha256 = encode_to_sha256(code)
	mid = code + ':' + code_sha256
	final = encode_to_b64(mid)
	print(final)
	exit(0)