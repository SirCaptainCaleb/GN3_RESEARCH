# Cyclic-kernel complements are radius-two stable when mu is at least six

## Statement

Let H be a minimum counterexample with minimum deletion-cover side mu at least 6. If X is the exceptional cyclic four-kernel and K=H-X, then K-S is non-Hamiltonian of path-cover number two for every S in K of size at most two. Hence every exact two-cover of K has both components of order at least three.

## Body

The known cyclic-kernel theorem gives the cases |S|=0,1 and says that for every u in X and distinct d,e in K, F=(X-{u}) union {d,e} is Hamiltonian. If K-{d,e} were Hamiltonian, then F together with K-{d,e} would two-cover H-u. The first side has order 5; the other has order n-6, at least 5 because n>10. Since H-u is not Hamiltonian (else it plus singleton u two-covers H), this is an exact deletion two-cover with smaller side at most 5, contradicting mu>=6. Thus every K-{d,e} is non-Hamiltonian; minimality gives pc=2. If an exact two-cover of K had a two-vertex component {d,e}, the other component would Hamiltonize K-{d,e}, contradiction; singleton components were already excluded.