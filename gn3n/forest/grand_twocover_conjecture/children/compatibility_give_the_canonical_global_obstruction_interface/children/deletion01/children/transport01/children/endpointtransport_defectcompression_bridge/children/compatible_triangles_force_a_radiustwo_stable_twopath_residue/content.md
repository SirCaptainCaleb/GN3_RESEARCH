# Endpoint compatible triangles force a radius-two stable two-path residue

## Statement

For an endpoint common-gap compatible cover triangle in a minimum counterexample, if T is its three label set and U is the complementary vertex set, then U and every induced U-S with |S| at most two are non-Hamiltonian of path-cover number exactly two. Every exact two-cover of U therefore has both components of order at least three.

## Body

# Radius-two stable residue

Let H be a minimum counterexample. Let F_a,F_b,F_c be a pairwise-compatible exact omission-cover triangle whose common insertion gap is an endpoint. Put T={a,b,c} and U=V(H)-T.

Endpoint-gap geometry makes the precedence tournament cyclic. Relabel it a->b->c->a. The common-gap theorem therefore gives the tight triples (c,b,a), (a,c,b), (b,a,c). On the ordinary edges cb,ba,ac these give a directed comparison cycle.

For distinct d,e in U, the five-set T union {d,e} is Hamiltonian: otherwise the five-vertex structure theorem would make its comparison digraph acyclic, contradicting the displayed cycle.

Hence U-{d,e} cannot be Hamiltonian, since complementary Hamilton paths on T union {d,e} and U-{d,e} would two-cover H. Minimality gives pc(U-{d,e})=2.

Likewise U-d cannot be Hamiltonian: if it had a Hamilton path, removing one endpoint e would make U-{d,e} Hamiltonian. Thus pc(U-d)=2.

Finally U cannot be Hamiltonian because T itself has a Hamilton path; otherwise T|U would two-cover H. Thus pc(U)=2.

If an exact two-cover P|Q of U had |P|=1 or 2, then Q would Hamiltonize U-S for a set S of order 1 or 2, contrary to the preceding conclusions. Therefore both components have order at least three. ∎