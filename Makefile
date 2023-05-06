CC = clang
CFLAGS = -Wall -Werror -std=c11
LDFLAGS = -lcs50

TARGETS = $(patsubst %.c,%,$(wildcard *.c))

all: $(TARGETS)

%: %.o
	$(CC) $(CFLAGS) -o $@ $< $(LDFLAGS)

%.o: %.c
	$(CC) $(CFLAGS) -c $< -o $@

clean:
	rm -f $(TARGETS) *.o