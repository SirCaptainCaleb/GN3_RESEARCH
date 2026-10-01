# Critical residue deletions either give two-hole witnesses or fall exactly onto equality

## Statement

Assume the dense-core all-special conjecture is true for forbidden length ell-1, and let ell=3m+1. Let H be a P_ell-free linear 3-graph on 2ell-1=6m+1 vertices with minimum degree at least 2m+1. Let
  P=(g_1,...,g_{ell-2},e)
be a spanning (ell-1)-edge path ending in a nonspecial edge e, and let a be either free vertex of g_1.

Then H-a is P_{ell-1}-free, e has rank ell-2 in H-a, and exactly one of the following holds:

(A) e is special in H-a. Then H-a supplies an alternate wrong-entrance (ell-2)-edge path Q_a ending in e, hence the same two-hole witness structure as in the good residue classes.

(B) e is nonspecial in H-a. Then
  delta(H-a)=2m.
Consequently delta(H)=2m+1, and there exists a vertex v_a!=a with
  d_H(v_a)=2m+1,
  d_{H-a}(v_a)=2m,
such that a and v_a lie together in an edge of H.

Thus the residue ell≡1 mod3 has no diffuse extra case: every failed deletion step lands exactly on the equality threshold and exposes a minimum-degree neighbor of the deleted hole.

## Body

Deleting a removes g_1 but leaves
  (g_2,...,g_{ell-2},e),
an (ell-2)-edge path ending in e. Since H-a has 6m vertices, it cannot contain a linear path of ell-1=3m edges, which would require 6m+1 vertices. Hence phi_{H-a}(e)=ell-2.

Linearity implies deletion of a lowers any surviving vertex degree by at most one, so
delta(H-a)>=delta(H)-1>=2m.

If e is special in H-a, (A) holds and the alternate-entrance witness follows from the unique-longest-entrance characterization exactly as in 8e4a8307bc49.

Suppose e remains nonspecial in H-a. If delta(H-a)>=2m+1, then
delta(H-a)>2(ell-1)/3=2m,
so the inductive dense-core conjecture at forbidden length ell-1 would make every edge of H-a special, contradiction. Therefore delta(H-a)=2m.

Choose v_a with d_{H-a}(v_a)=2m. Since d_H(v_a)>=2m+1 and deletion lowers degree by at most one, equality must hold:
d_H(v_a)=2m+1
and exactly one edge through v_a was deleted. That deleted edge contains a, so a and v_a are adjacent in a hyperedge. In particular delta(H)=2m+1.