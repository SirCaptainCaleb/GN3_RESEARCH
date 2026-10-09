# Universal genuine-target palettes are exactly cube dominating sets; sharp code compression

Fix n>=4. For a fixed target palette D subseteq Q_n, independent of the edge coloring, define genuine labels L_D(x)=R(x) intersect D. Sharing a label between antipodal roots always supplies a monochromatic antipodal geodesic by one-switch extraction and rotation.

THEOREM (exact universal nonemptiness criterion). The labels L_D(x) are nonempty for every root x and every antipodally odd binary edge coloring if and only if D is a dominating set of the ordinary cube graph. Consequently any such universal fixed palette satisfies
|D| >= ceiling(2^n/(n+1)).

Proof. Every R(x) contains the closed cube neighborhood B_1(x), so domination suffices. Conversely, if D misses B_1(x), prescribe all edges between distance layers 0 and 1 about x to have color 0, and all edges between layers 1 and 2 to have color 1. Give their antipodal edges opposite colors. These prescriptions concern the four distinct layer pairs 0-1, 1-2, (n-2)-(n-1), and (n-1)-n when n>=4, so they are consistent. Extend over remaining antipodal edge orbits arbitrarily. Every monochromatic geodesic from x has length at most one: a first edge has color 0 and every possible second geodesic edge has color 1. Thus R(x)=B_1(x), and L_D(x) is empty. Finally each selected target dominates exactly n+1 vertices, yielding the counting bound.

For n>=5, this lower bound exceeds n. Thus a coloring-independent palette consisting of at most n physical target vertices cannot even guarantee that every root receives a label. Adaptive domination compression remains available and is not covered by this lower bound.

SHARP CONSTRUCTION IN AN INFINITE FAMILY. Let n=2^m-1 with m>=3. Over F_2, let H be the m by n matrix whose columns are the distinct nonzero vectors of F_2^m, and take D=ker H. For every x, its syndrome Hx is zero, or equals exactly one column H_i. Thus x belongs to D or x+e_i belongs to D, respectively. So D dominates Q_n, and each root has a uniquely specified target of D at distance at most one. The matrix has rank m, giving |D|=2^(n-m)=2^n/(n+1), which attains the lower bound. Each row of H has 2^(m-1) ones, an even number; hence the all-ones vector belongs to D. The palette is antipodally invariant and L_D(bar x)=bar L_D(x).

The actual label is the whole set R(x) intersect D, retaining every reachable palette target. The unique distance-at-most-one target only certifies nonemptiness; using that one target alone does not establish a topological coincidence.

Scope. These palettes have nonempty genuine labels and sound overlap extraction. The theorem does not assert that restriction to a fixed palette preserves every overlap already present in the full reachability family. Exact preservation of all intersections is supplied instead by adaptive maximal-neighborhood compression and paired domination folds. A topological forcing theorem for the compressed family is still required.
