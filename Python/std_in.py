# leggo i dati passati tramite una pipe allo standard input e li passo allo standard output

import sys
standard_input = sys.stdin.readlines()
for line in standard_input:
    sys.stdout.write(line)
