# Compile 32-bit executable for compatibility.
# We need a 32-bit libs for this:
#   apt-get install libc6-dev-i386 libssl-dev:i386

CFLAGS = -g -fPIE -m32
LDFLAGS = -pie -m32

all: server

clean:
	@rm -rf *.o
	@rm -rf server

server: main.o httpd.o base64.o
	gcc $(LDFLAGS) -o server $^ -lcrypto

main.o: main.c httpd.h base64.h
httpd.o: httpd.c httpd.h
base64.o: base64.c base64.h

