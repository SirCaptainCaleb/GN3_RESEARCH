# General-r switching hyperedges split into retained pairs or external three-vertex bridges

## Statement


Retain the setup of 80e2e6b25cab. Thus Q is a rank-q anchor path ending at v, R=V(Q)\h, P is a maximum p-edge path ending at v with U=V(P)\last(P), and every switching edge f in a family F through v satisfies
  |C_Q(f)|>=2,
  C_Q(f)=(f\{v}) intersect R,
while f has exactly one off-v contact c_f with U.

Partition F into:
  F_ret={f: c_f in C_Q(f)},
  F_ext={f: c_f notin C_Q(f)}.

Then:

(1) For every f in F_ret one can choose
  a_f in C_Q(f)\{c_f}
so that
  a_f in R\U,
  c_f in R intersect U.
The pairs {a_f,c_f}, f in F_ret, are pairwise vertex-disjoint. Hence F_ret canonically supplies a matching from anchor-only vertices to retained anchor vertices.

(2) For every f in F_ext one can choose distinct
  a_f,b_f in C_Q(f)
so that
  a_f,b_f in R\U,
  c_f in U\R.
The triples {a_f,b_f,c_f}, f in F_ext, are pairwise vertex-disjoint. Hence F_ext supplies a three-vertex bridge hypermatching with two anchor-only endpoints and one maximum-path-only endpoint.

Consequently, if |F|=D, then either there is a retained crossing matching of size at least ceil(D/2), or there is an external bridge hypermatching of size at least ceil(D/2).

For r=3 the external case is impossible: |C_Q(f)|>=2 already exhausts the two vertices of f\{v}. Thus the dichotomy collapses to the ordinary anchor-to-maximum crossing matching used in the 3-uniform gap-one theory.


## Body


Fix f in F. Distinct edges of F all contain v, so linearity implies their off-v vertex sets f\{v} are pairwise disjoint. It is therefore enough to verify the asserted location of the chosen vertices edge by edge.

Suppose first that f lies in F_ret. Then c_f belongs to C_Q(f), and |C_Q(f)|>=2, so choose a_f in C_Q(f)\{c_f}. Since c_f is the unique off-v vertex of f lying in U, the vertex a_f is not in U. Thus a_f in R\U, while c_f belongs to R intersect U. Pairwise disjointness of the sets f\{v} makes all chosen pairs disjoint.

Suppose instead that f lies in F_ext. Choose distinct a_f,b_f in C_Q(f). Again c_f is the unique off-v U-contact, so a_f,b_f are outside U and hence lie in R\U. Also c_f cannot lie in R, because otherwise c_f would belong to C_Q(f), contrary to f in F_ext. Thus c_f lies in U\R. Pairwise disjointness again makes the chosen triples disjoint across f.

Finally one of F_ret,F_ext has size at least ceil(D/2), giving the stated alternative. If r=3, the set f\{v} has size two. The condition |C_Q(f)|>=2 then gives C_Q(f)=f\{v}, leaving no distinct off-v vertex c_f outside C_Q(f), so F_ext is empty.
