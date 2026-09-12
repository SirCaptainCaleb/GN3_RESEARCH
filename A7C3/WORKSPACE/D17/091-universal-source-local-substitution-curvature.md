# A universal source crossing has source-local reverse-trimer curvature

**Workspace:** D17
**State:** established
**Key:** `universal-source-local-substitution-curvature`

**Summary:** For a literal singleton source C_p=A|B and a universal offender z on the actual Hamilton word A, substitute p for z in that same word. If the substituted word is tight it gives an explicit crossing-free H-z cover, impossible. Hence one of at most three source-local turns involving p is bad; boundary antisymmetry reverses it to a proper tight trimer using p and vertices within distance two of z in the source order. R4 currentizes that trimer as a maximum three-forest, and R508 forces dual universal recompletion crossings at its two boundary dimers. Thus R927 Arm U enters the same current-trimer / maximum-three-forest portal layer by one local source-order move, without transition-count or fragmentation taxonomy.

### 1. In-place source substitution

Let H be a hypothetical smallest counterexample and retain a literal exact singleton-deletion source

  C_p = A | B

of H-p, with the ACTUAL Hamilton source order

  A=(a_0,a_1,...,a_m).

Fix z=a_i in A. Form the literal in-place replacement word

  A[p/z]=(a_0,...,a_{i-1},p,a_{i+1},...,a_m)

on support (A-{z}) union {p}. No Hamilton order is changed away from the physical position of z.

If A[p/z] is tight, then

  A[p/z] | B

is an exact two-nonempty-path cover of H-z. It selects no adjacency between A-{z} and B, because its two rails have supports (A-{z})+p and B. Consequently z is NOT universally crossing relative to C_p.

Therefore, if z IS universally crossing, A[p/z] is not tight. This also recovers directly the support fact that A-z+p is non-Hamiltonian: any Hamilton path on that support paired with B would be a crossing-free exact H-z cover.

A universal offender cannot lie on a source rail of order at most two. For |A|<=2 the support A-z+p has order at most two and hence is itself a nonempty tight path, again giving the crossing-free cover above. Thus in the universal case |A|>=3 and at least one consecutive turn exists in A[p/z].

### 2. The failure is confined to at most three physical turns

Every consecutive turn of A[p/z] not containing p is literally a consecutive turn of the retained source word A and is tight. Hence all failure is confined to the available members of the following source-local list:

  L_i=(a_{i-2},a_{i-1},p)          if i>=2,
  M_i=(a_{i-1},p,a_{i+1})          if 1<=i<=m-1,
  R_i=(p,a_{i+1},a_{i+2})          if i<=m-2.

Since A[p/z] is not tight, at least one available member is bad. Boundary antisymmetry R3 therefore makes its COMPLETE reversal tight. Thus a universal source crossing always yields at least one of the graph-intrinsic proper tight trimers

  J_L=(p,a_{i-1},a_{i-2}),
  J_M=(a_{i+1},p,a_{i-1}),
  J_R=(a_{i+2},a_{i+1},p),

for the corresponding available bad window. The trimer contains the physical source label p and only vertices at source-order distance at most two from the historical position of z. No alternative representative, path reversal, transition minimization, or support synchronization is used.

Endpoint cases are exact rather than exceptional. If z is a source endpoint, there is exactly one new candidate turn when |A|>=3, so its reversal is forced. If z is one step from an endpoint there are two candidates. For an internal z there are at most three.

There is a useful refinement in the middle case. If every available flank window L_i,R_i is tight but M_i is bad, then J_M is tight and every available outward continuation in the reversed source direction is blocked: R3 turns tight L_i into bad (p,a_{i-1},a_{i-2}) and tight R_i into bad (a_{i+2},a_{i+1},p). Thus the central source-substitution curvature comes with literal source-neighbor shields on every available side.

### 3. Currentization and dual boundary-dimer pressure

Let J=(j_0,j_1,j_2) be any tight trimer obtained in Section 2. It is a proper tight path: B is nonempty and z is not a vertex of J, so H-V(J) is nonempty. Accepted smallest-counterexample minimality R4 therefore gives an exact two-cover

  U | V

of H-V(J), making

  J | U | V

a literal maximum spanning three-forest which retains the source-local trimer exactly.

The current trimer automatically carries two universal recompletion cuts, and this can be reconstructed directly from accepted R508 rather than imported as a black box. Delete the outer vertex j_0. In R508 take

  D={j_0},   S={j_1,j_2},   C=V(H)-V(J),   Q=J.

Since Q is a tight Hamilton path on D union S, EVERY exact H-j_0 two-cover selects a physical adjacency crossing

  {j_1,j_2} | (V(H)-V(J)).

Dually, deleting j_2 and taking S={j_0,j_1} forces every exact H-j_2 two-cover to cross

  {j_0,j_1} | (V(H)-V(J)).

Thus the broad source-crossing obstruction has been localized to one source-anchored three-vertex carrier whose two boundary dimers both exert universal recompletion pressure against the same residual support. The actual source position i and the exact failed window L_i, M_i, or R_i remain part of the ancestry.

### 4. Parent-scale consequence for R927 Arm U

Combine the preceding local compiler with accepted R927. If the universal-crossing branch U is absent globally, R927 gives the odd uniform middle-layer branch M. If U occurs, choose the literal witnessing source C_p=A|B and offending z. Sections 1-3 immediately produce a source-anchored current reverse trimer and hence a literal maximum three-forest carrying that trimer together with its dual boundary-dimer recompletion cuts.

Therefore the R927 entrance may be sharpened to the parent-scale alternative

  UNIFORM MIDDLE LAYER
  OR
  SOURCE-LOCAL CURRENT-TRIMER CURVATURE.

This is a curvature-versus-saturation interpretation of the original U/M split. Successful in-place source substitution is the flat support move; a universal obstruction to that move is witnessed by curvature on one of at most three local source windows. In particular, transition-one existence, arbitrary-fragmentation classification, source-pivot cycles, and connected-interaction taxonomy are not required merely to export Arm U into the current-trimer / maximum-three-forest parent layer. They may still carry stronger information needed to CONSUME that parent portal, and nothing here invalidates those exact results.

The theorem does NOT close O4 and does NOT claim that a current trimer is itself contradictory. Its value is compression: Arm U has no separate unbounded entrance geometry once the literal source word is used. The surviving task is to consume the source-anchored trimer portal, preferably using its retained location/shields together with the dual R508 cut pressure rather than forgetting ancestry in generic maximum-forest dynamics.

Status: complete internal working mathematics. The proof uses accepted R3, R4, R508 and the literal source/universal-crossing premise of accepted R927. This section is unreviewed exposition and is not canonical certification.

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
        "revision_id": "R508"
    },
    {
        "relation": "dependency",
        "revision_id": "R927"
    }
]
```
