# The fully certified NORI vertices occupy at least 3/(n+2) of the cube, by width-three antipodal separation

THEOREM (NEW DENSITY LOWER BOUND FOR COMPLETELY FOUR-WINDOW-CERTIFIED ROOTS). Let n>=5 and color actual physical ordered three-faces of Q_n with active NORI antipodal-reversal oddness. Let M be the matching of DEAD physical cube edges traversed by no genuinely monochromatic 4-edge directed geodesic. Let D be the set of cube vertices incident to dead edges (so |D|=2|M|), and U=Q_n\D the FULLY CERTIFIED vertices, each incident physical edge lying on at least one actual mono4 path. The strengthened universal dead-rigidity radius-three theorem implies a thickness-three antipodal separator: EVERY full antipodal directed n-geodesic starting in D encounters at least THREE CONSECUTIVE vertices of U.
In contrast, every full antipodal geodesic starting in U automatically contains at least TWO U vertices—its root x and its antipode bar x—because U is antipodally invariant. Choose the starting root uniformly among all 2^n cube vertices and the full coordinate permutation uniformly among n!. Let N(P) be the number of U vertices visited along the resulting full antipodal geodesic, counting both endpoints. Conditioning on the root type gives
 E[N(P)] >= (3|D|+2|U|)/2^n.
But each of the n+1 vertex positions of a uniform rooted full geodesic is UNIFORMLY distributed over Q_n, so exactly E[N(P)]=(n+1)|U|/2^n. Comparing and substituting |D|=2^n−|U| yields
 (n+1)|U| >=3(2^n−|U|)+2|U|,
 and hence
    BOXED |U| >= ceil(3*2^n/(n+2)).
Because U is antipodally paired, the sharper integral form is |U| >=2 ceil(3*2^(n−1)/(n+2)). Equivalently, the number of physical dead edges is bounded above by
    |M| <= 2^(n−1)*(n−1)/(n+2),
with the appropriate integer/even rounding.
This improves the earlier antipodal one-point hitting-set density bound |U|>=ceil(2^n/(n+1)) and is derived from a genuine three-vertex physical-separator constraint, not an abstract topological index or heuristic random choice. Every U vertex has n individually witnessed monochromatic-four-geodesic incident edges, so the bound guarantees an unconditional DIMENSION-DEPENDENT MINIMUM AMOUNT OF CERTIFIED LOCAL PATH GEOMETRY in any NORI coloring.
SCOPE. The three certified consecutive vertices on a path do not guarantee that their separate local mono4 certificates have matching ordered two-direction memories or one color. The theorem does not prove a full <=1-switch antipodal path; it quantitatively strengthens the physical substrate for a possible root-coupled connector construction.
