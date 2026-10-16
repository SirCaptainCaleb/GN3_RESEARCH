# Reader-chain subdivision closes the rooted paired-reader three-nonlinear branch

- Stable ID: note_93f3f3c67ccccb85170dd72a
- Author: unspecified; session provenance retained
- Primary home: subsection:paired_direction_involutions_and_geodesic_endpoint_matchings
- Labels: NORI1, three-nonlinear, all-dimensional, closure, reader-chain, subdivision
- Lifecycle: active
- Epistemic status: proved
- Current version: 1
- Retention: current and at most one previous snapshot
- Created session: session_nori_r10003_3
- Updated session: session_nori_r10003_3
- Disposition: none
- Successor: none

## Related references

- note:note_79706c96899a6e835f8f9378

## Research note

THEOREM (arbitrary-depth rooted reader-chain closure). Let c be a balanced antipodally odd cube coloring with exceptional nonunary directions E={a,b,c} and every other direction unary. Suppose s_a+s_b+s_c=X_a+X_b+X_p, where X_i=epsilon_i*(-1)^x_i, p is outside E, and the three unmatched unary directions u_a,u_b,u_p have signed rules -X_a,-X_b,-X_p after cancelling opposing same-reader pairs. Let T0={a,b,c,u_a,u_b,u_p}. Suppose p belongs to a complementary same-reader unary pair P0, and repeatedly following the common reader of each pair through the containing paired vertex reaches T0, without first entering a reader cycle. Then c has a monochromatic full antipodal geodesic in every dimension, regardless of the nonlinear selector or all other unary reader cycles.

PROOF. We use the previously proved eight-pivot theorem, which gives for any r in T0 and any sign delta a full zero core geodesic on T0 union P0 if P0 reads r. The exceptional edges in its twelve explicit witnesses are guaranteed positive solely by the balance saturation conditions: s_a is positive when X_b=X_p=+, s_b when X_a=X_p=+, and s_c when X_a=X_b=X_p=+. These guarantees hold under arbitrary changes of the other vertex bits, so all such paths are selector-robust.

READER-SUBDIVISION LEMMA. Suppose a selector-robust red full path includes a complementary unary pair {v,w} whose opposite signed rules read a direction r already used by the path. Since both pair edges are red and their signed functions are opposite, the unique r-step lies strictly between the v- and w-steps. Introduce a new complementary unary pair {j,j'} with signed rules eta*chi_r and -eta*chi_r, and replace the old pair rules by opposite signed unary characters reading j instead of r. Insert j and j' on opposite sides immediately adjacent to the r-step, choosing the side for j where eta*chi_r is positive and the opposite side for j'. Both insertions occur between v and w because r is between them. Choose the initial bit j so that the first of v,w has positive signed color; its complement is then positive after j is crossed. The other old unary rules are unaffected. The selector-robust exceptional edges remain positive because the inserted moves do not alter X_a,X_b,X_p and their positivity criteria ignore arbitrary additional bits. Thus the new longer core also has a selector-robust red full path, with the pair {j,j'} straddling its reader r.

Let the chain of paired nodes be P0 -> P1 -> ... -> Pm -> T0, with Pk reading a member of P(k+1) and Pm reading a direction r in T0. Begin with the eight-pivot witness for P0 artificially reading r. Apply the subdivision lemma to P0, introducing P1 with reader r and redirecting P0 to its required reader inside P1. Apply it next to P1, introducing P2 with reader r and redirecting P1 to its required reader, and continue. After the last insertion, every paired node in the chain has its required unary reader, including Pm reading r. All exceptional steps remain positive independently of their nonlinear selector and the frozen bits outside this core. The construction therefore gives a red full geodesic on the enlarged core for EVERY frozen exterior assignment. The uniform frozen-core theorem then absorbs all other unary directions, including internally cyclic components, and yields a red full antipodal geodesic on the whole Q_n. QED.

The statement extends the finite eight-pivot reader theorem to arbitrarily long functional reader chains, without bounding the cube dimension or the selector complexity. In the two-internal/one-external reader pattern, the remaining paired-reader configuration outside this theorem is one where the reader chain of p enters a cycle disjoint from the six-pivot core (along with configurations where p is itself unmatched, addressed separately by a concurrent six-pivot result). No claim is made here for the internally cyclic reader-chain case.
