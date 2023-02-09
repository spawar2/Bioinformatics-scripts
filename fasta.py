# read a fasta file
# return a string
# fasta is
# "> junk "
# followed by letters

def fasta( filename):
    r = open(filename,"r")
    out = []
    for line in r:
        x = line.lstrip()
        if x[0] != '>':
            y = line.strip(' ')
            out.append(y)
    return "".join(out)
