# Universal-source fragmentation and the revised parent obstruction

**Workspace:** D17
**State:** working
**Key:** `universal-source-fragmentation-core`

**Summary:** Develops the arbitrary-fragmentation identity beyond transition one, the zero-excess literal-source forest, pair-deletion three-to-two representation, smaller-source currentization, first-excess taxonomy, and the revised parent obstruction that replaces transition-count casework.

### 10. Fragmentation identity without transition-one

Retain a literal source cover

  C_p = A | B

of H-p and a universally crossing vertex z in A. Put

  S=A-{z},   C=B union {p}.

The induced support C has path-cover number exactly two. The displayed paths B and (p) give pc(C)<=2. If C were Hamiltonian, a Hamilton path on C together with the original source rail A would be a spanning two-cover of H. Hence pc(C)=2.

Put r=pc(S). Smallest-counterexample minimality gives r<=2 and S is nonempty, so r is one or two. For any exact H-z two-cover T, let b_S(T),b_C(T) denote the numbers of maximal contiguous S- and C-blocks in its two rails, and let tau(T) count the selected S|C transitions. Splitting the two rails at all such transitions gives the exact block identity

  b_S(T)+b_C(T)=2+tau(T).

Every S-block cover of S has at least r components and every C-block cover of C has at least two, so

  b_S(T)>=r,   b_C(T)>=2.

Define the literal fragmentation excess

  eps(T)=(b_S(T)-r)+(b_C(T)-2).

Then

  tau(T)=r+eps(T),    eps(T)>=0.

Thus transition-one is precisely the Hamilton-S zero-excess case r=1, eps=0. If S is non-Hamiltonian, r=2 and EVERY target cover has tau>=2. No normalization can remove this lower bound.

If r=2, the deleted vertex z is internal in the retained source order A. Otherwise deleting an endpoint from A would leave a Hamilton path on S. Write the actual order

  A = L - z - R,

where L and R are both nonempty literal contiguous tight paths. Then L|R is a minimum two-cover of S.

### 11. Zero-excess non-Hamilton S and the literal-source forest

Assume pc(S)=2 and eps(T)=0. Then

  b_S(T)=2,   b_C(T)=2,   tau(T)=2.

After contracting its four maximal monochromatic blocks, the exact two-cover T is a two-component path forest on four vertices with two cross-color edges. Up to exchanging rail names and reversing the displayed word types, only three block patterns occur:

  S-C | S-C,
  S-C-S | C,
  C-S-C | S.

Here the symbols mean the ACTUAL T-blocks; no identification with L,R,B,(p), and no relation between their internal Hamilton orders, is implicit.

There is nevertheless a useful exact consumer when these four blocks have been currentized to the literal source pieces L,R,B,(p). In the S-C-S|C pattern, if the middle C block is (p), there is no direct S|B selected adjacency, contrary to universal crossing. If the middle C block is B and (p) is isolated, the three-block rail is a Hamilton path on S union B; together with the vacuous dimer (p,z) it two-covers H. Hence this pattern cannot survive.

In the C-S-C|S pattern, the isolated S block is L or R. Replace that whole disconnected rail by its original source order if necessary and attach z at the corresponding source end. The other rail is untouched, and the remaining label p lies on its C-side block. This yields a spanning two-cover. Thus this pattern also closes.

For the matching S-C|S-C pattern, source-end alignment determines whether z can be attached to one mixed rail while p remains on the other. Every aligned placement closes. The only nonclosing literal-source placements are the anti-aligned matchings

  L-B | p-R

or

  L-p | B-R,

with the exact dual displayed orientations understood rather than silently reversed. These do not yet span H, but they give a seam-free compatibility repair. From

  C_z=(L-B)|(p-R)

replace the p-leading component by the literal source subpath z-R to obtain

  C_p^new=(L-B)|(z-R).

Likewise

  C_z=(L-p)|(B-R)

gives

  C_p^new=(L-z)|(B-R).

On H-{p,z} the corresponding C_z and C_p^new restrictions agree literally. Hence the formerly missing pz compatibility is restored. No new junction is asserted in either repair.

### 12. Pair-deletion three-to-two representation

The non-Hamilton-S branch has a cleaner representation that removes the singleton p block entirely. Keep

  A=L-z-R

and put

  W=H-{p,z}.

Then pc(W)=2 exactly. Minimality gives pc(W)<=2. If W were Hamiltonian, its Hamilton path together with the vacuous dimer (p,z) would be a spanning two-cover of H, impossible.

The retained source supplies the literal three-cover

  L | R | B

of W. For any exact two-cover F of W define theta(F) to be the number of selected F-adjacencies whose endpoints lie in different classes among the three ACTUAL source supports L,R,B. Let b_L,b_R,b_B be the corresponding maximal block counts. Splitting the two F rails at every interclass transition gives

  b_L+b_R+b_B=2+theta(F).

Since every source class is nonempty, b_L,b_R,b_B>=1. Put

  eta(F)=(b_L-1)+(b_R-1)+(b_B-1).

Then exactly

  theta(F)=1+eta(F).

Thus theta-1 is the total fragmentation of the three literal source components. This is the natural component-drop potential on the common pair-deletion residue. It is not a claimed global monotone under arbitrary source changes.

### 13. One-transition component drop currentizes to a smaller endpoint source

Suppose an exact two-cover F of W has theta(F)=1. Then eta=0, so L,R,B each occur as one complete contiguous F-block, and exactly one pair of source classes is joined while the third class is a pure F rail.

The joined pair cannot be L and R: that mixed rail would be a Hamilton path on all of S=L union R, contradicting pc(S)=2. Hence either L is joined to B and R is the pure rail, or R is joined to B and L is the pure rail.

Assume first that F has an actual mixed Hamilton rail P_LB on L union B and an actual pure Hamilton rail Q_R on R. No relation between Q_R and the original order R is needed. Replace the ENTIRE disconnected rail Q_R by the original literal source path R. This introduces no seam. Since z-R is a literal suffix of A, prepend z and obtain the exact H-p two-cover

  C_p' = P_LB | (z-R).

Thus z is an endpoint of a source rail of order |R|+1, strictly smaller than |A|. The dual case gives

  C_p' = (L-z) | P_RB,

again with z an endpoint of a source rail of order |L|+1<|A|.

This is a genuine source currentization theorem for theta=1. Crucially, the mixed rail P_LB or P_RB is retained exactly as supplied by F; no source-order currentization of that rail is required.

Consequently, if one chooses a universal-crossing source triple (p,A|B,z) with |A| minimum among all universal-crossing offending rails, a theta=1 common-residue cover cannot leave z universal relative to C_p'. If it did, C_p' would be a universal-crossing source with a strictly smaller offending rail. Hence z is quiet relative to C_p'. By the support characterization of section 8, the source universe obtained from z's smaller rail is Hamilton after deleting z. Concretely, in the first case R union {p} is Hamiltonian; in the dual case L union {p} is Hamiltonian.

This does not yet close H. It shows that the theta=1 branch either moves the obstruction to an endpoint source, or under minimal-side extremality destroys the universal status and supplies a Hamilton replacement on the shortened source side.

### 14. First excess: exact theta=2 block taxonomy

Assume theta(F)=2. Then b_L+b_R+b_B=4, so exactly one of L,R,B is fragmented into two nonempty F-blocks and the other two source classes each occur as one whole block. The contracted F forest is either a three-block rail plus an isolated block, or two two-block rails.

First consider a three-block rail. If the isolated whole block is L or R, that isolated rail may be replaced by its original source order and z attached at the appropriate source end exactly as in section 13, producing a smaller endpoint source. If the isolated block is B and the repeated class is L or R, the three-block rail uses only L and R and spans all of S, contradicting pc(S)=2.

There is one additional formal P3|P1 topology when the isolated block is itself one fragment of the repeated class. It is not a new hard residue. For example, if L is repeated and the literal word is

  L_1 - B - R | L_2

(or L_1-R-B | L_2), then the contiguous B-R (respectively R-B) subpath is Hamiltonian on all of B union R, while the original source path L is Hamiltonian on all of L. Hence

  L | (B-R)

(or L | (R-B)) is an exact W-cover whose class-interaction uses only the L-isolated two-class join, and section 13 currentizes it to the smaller endpoint source. Repeated R is dual. If B is repeated and one B-fragment is isolated, the remaining three-block rail contains L-R or R-L consecutively and therefore Hamiltonizes S=L union R, impossible. Thus under the genuine hard assumption that no smaller source reduction exists, these isolated-repeated-fragment cells disappear.

Therefore the only three-plus-one residue avoiding source shrink and S-Hamiltonicity is

  L - B_1 - R | B_2

or its literal reversal, where B_1,B_2 are the two nonempty maximal B-blocks of F.

Now consider two two-block rails. If B is the repeated class, the form is

  L-B_1 | R-B_2

up to rail exchange and literal orientations. If L is repeated, the form is

  L_1-R | L_2-B,

and if R is repeated there is the exact dual

  R_1-L | R_2-B.

Here L_1,L_2 (or R_1,R_2) are the two actual maximal F-blocks of the fragmented source class. No claim is made that they are intervals of the original source order L (or R).

Thus theta=2 has four genuine excess families after the immediate source-shrink and S-Hamiltonian branches are removed: one B-fragmented bridge, one B-fragmented matching, and the two side-fragmented matching types. This is a complete block-word taxonomy, not an absorption theorem.

### 15. Revised parent obstruction

The transition-one bottleneck is no longer the correct frontier. In the non-Hamilton-S branch the common pair-deletion formulation proves:

  theta_min=1
    => an exact smaller endpoint source for the same physical z,

whereas

  theta_min>=2
    => every exact H-{p,z} two-cover fragments at least one of the three literal source components L,R,B.

The first excess theta=2 shapes are listed in section 14, but theta_min may be larger. The remaining parent theorem should therefore be a THREE-TO-TWO FRAGMENTATION CURRENTIZATION theorem: from the fixed literal three-cover L|R|B of W and the universal-crossing source data, either produce a theta=1 exact W cover, construct a spanning two-cover of H, or perform an actual globally verified source-family repair.

A second equivalent hard front is an endpoint-universal smaller source produced by section 13. In an endpoint source, the omitted label p cannot attach to any end of either source-side support whose p-augmentation is non-Hamiltonian; these exact endpoint shields should be retained rather than spent into anonymous payment or P4 output.

Generic component-drop balanced pairs R159/R176, a standalone R435 mismatch, or an isolated P4 do not consume this obstruction. The scarce information is the actual selected block geometry of the common residue together with the two omitted physical labels p,z and the original source seams through z.

Status: sections 10-14 are complete internal working arguments. They have not undergone independent canonical review. The universal source-crossing arm remains open at the theta_min>=2 / endpoint-universal fragmentation consumer.




## References

```json
[
]
```
