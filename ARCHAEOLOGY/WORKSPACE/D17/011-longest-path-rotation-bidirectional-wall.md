# A longest tight cycle carries universal reversed-edge walls against its whole two-covered complement

**Workspace:** D17
**State:** established
**Key:** `longest-path-rotation-bidirectional-wall`

**Summary:** Let Q be a globally longest tight path in a smallest counterexample and W its complement. R4 makes W exactly two-covered and |W|>=4. Every exterior x already reverse-signs the two boundary dimers of Q. If Q is in the R579 double-wrap branch, every cyclic rotation is again globally longest, so for every cycle edge q_i q_{i+1} its reverse D_i=(q_{i+1},q_i) is simultaneously head- and tail-signed by every x in W. Thus any ordered distinct x,y in W gives the tight P4 x-D_i-y. For every exact two-cover T of H-D_i, both rails are nontrivial. Any W-vertex occurring as a T endpoint forces a named reverse outer seam by the direct R834 splice mechanism. If no such endpoint exists, all W vertices are internal, all four T endpoints lie in Q-D_i (so |Q|>=6), and deleting any two exterior vertices from T creates at least three complementary blocks: b_T(x,y)=4-1_{xy selected}>=3. Hence the double-wrap longest-path residue is a universal bidirectional wall with either current reverse seams or pairwise maximal fragmentation, not an anonymous balanced-pair packet.

### 1. Longest-path complement and universal outer reverse stars
Let H be a hypothetical smallest Strong Level-(1) counterexample and let

  Q=(q_0,q_1,...,q_m)

be a globally longest tight path. Since H is not Hamiltonian, Q is proper. Put

  W=V(H)-V(Q).

Apply accepted R4 through its minimum-order proof mechanism. The proper path Q has an exact two-covered complement W; in particular pc(H[W])=2. Hence |W|>=4: a set of order one or two is Hamiltonian vacuously, and every three-set has a tight Hamilton order by R3, while a Hamilton W together with Q would two-cover H.

For every x in W, the literal prepend and append proposals

  (x,q_0,q_1,...,q_m),
  (q_0,...,q_m,x)

are longer than Q and therefore cannot be tight. Their only new turns are respectively (x,q_0,q_1) and (q_{m-1},q_m,x), so both are bad. R3 gives the exact reversals

  (q_1,q_0,x),
  (x,q_m,q_{m-1})                                    (LW.1)

for every x in W. Thus the two reversed boundary dimers of any globally longest order are signed by the entire complement, not merely by a chosen four-witness subset.

### 2. Double wrap makes every reversed cycle edge bidirectionally universal
Apply accepted R579 proof-aware to Q. In its DOUBLE-WRAP branch the two wrap seams are tight, so

  q_0,q_1,...,q_m,q_0

is a tight Hamilton cycle on V(Q). Every cyclic rotation of Q is therefore a tight path on the same support and has the same globally maximum order.

Index the cycle modulo r=|V(Q)| and fix one forward cycle edge q_i q_{i+1}. Put the tested reverse dimer

  D_i=(q_{i+1},q_i).

Use the cyclic rotation beginning q_i,q_{i+1},... . Longestness forbids prepending any x in W, so (x,q_i,q_{i+1}) is bad and R3 gives

  (q_{i+1},q_i,x) tight.                               (LW.2)

Use the rotation ending ...,q_i,q_{i+1}. Longestness forbids appending x, so (q_i,q_{i+1},x) is bad and R3 gives

  (x,q_{i+1},q_i) tight.                               (LW.3)

Hence for every cycle edge and every exterior vertex x, D_i is simultaneously tail-signed and head-signed by x. For distinct x,y in W, (LW.3) with x and (LW.2) with y concatenate directly to

  (x,q_{i+1},q_i,y),                                  (LW.4)

a tight P4. This is the R523 opposite-polarity mechanism specialized to a whole exterior witness set.

### 3. Every pair-deletion cover has nontrivial rails
Fix D=D_i. Since D is a proper tight dimer, R4 gives an exact two-cover

  T=T_1 | T_2

of H-D. Neither rail can be a singleton. If, say, T_1={z}, then the three-set V(D)+{z} has a tight Hamilton trimer by R3, and that trimer together with T_2 would two-cover H. Thus both T rails have order at least two and four distinct physical endpoints.

### 4. Any exterior endpoint forces a current reverse seam
Let x in W be a T endpoint. If x is the source of a rail U=(x,u_1,...), use the universal tail sign (D,x), namely

  (q_{i+1},q_i,x) tight.

If the outer seam (q_i,x,u_1) were tight, then

  (q_{i+1},q_i,x,u_1,...)

together with the other T rail would be a spanning two-cover of H. Therefore that seam is bad and R3 gives the named reverse seam

  (u_1,x,q_i) tight.                                   (LW.5)

If x is instead the terminal of U=(...,u_{s-1},x), use the universal head sign

  (x,q_{i+1},q_i) tight.

A tight seam (u_{s-1},x,q_{i+1}) would let U absorb D at its end and close H with the other rail. Hence it is bad and R3 gives

  (q_{i+1},x,u_{s-1}) tight.                           (LW.6)

These are exactly the direct splice mechanisms underlying accepted R834. Thus every occurrence of a W-label as an endpoint of an exact H-D two-cover emits a physical reverse seam in that same cover.

### 5. Seam-quietness forces pairwise maximal exterior fragmentation
Suppose one wishes to remain outside all outputs (LW.5)-(LW.6). Then no W vertex is a T endpoint. Consequently every x in W is internal in its T rail and has selected degree two. All four T endpoints lie in V(Q)-V(D), so necessarily

  |V(Q)|-2 >= 4,

i.e. |V(Q)|>=6.

Now fix distinct x,y in W and delete them from the two path rails of T. The number b_T(x,y) of maximal nonempty blocks on the remaining complement of {x,y} is the elementary path-forest deletion count

  b_T(x,y)=deg_T(x)+deg_T(y)-1_{xy in E(T)}
            =4-1_{xy in E(T)} >=3.                    (LW.7)

Equivalently every exterior pair is in the HIGH block-count regime of the R833/R846 middle-dimer analysis. Thus a seam-quiet double-wrap state is not locally quiet at all: the entire exterior set is forced internal and every two exterior deletions fragment the current exact cover into at least three complementary blocks.

### 6. Output and fence
For a globally longest Q, the R579 double-wrap branch therefore produces one universal geometric object. Every reversed cycle edge D has the whole exact two-covered complement W as simultaneous head and tail witnesses. For any exact H-D two-cover, either some exterior endpoint gives an explicit same-frame reverse seam, or all exterior vertices are internal and every exterior pair has deletion block count at least three.

This does not yet close the double-wrap branch and does not turn the resulting reverse seams into anonymous R159/R514 currency. The intended next consumer is linear-forest augmentation: use the full family of wall dimers D_i and the same complement W to show that reverse seams cannot be routed consistently around the entire cycle, or that the pairwise HIGH fragmentation forces a component-reducing reroute.

## References

```json
[
    {"relation":"dependency","revision_id":"R3"},
    {"relation":"dependency","revision_id":"R4"},
    {"relation":"dependency","revision_id":"R579"},
    {"relation":"dependency","revision_id":"R834"}
]
```
