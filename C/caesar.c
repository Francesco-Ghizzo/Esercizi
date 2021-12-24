#include <stdio.h>
#include <stdlib.h>
#include <sys/types.h>
#include <unistd.h>

int main(int argc, char **argv) {
	char buffer[100];
	char shifted_buffer[100];
	size_t nbytes;
	ssize_t bytes_read;
	int fd;
	fd = fileno(stdin);						/* Get file descriptor of stdin */
	nbytes = sizeof(buffer);
	bytes_read = read(fd, buffer, nbytes);				/* Read from stdin */ 
	int i, n;		
	char *ptr;
	char *string = argv[1];							/* Arguments to string */
	n = strtol(string, &ptr, 10);						/* Cast string to int */
	for (i=0; i<bytes_read; i++) {
		if      (buffer[i]<=90 && buffer[i]>=65) {			/* If UPPERCASE CHARACTERS, then */
			shifted_buffer[i] = ((buffer[i]-65+n)%26)+65;	/* shift n places and take the remainder of 26 */
		}
		else if (buffer[i]<=122 && buffer[i]>=97) {			/* If LOWERCASE CHARACTERS, then  */
			shifted_buffer[i] = ((buffer[i]-97+n)%26)+97;	/* shift n places and take the remainder of 26 */
		}
		else {								/* if SPECIAL CHARACTERS, then  */
			shifted_buffer[i] = buffer[i];			/* just copy buffer */
		}
	}
	fprintf(stdout, "%s\n", shifted_buffer);			/* Write shifted_buffer to stdout */ 
}



