# A portal-only pair-core quadrilateral is high-transition or collapses to a trimer deletion rail

**Workspace:** D17
**State:** established
**Key:** `universal-one-extension-portal-c4-octahedral-skeleton`

**Summary:** Let T=S-s and let a,b,c,d be a shortest pair-core C4, so the perimeter five-supports T+ab,T+bc,T+cd,T+da are Hamiltonian and the diagonals T+ac,T+bd are non-Hamiltonian. Assume the four perimeter edges are PORTAL. Fix any exact two-cover F of H-s and let tau_ab,tau_bc,tau_cd,tau_da count selected crossings of the four perimeter cuts. With W=Y-{a,b,c,d}, the six nonempty membership types T,W,a,b,c,d have four-cut incidence vectors forming K6 minus the perfect matching TW,ac,bd. Every inter-type selected edge crosses at least two perimeter cuts, while a two-path forest spanning six types needs at least four inter-type edges; hence sum tau>=8. If some tau>=3, this is the HIGH-TRANSITION output. Otherwise portal universality gives tau=2 on every cut, equality forces exactly four weight-two inter-type edges and one contiguous F-block of each type, and cut parity reduces the quotient to two three-vertex paths. Up to dihedral symmetry there are only two skeletons. The first has a-T-c and b-W-d (or the opposite pairing), making the forbidden diagonal T+ac Hamiltonian. The second has T-a-W and b-c-d, giving a literal exact H-s cover with a trimer rail. Therefore every portal-only C4 yields either a 3+-transition portal cut or an exact singleton-deletion trimer rail. In accepted R927 Arm M the trimer alternative is impossible at the present order, so every exact H-s cover has some perimeter portal cut with at least three selected crossings.

### 1. Portal-only quadrilateral setup
Retain a shortest pair-core quadrilateral from SV29868. Write the fixed trimer core as

  T=S-{s}

and label the exterior rim cyclically a,b,c,d. Thus

  K_ab=T+{a,b},  K_bc=T+{b,c},
  K_cd=T+{c,d},  K_da=T+{d,a}                         (CQ.1)

are Hamiltonian five-supports, while shortestness gives

  T+{a,c} non-Hamiltonian,
  T+{b,d} non-Hamiltonian.                               (CQ.2)

Assume all four perimeter edges are PORTAL, so their complementary supports in Y are non-Hamiltonian. By SV31303, one fixed arbitrary exact two-cover F of H-s crosses every one of the four cuts K_ab|Z_ab, K_bc|Z_bc, K_cd|Z_cd, K_da|Z_da simultaneously.

Let

  tau_ab, tau_bc, tau_cd, tau_da                         (CQ.3)

be the numbers of selected F-edges crossing these four cuts. Put

  W=Y-{a,b,c,d}.                                         (CQ.4)

SV26947 gives |Y|>=7, hence W is nonempty.

### 2. The six membership types form an octahedron
Record for each of the six nonempty vertex types T,W,a,b,c,d its membership vector in the ordered cuts (ab,bc,cd,da):

  T =1111,   W =0000,
  a =1001,   b =1100,   c =0110,   d =0011.              (CQ.5)

For any selected edge uv of F, its contribution to

  Sigma=tau_ab+tau_bc+tau_cd+tau_da                     (CQ.6)

is the Hamming distance between the two membership vectors. Edges within one type contribute 0. Edges between different types contribute 2 or 4. The distance-four pairs are exactly

  T-W,   a-c,   b-d.                                     (CQ.7)

Thus the distance-two adjacency graph on the six types is K6 minus one perfect matching, equivalently the octahedral graph K_{2,2,2}.

Contracting all vertices of one type can only decrease the number of connected components. Since F has two path components and all six types are nonempty, its type quotient has at most two components and therefore uses at least four inter-type selected edges. Every such edge contributes at least two to Sigma. Hence

  tau_ab+tau_bc+tau_cd+tau_da >= 8.                      (CQ.8)

This bound is purely the six-type path-forest geometry.

### 3. Equality has one block of each type and no distance-four edge
Portal universality gives tau_e>=1 for every perimeter cut e. If some tau_e>=3, retain that physical cut and its three-or-more selected crossings; this is the HIGH-TRANSITION output.

Assume no such output. Then tau_e<=2 for all four e. Together with (CQ.8),

  tau_ab=tau_bc=tau_cd=tau_da=2,
  Sigma=8.                                                (CQ.9)

Equality in the proof of (CQ.8) has two consequences. First F has exactly four inter-type selected edges, all of Hamming weight two, so none of the pairs in (CQ.7) is selected. Second each type occurs as one connected contiguous F-block. Indeed, if some type had two same-type connected blocks, the block quotient would have at least seven vertices but still only two components, requiring at least five inter-block edges, contradicting the exact total four.

Hence contracting each of the six literal blocks gives a spanning two-component path forest J on the six type vertices, with four edges, contained in K_{2,2,2}.

### 4. Cut parity leaves only two quotient skeletons
Because every perimeter cut has exactly two selected crossing edges, every cut has even boundary in J. In any forest, cut-boundary parity equals the parity of the number of odd-degree vertices lying on that side. The four cut equations from (CQ.5) therefore constrain the endpoint set E(J).

A singleton component would leave only two odd-degree vertices, but the four parity equations have no two-element solution. Thus both J-components are nontrivial and |E(J)|=4. Solving the four elementary parity equations gives exactly

  E(J)={a,b,c,d},
  or E(J)={T,W,a,c},
  or E(J)={T,W,b,d}.                                     (CQ.10)

In each case the two non-endpoints form one of the forbidden distance-four pairs in (CQ.7), so they cannot be adjacent. Since J has two path components and exactly two degree-two vertices, the components must therefore both have order three, one degree-two vertex in each.

For E={a,b,c,d}, the centers are T,W. The four cut equations force, up to cyclic relabelling,

  a - T - c,
  b - W - d,                                             (CQ.11)

or the same skeleton with the two opposite exterior pairs exchanged.

For E={T,W,b,d}, the centers are a,c, and the equations force, up to reflection,

  T - a - W,
  b - c - d.                                             (CQ.12)

The case E={T,W,a,c} is the quarter-turn of (CQ.12). Thus (CQ.11) and (CQ.12) are the only two dihedral skeleton types.

### 5. One skeleton contradicts the diagonal; the other is a trimer rail
In skeleton (CQ.11), every type is one literal contiguous F-block and one F-component has support exactly

  {a} union T union {c}.

That component is a Hamilton tight path on T+{a,c}, contradicting the diagonal non-Hamiltonicity in (CQ.2). Hence (CQ.11) is impossible.

In skeleton (CQ.12), the second F-component is literally

  b - c - d                                               (CQ.13)

up to reversal, hence is a tight trimer rail. The other component spans T+{a}+W. Therefore F itself is an exact singleton-deletion cover

  H-s = (T+{a}+W) | (b,c,d)                              (CQ.14)

with one rail of order three. Cyclic rotations give the equivalent four labelled forms.

Consequently every portal-only pair-core quadrilateral has the dichotomy

  some perimeter cut has at least three selected F-crossings,
  or F has a literal trimer rail.                         (CQ.15)

The statement holds for every exact H-s cover F, with the selected perimeter cut allowed to depend on F.

### 6. R927 Arm-M corollary
Now assume accepted R927 alternative (M). Then |V(H)|=2k+1 and every exact singleton-deletion support partition is k|k. Since |Y|>=7 and |S|=4, |V(H)|>=11, so k>=5. The trimer exact cover (CQ.14) is impossible. Therefore in Arm M:

  for every exact two-cover F of H-s,
  at least one of the four perimeter portal cuts has tau_e(F)>=3.   (CQ.16)

Thus the portal-only C4 cannot survive in the uniform arm as a low-transition holonomy. Its only possible form is a universally high-transition four-cut system. Outside Arm M, R927 already places H in the universal-source-crossing arm.

No claim is made here that a three-transition portal cut is already absorbable. The gain is a finite parent compression: the only large-order uniform C4 residue is transition multiplicity at least three in every exact representative.

## References

```json
[
    {
        "relation": "dependency",
        "revision_id": "R927"
    }
]
```
