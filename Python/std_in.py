# leggo i dati passati allo standard input tramite una pipe e li passo allo standard output

import sys
standard_input = sys.stdin.readlines()
for line in standard_input:
    sys.stdout.write(line)
