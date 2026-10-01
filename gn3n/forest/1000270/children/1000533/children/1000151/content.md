# Hamiltonian five-set stars synchronize into endpoint extenders or parallel middles

## Statement

Let D be a fixed four-vertex set in a boundary tournament H, and let U be a set of vertices disjoint from D such that H[D union {v}] is Hamiltonian for every v in U. Then there is a subset U' of size at least ceil(|U|/120) and one of the following two structures. (1) There is a fixed Hamiltonian order R of D such that every v in U' extends R at the same endpoint. (2) There are fixed distinct a,b in D such that (a,v,b) is tight for every v in U'. In case (2), every three distinct vertices p,q,r in U' together with a,b induce a Hamiltonian five-set.

## Body

For each v in U choose one Hamiltonian order of D union {v}. Replace the symbol v by a placeholder *. There are exactly 5·4!=120 possible resulting templates, so some template occurs for a set U' of size at least ceil(|U|/120). If * is the first or last symbol, deleting it leaves the same four-symbol order R of D; all consecutive triples of R already occurred in the chosen five-path, so R is a tight Hamiltonian path, and the triple involving * shows that every v in U' extends the same endpoint of R. If * is internal, let a,b be its two neighboring symbols in the common template. Then (a,v,b) is tight for every v in U'. For any three distinct p,q,r in U', the certified parallel-middle lemma in localextend01 applied to the common ordered pair a,b shows that H[{a,b,p,q,r}] has a Hamiltonian tight path. This proves the dichotomy.
