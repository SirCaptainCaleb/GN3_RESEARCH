# Cubical Tucker neutral simplex + nested support labels forces full geodesic; exact antipodal equivariance gap

# Key extraction insight: cubical Tucker neutrality plus CHAIN labels forces a full geodesic

Let n>=2. For a finite set of n-bit labels lambda(V(sigma)) subset {0,1}^n identify each label with a coordinate support S subseteq[n].

**Theorem 1 (exact chain-neutrality lemma).** Suppose the supports appearing as labels on ONE simplex sigma are totally ordered by inclusion (a Boolean-lattice chain). If sigma is NEUTRAL in the cubical Tucker sense -- for each coordinate i both 0 and 1 occur among its labels -- then the MINIMUM support in sigma is empty and the MAXIMUM support is [n]. Thus lambda(sigma) contains the EXACT complementary pair (0^n,1^n).

Proof. Let A and B be minimum and maximum. Because every label T obeys A subseteq T subseteq B, coordinate i can vary among labels only if i notin A and i in B. Neutrality for all i yields A=empty and B=[n]. QED.

**Theorem 2 (conditional, immediately closing the edge proving ground).** Suppose a triangulation T of an n-dimensional ball has antipodally symmetric boundary and a labeling lambda:V(T)->{0,1}^n such that:
(i) lambda(-v)=complement(lambda(v)) on the boundary;
(ii) for each simplex sigma, its support labels form a chain under inclusion;
(iii) whenever a simplex has labels empty and full, those labels are certified by a single ACTUAL one-color cube-geodesic prefix chain sharing a physical root (rather than two unrelated paths).
Then there is a monochromatic antipodal geodesic: cubical Tucker (Grant-Ma Theorem 1.9) supplies a neutral simplex, Theorem 1 supplies both extreme labels, and (iii) extracts the witnessed full geodesic. If (iii) instead certifies an at-most-one-switch edge-geodesic chain, antipodally odd edge coloring rotates that into a monochromatic antipodal geodesic.

For full NORI, replacing the word-color condition in (iii) by at most one change in the ORDERED-THREE-FACE window word likewise gives the grand conclusion as soon as this hypothetical carrier is established. Thus one can obtain exact complementary support labels from the EXISTING cubical Tucker conclusion, without needing a new "fully complementary edge" theorem.

**Theorem 3 (the actual barrier is antipodal equivariance).** On the natural barycentric subdivision sd(Q_n), a vertex corresponding to a face H has support label S(H)=free-coordinate set. Every simplex is a nested face chain, so its S(H) labels form an inclusion chain. But physical antipodality maps H to bar H with the SAME free-coordinate support: S(bar H)=S(H), not complement S(H). Therefore lambda(-v)=lambda(v), not complement lambda(v), so this *correctly chain-compatible* labeling does NOT meet cubical Tucker's antipodal boundary requirement. The user's root-progress state space E_q(x,S) has the analogous issue: physical oddness maps E_q(x,S) to E_(1-q)(bar x,S), again preserving S. The formal involution beta(x,S)=(bar x,[n]\S) would supply complemented labels, but its preservation of ACTUAL reachability states is precisely an additional nontrivial connector assertion, not a consequence of color oddness.

**Topological interpretation.** Earlier arbitrary-bit-string Tucker obstruction showed that neutral simplices need not contain complementary pairs: e.g. 000,011,101 in Q_3. This obstruction disappears entirely for geodesic PREFIX CHAINS, since they have nesting. The missing NORI theorem can now be stated sharply: construct an n-ball (or an appropriately indexed equivariant carrier) of actual path-certified root-progress states whose boundary involution sends SUPPORTS to COMPLEMENTS while each simplicial flag keeps labels nested and path-compatible. If it exists, known Grant–Ma cubical Tucker yields full closure. No such carrier construction has yet been proved, so this is a CONDITIONAL extraction theorem, not an unconditional solution.
