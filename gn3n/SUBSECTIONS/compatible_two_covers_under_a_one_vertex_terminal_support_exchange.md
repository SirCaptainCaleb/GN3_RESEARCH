# Compatible two-covers under a one-vertex terminal-support exchange

## Metadata

- ID: compatible_two_covers_under_a_one_vertex_terminal_support_exchange
- Parent Section: terminalization_reachability_and_the_exact_frontier
- Position: 10
- Row version: 1
- Development version: 1
- Composition version: None
- Composition stale: False

## Cold composition

(none yet)

## Development

## A one-vertex exchange admits compatible (5|5) two-covers

The boundary-crossing coherence problem requires a stronger statement than mere two-coverability of each terminal support. The required strengthening is true.

**Lemma (compatible one-vertex exchange).** Let (T) be a nine-vertex set in a boundary tournament and let (x,y
otin T) be distinct. Then there is a partition
[
T=Asqcup B,qquad |A|=4,quad |B|=5,
]
such that all three five-sets
[
B,qquad Acup{x},qquad Acup{y}
]
are Hamiltonian.

Consequently the two ten-sets
[
Tcup{x},qquad Tcup{y}
]
admit complementary Hamiltonian (5|5) covers sharing the same Hamiltonian side (B).

### Proof

Call a five-set **good** when it is Hamiltonian.

Let (mathcal Nsubseteqinom{T}{5}) be the non-Hamiltonian five-sets and put (b=|mathcal N|). Every six-set contains at least four Hamiltonian five-subsets, so at most two of its six five-subsets are non-Hamiltonian. Counting incidences between (mathcal N) and six-subsets of (T),
[
4ble 2inom96=168,
]
hence
[
ble42.
]

Define
[
mathcal B_x={Aininom{T}{4}:Acup{x}	ext{ is non-Hamiltonian}},
]
and define (mathcal B_y) analogously.

Fix (Kininom{T}{5}). In the six-set (Kcup{x}), if (K) is Hamiltonian then at most two of the five sets
[
Acup{x},qquad Aininom K4,
]
can be non-Hamiltonian. If (K) is non-Hamiltonian, then (K) itself already occupies one of the at most two bad deletions, so at most one of those five (x)-extensions is bad. Therefore
[
sum_{Kininom T5}|mathcal B_xcapinom K4|
le 2(126-b)+b
=252-b.
]
Every (Aininom T4) lies in exactly five five-subsets (Ksubset T), hence
[
5|mathcal B_x|le252-b.
]
The same estimate holds for (mathcal B_y).

Suppose the lemma fails. For every (Aininom T4) whose complement (B=Tsetminus A) is Hamiltonian, at least one of (A+x,A+y) is non-Hamiltonian. There are (126-b) such (A), so
[
126-b
le |mathcal B_xcupmathcal B_y|
le |mathcal B_x|+|mathcal B_y|
le rac{2(252-b)}5.
]
Rearranging gives
[
bge42.
]
Thus every inequality is an equality:
[
b=42,qquad
|mathcal B_x|=|mathcal B_y|=42,qquad
mathcal B_xcapmathcal B_y=arnothing.
]

Moreover the local incidence estimates are sharp for every (Kininom T5). Hence each Hamiltonian (K) contains exactly two members of (mathcal B_x), while each non-Hamiltonian (K) contains exactly one. The identical statement holds for (mathcal B_y).

Let (W) be the (126	imes126) inclusion matrix with rows indexed by five-sets (Ksubset T), columns indexed by four-sets (Asubset T), and
[
W_{K,A}=1iff Asubset K.
]
Writing (mathbf b_x,mathbf b_y) for the characteristic vectors of (mathcal B_x,mathcal B_y), and (mathbf n) for that of (mathcal N), the equality conditions give
[
Wmathbf b_x=2mathbf1-mathbf n
=Wmathbf b_y.
]
But (W) is nonsingular. Indeed, after identifying each row (K) with its four-set complement (Tsetminus K), (W) becomes the disjointness matrix of the Kneser graph (KG(9,4)). Its Johnson-scheme eigenvalues are
[
5,-4,3,-2,1,
]
all nonzero. Therefore
[
mathbf b_x=mathbf b_y,
]
contradicting
[
mathcal B_xcapmathcal B_y=arnothing
]
and (|mathcal B_x|=42).

The contradiction proves the lemma. (square)

### Relevance to terminal surgery

When a rank-two residue changes an order-ten terminal support by exchanging one endpoint vertex, the two supports have the form (T+x) and (T+y). The lemma supplies two-covers
[
Bmid(A+x),qquad Bmid(A+y)
]
with a common Hamiltonian side. Thus the local replacement can be chosen compatibly across that one-vertex support exchange; only the exchanged endpoint side changes. This removes the main combinatorial ambiguity in boundary-crossing square residues and is the natural input for the remaining braid-residue check.
