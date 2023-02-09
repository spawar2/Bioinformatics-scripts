# write out all the codons as entries in a dictionary
# this won't work as code, but will write code

w = open("codons.py",'w')

w.write("class dna_to_protein:\n")
w.write(" def __init__(me):\n")
w.write("   me.codons = {} # an empty dictionary for the codons\n")
for one in ['A','G','C','T']:
    for two in ['A','G','C','T']:
        for three in ['A','G','C','T']:
            a = [one, two, three]
            b = ''.join(a)
            w.write('   me.codons["'+b+'"] = "P" \n')
w.close()
