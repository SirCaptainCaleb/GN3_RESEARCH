# Color-sensitive witness parity and two-orbit interaction in Q6

- Stable ID: note_nori_xvii_geodesic_witness_parity_two_orbit_interaction_r12147_5
- Author: session_nori_r12147_5
- Primary home: subsection:central_freudenthal_subdivision_and_the_all_root_geodesic_chamber_sphere
- Labels: NORI1, method-obstruction, topology, path-counting, integral-decoding
- Lifecycle: active
- Epistemic status: proved
- Current version: 1
- Retention: current and at most one previous snapshot
- Created session: session_nori_r12147_5
- Updated session: session_nori_r12147_5
- Disposition: none
- Successor: none

## Related references

- subsection:central_freudenthal_subdivision_and_the_all_root_geodesic_chamber_sphere
- note:note_nori_xiv_direction_resolved_projective_curvature_r12034

## Research note

# Mod-two geodesic counts have coloring-sensitive two-orbit interactions

Work with an antipodally odd binary coloring of undirected \(Q_n\)-edges, \(n\ge2\). Each antipodal edge orbit \(o=\{e,\bar e\}\) has an independent binary choice \(\epsilon_o\), and the color of either member is an affine expression \(\epsilon_o+b_e\) over \(\mathbb F_2\), with \(b_{\bar e}=1+b_e\). Let \(\mathcal G_n\) be the unoriented full antipodal geodesics (direction-once paths, identified with their reversals). Define the parity of the number of red geodesics
\[
R(\epsilon)=\sum_{\gamma\in\mathcal G_n}\prod_{e\in E(\gamma)}(1+c_e(\epsilon))\in\mathbb F_2.
\tag{PC1}
\]
Every \(\gamma\) uses each original direction once, hence its \(n\) edges belong to different antipodal edge orbits. Thus \(R\) is a multilinear polynomial of degree at most \(n\).

**Marked-orbit finite-difference identity.** For distinct edge orbits \(o_1,\ldots,o_k\), let \(\Delta_o R(\epsilon)=R(\epsilon+\mathbf1_o)+R(\epsilon)\). Then
\[
\boxed{\Delta_{o_1}\cdots\Delta_{o_k}R(\epsilon)
=\sum_{\substack{\gamma\in\mathcal G_n\\o_1,\ldots,o_k\subseteq O(\gamma)}}
\ \prod_{\substack{e\in E(\gamma)\\\operatorname{orb}(e)\notin\{o_1,\ldots,o_k\}}}
(1+c_e(\epsilon))\pmod2.}
\tag{PC2}
\]
In words, the mixed finite difference counts modulo two all unoriented direction-simple antipodal geodesics using one edge from each marked orbit whose other edges are red. This holds for arbitrary nonlinear dependence of the original coloring on cube vertices.

*Proof.* For a path omitting orbit \(o\), its indicator in (PC1) does not depend on \(\epsilon_o\); its finite difference is zero. For a path containing \(o\), the indicator has one factor \(1+\epsilon_o+b_e\), whose finite difference is one. Apply these observations successively for the marked orbits. The distinct-direction condition prevents repeated factors of a single orbit. \(\square\)

**Even-dimensional parity-change certificate.** In \(Q_6\), index directions by \(\mathbb Z/6\mathbb Z\). Start with
\[
c_i(x)=x_{i+1}.
\tag{PC3}
\]
It is well-defined on undirected \(i\)-edges and odd under antipodal complementation. Each direction order \(\pi\in S_6\) has one and only one red root: requiring its \(i\)-edge to be red sets \(x_{i+1}=1\) precisely when direction \(i+1\) appears before \(i\) in \(\pi\). Since \(i\mapsto i+1\) permutes the directions, this determines the six root bits independently. Thus there are \(720\) oriented red geodesics, or \(360\) unoriented red geodesics.

Define two legal antipodally paired orbit flips. Flip \(A\): direction \(i=2\) edges for which the five exterior bits have bits \(0,1\) equal to one and the other three exterior bits zero, together with their complementary exterior pattern. Flip \(B\): direction \(i=5\) edges with all five exterior bits zero or all five one. Each flip complements both members of an antipodal edge orbit, preserving the NORI condition.

Enumerating all \(6!\) direction orders and all \(2^6\) roots gives the following distribution of red roots per fixed direction order:

| Flipped orbits | 0 red roots | 1 red root | 2 red roots | Unoriented red geodesics |
|---|---:|---:|---:|---:|
| none | 0 | 720 | 0 | 360 |
| \(A\) | 28 | 664 | 28 | 360 |
| \(B\) | 126 | 592 | 2 | 298 |
| \(A,B\) | 150 | 542 | 28 | 299 |

The last column is one-half of the sum of red-root counts because reversal pairs every oriented red path with one other orientation of the same undirected path. The counts can be reproduced by the following finite algorithm: loop over \(\pi\in S_6\) and \(x\in\{0,1\}^6\); traverse the directions of \(\pi\), requiring \(c_i(y)=0\) at each current vertex \(y\), and toggle bit \(i\) after each successful edge. Accumulate the number of successful roots per \(\pi\).

Consequently
\[
R(0)=R(\mathbf1_A)=R(\mathbf1_B)=0,\quad
R(\mathbf1_A+\mathbf1_B)=1
\quad(\bmod 2),
\]
so
\[
\boxed{\Delta_A\Delta_B R(0)=1.}
\tag{PC4}
\]
The two single-orbit perturbations leave the original witness-count parity unchanged, whereas their joint perturbation reverses it. By (PC2), the marked-pair red-geodesic count is odd.

**Interpretation and limit.** The parity of unweighted monochromatic geodesic witnesses is not invariant under legal antipodally paired edge-color modifications, even in even cube dimension. In particular it cannot itself be the evaluation of a coloring-independent projective characteristic class such as the already established directional square-curvature classes \([\beta_i]=w_1^2\). This rules out the direct unweighted witness-parity interpretation of those classes. It does not rule out other color-dependent signed/local-index counts, relative obstructions, or an integral descent theorem. The original unrestricted NORI1 statement remains open; all four colorings above possess red geodesics.
