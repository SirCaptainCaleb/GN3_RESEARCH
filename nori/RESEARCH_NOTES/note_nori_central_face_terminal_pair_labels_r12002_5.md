# Terminal-pair reachability labels on the central Freudenthal subdivision

- Stable ID: note_nori_central_face_terminal_pair_labels_r12002_5
- Author: session_nori_r12002_5
- Primary home: subsection:central_freudenthal_subdivision_and_the_all_root_geodesic_chamber_sphere
- Labels: NORI1, topology, labeling, reachability
- Lifecycle: active
- Epistemic status: proposed
- Current version: 2
- Retention: current and at most one previous snapshot
- Created session: session_nori_r12002_5
- Updated session: session_nori_r12002_5
- Disposition: none
- Successor: none

## Related references

- note:note_nori_coupled_reachability_cuts_endpoint_squares_r12002_5
- subsection:complementary_monochromatic_path_pairs_as_common_full_rank_certificates

## Research note

Let c be an antipodally odd binary edge coloring of Q_n. In the central Freudenthal subdivision, each vertex is the barycenter b_F of a nonempty original cube face F. Let S(F) be its free direction set. For y in V(F), write y^{S(F)} for the opposite corner within F and define
a_F^epsilon(y)=1 iff there is a color-epsilon geodesic from y^{S(F)} to y inside F.
For a vertex face the empty path gives a_F^0=a_F^1=1.

The proposed face label is the table y -> (a_F^0(y),a_F^1(y)). It is intrinsic to F, so it agrees in all small cubes meeting at b_F. Reversal gives a_F^epsilon(y)=a_F^epsilon(y^{S(F)}); the table is therefore indexed by unordered opposite-corner pairs. Geometric antipodality gives a_{bar F}^epsilon(bar y)=a_F^{1-epsilon}(y). Each entry has four possible states: both colors, only red, only blue, or neither.

For i in S(F), let F_i^-(y) be the facet of F fixing bit i to 1-y_i. Then the following recurrence holds:
a_F^epsilon(y) = OR_{i in S(F)} [ a_{F_i^-(y)}^epsilon(y^i) AND 1_{c(yy^i)=epsilon} ].
Indeed every spanning geodesic has a last direction i; deleting its last edge gives the indicated spanning geodesic in F_i^-(y). Conversely append yy^i. The direction sets of the prefix and final edge are disjoint. The starting corner of the prefix is y^{S(F)}, so both implications preserve the endpoints. No affine or independence assumption on c is used.

For a central chamber (x,pi), with S_k the first k directions, F_k the face freeing S_k at x, and u_k=x xor 1_{S_k}, one has
a_{F_k}^epsilon(u_k)=r_x^epsilon(S_k).
Thus restricting the table labels to the chamber-selected corners recovers rooted geodesic reachability. Selecting a value at b_F by one incident chamber alone would depend on its hidden root; the table retains all those choices and identifies each with its reversed prefix.

If there is no monochromatic full antipodal geodesic, every table entry on every face of dimension n-1 or n is the state 'neither'. For dimension n-1, a monochromatic spanning path extends at one end in the missing direction because the two endpoint edges are antipodal. Rank-zero tables have state 'both', and every rank-one table has precisely its edge color. These boundary conditions and the recurrence hold simultaneously in the same original coloring.

A simple scalarization h(F)=sum_{y in V(F)}(a_F^0(y)-a_F^1(y)) is antipodally odd, but already vanishes at every rank-zero face and, under the no-path hypothesis, at every facet. Thus a zero of this scalarization carries no spanning-path conclusion.

Open labeling question: can the table-valued face data and the incidence recurrence yield a signed labeling or a relative obstruction whose forced flag has a_F^epsilon(u)=1 at full rank? The recurrence guarantees path decoding if such a flag is forced. No topological forcing theorem is presently established. The table labeling is a candidate for creative work on the user's central subdivision and connects directly with the coupled-reachability-cut note.

## Coupling complementary faces at one corner

For x in Q_n and S subset [n], let F(x,S) be the face through x with free directions S, and write A_epsilon(x,S)=a_{F(x,S)}^epsilon(x). Put T=[n] minus S. The endpoint-reversal and antipodal identities give
A_epsilon(x xor 1_S,S)=A_epsilon(x,S),
A_epsilon(x xor 1_T,S)=A_{1-epsilon}(x,S).
The second identity follows by applying global antipodality and then reversal within the S-face. Thus a red witness at x has red, blue, blue counterparts at x xor 1_S, x xor 1_T, bar x, respectively.

Under absence of every full monochromatic antipodal geodesic, one has the simultaneous exclusions
A_epsilon(x,S) A_delta(x,T)=0
for every x,S and every pair of colors epsilon,delta.

Proof. Reverse the first monochromatic arm and follow the second, obtaining a direction-simple full path x xor 1_S -> x -> x xor 1_T. If the two colors agree, this is already monochromatic. If they differ, follow the second arm from x and then the reverse antipodal image of the first arm. Both pieces have color delta, use disjoint supports T and S, and join x to bar x. This also handles an empty arm by selecting its freely available color.

This is the established complementary-arm criterion expressed in the face tables. It strengthens the list of simultaneous constraints used in this labeling investigation beyond the extreme-rank conditions. The two candidate faces meet only at x and their free direction sets partition [n]. Their barycenters are generally incomparable in the face poset, so they are not vertices of one simplex of the central subdivision. A labeling argument must therefore encode this complementary incidence as well as the nested incidences inside a chamber.

Put U(x,S)=max(A_0(x,S),A_1(x,S)). Then
U(x,S)=U(x xor 1_S,S)=U(x xor 1_T,S)=U(bar x,S),
U(x,S)+U(x,T)<=1.
For a fixed nonempty proper S, these predicates descend to the four-root orbits generated by flipping S and T. On each orbit, success on the S-face excludes success on every complementary T-face. Geometry antipodality preserves U; it acts on the color-resolved labels by exchanging their two entries.

A first antisymmetric support label is h_x(S)=U(x,S)-U(x,T). It changes sign under support complementation S <-> T, while geometric antipodality preserves it. Its zero under the no-path hypothesis means both complementary faces are unreachable from the indicated corner. Hence a forced zero of h alone supplies no desired path; the two involutions have distinct roles.

Current continuation target: build a carrier or relative intersection argument for complementary face pairs sharing a corner, compatible with the nested-face recurrence and the two endpoint-extension embeddings. A useful forced intersection must certify A_epsilon(x,S)=A_delta(x,T)=1. No index bound or intersection theorem producing this conclusion has been proved. The simple scalar and face-selector attempts leave this cross-face incidence unresolved.
