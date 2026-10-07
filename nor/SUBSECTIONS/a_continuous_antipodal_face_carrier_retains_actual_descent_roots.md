# A continuous antipodal face carrier retains actual descent roots

## Metadata

- ID: a_continuous_antipodal_face_carrier_retains_actual_descent_roots
- Parent Section: protected_root_certificates_and_cellular_extraction
- Position: 32
- Row version: 1
- Development version: 1
- Composition version: 1
- Composition stale: False

## Composition

For reversal-odd coordinate labels with every order bad, average all actual 10 dropped/entering-coordinate roots over each proper permutahedron face and extend over barycentric flags. This defines a continuous odd map on the free antipodal boundary. The map is nonzero on every face whose blocks have size at most r, including arbitrary products of small blocks. Any zero expands into a positive dependence of actual roots refining one common face, and a directed cycle localizes in a block of size at least r+1. This removes gap-weight artifacts. No theorem yet forces a zero, and the raw root carrier does not automatically retain protected deletion provenance.

## Development

## A continuous antipodal face carrier retains actual descent roots

Work in the translation-invariant coordinate sector of NOR. Let h be a reversal-odd binary label on ordered r-tuples of distinct coordinates, and assume every full coordinate order has at least two color changes. Every order then contains a 10 transition. This hypothesis is the negation of the coordinate-sector conclusion; no basepoint-dependent claim is made.

Let P be the centered type-A permutahedron. Its boundary has the free involution pi -> pi^rev. A proper face F is an ordered partition B_1|...|B_s with s>=2. Its vertices are precisely the coordinate orders refining that partition.

For every such face form the multiset
\[
\mathcal R_{10}(F)=
\{e_{v_i}-e_{v_{i+r}}:
\pi=(v_1,\ldots,v_n)\text{ refines }F,\ 
h(v_i,\ldots,v_{i+r-1})=1,\ 
h(v_{i+1},\ldots,v_{i+r})=0\}.
\]
Multiplicity records the carrying order and transition. This is a nonempty finite multiset. Define its average g_F and convex hull K_F.

### Theorem

There is a continuous odd piecewise-affine map
\[
G:|\operatorname{sd}\partial P|\longrightarrow W
\]
with the following properties.

1. G(b_F)=g_F at each face barycenter.
2. On a barycentric simplex with flag F_0 subset ... subset F_t, its image lies in K_{F_t}.
3. G is nonzero on the subcomplex consisting of faces whose blocks all have size at most r.
4. Any zero of G yields a positive dependence of actual 10 window-slide roots carried by refinements of one common proper face. A directed cycle in that dependence lies in a single block of size at least r+1.

This avoids the coloring-independent gap-weight zeros of root §30. It does not assert that G has a zero.

### Construction and proof

Set G(b_F)=g_F and extend affinely over every barycentric simplex. The assigned vertex values agree on common simplex faces, so this defines a continuous map.

If H subset F, every order refining H also refines F. Thus R_10(H) is a submultiset of R_10(F), and K_H subset K_F. Convexity proves property 2.

Reversal sends each 10 transition to a 10 transition, while reversing its dropped and entering coordinates. Hence
\[
\mathcal R_{10}(-F)=-\mathcal R_{10}(F),\quad g_{-F}=-g_F.
\]
Barycenters and flags reverse compatibly. The affine extension is therefore odd. Because P is centered and its center is in its interior, the boundary involution is free.

Suppose every block of F has size at most r. Give a coordinate a the midpoint mu(a) of its block's occupied ranks, and put
\[
L_F(e_a-e_b)=\mu(b)-\mu(a).
\]
Every root in R_10(F) joins coordinates exactly r ranks apart in a carrying refinement. They cannot lie in one block. Since the dropped coordinate is earlier, their distinct blocks occur in strictly increasing order. Hence L_F is strictly positive on every root of R_10(F), and on every point of K_F. Property 2 excludes a zero on every simplex contained in F. The union of small-block faces is a subcomplex because taking a face refines blocks. This proves property 3. Normalizing G gives a continuous odd sphere-valued map on that subcomplex.

If G(x)=0, take a barycentric simplex containing x with largest face F. Each g_H contributing with nonzero barycentric coefficient is an average of actual roots in R_10(F). Expanding these averages gives a positive root dependence after zero coefficients are discarded.

Orient e_a-e_b as b -> a. Balance of each coordinate coefficient makes the dependence a nonzero positive circulation, hence supplies a directed cycle. The ordered block index is nonincreasing along every edge. It must be constant along a cycle. All cycle vertices therefore lie in one block B. Each cycle edge has endpoints r ranks apart in a carrying order; its entire r+1-coordinate window union lies in B. Consequently |B|>=r+1. This proves property 4.

### What this does and does not repair

The map carries actual dropped/entering-coordinate roots, rather than shared middle-pair roots multiplied by weights. All convex coefficients at a zero are positive and all carrying orders refine one face. Thus its zero, if forced, has the sign and face compatibility required for physical cycle localization.

For r=3, every product of singleton, doubleton, and tripleton blocks is zero-free. Genuine cancellation must occur in a block of at least four coordinates. An A3 reversal pair can still cancel automatically; root §29 remains a warning that such a local circuit does not imply a good spanning order.

There is no Borsuk--Ulam reason for this single map to vanish: the domain is S^{n-2} and W has dimension n-1. An odd nonvanishing map of these dimensions can exist. A successful next step needs a relative obstruction, an additional compatible label, or a fixed-point correspondence whose solutions give either an actual NOR order or a zero of this physical carrier. Merely adding a second averaged field gives possible signed dependence, not automatically a positive root dependence.

Finally, R_10(F) records actual transitions but does not attach protected deletion witnesses or preserve a common threshold cut. The geometrical carrier theorem establishes sign and face compatibility only. It does not establish witness compatibility or a terminating bridge surgery.
