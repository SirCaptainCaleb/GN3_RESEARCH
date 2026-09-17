# The R953 three-cover row forces a double-internal solo endpoint or perfect endpoint assignment

**Workspace:** D17
**State:** established
**Key:** `three-petal-cover-row-endpoint-dichotomy`

**Summary:** At the R953 three-petal fixed point, retain one Hamilton order on each petal L,B,Z and on each pair union L+B,L+Z,B+Z, giving the three exact H-p covers (L+B)|Z, (L+Z)|B, (B+Z)|L. Let E_L,E_B,E_Z be the two endpoints of the solo-petal paths. Either some x in one E_P is internal in both pair-union Hamilton paths containing P, or every one of the six disjoint solo endpoints appears exactly once among the six endpoint slots of the three pair-union paths. In the first branch, deleting p and x leaves one literal exact two-cover and two literal three-covers of the same residue H-{p,x}; this retains the whole three-cover row rather than collapsing an endpoint disagreement immediately to an anonymous balanced pair. The equality branch is a rigid endpoint-perfect assignment and is the only alternative. No closure is claimed.

### Setup\
Retain the accepted R953 same-size fixed point with disjoint k-petals L,B,Z and common omitted label p. Choose one actual Hamilton path on each petal and one actual Hamilton path on each Hamilton pair union L+B, L+Z, B+Z. Thus H-p has the three simultaneous exact covers\
\
  F_Z=(L+B)|Z,\
  F_B=(L+Z)|B,\
  F_L=(B+Z)|L.\
\
All six displayed rails have order at least two in the live fixed-point regime. Let E_L,E_B,E_Z be the two physical endpoints of the chosen Hamilton paths on L,B,Z. These are six distinct physical vertices because the petals are disjoint.\
\
### Endpoint-incidence dichotomy\
Consider the three pair-union Hamilton paths. Together they have exactly six endpoint slots, two on each of L+B, L+Z, B+Z.\
\
Suppose first that every x in E_L is an endpoint of at least one of the two pair-union paths containing L, and similarly for E_B and E_Z. The six solo endpoints are distinct, so covering all six of them requires at least six pair-union endpoint incidences. Exactly six slots exist. Hence equality holds throughout: every pair-union endpoint is one of the six solo endpoints, and every solo endpoint occurs in exactly one of the two adjacent pair-union paths. Call this the endpoint-perfect branch.\
\
Otherwise, for some petal P in {L,B,Z} there is a solo-path endpoint x in E_P which is not an endpoint of either pair-union Hamilton path containing P. Since both pair-union paths contain every vertex of P, x is internal in both of those paths. Call this the double-internal branch.\
\
These two branches are exhaustive.\
\
### Same-residue three-cover consequence in the double-internal branch\
Assume for notation P=L and x in E_L is internal in both chosen Hamilton paths on L+B and L+Z. Delete x in addition to p.\
\
From F_L=(B+Z)|L, trimming the endpoint x from the literal L-path leaves a Hamilton path on L-x, so we retain an exact two-cover of H-{p,x}:\
\
  (B+Z) | (L-x).\
\
From F_Z=(L+B)|Z, deleting the internal occurrence of x splits the pair-union path into two nonempty tight subpaths while the Z-rail is unchanged, giving a literal three-cover of the same H-{p,x}. From F_B=(L+Z)|B we obtain a second literal three-cover of that same residue by the identical internal-deletion operation.\
\
Thus the three canonical R953 representatives yield, on one common further puncture, one actual exact two-cover and two actual three-covers whose path fragments retain their parent pair-union orders. Accepted R159/R408 may be applied to either component drop, but doing so separately discards this simultaneous row. The stronger current target is to consume the one-two-versus-two-three-cover configuration while retaining all three representatives.\
\
### Scope\
This is an elementary endpoint-counting consequence of the accepted R953 support row. It does not assert that the two component-drop balanced pairs are distinct, does not currentize them automatically, and does not close the endpoint-perfect branch. Its purpose is to expose a parent interface strictly above the stationary recurrence machinery: either a common-puncture double component-drop row, or a rigid endpoint-perfect assignment on the three pair unions.\
\
## References\
\
```json\
[\
    {\
        "relation": "dependency",\
        "revision_id": "R953"\
    },\
    {\
        "relation": "related",\
        "revision_id": "R408"\
    }\
]\
```\
