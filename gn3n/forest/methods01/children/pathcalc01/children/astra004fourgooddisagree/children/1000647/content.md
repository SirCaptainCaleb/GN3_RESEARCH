# Absence of order disagreement forces universal six-set Hamiltonicity

## Statement

Let H be a minimum counterexample. If no two tight Hamiltonian paths on overlapping induced supports of H exhibit order disagreement, then every six-vertex induced subtournament of H is Hamiltonian. Consequently, for every six-set S, H-S is non-Hamiltonian with path-cover number exactly two. Moreover the minimum smaller-component order mu among all one-vertex deletion two-covers satisfies mu>=6.

## Body

Let S be any six-vertex subset of V(H). By the certified four-of-six theorem in smallset01, at least four vertices d in S have H[S-{d}] Hamiltonian. If H[S] were non-Hamiltonian, the certified theorem astra004fourgooddisagree, applied to arbitrary Hamilton paths on four such deletions, would force order disagreement between two of them, contrary to the hypothesis. Hence H[S] is Hamiltonian.

Since S is a proper Hamiltonian support in a minimum counterexample, minimum-counterexample calculus gives pc(H-S)<=2. The complement H-S cannot be Hamiltonian, because Hamilton paths on S and H-S would form a spanning two-cover of H. Therefore H-S is non-Hamiltonian and pc(H-S)=2.

Finally suppose some deletion cover H-x=P|Q had a component P of order at most five. Every deletion-cover component has order at least three in a minimum counterexample, so 3<=|P|<=5. The certified theorem 6f72075b0b54 then supplies a four-label fixed-complement deletion family whose chosen Hamilton paths necessarily contain order disagreement, again contrary to the hypothesis. Thus every component of every deletion cover has order at least six, i.e. mu>=6.
