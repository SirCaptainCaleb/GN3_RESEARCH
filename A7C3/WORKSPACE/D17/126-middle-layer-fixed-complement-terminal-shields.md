# Residual-pair complements carry universal terminal shields through three exchange fibers

**Workspace:** D17
**State:** working
**Key:** `middle-layer-fixed-complement-terminal-shields`

**Summary:** In the near-maximal uniform branch, every oriented Hamilton residual-pair path Z_ab=O+a+b is nonextendable by every exterior vertex, so both terminal dimers are universally same-polarity shielded. For the third residual c, the exact singleton fibers H-c, H-p_0, and H-p_{k-1} can all be chosen with the SAME complement rail Z_ab while the other rail exchanges c for one endpoint of P. Thus the two-ended shield packet is current across a three-cover row, not an isolated local sign. No absorption is claimed.

### Universal terminal shields on one residual-pair rail

Work in the uniform middle-layer residue and the near-maximal setup of `middle-layer-nearmax-outer-terminal`: \(|O|=k-2\), the residual exterior triple is \(R=\{a,b,c\}\), and every Hamilton path on
\[
Z_{ab}=O\cup\{a,b\}
\]
has endpoints exactly \(a,b\).

Choose one actual orientation
\[
Z_{ab}=(a,o_1,\ldots,o_{k-2},b).
\]
Let \(y\notin Z_{ab}\). Since \(|Z_{ab}|=k\), the support \(Z_{ab}+y\) has size \(k+1\) and is non-Hamiltonian in the uniform residue. If \((y,a,o_1)\) were tight, prepending \(y\) would Hamiltonize \(Z_{ab}+y\). Hence it is bad, and R3 gives
\[
(o_1,a,y)\text{ tight}. \tag{FC1}
\]
Similarly \((o_{k-2},b,y)\) is bad, so
\[
(y,b,o_{k-2})\text{ tight}. \tag{FC2}
\]
Thus **every exterior vertex has the same terminal polarity at both ends of this retained residual-pair path**. This is simultaneous in the literal order \(Z_{ab}\); no path reversal is used.

In particular the deleted source endpoint \(p_0\) and the third residual label \(c\) give two same-polarity witnesses on each tested terminal dimer:
\[
(o_1,a,p_0),\ (o_1,a,c)\text{ tight},
\]
\[
(p_0,b,o_{k-2}),\ (c,b,o_{k-2})\text{ tight}. \tag{FC3}
\]
By R523 language these are two-ended same-polarity collision packets, not opposite-polarity P4 certificates.

### The shield packet is current in three fixed-complement exchange fibers

The relational gain is that the same path \(Z_{ab}=\Omega-c\) occurs as an actual rail in several singleton-deletion covers. Uniformity Hamiltonizes every displayed complementary \(k\)-support, so we may choose
\[
H-c=P\mid Z_{ab}, \tag{FC4}
\]
\[
H-p_0=L_c\mid Z_{ab},\qquad V(L_c)=(P-\{p_0\})\cup\{c\}, \tag{FC5}
\]
and dually
\[
H-p_{k-1}=R_c\mid Z_{ab},\qquad V(R_c)=(P-\{p_{k-1}\})\cup\{c\}. \tag{FC6}
\]
The orders on \(L_c,R_c\) may be reselected arbitrarily among actual Hamilton paths on their supports. Equations (FC1)--(FC3), however, remain tied to the one retained literal complement order \(Z_{ab}\).

So one R966 exchange row is now **cover-current with a fixed Hamilton complement carrying universal two-ended shields**: the first rail changes from \(P\) to a left or right one-vertex replacement while the second rail and its physical endpoint neighbors are unchanged. This is strictly more relational data than an isolated R435 event or an anonymous endpoint shield.

### One-hole dimer seam specialization

If an oriented residual-pair path has \(q\) as one endpoint, say
\[
Z_{rq}=(q,d,\ldots,r),
\]
then deleting \(q\) leaves the contiguous path \(A_r=(d,\ldots,r)\). In any exact \(H-p_0\) cover whose other rail is disjoint from \(Z_{rq}\), the proposed rail
\[
(p_0,q,d,\ldots,r)
\]
has only the first new turn \((p_0,q,d)\) uncertified. If that turn were tight, this rail together with the untouched complementary rail would two-cover \(H\). Hence
\[
(p_0,q,d)\text{ bad},\qquad (d,q,p_0)\text{ tight}. \tag{FC7}
\]
The exact terminal dual holds when \(q\) is the other endpoint. Thus every reselected residual-pair complement turns its actual \(q\)-neighbor into a signed seam witness on the omitted dimer \((p_0,q)\).

This is a current seam interface, not closure. Same-polarity collisions can survive, and the k=7 local two-cap fence shows that the terminal shield array alone is insufficient. The live consumer must exploit the exchanged first rails in (FC4)--(FC6), or introduce a genuinely new seam in a common pair-deletion residue.

Status: complete symbolic working deduction conditional on the current near-maximal endpoint-rigidity section; unreviewed. 

## References

```json
[
    {
        "relation": "dependency",
        "revision_id": "R3"
    },
    {
        "relation": "conditional_dependency",
        "revision_id": "R927"
    },
    {
        "relation": "related",
        "revision_id": "R523"
    },
    {
        "relation": "related",
        "revision_id": "R966"
    }
]
```
