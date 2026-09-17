# The final-gap puncture kills the p-source half and reduces outgoing p-terminal seams to R542

**Workspace:** D17
**State:** working
**Key:** `stationary-one-p-finalgap-consumer`

**Summary:** In the quiet c=2,d=1,tau_Z=1 stationary cell, compare the p-containing A block with the exact final-gap Hamilton puncture K_A. Outside explicit R435 geometry, if p is the source of its current A block then that block is exactly (p,a_{k-1}); all possible A-B seam placements then give the forbidden subthreshold singleton cover. If p is terminal and the unique A-B seam leaves A, its A endpoint is a_{k-1}; K_A followed by B is Hamilton unless the one remaining turn (p,a_{k-1},b_1) is bad. In the bad case its reverse and the terminal-puncture reverse turn give two head witnesses on reverse boundary dimer (a_{k-1},p), so accepted R542 applies. Thus the only direct-repair survivor is p terminal with an incoming B-to-A seam (plus explicit R435/R542 outputs).


### Setup
Retain the quiet stationary `c=2,d=1,tau_Z=1` cell of `stationary-one-p-cut-or-cross`, up to A/B duality. Thus p has exactly one selected incidence with A and none with B; A has exactly two current blocks, B and Z are full current blocks, and the two common crosses consist of one Z-incidence and one unique A-B seam. Write

  A=(a_1,...,a_{k-1}),   B=(b_1,...,b_{k-1}),

and retain the exact quiet final-gap puncture

  K_A=(a_1,...,a_{k-2},p,a_{k-1}).

Let U be the current A-block containing p and V the other current A-block. Branch explicitly if U or V has R435 reversal/reverse-trimer/cycle geometry relative to K_A (equivalently to the retained A contact order). Outside that branch, the K_A-contacts encountered along each current block occur in K_A-order.

The final-gap theorem also gives the exact tight turn

  (u_X,a_{k-1},p).

Every closure below pairs a Hamilton path on M=A union B union {p}, of order 2k-1, with the literal stationary path u_X+Z, of order k+1, inside H-u_Y. Both orders are strictly below a=2k, so `subminimum-source-saturation` forbids such a singleton cover.

### 1. If p is the source of U, then U is exactly (p,a_{k-1})
Suppose p is the source of its current block U. Since p is the penultimate vertex of K_A, K_A-order monotonicity says that every later U-contact must lie after p in K_A. The only such vertex is a_{k-1}. The selected p-A incidence makes U nontrivial, hence

  U=(p,a_{k-1}).

Consequently V contains all a_1,...,a_{k-2}, in that retained order.

If the unique A-B seam touches V, the balancing constructions already present in `stationary-one-p-cut-or-cross` close immediately: an outgoing V-to-B seam has its retained predecessor in V (or starts at a_1), while an incoming B-to-V seam enters at a_1 and continues to a_2 in V. Thus no survivor has its A-B seam on V.

Hence a surviving seam would have to touch U. Because the selected U-edge is p followed by a_{k-1}, p is the source and a_{k-1} the only available external endpoint. The A-B seam is therefore U-to-B, and the current rail contains

  p, a_{k-1}, b_1, b_2, ... .

So it certifies both complete junction turns

  (p,a_{k-1},b_1),
  (a_{k-1},b_1,b_2).

These are exactly the two new turns needed to concatenate K_A with the retained B order. Therefore

  K_A - B

is Hamiltonian on M, producing the forbidden singleton cover

  H-u_Y : (K_A-B) | (u_X+Z).

Thus the entire p-source branch is impossible outside explicit R435 geometry.

### 2. If p is terminal and the A-B seam leaves A, the only obstruction is one R542-ready turn
Now suppose p is terminal in U and the unique A-B seam is directed from an A block into the full B block. Since U ends at p it cannot supply an outgoing A-B seam. Thus the seam leaves V.

Outside R435 geometry, every V-contact is K_A-monotone. The vertex a_{k-1}, which is the final K_A vertex, cannot lie in U because U terminates at p, which precedes a_{k-1} in K_A. Hence a_{k-1} lies in V and is necessarily the terminal vertex of V. Therefore the current A-B seam is

  a_{k-1} -> b_1,

and certifies

  (a_{k-1},b_1,b_2).

To concatenate K_A with B, every turn is inherited except possibly

  h=(p,a_{k-1},b_1).

If h is tight, K_A-B is Hamiltonian on M and the preceding subthreshold singleton cover closes the branch.

If h is bad, boundary antisymmetry gives the exact reverse

  (b_1,a_{k-1},p)

tight. Together with the already retained terminal-puncture turn

  (u_X,a_{k-1},p)

this gives two distinct head witnesses b_1 and u_X on the same tested oriented dimer

  D=(a_{k-1},p).

The tight final-gap trimer

  (a_{k-2},p,a_{k-1})

has D as its reverse terminal boundary dimer. Both witnesses lie outside that trimer. Therefore accepted R542 applies with the source identities and tested order retained. This is a genuine source-anchored short-carrier packet, not anonymous payment.

Hence the p-terminal / outgoing-A-to-B branch yields either the forbidden subthreshold singleton cover or an R542 packet.

### 3. Exact direct-repair survivor
After the two preceding eliminations, a quiet `c=2,d=1,tau_Z=1` cell that remains for direct reconstruction has, up to A/B duality:

- p terminal in its current A block U;
- the unique A-B seam directed from full B into an A block;
- a pinned consecutive retained A edge crossing U and V at that interface, as in `stationary-one-p-cut-or-cross`;
- the exact final-gap puncture K_A;
- one remaining selected Z-incidence.

In this incoming B-to-A cell the historical A-u_X-Z source can only be split using an A-suffix, so the tempting prefix-to-u_X splice is invalid. The next repair must use the pinned cross-edge, the p-incidence, and the final-gap order to rotate/recombine the two A-blocks while preserving the complete incoming B seam window.

Status: complete working reduction. It does not claim that the surviving incoming seam is closed, and it does not treat the R542 output as a spanning cover.


## References

```json
[
    {
        "relation": "dependency",
        "revision_id": "R435"
    },
    {
        "relation": "dependency",
        "revision_id": "R3"
    },
    {
        "relation": "dependency",
        "revision_id": "R542"
    }
]
```
