# Hamiltonian five-set stars synchronize with a sixty-type bound

## Statement

Let D be a fixed four-vertex set in a boundary tournament H, and let U be a set of vertices disjoint from D such that H[D union {v}] is Hamiltonian for every v in U. Then there is a subset U' with
|U'| >= ceil(|U|/60)
and one of the following two structures.
(1) There is a fixed Hamiltonian order R of D such that every v in U' extends R at the same endpoint.
(2) There are fixed distinct a,b in D such that (a,v,b) is tight for every v in U'.
In case (2), every three distinct p,q,r in U' together with a,b induce a Hamiltonian five-set.

## Body

For each v in U choose one Hamiltonian order P_v of D union {v}.

If v is an endpoint of P_v, delete v. The remaining four symbols occur consecutively, so they form a Hamiltonian order R_v of D. Record the type of v as the pair consisting of the side on which v occurs (left or right) and the ordered word R_v. There are at most 2*4!=48 endpoint types.

If v is internal in P_v, record only the ordered pair (a_v,b_v) of its two neighboring vertices from D, so that (a_v,v,b_v) is a consecutive tight triple of P_v. There are at most 4*3=12 such ordered-neighbor types.

Thus at most 60 types occur altogether. By pigeonhole, some type is realized by a set U' of size at least ceil(|U|/60).

If the repeated type is an endpoint type, all v in U' extend the same Hamiltonian order R of D at the same endpoint, giving (1).

If the repeated type is an internal type (a,b), then (a,v,b) is tight for every v in U', giving (2). For any three distinct p,q,r in U', the parallel-middle theorem in localextend01 applied to the fixed ordered pair (a,b) gives a Hamiltonian path on {a,b,p,q,r}. Hence every such five-set is Hamiltonian. ∎