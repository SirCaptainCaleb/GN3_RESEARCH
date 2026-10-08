# Audit: universal support-pair Smith lifting is refuted by an explicit cochain — preserved pre-item development

## Development

## Audit: universal Smith lifting fails even when a two-cover exists

This audits the proposed universal transport in [[hamiltonian_support_pairs_and_smith_chains_give_a_direct_closure_target]]. Its conditional closure theorem remains correct. The stronger assertion that every boundary tournament admits the required Smith chains in the support-pair order complex is false.

### An explicit edge-ordered boundary tournament

On vertices 1,...,6, order the edges as follows:
12 < 13 < 23 < 45 < 16 < 26 < 36 < 46 < 15 < 25 < 35 < 56 < 14 < 24 < 34.
Declare (u,v,w) tight exactly when uv precedes vw. This satisfies boundary antisymmetry.

Write X={1,2,3} and S={4,5,6}. The only non-Hamiltonian four-sets are S union {x}, x in X.

Proof. Assign the equivalent ranks
r12=1, r13=2, r23=3;
r45=10, r46=20, r56=30;
r6x=10+x, r5x=20+x, r4x=30+x.
On S union {x}, the three opposite-edge matching blocks are {45,6x}, {46,5x}, {56,4x}. Thus the matching-block argument excludes a Hamilton path.

Every other four-set has either one S vertex or two S vertices. With one S vertex s, the path (1,2,3,s) is increasing. With two S vertices and two X vertices x<y, use (x,5,y,4) for S-pair {4,5}, (x,6,y,4) for {4,6}, or (x,6,y,5) for {5,6}. The ranks strictly increase. This proves the classification without an orientation search.

The actual spanning two-cover is (1,2,3)|(5,4,6).

### An elementary cochain obstruction to Smith chains

Let K be the support-pair order complex with both supports of order at least two, and let T swap them. There are a zero-cochain g and a one-cochain lambda over F_2 such that
g+Tg=1,
delta(lambda)=0,
lambda+Tlambda=delta(g).

These identities rule out Smith chains c0,c1,c2 with odd augmentation and boundary(c1)=(1+T)c0, boundary(c2)=(1+T)c1. Indeed:
0 = lambda(boundary c2)
  = (lambda+Tlambda)(c1)
  = delta(g)(c1)
  = g((1+T)c0)
  = (g+Tg)(c0)
  = aug(c0)
  = 1.
This contradiction applies to any choice of the chains, not just a particular source-cell boundary.

### Reproducible finite cochain certificate

Encode a vertex subset by its six-bit mask, with label i contributing 2^(i-1). Enumerate allowed masks in increasing numerical order: sizes two, three or four, except masks 57,58,60. These are precisely the possible component supports of K, since a disjoint second support must have at least two vertices.

Enumerate ordered disjoint pairs (a,b) lexicographically. Let g(a,b)=1 when a>b and 0 otherwise. Enumerate comparable ordered vertex-index pairs (i,j) lexicographically. For edge number z, lambda is bit z of the following hexadecimal integer, the least significant bit being edge zero:

a52815c5757000000000a0822a2c0a0b800504115160505c0a0822a2c0a0b82b5a84010100962c58002be0989841818b015f04c4c20c0c5abe0989841818b0820001111120201710000888890100b80011111202017000000280000000000a00000000002800000

The following verifier checks every cochain equation using only exact integer and mod-two arithmetic:

```python
bad = {57, 58, 60}
subsets = [
    a for a in range(1, 64)
    if a.bit_count() in (2, 3, 4) and a not in bad
]
states = [(a, b) for a in subsets for b in subsets if not a & b]
index = {s: i for i, s in enumerate(states)}
swap = {i: index[b, a] for i, (a, b) in enumerate(states)}
g = {i: int(a > b) for i, (a, b) in enumerate(states)}

def less(s, t):
    return (
        s != t
        and not (s[0] & ~t[0])
        and not (s[1] & ~t[1])
    )

edges = [
    (i, j)
    for i, s in enumerate(states)
    for j, t in enumerate(states)
    if less(s, t)
]
edge_index = {e: z for z, e in enumerate(edges)}
triangles = [
    (i, j, k)
    for i, j in edges
    for k, t in enumerate(states)
    if less(states[j], t)
]
certificate = int(
    "a52815c5757000000000a0822a2c0a0b800504115160505c0"
    "a0822a2c0a0b82b5a84010100962c58002be0989841818b0"
    "15f04c4c20c0c5abe0989841818b08200011111202017100"
    "00888890100b80011111202017000000280000000000a00"
    "000000002800000", 16
)
lam = [(certificate >> z) & 1 for z in range(len(edges))]
assert (len(states), len(edges), len(triangles)) == (254, 900, 648)
assert certificate >> len(edges) == 0
assert all(g[i] ^ g[swap[i]] == 1 for i in range(len(states)))
assert all(
    lam[edge_index[i, j]]
    ^ lam[edge_index[i, k]]
    ^ lam[edge_index[j, k]] == 0
    for i, j, k in triangles
)
assert all(
    lam[z] ^ lam[edge_index[swap[i], swap[j]]] == g[i] ^ g[j]
    for z, (i, j) in enumerate(edges)
)
```

The certificate was checked against all 648 triangles and all 900 edges. It is a cochain, not a content hash.

Consequently no equivariant map S^2->K exists: such a map would supply the length-two Smith chains. Since the unrestricted Q_6 has coindex two, there is likewise no equivariant map Delta Q_6->K. Thus the proposed universal transport theorem is refuted.

### Rank is still an exact invariant; index is not

The dimension bound in [[support_pair_rank_is_exactly_two_cover_deletion_distance]] strengthens to equality:
dim K(H)=n-kappa_2(H)-4 for n>=4.

Proof. Maximum total support is n-kappa_2(H). This is at least four, since any four vertices have a two-cover by two pairs. Normalize a maximum pair to have both sides of order at least two. Choose Hamilton orders on its sides, start with two-vertex prefixes, and add one prefix vertex at a time. This gives a chain visiting every total support size from four to n-kappa_2(H), proving the lower dimension bound. The previously proved rank upper bound gives equality.

For the explicit tournament above, kappa_2=0 and dim K=2, but Smith chains of length two do not exist. Therefore full support rank cannot be replaced by maximal equivariant index, even in an edge-ordered tournament.

### Consequence for the proof strategy

A universal topological transport theorem that forgets all blocked-extension data is too strong. Merely enriching path orders while retaining an equivariant forgetful map to this same K cannot restore the refuted universal sphere map.

The conditional Smith-chain closure criterion is not refuted. A proof under the hypothesis of a minimum counterexample could still use endpoint noninsertability, non-Hamiltonian one-vertex extensions, and complementary deletion covers to construct chains that do not exist for arbitrary H. Those hypotheses must do identifiable work in each filling.

In particular, the earlier isolated-loop test asks for too much when it demands that every local loop fill, while the universal Smith route also asks for too much when it demands maximal index in all tournaments. The next admissible target is a relative or counterexample-specific obstruction using the blocked-extension information. No such theorem is asserted here.

This is a fixed intrinsic counterexample to a proposed abstraction, not a small-order verification cutoff and not a counterexample to the grand conjecture.
