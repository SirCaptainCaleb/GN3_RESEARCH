# Incoming one-p seams reduce to two hard Z placements

**Workspace:** D17
**State:** working
**Key:** `stationary-one-p-incoming-partial-consumer`

**Summary:** In the quiet c=2,d=1,tau_Z=1 stationary cell, after the final-gap reduction leaves p terminal and an incoming B-to-A seam, two further configurations are consumed. If B enters the p-containing A block U, either the complementary V-u_X-Z reconstruction gives a forbidden subthreshold singleton cover or the unique failed turn yields an accepted R542 packet on reverse boundary dimer (u_X,a_{k-1}). If B instead enters the other block V and the lone Z-cross is Z-U, then prepending u_X to Z gives a subthreshold singleton cover whenever |V|>=2; when |V|=1 the same H-u_Y fiber contains two exact covers differing by a legal transfer of a_{k-1}, forbidden by the movable-pivot parent. Thus the only direct-repair survivors have B entering V and the Z-cross incident with B or V.

### Setup
Retain the quiet stationary `c=2,d=1,tau_Z=1` cell after `stationary-one-p-finalgap-consumer`, outside explicit R435 block-order geometry. Up to A/B duality, p is terminal in its current A block U, the other A block is V, B and Z are full retained-order blocks, and the unique A-B seam is incoming from B. Write

  A=(a_1,...,a_{k-1}),   K_A=(a_1,...,a_{k-2},p,a_{k-1}).

Because U is K_A-monotone and terminates at p, it cannot contain a_{k-1}; hence a_{k-1} lies in V and is the terminal V-contact. The historical stationary source supplies the literal continuation

  a_{k-1},u_X,z,...

through u_X+Z, while terminal puncture localization supplies

  (u_X,a_{k-1},p)

tight.

### 1. If B enters U, the branch is subthreshold or R542
Suppose the current A-B seam is B -> U. Then the current rail containing B continues through U and ends at p. The other current A block V is disjoint from that rail except possibly for the unique Z-cross topology. Ignore that Z-cross and retain the current path B-U-p.

If V is the singleton {a_{k-1}}, then the literal historical path

  a_{k-1},u_X,Z

paired with B-U-p gives an exact cover of H-u_Y whose two rail orders are both below a=2k. This contradicts `subminimum-source-saturation`.

Assume |V|>=2 and write v for the predecessor of a_{k-1} in the actual V order. Test the one new turn

  h=(v,a_{k-1},u_X).

If h is tight, then V-u_X-Z is a literal tight path: every old V turn is retained, (a_{k-1},u_X,z) is the historical source turn, and all later Z turns are retained. Thus

  H-u_Y : (B-U-p) | (V-u_X-Z)

is an exact singleton cover. Put s=|U| and t=|V|=k-1-s. Its rail orders are

  k+s <= 2k-2,
  k+t+1 <= 2k-1,

so both are strictly below 2k, contradiction.

If h is bad, boundary antisymmetry gives

  (u_X,a_{k-1},v)

tight. Together with (u_X,a_{k-1},p), this gives two distinct tail witnesses v,p on the same tested oriented dimer D=(u_X,a_{k-1}). The historical trimer

  (a_{k-2},a_{k-1},u_X)

is tight and has D as its reverse terminal boundary dimer. Moreover v cannot equal a_{k-2}, since then h itself would be that historical tight turn. Hence accepted R542 applies with the exact tested order and source ancestry retained.

Therefore outside explicit R435/R542 outputs, B cannot enter U.

### 2. If B enters V and Z enters U, the entire topology is impossible
Now suppose B enters V, while the unique Z-incidence is with U. Since p is terminal in U, the quotient rail has orientation

  Z - U - p,

while the other rail is B-V. Prepend u_X to the full retained Z block using the literal historical u_X+Z path. This gives an exact H-u_Y cover

  (B-V) | (u_X-Z-U-p).

Let t=|V| and s=|U|=k-1-t. The rail orders are

  k-1+t,
  2k+1-t.

If t>=2, both are strictly below 2k, contradicting `subminimum-source-saturation`.

It remains t=1. Since a_{k-1} lies in V, necessarily V={a_{k-1}} and U contains all a_1,...,a_{k-2}. K_A-monotonicity then makes the current U-p order exactly

  a_1,...,a_{k-2},p.

Put

  P=(u_X-Z-a_1-...-a_{k-2}-p).

The current cover is

  H-u_Y : P | (B+a_{k-1}).

The final-gap turn (a_{k-2},p,a_{k-1}) is tight, so appending a_{k-1} gives a Hamilton path P+a_{k-1}; B itself is Hamiltonian. Hence the same singleton fiber also has the exact cover

  H-u_Y : (P+a_{k-1}) | B.

These two covers differ by a legal one-vertex transfer of a_{k-1}. The movable-pivot parent in `three-petal-hamilton-deletion-closure` forbids such a transfer in the present high-a regime, because n=3k+1<4k=2a. Contradiction.

Thus the Z-U topology is impossible.

### 3. Remaining direct-repair interface
Outside explicit R435 and the R542 output above, the only surviving quiet `c=2,d=1,tau_Z=1` configurations have

- p terminal in U;
- B entering the non-p block V;
- the pinned consecutive retained A edge from `stationary-one-p-cut-or-cross`; and
- the lone Z-cross incident with B or with V, not U.

Equivalently the quotient rails are of type Z-B-V | U-p or B-V-Z | U-p, with exact orientations inherited from the current cover. These are the two remaining reconstruction targets.

Status: working exposition. The first branch exports a genuine accepted R542 packet rather than closure; the second branch is completely eliminated only using the working movable-pivot parent. No claim is made about the two surviving Z placements.

## References

```json
[
    {
        "relation": "dependency",
        "revision_id": "R3"
    },
    {
        "relation": "dependency",
        "revision_id": "R435"
    },
    {
        "relation": "dependency",
        "revision_id": "R542"
    }
]
```
