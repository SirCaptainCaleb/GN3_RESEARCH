# Every prescribed pair in a minimum counterexample lies in a Hamiltonian four-set with two-path complement

## Statement

Let H be a minimum counterexample. For every two distinct vertices L,R and every three-element set D disjoint from {L,R}, there are distinct y,z in D such that W={L,R,y,z} is Hamiltonian and H-W is non-Hamiltonian with path-cover number two. In particular H contains such a four-set unconditionally, so every branch of a local-reversal reduction already satisfies the former four-or-five-set existence conclusion.

## Body

Fix L,R and an exterior three-set D. Partition D according to whether (L,y,R) or (R,y,L) is tight. Boundary antisymmetry gives exactly these two classes. Two labels y,z share a class. If (L,y,R) and (L,z,R) are tight, then exactly one of (y,L,z) and (z,L,y) is tight; respectively (y,L,z,R) or (z,L,y,R) is a Hamilton path on W. Each displayed path has precisely the two checked consecutive triples. If instead (R,y,L) and (R,z,L) are tight, use respectively (y,R,z,L) or (z,R,y,L), according to the reversal pair (y,R,z)/(z,R,y). Thus W is Hamiltonian in both cases. This is the elementary fixed-pair argument recorded in bd3c8d17ca06, reproduced here in full.

By mincex01, |H|>10, so W is proper. Minimality gives pc(H-W)<=2, and pc(H-W)=1 would combine with the Hamilton path on W to two-cover H, a contradiction. Hence pc(H-W)=2.

This strengthens and bypasses the previous global four-or-five-set existence proof: no endpoint-reversal classification, maximal witness, or matching-block extension is needed for this conclusion. It does not assert that W retains an entire previously chosen triple, a displayed orientation of L,R, or a preselected complement cover. Those stronger compatibility requirements, when needed by consumers, remain separate obligations.