# The short-cell common complement has order at least four

**Workspace:** D17
**State:** established
**Key:** `singleton-deep-p5-short-donor-order-floor`

**Summary:** In the short G1 common-complement cell, the donor Hamilton rail B cannot have order at most three. Order one is already excluded by the endpoint-transfer section. If |B|=2, after borrowing either endpoint the donor residue plus any deleted pair is a three-set and hence has a tight Hamilton trimer by R3, closing H with the Hamilton five-core X+b. If |B|=3, B itself is a tight trimer and accepted SV16094 says B+z is non-Hamiltonian for every z in U. Accepted R522 applied to the same tight trimer B and any two distinct z,w in U therefore Hamiltonizes B+{z,w}. Choosing {z,w} to be any of the four deleted pairs D of SV16347 and pairing this Hamilton P5 with the explicit Hamilton P4 on X=U-D gives a spanning two-cover of H. Hence every surviving short-cell branch has |B|>=4.


### 1. Setup
Retain the accepted exact short-cell unit `singleton-deep-p5-short-r961-currentization` SV16094 and the current transfer unit `singleton-deep-p5-short-pair-support-transfer` SV16347. Thus

  H = U disjoint-union B,
  U={s,q,t,p,u,v},

B is a literal Hamilton path, B+z is non-Hamiltonian for every z in U, and for each

  D in {{s,q},{s,u},{q,t},{t,p}}

the complementary four-set

  X=U-D

has an explicit tight Hamilton P4 A_X.

The working transfer unit already notes that |B|=1 closes: for the unique b in B, the Hamilton five-set X+b is all of H-D, and the deleted physical dimer D is a second path.

### 2. Order two closes by direct donor restoration
Suppose |B|=2 and write B=(b_0,b_1). Choose any one of the four deleted pairs D={x,y} and borrow either endpoint b into the Hamilton five-core X+b, as in SV16347. The donor support is

  (B-{b}) union D,

a three-vertex set. By R3, for every three distinct vertices exactly one order in each complete-reversal pair is tight; in particular the three-set has a tight Hamilton trimer. Therefore the Hamilton five-core X+b and this Hamilton donor trimer are disjoint and span H, contradiction.

Hence |B| is not two.

### 3. Order three closes by the accepted shared-trimer amplifier
Suppose |B|=3 and retain its literal Hamilton order

  B=(b_0,b_1,b_2).

Then B itself is a graph-intrinsic tight trimer. Accepted SV16094 gives

  B+z is non-Hamiltonian for every z in U.                 (DF.1)

Fix any two distinct z,w in U. Both four-sets B+z and B+w are therefore no-P4 extensions of the same tight trimer B. Accepted R522 applies exactly: two no-P4 extensions of one tight trimer force a Hamilton P5. Consequently

  B union {z,w} is Hamiltonian for every distinct z,w in U. (DF.2)

Now choose any of the four retained deleted pairs D={z,w}. By SV16347 its complement X=U-D has an explicit Hamilton P4 A_X. Equation (DF.2) supplies a Hamilton P5 on B union D. These two paths are vertex-disjoint and

  X disjoint-union (B union D) = U disjoint-union B = H.

Thus they form a spanning two-cover of H, contradiction.

### 4. Consequence
Every surviving short-cell branch satisfies

  |B| >= 4.                                                (DF.3)

This is a genuine donor-rail floor, not a size heuristic. In particular after borrowing b_0 the residual literal donor B-b_0 has at least three vertices and exposes the actual source seam window b_1,b_2; dually after borrowing b_k the residual donor B-b_k exposes b_{k-2},b_{k-1}. These are the first nontrivial seam windows for the Director-v45 donor-repair problem.


## References

```json
[
    {
        "relation": "dependency",
        "revision_id": "R3"
    },
    {
        "relation": "dependency",
        "revision_id": "R522"
    }
]
```
