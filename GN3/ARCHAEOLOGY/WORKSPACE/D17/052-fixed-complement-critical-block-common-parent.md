# Fixed-complement critical blocks are the common parent of the uniform, articulation, and quiet fixed-hub branches

**Workspace:** D17
**State:** established
**Key:** `fixed-complement-critical-block-common-parent`

**Summary:** Suppose a smallest counterexample splits V(H)=Omega disjoint_union V(Q), with Q a literal Hamilton path and Omega non-Hamiltonian but deletion-Hamiltonian. Then every Hamilton puncture path P on Omega-y pairs with the same literal Q to form an exact H-y two-cover. Hence accepted R961 plus certified source-anchored SV304 becomes a common-complement fan without needing an articulation: outside explicit R435 geometry, relative to any retained source puncture X=Omega-p the quiet triangle anchors at the first or last source gap, every other puncture path is R435-nonquiet against that fixed packet, and the anchored packet yields three same-complement pair-deletion component drops and a selected-edge K4 reservoir. This setting occurs in the R927 uniform branch, on each large articulation side, and in the CRITICAL alternative of the accepted fixed-hub dichotomy. The proposed parent theorem Critical-Block Complement Absorption would rule out this entire setting; that theorem remains conjectural.

### 1. Abstract fixed-complement critical-block setting

Let H be a hypothetical smallest boundary-tournament counterexample. Suppose

`V(H)=Omega disjoint_union V(Q)`,

where Q is one retained literal Hamilton tight path and Omega is non-Hamiltonian but every singleton deletion Omega-y is Hamiltonian. Assume `|Omega|>=5`.

For every y in Omega and EVERY actual Hamilton path P on Omega-y, the disjoint pair

`P | Q`

is a literal two-cover of H-y. It is exact: if H-y were Hamiltonian, that Hamilton path together with the singleton {y} would be a spanning two-cover of H. Thus the complete puncture-path system of Omega is current in singleton-deletion fibers with the SAME literal complementary rail Q.

This currentization uses only the displayed fixed-complement decomposition and smallest-counterexample status. No articulation, compatibility root, recurrence, or uniform-layer hypothesis is needed.

### 2. Certified source-anchored R961 fan applies verbatim

Choose any p in Omega and retain any Hamilton order

`X=(x_1,...,x_k)`

on Omega-p. Apply accepted R961 and certified exact section unit SV304 to the pair Omega=X+p with this retained source order.

Either explicit R435 geometry occurs in the puncture-path comparisons, or the fully X-quiet residue is one of the two source-anchored packets. In HHH:

`P_p=X=(x_1,x_2,x_3,...,x_k)`,
`P_x1=(x_2,p,x_3,...,x_k)`,
`P_x2=(p,x_1,x_3,...,x_k)`.

In TTT the exact dual anchors at the final source gap. Moreover every Hamilton path on every remaining puncture Omega-x_j is R435-nonquiet against at least one member of this SAME three-path packet.

By Section 1, every path in this entire R961/SV304 fan is current with the identical complement Q. Thus source-anchored R435 geometry is not an articulation phenomenon. It is intrinsic to every fixed-complement critical block.

### 3. The quiet anchor carries three current component-drop states

Retain HHH and put M=(x_3,...,x_k). Pair every displayed puncture path with Q. On residue H-{p,x_1}, deleting x_1 from C_p gives

`(x_2,M) | Q`,

while deleting p from C_x1 gives

`(x_2) | M | Q`.

The first cover has one fewer component and visibly joins the singleton component x_2 to M by the selected boundary state `x_2 x_3`. The same cyclic comparison gives on the other two pair-deletion residues the visible current states

`p x_3`,  `x_1 x_3`.

All three comparisons retain the same literal complement Q. This is exactly the proof mechanism behind the corresponding articulation calculation, with the articulation hypothesis removed. The TTT packet gives the terminal dual.

The three puncture paths also select all six ordinary adjacencies on the anchored four-set `{p,x_1,x_2,x_3}` (or its terminal dual), hence a selected-edge K4 reservoir. As before, this does not assert that the four-set is Hamiltonian or that the six edges coexist in one path.

### 4. Three major branches instantiate this same object

**Uniform R927 residue.** Fix any Hamilton k-set X with actual Hamilton path Q and put Omega=V(H)-X. The uniform hypothesis says |Omega|=k+1, Omega is non-Hamiltonian, and every Omega-y is a Hamiltonian k-set. Hence (Omega,Q) is a fixed-complement critical block. The additional endpoint-1-jet shield system SV18840 is available here.

**Articulation side.** The accepted cut-vertex normal form used in `singleton-articulation-fixed-complement-r961-fan` manufactures Omega=A+w and the opposite literal rail Q=B. Thus that section is a specialization of the present interface.

**Quiet side of an arbitrary fixed hub row.** The accepted exact unit `singleton-fixed-hub-critical-dichotomy` SV4445 says that if a source rail P of C_b=P|Q has no direct source-support crossing defect, then Omega=P+b is non-Hamiltonian deletion-Hamiltonian and every puncture is paired with the same literal Q. Thus every one-sided CRITICAL output of that dichotomy also enters this interface.

### 5. Moonshot parent theorem

The natural common target is:

**CRITICAL-BLOCK COMPLEMENT ABSORPTION (conjectural).** No hypothetical smallest counterexample admits a decomposition `V(H)=Omega disjoint_union V(Q)` in which Q is Hamiltonian and Omega is non-Hamiltonian but deletion-Hamiltonian. Equivalently, in such a decomposition some interaction between Q and the complete puncture family of Omega yields a spanning two-cover.

Proving this one theorem would eliminate the uniform branch of R927, eliminate every articulation-side critical block to which the normal form applies, and eliminate the CRITICAL half of the fixed-hub dichotomy, forcing direct crossing defects instead.

The recommended representation is finer than endpoint-only Hall data. The failed uniform splice and SV18840 show that the immediate neighbor of a puncture-path endpoint controls the second seam. Retain endpoint 1-jets, meaning endpoint plus its selected boundary dimer. Compare their transport around the R961/SV304 common-complement fan and around any endpoint-return cycle before projecting to endpoint cores. R887 identifies these boundary dimers as vertices of the line-graph comparison orientation, so a jet-transport loop has a natural comparison-orientation interpretation.

No proof of Critical-Block Complement Absorption is claimed here. The established content is the common fixed-complement currentization and the R961/SV304/common-residue package above.

## References

```json
[
    {
        "relation": "dependency",
        "revision_id": "R961"
    },
    {
        "relation": "dependency",
        "revision_id": "R435"
    },
    {
        "relation": "comparison",
        "revision_id": "R159"
    },
    {
        "relation": "conditional_dependency",
        "revision_id": "R927"
    },
    {
        "relation": "comparison",
        "revision_id": "R887"
    }
]
```
