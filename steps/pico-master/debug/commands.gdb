set pagination off
set follow-fork-mode child
set logging file out_gdb.txt
set logging on
b main.c:179
commands 1
info frame
x/32x $sp
c
end

b main.c:181
commands 2
info frame
x/32x $sp
c
end

b httpd.c:32
commands 3
info frame
x/32x $sp
c
end

r
set logging off
