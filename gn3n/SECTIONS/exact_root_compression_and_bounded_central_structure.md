# Exact-root compression and bounded central structure

**Summary:** Exact-root recurrence has no unbounded nonzero residue: nonzero carriers compress to at most four central vertices and ten determining vertices, while kappa_2>=2 forces a zero-root chamber.

## Statement

The exact inversion root converts every nonzero recurrent carrier into bounded central GN3 structure: the central block has order at most four, at most ten actual vertices determine the varying root data, and root circulation reduces to opposite pairs and directed three-cycles; for deletion distance at least two every positive exact-root carrier contains a zero-root chamber.

## Cold composition

## Exact-root compression and bounded central structure

The exact status coordinates from [[spanning_orders_and_defect_helly]] are
[
p(pi)=min{i:epsilon_i=0},qquad
q(pi)=max{i:epsilon_i=1},qquad
c(pi)=m+1-q(pi),
]
with exact deficiency
[
delta(pi)=q-p-1=m-(p+c).
]
The exact root
[
psi(pi)=e_{p(pi)}-e_{c(pi)}
]
is odd under reversal. Unlike the older switch-root compression, its anti-diagonal displacement is exactly the order-level distance from a two-cover.

### Positive root balance

The barycentric odd-map construction of [[convex_root_balance_and_bourgin_yang]] yields a proper permutahedron face (F) and strictly positive chamber weights satisfying
[
sum_{piinmathcal V(F)}lambda_pipsi(pi)=0.
]
Interpreting (e_i-e_j) as the directed root (i	o j), every occurring nonzero root lies on a directed return cycle inside the same carrier face. The common-face condition is essential: all witnessing orders vary only by permutations within one ordered block partition.

### Bounded central block theorem

The facewise endpoint-transport and block-separation arguments developed in the former recurrence Section imply the following canonical compression.

**Theorem.** Suppose a positive exact-root carrier has positive deficiency in every chamber and contains no zero root. Then all varying exact-root data are controlled by a central face block (B) with
[
|B|le4.
]
Moreover at most ten actual vertices are needed to determine all varying exact-root labels in the carrier, and every simple directed root cycle has length two or three.

Thus the nonzero exact-root branch has no unbounded permutahedral residue. The only root-level recurrence left is a bounded interaction among opposite roots and, before the final moment reduction, directed triangles.

### Cubic moment and pairwise root symmetry

After translation to the four-coordinate model, every occurring nonzero root lies on the graph
[
01,quad02,quad03,quad12.
]
Append the odd cubic coordinate
[
sigma(i,j)=(j-i)^3.
]
Root balance makes the antisymmetric edge weights a circulation. The bridge (03) carries no circulation; the remaining triangle has one-dimensional cycle space. Cubic balance evaluates that triangle as
[
1^3+1^3-2^3=-6,
]
forcing its circulation coefficient to vanish. Hence
[
w_{ij}=w_{ji}
]
for every occurring root pair. No further odd scalar depending only on the ordered root can distinguish the carrier: root-only topology is exhausted at pairwise opposite-root balance.

### Deletion distance and the zero-root branch

The deletion-distance identity gives
[
kappa_2(H)=min_pimax(0,delta(pi)).
]
For
[
k=kappa_2(H)ge2,
]
the bounded-central-block analysis forces every positive exact-root carrier to contain a chamber with
[
p=c.
]
This is a genuinely balanced canonical partial two-cover:
[
P_pimid X_pimid Q_pi,qquad |P_pi|=|Q_pi|,
]
but (X_pi) may still be nonempty. A zero root is therefore not itself the grand-theorem conclusion.

For (k=1), the nonzero branch is already confined to the same bounded four-coordinate/four-vertex central geometry. Thus the exact-root theory separates the problem cleanly:

- nonzero recurrence is finite and bounded;
- for (kge2), topology forces the diagonal (p=c);
- further progress must use actual vertices, hole supports, or local status data rather than more root moments.

### Relation to the local-witness route

The local-witness compression developed next reaches the same numerical scale from a different invariant. This agreement is structural: root recurrence compresses the *extreme inversion coordinates*, whereas local witnesses compress the *nearest actual forbidden pattern*. The two routes should be regarded as complementary descriptions of the same finite central geometry, not independent grand-theorem obligations.

## Metadata

- ID: exact_root_compression_and_bounded_central_structure
- Kind: section
- Version: 1
- Math version: 1
- Audit: unaudited
- Refutation: unrefuted
- Composition version: 1
- Composition stale: False

## Development tree

- [Subsection 1 — (untitled)](../SUBSECTIONS/exact_root_compression_and_bounded_central_structure_subsection_a.md) (`exact_root_compression_and_bounded_central_structure_subsection_a`; development v1; composition vNone; stale=True)
