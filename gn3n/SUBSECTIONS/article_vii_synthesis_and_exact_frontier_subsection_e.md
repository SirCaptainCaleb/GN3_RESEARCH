# Root-only exhaustion and the k=1 anchored residue

## Metadata

- ID: article_vii_synthesis_and_exact_frontier_subsection_e
- Parent Section: article_vii_synthesis_and_exact_frontier
- Position: 5
- Row version: 2
- Development version: 2
- Composition version: None
- Composition stale: False

## Cold composition

(none yet)

## Development

### A cubic root moment kills the last asymmetric circulation

Assume a positively balanced exact-root carrier has already been reduced by [[topological_recurrence_to_local_gn3_structure]] to the four-coordinate nonzero branch. Translate the occurring exact-root coordinates so that they lie in
[
{0,1,2,3},
]
with every occurring nonzero arc satisfying
[
i+jle3.
]
The underlying undirected root graph is therefore
[
01,quad02,quad03,quad12.
]
It is a triangle on (0,1,2) with the bridge (03).

For an exact root (i	o j), define the odd scalar
[
sigma(i,j)=(j-i)^3.
]
Reversal sends (i	o j) to (j	o i), hence negates (sigma).

Augment the exact-root odd map by this scalar. On a carrier of a zero of the augmented map, let (w_{ij}) be the total positive chamber weight carrying root (i	o j). Root balance says that the antisymmetric edge weights
[
a_{ij}=w_{ij}-w_{ji}
]
form a circulation on the underlying graph.

Because (03) is a bridge, every circulation has
[
a_{03}=0.
]
The cycle space of the remaining triangle is one-dimensional, so for some scalar (t),
[
a_{01}=a_{12}=t,qquad a_{02}=-t
]
with the orientation convention (0	o1	o2	o0).

The cubic-coordinate balance is
[
0=sum_{i<j}a_{ij}(j-i)^3.
]
Substituting the triangle circulation gives
[
0=t(1^3+1^3-2^3)=-6t.
]
Hence (t=0). Therefore every antisymmetric edge weight vanishes:
[
oxed{w_{ij}=w_{ji}quad	ext{for every occurring root pair }{i,j}.}
]

Thus, after the four-coordinate reduction, one extra odd scalar eliminates all directed three-cycle imbalance and upgrades positive root circulation to pairwise opposite-root balance.

### Root-only odd information is exhausted after pairwise symmetry

Once
[
w_{ij}=w_{ji}
]
holds for every root pair, every further odd scalar depending only on the ordered root ((i,j)) cancels automatically between opposite roots. Consequently no additional one-dimensional odd moment of the exact-root coordinates can distinguish the remaining carrier.

This is a useful guardrail: further topological compression must introduce information about actual vertices, hole supports, roles, or local violation data rather than another function of (p,c) alone.

The anchored role maps, rooted omission vectors, and coordinatewise local violation gauges developed elsewhere in Article VII are therefore the natural continuation.

### The deletion-distance split

The current exact-root structure gives a clean global split by
[
k=kappa_2(H).
]

If (kge2), [[topological_recurrence_to_local_gn3_structure]] proves that every positive exact-root carrier contains a zero root (p=c). The unresolved object is then an equal-side canonical partial two-cover with a nonempty hole.

If (k=1), the nonzero exact-root branch may survive. The four-coordinate theorem reduces it to the bounded two-, three-, or four-vertex central configurations. In this branch the no-direct-side-flip lemma for canonical roles is unavailable: a vertex can in principle move directly from the left canonical path to the right canonical path across one adjacent swap. This is precisely why the (k+2)-anchor argument valid for (kge2) does not automatically close (k=1).

A useful next lemma would classify such a direct side flip at (k=1) as an endpoint transfer between two deficiency-one deletion covers. This classification has not yet been completed here and should not be treated as proved.

Accordingly the structural frontier after the cubic reduction is:

- (kge2): exploit equal-side holes and the universal-hole / anchored-role topology;
- (k=1): analyze the bounded four-coordinate carrier together with direct side-transfer edges;
- root-only odd moments need not be pursued further.
