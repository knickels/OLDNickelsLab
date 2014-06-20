# Before use this Makefile the variables CC an INCLUDE must be configured
#
# Example:
#  CC = wine /usr/local/mplabC30/bin/pic30-coff-gcc.exe
#  INCLUDE = -I/usr/local/epuckProjectLibs/include -I/usr/local/mplabC30/support/h/

CC = wine <path to mplabC30 install>/bin/pic30-coff-gcc.exe
INCLUDE = -I<path to libepuck install>/include -I<path to mplabC30 install>/support/h/
C_ARGS = -mcpu=30F6014A -c -x c -g

all:main.o epuckPlayer.o

main.o:main.c
	$(CC) $(C_ARGS) $(INCLUDE) main.c

epuckPlayer.o:epuckPlayer.c
	$(CC) $(C_ARGS) $(INCLUDE) epuckPlayer.c

clean:
	rm -f main.o epuckPlayer.o output.cof output.hex proj.map
