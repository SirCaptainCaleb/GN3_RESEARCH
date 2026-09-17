# Connected interaction, pairwise non-Hamiltonicity, and rainbow/split-star compression

**Workspace:** D17
**State:** working
**Key:** `universal-source-connected-rainbow-splitstar`

**Summary:** Class-interaction connectivity is characterized exactly by pairwise non-Hamiltonicity, and arbitrary fragmentation compresses to the rainbow-hinge or split-star-weave physical two-cut objects.

### 20. Class-interaction connectivity is the arbitrary-fragmentation core

The scalar transition count is stronger than necessary for source reduction. Retain the minimum-side universal source

  C_p=A|B,   A=L-z-R,

and the common residue

  W=H-{p,z}

with literal source three-cover L|R|B. For an arbitrary exact two-cover F of W define its CLASS-INTERACTION GRAPH J(F) on vertex set {L,R,B}: put an edge XY in J(F) exactly when some selected adjacency of F has one endpoint in source class X and the other in source class Y. Multiple transitions of the same type give only one edge. No assumption is made that an F-block is an interval in the original source order.

If J(F) is disconnected, the universal arm is already reduced. Since all three source classes are nonempty, a disconnected graph on {L,R,B} has an isolated class K. No selected F-state joins K to either other class. Therefore every F-rail meeting K is wholly contained in K. Because F has exactly two nonempty rails and the other two source classes are both nonempty, K cannot occupy two rails: that would leave no rail for the other classes. Hence all vertices of K lie on one pure F-rail, that rail contains no other class, and the other F-rail contains every vertex of the other two source classes. Consequently the union of the other two classes is Hamiltonian in the ACTUAL order supplied by the second F-rail.

There are three cases.

* If K=B, then L union R=S is Hamiltonian, contradicting pc(S)=2.
* If K=R, then L union B has an actual Hamilton path P_LB. Replace the pure F-rail on R, if necessary, by the original literal source path R. Since z-R is a literal suffix of A, the two paths

    P_LB | (z-R)

  form an exact H-p source in which z is an endpoint of a rail of order |R|+1<|A|. This is the section-13 source shrink, with no restriction on how often L and B alternated inside P_LB.
* If K=L, the dual construction gives the exact smaller endpoint source

    (L-z) | P_RB.

Thus the source-shrinking conclusion depends only on DISCONNECTION of J(F), not on theta(F)=1, eta(F)=0, or any bound on the number of transitions. In particular, the first-excess taxonomy is diagnostic only.

The genuine arbitrary-fragmentation residue is therefore the graph-intrinsic statement relative to the fixed literal source classes:

  J(F) is connected for EVERY exact two-cover F of W.

Since J(F) has only three vertices, every surviving exact W-cover contains selected transitions of at least two distinct source-class pair types. This is the minimal relational currency that an arbitrary-fragmentation consumer must use. A proof which only counts repeated transitions of one type is aiming below the actual obstruction.

A useful extremal reformulation is to choose F minimizing first rho(F)=|E(J(F))| and then the total transition count. The hard residue has rho(F) in {2,3}. If rho=2 the two interaction types form a length-two tree on {L,R,B}; if rho=3 all three pair types occur. What is not proved is that rho=3 can be switched to rho=2, or that a rho=2 cover can be currentized to a disconnected interaction graph. Any such switch must retain complete tight-path seam windows: the accepted R461 two-endpoint-cut fence shows why a one-sided source surgery cannot in general complement a native splice obstruction.

This connectivity reduction is valid for arbitrary transition multiplicity and is the preferred parent representation after Director v10. The remaining theorem is a CONNECTED-INTERACTION TWO-CUT CURRENTIZATION: consume two differently typed actual transitions in one common-residue cover to produce a disconnected J-cover, a spanning two-cover of H, or a verified source-family improvement. Separate R176 births from the two transitions are insufficient because bare balanced pairs need not currentize any cover.

Status: complete internal working argument. It uses only the exact source three-cover, pc(W)=2, pc(L union R)=2, and literal path replacement at a whole pure rail. It is not yet canonically reviewed.


### 21. Connected interaction is exactly pairwise non-Hamiltonicity

Retain the minimum universal source and common residue of section 20:

  C_p=A|B,   A=L-z-R,   W=H-{p,z},

with L,R,B nonempty literal Hamilton source classes and pc(W)=2. In the hard residue, J(F) is connected for every exact two-cover F of W.

This quantification over exact covers has an equivalent support-only formulation:

  pc(L union R)=pc(L union B)=pc(R union B)=2.

Each pair-union has path-cover number at most two because its two source classes are themselves tight Hamilton paths. If, say, L union B were Hamiltonian, a Hamilton path on L union B together with the literal source path R would be an exact W two-cover whose interaction graph isolates R, contradicting the hard residue. The same argument applies to the other pairs. Conversely, if some exact W-cover has disconnected J(F), section 20 / accepted R931 isolates one class and shows that the union of the other two classes is Hamiltonian. Therefore pairwise non-Hamiltonicity is equivalent to connected interaction for every exact W-cover.

Thus the connected-interaction core may be viewed without choosing F: three Hamilton atoms L,R,B, every two-atom union non-Hamiltonian but exactly two-coverable, while their full union W has pc(W)=2. The special pair L union R=A-z also retains the literal one-vertex Hamilton bridge L-z-R in H-p, whereas L union R union {p}=A-z+p is non-Hamiltonian by universality of z.

There is also an exact pair-restriction ledger for every chosen exact W-cover F. Let b_L,b_R,b_B be its maximal source-class block counts and let e_LR,e_LB,e_RB count selected transitions of the three pair types, so theta=e_LR+e_LB+e_RB and b_L+b_R+b_B=2+theta. For distinct classes X,Y put

  c_XY(F)=number of path components of F[X union Y].

The induced quotient on the X- and Y-blocks is a forest, hence

  c_XY=b_X+b_Y-e_XY.

Summing over the three pairs gives

  c_LR+c_LB+c_RB = 4+theta.

In the hard residue each pair support has path-cover number two, so c_XY>=2. Writing sigma_XY=c_XY-2 gives the exact nonnegative slack identity

  sigma_LR+sigma_LB+sigma_RB = theta-2.

This is only a ledger, not a monotone potential. It says that every transition beyond the two interaction types required for connectivity is paid exactly as excess fragmentation in the three pair restrictions.

### 22. Arbitrary fragmentation compresses to a rainbow hinge or a split-star weave

Fix any exact W two-cover F in the hard residue and contract each maximal L-, R-, or B-block to its source-class label along the two F rails. Adjacent labels differ. Since J(F) is connected, at least two distinct pair types occur.

There is an exact dichotomy requiring no bound on theta.

(RAINBOW HINGE.) Some F rail contains three consecutive maximal blocks

  X - K - Y

whose labels X,K,Y are all distinct. The two selected interblock adjacencies are then differently typed actual transitions sharing the same literal middle F-block K. This is the preferred local two-cut interface: both selected seams are current in one rail and no transition multiplicity elsewhere is discarded.

(SPLIT-STAR WEAVE.) No such rainbow triple occurs. Then in every rail word the label two positions later equals the current label: otherwise three consecutive labels would be pairwise distinct. Hence every nontrivial rail alternates between at most two fixed source classes. A single nontrivial rail cannot realize connected J on all three labels, and a trivial second rail adds no interaction edge, so both rails are nontrivial and their two label-pairs are distinct. On three labels, the two pairs necessarily share a unique center K. After renaming the leaves X,Y,

  rail P alternates only between X and K,
  rail Q alternates only between K and Y.

Consequently J(F) is exactly the tree X-K-Y. The leaf class X occurs only on P, the leaf class Y only on Q, and only K is split between the rails. At support level there is a nontrivial partition K=K_1 disjoint-union K_2 such that

  V(P)=X union K_1,   V(Q)=K_2 union Y.

Because K itself has a retained literal Hamilton source order and K_1,K_2 are both nonempty, scanning that source order yields at least one consecutive source state with one endpoint in K_1 and the other in K_2. Thus the split-star residue always carries an actual source adjacency crossing the two F rails in addition to the two leaf-center interaction systems. In the B-centered case this is exactly

  V(P)=L union B_1,   V(Q)=B_2 union R,

with a literal B-source state crossing P|Q and the independent literal source bridge L-z-R. This is the arbitrary-fragmentation version of the old anti-aligned weave. A naive graph tail-switch is not licensed when these connectors hit internal rail vertices: cutting at both connectors can leave more than two path fragments, and every tight reconnection requires its complete turn window. The remaining theorem must therefore consume the rainbow hinge or split-star weave through an actual tight two-cut reconstruction.



## References

```json
[
]
```
