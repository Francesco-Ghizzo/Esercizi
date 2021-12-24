#include <stdio.h>
#include <sys/types.h>
#include <unistd.h>

int main(int argc, char **argv) {
	char buffer[100];
	size_t nbytes;
	ssize_t bytes_read;
	int fd;
	fd = fileno(stdin);						/* Get file descriptor of stdin */
	nbytes = sizeof(buffer);
	bytes_read = read(fd, buffer, nbytes);				/* Read from stdin */ 
	fprintf(stdout, "%s\n", buffer);				/* Write buffer to stdout */ 
}



