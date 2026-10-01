# The switching label is universally noninsertable before rescue and forced internal after rescue

## Statement

In the one-split toggle of compattoggle29, the switching label c has two simultaneous global properties. First, c is noninsertable into every Hamilton path on R union {a} and into every Hamilton path on S union {b}. Second, c is an internal vertex of every Hamilton path on R union {b,c} and of every Hamilton path on S union {a,c}. Likewise b is noninsertable into every Hamilton path on R, and a is noninsertable into every Hamilton path on S.

## Body

# Proof

By compattoggle29,

R union {a} is Hamiltonian but R union {a,c} is non-Hamiltonian.

Take any Hamilton path P on R union {a}. If c could be inserted at any position of the displayed order of P to form a tight path, the resulting path would span R union {a,c}, contradicting its non-Hamiltonicity. Hence c is noninsertable into every Hamilton path on R union {a}.

The same argument using S union {b} Hamiltonian and S union {b,c} non-Hamiltonian shows that c is noninsertable into every Hamilton path on S union {b}.

Now R union {b,c} is Hamiltonian while R union {b} is non-Hamiltonian. Let Q be any Hamilton path on R union {b,c}. If c were an endpoint of Q, deleting that endpoint would leave a tight Hamilton path on R union {b}, contradiction. Thus c is internal in every Hamilton path on R union {b,c}.

Similarly S union {a,c} is Hamiltonian while S union {a} is non-Hamiltonian, so c is internal in every Hamilton path on S union {a,c}.

Finally R is Hamiltonian while R union {b} is non-Hamiltonian, so b is noninsertable into every Hamilton path on R. Symmetrically, a is noninsertable into every Hamilton path on S.

Thus the one-split residue is not merely a Boolean Hamiltonicity toggle: the same switching label c is universally blocked from insertion into the two one-label-good supports and universally excluded from the endpoints of every Hamilton path on the two rescued two-label supports.