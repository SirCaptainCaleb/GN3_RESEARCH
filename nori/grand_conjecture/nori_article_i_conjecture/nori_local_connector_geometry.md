# Local monochromatic connectors, certified squares, and dead-edge rigidity

# Certified squares, dead-edge rigidity, and monochromatic hubs

A physical cube edge is called *live* if some genuinely monochromatic four-edge geodesic traverses it, and *dead* otherwise. These notions depend on actual ordered-three-face colors, not merely on an edge shadow assigning one arbitrarily selected color to each edge. Under NORI antipodal-reversal oddness, certified short paths organize into antipodally related physical root squares, and dead edges exhibit strong local rigidity.

## Local rigidity converts missing certificates into long ones

**Theorem 1 (dead-edge hub lemma).** Let \(n\ge7\). If an edge \(e=\{z,z\oplus e_i\}\) is dead, there is a bit \(t\) such that at either endpoint \(h\) of \(e\), every ordered three-face through \(h\) with free triple avoiding direction \(i\) has color \(t\). Consequently \(h\) lies on monochromatic six-edge geodesics in any chosen six distinct directions avoiding \(i\), with its position among their vertices chosen so every three-direction window contains \(h\).

**Proof.** If two such local ordered faces of different colors met through the same endpoint in an admissible four-move gallery passing through \(e\), a cyclic five-direction exchange would supply a monochromatic four-edge witness traversing \(e\), contradicting deadness. Propagating this constraint around the three-face incidence links gives a common bit \(t\) for all triples avoiding \(i\). Choose six other directions \(p_1,\ldots,p_6\) and any root \(h\oplus\{p_1,p_2,p_3\}\); the directed geodesic through \(h\) after three moves has each consecutive three-window spanning \(h\). Every such window has color \(t\), so the full six-move word is monochromatic. \(\square\)

For \(5\le n\le7\), a similarly placed spanning path already yields the requested zero- or one-switch antipodal geodesic. In larger dimensions the six-move hub is a certified local component, not by itself a full-dimensional solution.

## Geometry of the certified root-square carrier

The dead edges form a matching: if two adjacent cube edges were both dead, their common physical three-face exchange links would force one of them into a monochromatic four-geodesic. Accordingly every antipodal path has live-edge opportunities, and the set of completely four-geodesic-covered roots separates some dead-edge regions. Under the ordered-face reversal law, centered five-window parity also creates physical certified squares, often in both colors; these squares form honest two-dimensional carriers with constraints on their antipodal connectivity and local degree.

If a hub supports both monochromatic colors, the overlap gives a *bichromatic root diamond*: two real short path families with compatible root-square incidence, but potentially incompatible outward terminal colors. The exact two-ended cap equalities force either a short one-switch six-geodesic or a rigid mixed-color obstruction. The latter cannot be ignored when extending a short hub path to a full geodesic.

## Transposition descent and near-midpoint defects

Swapping adjacent directions of a full order changes only the three-window comparisons local to the exchanged directions. When a dead-edge incidence is present, the admissible swaps can be chosen not to increase total defect. Repetition yields normal forms where interior dead-edge obstacles have been eliminated and any obstruction remains near a terminal cap. This is a structural reduction, not a global one-switch theorem: a path can still have several changes in its live interior.

Likewise, high-index permutation topology guarantees genuine paths through near-midpoint physical hubs, but meeting at the same hub with opposite central labels does not suffice for a one-switch splice. There are legal local root rectangles in which both original paths and both exchanges retain three changes. Each proposed repair must check both new ordered-three-face seam windows, with their correct fixed exterior bits.

Thus certified squares and dead-edge rigidity give two complementary sources of control: short monochromatic geodesics in the presence of dead edges, and dense genuinely certified carriers when few are dead. The remaining closure problem is to connect their paths through valid two-window seams without accumulating further defects.
