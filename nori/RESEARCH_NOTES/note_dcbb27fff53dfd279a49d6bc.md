# A realizable double-positive region in capped-arm root transport

- Stable ID: note_dcbb27fff53dfd279a49d6bc
- Author: unspecified; session provenance retained
- Primary home: subsection:cyclic_variation_selection_for_antipodal_and_boundary_path_galleries
- Labels: root-transport, capped-arms, local-obstruction
- Lifecycle: active
- Epistemic status: proved
- Current version: 1
- Retention: current and at most one previous snapshot
- Created session: session_nori_r8293_1
- Updated session: session_nori_r8293_1
- Disposition: none
- Successor: none

## Related references

- subsection:cyclic_variation_selection_for_antipodal_and_boundary_path_galleries

## Research note

# A realizable double-positive region in capped-arm root transport

Let \(n=m+2\) with \(m\ge2\), choose dimensions \(i,j\), and let \(v=0\). In the face
\[
F=\{x:x_i=0,\ x_j=1\}\cong Q_m
\]
give every edge in an exterior dimension color one. Give the incident direction-\(i\) edge at \(v\) color one and the direction-\(j\) edge at \(v\) color zero. Prescribe the antipodal edges with complementary colors. These prescriptions are consistent: the exterior edges of \(F\) are paired with the exterior edges of its opposite face, and the two cap-edge orbits have different directions. Extend arbitrarily to the remaining antipodal edge pairs.

Let \(S\) be the full switch set of this antipodally odd coloring, and let \(s\) be the turn with directions \(i,j\) at \(v\). It is retained. For a root \(x=(0,1,y)\in F\), every prefix from \(x\) to \(v\) with final direction \(j\) traverses exterior edges of color one followed by a cap of color zero. Therefore its minimum internal switch count is
\[
p_s(x,v)=\mathbf1_{\{y\ne0^m\}}.
\]
Antipodal reversal expresses the suffix minimum as a path in \(F\) from \(y\) to \(1^m\), followed by the direction-\(i\) cap at \(\bar v\), which also has color zero. Thus
\[
q_s(x,v)=\mathbf1_{\{y\ne1^m\}}.
\]

The arm types are \((0,1)\) at \(0^m\), \((1,0)\) at \(1^m\), and \((1,1)\) everywhere else. In particular there is no root of type \((0,0)\), and any edge path in this eligible root cube from one endpoint type to the other passes through a \((1,1)\) root.

Moreover the complete path from \(v\) to \(\bar v\) with dimension order
\[
(j,d_1,\ldots,d_m,i)
\]
has color word \(0,1^m,0\). Its antiperiodically completed cyclic period has three switches: two internal changes and the closing comparison. Deleting \(s\) leaves the two-switch period and its two one-switch cuts. Thus the opposite arm types and the intermediate double-positive region occur in a permitted NORI1 coloring and on a three-switch Petrie period.

This example concerns a single deletion witness period and its arm families. It supplies no globally critical obstruction. It shows that opposite endpoint arm types, connected root transport, and one three-switch period do not suffice to force a zero-cost pair of arms at that turn. A proof must use additional critical cycles, other turn locations, or a global compatibility condition.
