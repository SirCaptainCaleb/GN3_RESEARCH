# Every minimum counterexample has a Hamiltonian five- or six-set carrying a genuine reversal

## Statement

Let H be a minimum counterexample. Then at least one of the following holds. (1) H contains a proper Hamiltonian six-vertex set U with non-Hamiltonian path-cover-two complement. (2) H contains a proper Hamiltonian five-vertex set W that contains all three vertices of a genuine reversing tight triple T, where T reverses an ordered edge (u,v) of another tight path; moreover H-W is non-Hamiltonian with path-cover number two.

## Body

Take the six distinct vertices u,v,a,x,y,z from reversal_stable_shell01, where a,u,v are the vertices of the genuine reversing tight triple and F={u,v,x,y,z} has the displayed alternating Hamiltonian five-path. Put S={a,u,v,x,y,z}. If H[S] is Hamiltonian, S is proper because a minimum counterexample has order greater than ten. Its complement cannot be Hamiltonian, or complementary Hamilton paths would two-cover H; by minimality the complement has path-cover number two, giving (1). Suppose H[S] is non-Hamiltonian. By the certified four-of-six theorem, at least four of the six one-vertex deletions S-r are Hamiltonian. The deletion S-a=F is already Hamiltonian. Thus at least three of the other five deletion labels in {u,v,x,y,z} are good. At most two of those labels are u,v, so at least one label t belongs to {x,y,z} and has S-t Hamiltonian. Put W=S-t. Then W contains a,u,v and therefore contains the original genuine reversing tight triple on those three vertices. The set W is proper. If H-W were Hamiltonian, its Hamilton path together with one on W would two-cover H, contradiction. Minimality therefore gives path-cover number two for H-W. This proves (2).
