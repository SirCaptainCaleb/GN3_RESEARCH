# Minimum counterexample makes the all-refinements root carrier zero-free on every proper permutahedron face

## Composition

(none yet)

## Development

## Minimum counterexample makes the all-refinements root carrier zero-free on every proper permutahedron face

Work in ternary arity in a minimum-coordinate counterexample. Let G be the all-refinements actual-10-root carrier of root §42 on the centered permutahedron.

Root §42 proves zero-freeness on faces whose Coxeter blocks have size at most five by using a local rotation lemma to find, inside each block, an internal order with no 10 descent.

In a minimum counterexample the same argument extends to EVERY proper face.

### Internal descent-free orders from minimality

Let F=B_1|...|B_s be any proper permutahedron face. Since F is proper, s>=2, so every block satisfies

|B_j|<n.

By minimum-coordinate counterexamplehood, the ternary NOR statement holds on each proper coordinate subset B_j. Therefore B_j admits a spanning coordinate order whose ternary word is one-change,

0^*1^*,

and hence contains no internal 10 descent.

Choose such an order independently inside every block and concatenate the blocks in the fixed face order.

### A crossing 10 root must exist

Suppose, for contradiction, that no order refining F carries an actual 10 slide root whose endpoints lie in distinct blocks.

In the particular concatenated order chosen above:
- no internal block contains a 10 descent, by construction;
- any 10 descent crossing a block boundary would have a slide root with endpoints in distinct blocks.

By the supposition, the latter cannot occur.

Hence the full concatenated order has no 10 descent anywhere. Its binary ternary word is therefore monotone nondecreasing, i.e.

0^*1^*,

which is a spanning NOR-good full order. This contradicts counterexamplehood.

Therefore every proper face F carries at least one actual 10 root crossing distinct blocks.

### Strict inward separation

Use exactly the inward face functional from root §42:

L_F(e_a-e_b)=mu_F(b)-mu_F(a),

where mu_F is constant on each ordered block and strictly increases with block order.

Every slide root refining F has L_F>=0, and every crossing root has L_F>0.

Since the all-refinements face vector g_F averages every actual 10 occurrence with positive coefficient and at least one crossing occurrence exists,

L_F(g_F)>0.

The barycentric-flag interpolation argument of root §42 then gives

L_F(G(x))>0

for every point x whose largest supporting face is the proper face F.

Thus:

### Theorem

In a minimum-coordinate ternary counterexample, the all-refinements actual-root carrier G is nonzero on the ENTIRE boundary of the centered permutahedron.

Moreover on each proper face it lies strictly in the same inward face-normal halfspace as the inward radial field -x. Hence the boundary normalization of G is odd-homotopic to the inward radial map.

### Topological consequence

The old block-size-at-most-five restriction is unnecessary once minimum-counterexample analysis is authorized.

Any zero of this particular carrier must lie over the full top-dimensional permutahedron face.

Likewise, for the distance-lifted all-descent switch-prism carrier whose physical component is this same G, no zero can project to a proper permutahedron face. Every unresolved zero projects to the full permutahedron interior.

### Important limitation

This does NOT solve the extraction problem.

The full permutahedron center is fixed by reversal, and any globally odd equivariant extension may have the familiar tautological central zero coming from averaging reversal pairs. The theorem removes all proper-face zeros but does not prove that an interior zero is nontrivial or witness-compatible.

Its value is localization: under minimum counterexamplehood, all fixed-point obstruction is forced into the top cell. Any useful blow-up, Sperner refinement, or center-resolution argument may therefore work entirely at the full-face center while treating the whole proper boundary as a certified zero-free inward carrier.
