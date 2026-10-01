# Synchronized reverse crosses give a Hamiltonian four-set unless their orientations oppose

## Statement

Under compatdualreverse25, let r in R and s in S be the two core vertices witnessing reverse cross triples for the same special-label pair x,y. If the two triples have the same orientation through x,y, i.e. after possibly interchanging x,y both (y,r,x) and (y,s,x) are tight, then H[{x,y,r,s}] is Hamiltonian. Therefore the only non-Hamiltonian four-vertex residue from the synchronized two-core reverse-pair branch is the opposite-orientation pattern, in which after relabeling (y,r,x) and (x,s,y) are tight.

## Body

# Proof

By compatdualreverse25 there are core vertices r in R and s in S and tight reverse-cross triples using the same special-label pair x,y.

If the two triples have the same orientation through x,y, relabel x,y if needed so they are

(y,r,x) and (y,s,x).

These are two parallel-middle triples with common ordered endpoints y,x and middle vertices r,s. The two-parallel-middle lemma in localextend01 therefore implies that at least one of

(y,r,x,s), (y,s,x,r)

is a tight Hamilton path on {x,y,r,s}. Hence the four-set is Hamiltonian.

Thus if this four-set is non-Hamiltonian, the two synchronized reverse-cross triples cannot have the same orientation. After interchanging x,y if necessary, the remaining pattern is

(y,r,x) and (x,s,y),

which is the claimed opposite-orientation cyclic residue.
