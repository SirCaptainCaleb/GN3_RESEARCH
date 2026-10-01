# Hamiltonian five-set stars synchronize into same-end extenders or a complete Hamiltonian four-grid

## Statement

Let D be a fixed four-vertex set in a boundary tournament H, and let U be disjoint from D with H[D union {v}] Hamiltonian for every v in U. Then there is U' subseteq U with
|U'| >= ceil(|U|/60)
such that one of the following holds.
(1) There is a fixed Hamiltonian order R of D and every v in U' extends R at the same endpoint.
(2) There are fixed distinct a,b in D such that (a,v,b) is tight for every v in U'. Consequently, for every distinct p,q in U', the four-set {a,b,p,q} is Hamiltonian; moreover every three distinct p,q,r in U' make {a,b,p,q,r} Hamiltonian.

## Body

Use the same 60-type classification as in five_star_sync60_01. For each v in U choose a Hamiltonian order P_v on D union {v}. If v is an endpoint, record its side and the induced four-vertex order of D; there are at most 48 such types. If v is internal, record its ordered neighboring pair (a_v,b_v) in D; there are at most 12 such types. Hence some type occurs on U' with |U'|>=ceil(|U|/60).

An endpoint type gives outcome (1).

For an internal type there are fixed distinct a,b in D with (a,v,b) tight for every v in U'. This is the common oriented fixed-pair hypothesis of endpoint_reversal_fixedpair01 (with the fixed ordered endpoints relabeled). Therefore every distinct p,q in U' make {a,b,p,q} Hamiltonian.

Also, for any three distinct p,q,r in U', the parallel-middle theorem in localextend01 applied to the common ordered pair a,b gives a Hamiltonian path on {a,b,p,q,r}. Thus outcome (2) has both the complete Hamiltonian four-grid and the Hamiltonian five-set consequence. ∎
