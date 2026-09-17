# The first portal-C4 excess layer either descends from Sigma=12 to the current floor or emits current component/reversal geometry

**Workspace:** D17
**State:** established
**Key:** `universal-one-extension-portal-c4-first-excess-extinction`

**Summary:** At Sigma=12 the exact identity from SV34314 gives (B-6)+f=2. Because W is fragmented, either (i) B=7,f=1 with T contiguous; (ii) B=8,f=0 with W in three blocks and T contiguous; or (iii) B=8,f=0 with W in two blocks and T in two blocks. Every T-contiguous case is consumed by the floor mechanisms: deg(T)=1 gives the same current singleton/core switch or non-Hamilton-core fresh forest; deg(T)=2 cannot have opposite rim neighbors, and adjacent-rim or rim-W neighbors give an endpoint-controlled Hamilton P5 to which R966 applies. Hence only the double-fragment cell is new. There T consists of a dimer block and singleton block. If e_F(T,Y)>=3, deleting T leaves at least three Y-components while pc(Y)=2, giving a current component-drop portal in an exact Y-cover, liftable through a Hamilton universal extension S+r. If e_F(T,Y)=2, both T-fragments are endpoint blocks. Orient the dimer locally as (p,q,y,...) and let r be the singleton. If (r,p,q) is tight, delete the singleton's unique rim attachment and add rp; this consolidates T, preserves an exact H-s two-cover, and removes exactly one weight-two transition, so Sigma drops 12->10. If (r,p,q) is bad, R3 gives (q,p,r), a tight trimer selecting the same dimer oppositely; R4 currentizes it in an actual maximum forest. The terminal-end orientation is dual, testing (p,q,r). Thus no static Sigma=12 C4 cell survives.

### 1. Exact Sigma=12 parent split
Retain the surviving portal-only shortest pair-core C4 in accepted R927 Arm M, k>=8, and let F be an exact H-s two-cover with

  Sigma(F)=12.

Use the exact identity of SV34314:

  Sigma = 8 + 2(B-6) + 2f,

where B is the total number of maximal blocks of the six types T,W,a,b,c,d and f counts selected transitions joining the antipodal type pairs

  T-W, a-c, b-d.

Thus

  (B-6)+f=2.                                           (EX.1)

The large type W is fragmented, so B>=7. The four rim types are singletons and cannot fragment. Therefore exactly one of the following holds:

(A) B=7, f=1. Then W has exactly two blocks and T is contiguous.

(B) B=8, f=0, with W in exactly three blocks and T contiguous.

(C) B=8, f=0, with W in exactly two blocks and T in exactly two blocks.   (EX.2)

No forest-shape enumeration is used.

### 2. Every T-contiguous Sigma=12 cell reuses the floor consumers
Assume (A) or (B). The contiguous T-block has positive quotient degree by the universal cut fan and degree at most two.

If deg_F(T)=1, there is exactly one selected T|Y transition. The proof of SV35429 does not use f=0 or the number of W-blocks: deleting T leaves an exact two-cover A|B of Y. If S is Hamiltonian, the singleton-rooted maximum forest and the S-rooted maximum forest are connected by the explicit length-at-most-two insertion walk of SV35429; if S is non-Hamiltonian, SV31933 gives the endpoint-indexed fresh maximum-forest export.

Assume deg_F(T)=2. Two opposite rim neighbors would make the literal quotient segment x-T-y a Hamilton path on the forbidden diagonal T+{x,y}, impossible.

If both neighbors are rim labels, they are adjacent on the C4. The segment x-T-y is therefore a Hamilton P5 with endpoint replacements S+x and S+y, so accepted R966 applies with exterior s exactly as in SV34757.

If one neighbor is a W-block, let w be the physical W-vertex adjacent to T and let x be the other, rim neighbor. The literal five-vertex segment

  x - T - w                                             (EX.3)

is Hamiltonian on T+{x,w}, with endpoints x,w. Its two endpoint-replacement supports are

  S+w,
  S+x,

both Hamiltonian by universal one-extension. Hence accepted R966 again applies with exterior s. Its Hamilton-extension and all three R435 species currentize exactly as in SV34757.

The case of two W-neighbors cannot occur: it would contribute two T-W antipodal transitions, while f<=1 in (A) and f=0 in (B).

Therefore every T-contiguous Sigma=12 cell already exits to current maximum-forest / R435 / high-transition dynamics.

### 3. The only new face is double fragmentation
Retain (C). Then

  T = T_1 disjoint_union T_2,
  W = W_1 disjoint_union W_2,                           (EX.4)

as maximal F-blocks, while a,b,c,d remain singleton blocks. Every inter-type selected transition has octahedral weight two.

Because |T|=3, one T-block is an oriented dimer and the other a singleton. Put

  e=e_F(T,Y).

The coarse T|Y block identity gives

  b_T+b_Y = 2+e.

Here b_T=2, so

  b_Y=e.                                                (EX.5)

Thus deleting T from F leaves exactly e literal path components on Y.

### 4. Three or four T-boundary transitions are current component-drop geometry
Suppose e>=3. The complement Y is non-Hamiltonian in the universal-core setup, and by smallest-counterexample minimality pc(Y)=2. Choose an exact two-cover

  Y=U|V.                                                (EX.6)

The inherited cover F[Y] has e>=3 components. Hence U|V must select at least e-2 physical edges joining distinct components of F[Y]; otherwise it could not reduce those e components to two paths. Retain one such selected crossing state and the two F[Y]-components it joins.

This is a literal current component-drop portal on one fixed residual support Y, not an anonymous component count. Moreover choose an endpoint r of U or V not needed as an endpoint of one retained crossing when possible; the universal-extension path on S+r together with the trimmed residual rail and the untouched opposite rail gives an actual maximum spanning three-forest carrying the residual recompletion. Thus the e>=3 branch already exits to current representative/component-drop dynamics.

### 5. The rigid e=2 cell has two endpoint T-fragments
Assume e=2. Then both T-blocks have quotient degree one. Let the oriented dimer block be (p,q) and let r be the third T-vertex.

Because f=0, neither T-block attaches to W. Each unique attachment therefore meets a rim label.

First suppose the dimer block occurs locally in its F-rail as

  (p,q,y,...)                                           (EX.7)

for a rim label y. Thus p is the free end of the dimer block. The singleton r has its own unique selected attachment to a rim label z on its F-rail.

Test the outward core turn

  (r,p,q).                                              (EX.8)

#### Tight outward turn: strict energy descent
If (r,p,q) is tight, delete the unique selected attachment incident with r and add the edge rp. If the two T-blocks lie on different F-rails, the deletion splits r from one rail and the addition joins it to the dimer rail; if they lie on the same rail, the same deletion first separates the endpoint singleton and the addition reattaches it at the free dimer end. In either case the number of path components remains two.

The new dimer-side rail is locally

  (r,p,q,y,...),                                        (EX.9)

which is tight by (EX.8) and the inherited turn (p,q,y). All other path turns are unchanged. Hence we obtain another exact H-s two-cover F'.

The deleted r-rim attachment is a T|rim transition and therefore contributes exactly two units to Sigma. The added rp edge is internal to T and contributes zero. No other selected edge changes. Consequently

  Sigma(F')=Sigma(F)-2=10.                              (EX.10)

Thus the tight outward branch strictly descends to the already-currentized floor SV35429.

#### Bad outward turn: current reverse-dimer trimer
If (r,p,q) is bad, boundary antisymmetry R3 gives

  (q,p,r) tight.                                        (EX.11)

This is a graph-intrinsic tight trimer on T selecting the same physical dimer {p,q} in the opposite direction q->p. The singleton-rooted maximum forest {s}|F still contains the original selected direction p->q inside its dimer T-block. By accepted R4, the proper trimer (q,p,r) lies literally in another actual maximum spanning three-forest. Hence the failed strict descent produces a CURRENT same-dimer selected reversal in maximum-forest space.

### 6. Terminal-end dimer orientation is dual without path reversal
If the dimer block instead occurs locally as

  (...,y,p,q),                                          (EX.12)

then q is its free end. Test

  (p,q,r).                                              (EX.13)

If tight, delete r's unique rim attachment and add qr, producing the tight local rail (...,y,p,q,r) and again lowering Sigma from 12 to 10. If bad, R3 gives

  (r,q,p) tight,                                        (EX.14)

which currentizes the reverse dimer q->p by R4. This is the exact forward dual of Section 5; no reversal of an inherited tight path is asserted.

### 7. First-excess extinction
Combining Sections 2-6, every exact portal-C4 representative with

  Sigma=12                                              (EX.15)

has one of the following strict destinations:

1. a T-contiguous floor consumer, hence current R435 / maximum-forest / high-transition output;
2. a current residual component-drop portal if e_F(T,Y)>=3;
3. a strict same-fiber energy descent Sigma 12 -> 10;
4. an actual maximum-three-forest representative selecting the fragmented T-dimer in the opposite direction.

Therefore Sigma=12 has no terminal static C4 state. After quotienting the current Sigma=10 and Sigma=12 exits, any surviving energy-minimal portal-C4 class must begin at Sigma>=14.

## References

```json
[
    {
        "relation": "dependency",
        "revision_id": "R3"
    },
    {
        "relation": "dependency",
        "revision_id": "R4"
    },
    {
        "relation": "dependency",
        "revision_id": "R966"
    }
]
```