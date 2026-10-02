# A span-two omission replacement always creates a Hamiltonian four-window

## Statement

Let H be a minimum counterexample and let H-x=P|Q be a deletion two-cover with P=(p_0,...,p_{m-1}). Suppose for some 0<=j<=m-3 the cross triple (p_j,x,p_{j+2}) is tight. Then the four-set W={p_j,p_{j+1},x,p_{j+2}} is Hamiltonian. Consequently H-W is non-Hamiltonian with path-cover number two. In particular, the span-two clean omission-replacement branch of f05c3c78500c is already an anchored Hamiltonian four-window and is not a neutral transport residue.

## Body

Put u=p_j, y=p_{j+1}, and v=p_{j+2}. The displayed path P gives the tight triple (u,y,v), while the hypothesis gives the parallel tight triple (u,x,v). Boundary antisymmetry applied to the triple on {x,u,y} says exactly one of (x,u,y) and (y,u,x) is tight. If (x,u,y) is tight, then (x,u,y,v) is a tight Hamilton path on W because its two consecutive triples are (x,u,y) and (u,y,v). If instead (y,u,x) is tight, then (y,u,x,v) is a tight Hamilton path on W because its two consecutive triples are (y,u,x) and (u,x,v). Thus W is Hamiltonian in all cases. Since H is a minimum counterexample, W is proper; if H-W were Hamiltonian, Hamilton paths on W and H-W would form a spanning two-cover of H. Hence H-W is non-Hamiltonian, and minimum-counterexample calculus gives path-cover number two. No cyclic rotation of an ordered triple is used.