# Uniform ordered-r-face one-switch facet paths conserve reversed terminal (r−1)-cap polarity

# General ordered-r-face NORI: one-switch facet paths preserve complementary-cap potential

Fix integers 2<=r<n, and a binary coloring of PHYSICAL ORDERED r-dimensional cube faces satisfying the antipodal reversal law
 c(bar F,rev pi)=1-c(F,pi).
Let g∈[n], U=[n]\{g}, and let P be a full U-geodesic from root x to y=x XOR U, with direction word p1,...,p_(n-1). Suppose P's r-face window-color word has at most ONE switch. Assume the global n-dimensional conjectural one-switch conclusion FAILS.

**Theorem.** Every such P has exactly one switch. Write its first window-color block as q and its final block as 1-q. Define the actual ordered-r-face cap labels at root x, for ordered (r-1)-tuples t of distinct directions in U,
 A_t(x;g)=c(F(x;{g} union set(t)),(g,t)).
Then every U-spanning good P obeys
  A_(p1,...,p_(r-1))(x;g)
   = A_(p_(n-1),p_(n-2),...,p_(n-r+1))(x;g)
   = 1-q.
Thus if a single one-switch spanning facet path has UNEQUAL cap values for its initial (r-1)-tail and the REVERSE of its terminal (r-1)-tail, the full n-dimensional one-switch conjecture HOLDS. The cap values are independent of the chosen g-facet (g is a FREE cap direction). For r=3 this is exactly the proved ordered-pair cap conservation theorem.

**Proof.**
If P is monochromatic, appending g introduces only one new ordered-r-face window to its existing constant word, resulting in a full n-edge antipodal one-switch geodesic. Thus under failure P has one switch, and both color blocks nonempty.
Prepending the unused direction g adds a single initial r-window before the original word, with color alpha=A_(p1,...,p_(r-1))(x;g). To prevent a full one-switch geodesic we must have alpha=1-q.
Appending g instead adds a single final r-window after color 1-q, with color gamma=c(F(y;{p_(n-r+1),...,p_(n-1),g}),(p_(n-r+1),...,p_(n-1),g)). To prevent one switch we need gamma=q.
Because y=x XOR U, every exterior coordinate of the two physical faces F(y;{g,p_(n-r+1),...,p_(n-1)}) and F(x;{g,p_(n-r+1),...,p_(n-1)}) is complemented. They are global antipodes of one another. The terminal r-tuple (p_(n-r+1),...,p_(n-1),g) is the REVERSE of (g,p_(n-1),...,p_(n-r+1)). By the active r-face reversal oddness, gamma=1-A_(p_(n-1),...,p_(n-r+1))(x;g). Hence the reverse-last cap equals 1-q, equal to the first cap. QED.

**Rooted cap graph and polarity synchronization.** For fixed projected root on U, build the undirected graph on ordered (r−1)-tuples in U whose edges are witnessed by qualifying facet geodesics P, between P's first r−1 directions and the reverse of its last r−1 directions; witness colors are omitted. Under hypothetical grand failure, every edge has EQUAL endpoint cap labels. Therefore any cross-cap edge with opposite labels certifies grand closure. Two qualifying paths sharing one cap vertex must have the SAME first window-block color, even if their interior direction orders differ or they lie in opposite parallel g-facets. The theorem is a dimension-independent, all-window-arity extraction criterion but does NOT by itself force the requisite cross-cap edge.
