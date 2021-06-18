
import sys

offset_ultimate = int(sys.argv[1])
offset_stack = int(sys.argv[2])

hardcoded_base_param_arg = 'ffffce18'

b = int(hardcoded_base_param_arg, 16)
base_param_arg = b - offset_stack


print(b)
print(base_param_arg)
print(offset_stack)


param_arg = hex(base_param_arg)[2:]
print('Stack: ', param_arg)
