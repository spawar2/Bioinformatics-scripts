import codons
import fasta

a = fasta.fasta("fasta.txt")

t = codons.dna_to_protein()
# forward using slices
print t.translate(a)
print ' '+t.translate(a[1:])
print '  '+ t.translate(a[2:])
#backward using slices
b = list(a)
b.reverse()
c = []
comp = {'A':'T', 'G':'C','T':'A','C':'G'}
for i in b:
    c.append( comp[i])
print t.translate(c)
print ' '+t.translate(c[1:])
print '  '+t.translate(c[2:])
