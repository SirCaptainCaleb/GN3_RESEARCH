# Mixed antipodal face blockers and red witness edges at a globally unavoidable paired square

- Stable ID: note_nori_strict_square_mixed_face_blockers_r11992_6
- Author: unspecified; session provenance retained
- Primary home: subsection:obstruction_compatibility_and_a_programme_for_nori1_closure
- Labels: NORI1, paired-flat, square-switch, global-unavoidability, blocked-faces, red-witness-edges
- Lifecycle: active
- Epistemic status: proved
- Current version: 1
- Retention: current and at most one previous snapshot
- Created session: session_nori_r11992_6
- Updated session: session_nori_r11992_6
- Disposition: none
- Successor: none

## Related references

- subsection:gauge_critical_switches_and_clustered_witnesses_on_full_paths
- article:nori_article_xvii_sustained_research_and_unrestricted_forcing

## Research note

# Mixed-face blocking at a globally unavoidable paired square

Let n=2m with m>=2 and group the cube directions as P_i={2i,2i+1}. Let G be a legal paired-flat coloring: the two edge colors in P_i at any vertex are f_i and 1+f_i, where f_i depends only on bits outside P_i and satisfies f_i(bar z)=1+f_i(z). Red is color 0.

Fix an antipodally paired square orbit S supported in P_0. For each j!=0, the two squares of S have restricted P_j vertex words a_j and bar a_j. Let B_j={0,1}^2\{a_j,bar a_j}, and let F(j,t)={x:x|_(P_j)=t} for t in B_j.

**Theorem (simultaneous mixed-face blockers and witness edges).** Suppose every red full antipodal geodesic of G meets S. Then, for every j!=0 and t in B_j, the (n-2)-face F(j,t) admits neither a red nor a blue spanning geodesic. All these obstructed faces inherit their colors from the same G; faces with distinct j intersect in (n-4)-faces.

If G has a red full antipodal geodesic P, then for all but at most one j!=0, P contains a red edge entirely within F(j,t) for some t in B_j. Therefore one common red witness supplies edges in at least m-2 different pairs of obstructed faces. Their membership in pairwise intersections is not asserted.

**Proof.** Suppose a red spanning geodesic Q exists in F(j,t), from x to y. One P_j-direction a is red at x. The oddness of f_j across all directions outside P_j makes the other P_j-direction b red at y. Prepend the red a-edge at x and append the red b-edge at y. The result is a red spanning antipodal geodesic using every original direction once. Its middle portion Q avoids S, since t is outside the two P_j states appearing in S; the added edges avoid S since they have directions in P_j. This contradicts global hitting. A blue spanning geodesic in F(j,t) has an antipodal red image in F(j,bar t), which is similarly impossible. Intersections of faces fixing different direction pairs are (n-4)-cubes.

For the witness assertion, project a red spanning antipodal geodesic P to the two bits in P_j. They change twice and visit three of the four possible words. The two P_j steps cannot be consecutive: after a red P_j step, the other member of P_j remains blue because f_j ignores its own pair bits. If the initial word belongs to {a_j,bar a_j}, then the intermediate word lies in B_j; at least one step of another pair occurs between the two P_j steps, providing a red edge inside an obstructed face. If the initial word belongs to B_j, so does the final word; a red edge appears within an obstructed face unless the two P_j steps are the first and last steps of P. At most one j has this exceptional placement. QED.

**Scope and gap.** At a hypothetical strict good-to-bad paired-square boundary, red hitting is established. Hence this theorem produces compatible blocked (n-2)-faces and weak red-edge anchors without imposing affine hypotheses. Previously established anchored face-capacity arguments require specific anchor placements and a quantitative overlap/surplus inequality. Neither follows here. A remaining forcing step must align the anchors with those face-capacity hypotheses, or use the simultaneous blocked faces through a different inequality.
