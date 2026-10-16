# Balanced six-cube refutes canonical star-midpoint completion

- Stable ID: note_nori_balanced_q6_canonical_star_midpoint_failure_20261015
- Author: unspecified; session provenance retained
- Primary home: subsection:gauge_critical_switches_and_clustered_witnesses_on_full_paths
- Labels: balanced-cube, counterexample, paired-midpoint, negative-certificate
- Lifecycle: active
- Epistemic status: proved
- Current version: 2
- Retention: current and at most one previous snapshot
- Created session: session_nori_r9962_4
- Updated session: session_nori_r9962_4
- Disposition: none
- Successor: none

## Related references

- note:note_nori_balanced_nonpaired_q6_20261015

## Research note

For a vertex-balanced antipodally odd coloring of Q_{2m}, put D(x)={i:c_i(x)=0} and y(x)=x xor 1_{D(x)}. Then |D(x)|=m and y(bar x)=y(x). The proposed canonical-midpoint strengthening asserts that for some x, zero-colored geodesics x->y(x) and bar x->y(x) exist. This would imply NORI1.

**Six-dimensional counterexample.** Encode x in 0,...,63 using bits 0,...,5. The undirected direction-i edge color is bit rho_i(x) of T_i, with rho_i(x)=(x mod 2^i)+2^i floor(x/2^(i+1)); this deletes bit i. Index the least significant bit as zero. Take
T=(0x44ee88dd,0x3a3aa3a3,0x7d417d41,0xc0f330fc,0xaa0f0faa,0xdd771144).
Checking all 64 vertices proves every vertex has three zero edges and c_i(bar x)=1-c_i(x) for all i. For each root x, enumerate the six orders of D(x) and the six orders of its complement from bar x. No x has zero-colored three-step paths in both faces meeting at y(x). Yet there are 252 rooted zero full antipodal geodesics: 28 roots have 3, 12 have 4, and 24 have 5. One witness is root 0 with direction order (3,1,5,4,0,2).

**All even dimensions.** Given any balanced odd coloring c of Q_n with n>=6, add directions a=n,b=n+1, leave the old edge rules independent of the new bits, and put c_a(x)=x_0, c_b(x)=1-x_0. This preserves antipodal oddness and balance. The canonical D set of the extension is D_old together with one new direction. Projecting any putative pair of zero half-geodesics meeting at its canonical midpoint onto the first n directions would produce the corresponding pair in Q_n. Thus the displayed obstruction lifts to every even n>=6. In addition every original rooted zero full geodesic extends: insert the new zero-colored direction selected by x_0 immediately before its unique direction-0 step and the other immediately after it. Thus every root still has a zero full geodesic in the lifted examples.

The conclusion concerns this canonical midpoint selection, and does not refute NORI1. A self-contained finite verifier is available.
