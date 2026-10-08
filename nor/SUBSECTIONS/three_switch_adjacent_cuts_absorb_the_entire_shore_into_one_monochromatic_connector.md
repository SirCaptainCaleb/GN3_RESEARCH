# Three switch-adjacent cuts absorb the entire shore into one monochromatic connector

## Metadata

- ID: three_switch_adjacent_cuts_absorb_the_entire_shore_into_one_monochromatic_connector
- Parent Section: protected_root_certificates_and_cellular_extraction
- Position: 362
- Row version: 1
- Development version: 1
- Composition version: 1
- Composition stale: False

## Composition

Three switch-adjacent cuts give canonical two-zero-path decompositions of a good shore order. Their unported monochromatic concatenations do not automatically give a compatible connector. Article IV promotes the three cuts as candidates to be tested through exact endpoint ports.

## Development

Let A be one shore of a shortcut-free switching split B -> z -> A -> x, so z dominates A, A dominates x, and alpha(x,z,a)=0 for every a in A.

Take a NOR-good order
O=(a_1,...,a_k)
of A with bichromatic word
0^p 1^q.
For each cut index j in {p,p+1,p+2} that lies between 1 and k-1, define
P_j=(a_1,...,a_j)
and
R_j=(a_k,a_{k-1},...,a_{j+1}).

Every internal window of P_j has color 0, because its window ranks are at most p. Every internal window of R_j also has color 0, because the corresponding windows in the unreversed suffix have color 1 and reversal complements ternary color.

Write e_i=1 when a_i -> a_{i+1} in the switching-normalized shore tournament and e_i=0 otherwise.

Consider
Q_j=P_j, x,z, R_j.
All internal windows of P_j and R_j are zero. The two windows meeting x,z are zero because alpha(a,x,z)=alpha(x,z,a)=0 on A. The remaining two possible collar windows satisfy
alpha(a_{j-1},a_j,x)=1-e_{j-1},
alpha(z,a_k,a_{k-1})=e_{k-1},
with endpoint clipping. Therefore Q_j is monochromatic zero whenever
e_{j-1}=1 and e_{k-1}=0.

There is a symmetric placement
Q'_j=R_j,x,z,P_j.
Its two nontrivial collars are zero exactly when
e_{j+1}=0 and e_1=1.

Hence a spanning monochromatic connector on A union {x,z} exists whenever either:
(1) the final shore edge is backward and at least one of e_{p-1},e_p,e_{p+1} is forward; or
(2) the first shore edge is forward and at least one of e_{p+1},e_{p+2},e_{p+3} is backward,
with out-of-range bits omitted.

This reduces collective absorption of the entire minimum shore to a finite endpoint-edge condition on one good shore order. The three admissible cut positions are exactly the cuts for which the left block lies wholly in the zero phase and the reversed right block lies wholly in the one phase.
