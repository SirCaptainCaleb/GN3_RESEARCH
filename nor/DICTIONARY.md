## Coloring Symmetries

antipodal complement-reversal: For an ordered cube-vertex window W=(X_0,...,X_r), define J(W)=(bar X_r,...,bar X_0), where bar X=V\X. J is an involution. An odd window coloring satisfies chi(J(W))=1-chi(W).
  Note: This combines vertex complementation and reversal of the window. It differs from complementation alone C(W)=(bar X_0,...,bar X_r), and from reversal alone R(W)=(X_r,...,X_0).

antipodal vertex coloring: A vertex coloring c of the cube Q_V=2^V is antipodally odd if c(V\A)=1-c(A) for every A subset of V.
  Note: Its involution is vertex complementation A -> V\A. This is the N_1 symmetry, and does not by itself define an odd coordinate-tuple label.

antipodal window coloring: A window coloring is odd under complementation alone if chi(bar X_0,...,bar X_r)=1-chi(X_0,...,X_r).
  Note: State complementation alone explicitly; this condition differs from the NOR antipodal complement-reversal rule. A coloring invariant under every cube translation cannot be odd under complementation alone.

odd coloring: A binary coloring c on a domain D equipped with an involution iota is odd with respect to iota if c(iota(x))=1-c(x) for every x in D. In sign notation epsilon:D -> {-1,+1}, the same condition is epsilon(iota(x))=-epsilon(x).
  Note: Always name the domain and involution. Oddness is not a property of a coloring alone. A fixed point of iota prevents such a binary coloring.

reversal-odd coordinate coloring: A binary coloring h of ordered r-tuples of distinct coordinates is reversal-odd if h(v_r,...,v_1)=1-h(v_1,...,v_r).
  Note: Specify coordinate arity r. For r=1, reversal fixes every tuple, so no such binary coloring exists on a nonempty domain. The r=0 domain also has a fixed point.

reversal-odd vertex-window coloring: A coloring of ordered cube-vertex windows is reversal-odd if chi(X_r,...,X_0)=1-chi(X_0,...,X_r).
  Note: The entries here are cube vertices, not coordinate directions. For a one-vertex window reversal is the identity, so binary reversal oddness is impossible.

## Nor Definitions

basepoint-dependent window coloring: A coloring of geodesic windows may be written chi(A;v_1,...,v_r), where A is the initial cube vertex and v_1,...,v_r are the flipped coordinates. It is basepoint dependent if some translation changes its value.
  Note: Writing an arbitrary window coloring in these coordinates does not make it translation invariant. Results for coordinate labels h cannot automatically be applied to basepoint-dependent colorings.

cube translation: For B subset of V, the cube translation tau_B sends A to A symmetric-difference B. It acts on a vertex window by applying tau_B to each vertex.
  Note: Vertex complementation is tau_V. Translation preserves the ordered list of flipped coordinate directions.

k (NOR index): The NOR index k is the arity of the colored ordered tuple of consecutive cube vertices. An N_k local object is (X_0,...,X_{k-1}), containing k cube vertices and k-1 cube steps.
  Note: Examples: k=1 colors vertices; k=2 colors edges; k=3 colors three consecutive cube vertices; k=4 colors four consecutive cube vertices and is the level containing the GN3 coordinate-triple model. Reserve k for this meaning throughout NOR.

k-tuple window: An ordered tuple (X_0,...,X_{k-1}) of k consecutive vertices of a cube geodesic. It contains k-1 successive cube edges and k-1 distinct flipped coordinate directions.
  Note: This is the local colored object of N_k.

N_k: The NOR conjecture for binary colorings of ordered k-tuples (X_0,...,X_{k-1}) of consecutive cube vertices, with the project's antipodal complement-reversal rule. N_k asks for an antipodal geodesic whose sliding k-tuple color word changes at most once.
  Note: k is tuple arity. Therefore N_1 is the vertex-coloring level, N_2 the edge-coloring level, N_3 the three-vertex/two-step level, and N_4 the four-vertex/three-step level containing GN3. If translation invariance gives a coordinate label h(v_1,...,v_r), then r=k-1 and that label belongs to N_{r+1}.

translation-invariant coordinate label: For a translation-invariant N_k coloring, a k-tuple window has r=k-1 flipped coordinate directions v_1,...,v_r and may be represented as chi(X_0,...,X_r)=h(v_1,...,v_r).
  Note: The arity of h is r=k-1. Never use the arity of h as the NOR index. In particular a ternary coordinate label h(u,v,w) belongs to N_4. Under the NOR antipodal complement-reversal rule, h must be reversal-odd. For r=1 this is impossible on a nonempty domain; the directed coordinate sector must not be conflated with the full basepoint-dependent N_2 model.

translation-invariant window coloring: A window coloring chi is translation invariant if chi(X_0 symmetric-difference B,...,X_r symmetric-difference B)=chi(X_0,...,X_r) for every B subset of V.
  Note: On geodesic windows this is equivalent to dependence only on the ordered r distinct flipped coordinates. Under this hypothesis, antipodal complement-reversal oddness is equivalent to reversal oddness of the coordinate label h.

## Paths And Color Words

antipodal geodesic: A cube path from A to bar A that flips each coordinate of V once, in some order.
  Note: A is arbitrary. The pole-to-pole geodesics, from the empty set to V or conversely, are a subclass; a claim for them alone is weaker than a claim for every antipodal geodesic.

color change: A color change in a color word (c_0,...,c_m) is an index i with c_i != c_{i+1}. The number of changes is the number of such indices.
  Note: A one-change word has at most one change and includes a constant word. Oddness of the coloring is a symmetry condition, not a bound on changes along a path.

pole-to-pole geodesic: An antipodal geodesic whose endpoints are the empty set and V.
  Note: The poles depend on the chosen presentation Q_V=2^V. Translating a pole-to-pole path gives other antipodal geodesics, but its color word need not be preserved unless the coloring is translation invariant.

window color word: For a cube path (X_0,...,X_n) and a coloring of k-vertex windows, the window color word is chi(X_i,...,X_{i+k-1}) for i=0,...,n-k+1, when n+1 >= k.
  Note: At k=1 this is a vertex color word; at k=2 it is an ordered-edge color word. State which local objects are colored.

## Prohibited

exact [prohibited]: 
  Note: Do not use exact as a technical modifier. State the precise property, equivalence, or equality directly instead.

memory [prohibited]: 
  Note: Use uniformity, k, Norine order, or arity according to context.
