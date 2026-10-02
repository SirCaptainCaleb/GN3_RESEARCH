# The six-set matching exception has a canonical orientation split and complete hook rectangle

**Summary:** The six-set matching exception has a canonical orientation split and complete hook rectangle.

## Statement

Let H be any boundary tournament and U any six-vertex set. Let D={d in U:H[U-{d}] is Hamiltonian}, and join d,e in D when H[U-{d,e}] is Hamiltonian. If this good two-deletion graph has no adjacent edges, then |D|=4 and it is a perfect matching; H[D] is a non-Hamiltonian matching-block K4. Writing U-D={a,b}, define the fixed-pair extension graph K on D by yz in E(K) iff H[{a,b,y,z}] is Hamiltonian. Then K is the same perfect matching as the good two-deletion graph. Consequently D=C_+ disjoint-union C_- with |C_+|=|C_-|=2, where C_+={y:(a,y,b) is tight} and C_-={z:(b,z,a) is tight}; the two matching edges are exactly C_+ and C_-. For every cross pair y in C_+, z in C_-, the four-set {a,b,y,z} is non-Hamiltonian and the four triples (a,y,b), (b,z,a), (y,a,z), (z,b,y) are tight. Thus the sole no-overlap six-set residue is not merely a matching-block four-core but a canonical 2-by-2 opposite-orientation hook rectangle around the complementary pair.

## Body

By sixset_deletion_graph_strengthened01, absence of adjacent edges forces |D|=4, the good two-deletion graph J to be a perfect matching, and H[D] to be a non-Hamiltonian matching-block K4. Write U-D={a,b}. For y,z in D, the fixed-pair four-set {a,b,y,z} equals U-(D-{y,z}). Hence yz is an edge of its fixed-pair Hamiltonian extension graph K exactly when the complementary pair D-{y,z} is an edge of J. On a four-element vertex set, complementation interchanges the two edges of a perfect matching, so K has exactly the same perfect-matching edge set as J. Apply fixedpair_perfect_matching_orientation01 to a,b,D. It partitions D into two orientation classes C_+,C_- of size two and identifies those classes with the matching edges. Apply fixedpair_perfect_matching_hooks01 to obtain, for every cross pair y,z, non-Hamiltonicity of {a,b,y,z} and the four displayed tight triples. No ambient minimality is used.

## Metadata

- ID: sixset_deletion_matching_oriented01
- Kind: toolkit
- Math version: 1
- Audit: unaudited
- Refutation: unrefuted
