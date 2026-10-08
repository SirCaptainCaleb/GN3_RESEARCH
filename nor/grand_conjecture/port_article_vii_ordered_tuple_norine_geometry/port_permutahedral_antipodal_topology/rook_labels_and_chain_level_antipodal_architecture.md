# Wu--Yang rook labels and chain-level antipodal architecture

## Composition


Wu--Yang prove Norine's original non-geodesic conjecture by reducing a counterexample to an antipodally symmetric rook labeling, sending \((a,b)\) to \(e_a-e_b\), passing cubical chains through the Freudenthal subdivision, and then mapping rook galleries to spherical positive-cone chains. The resulting equivariant augmentation-preserving chain map is impossible by an algebraic chain-level Borsuk--Ulam/Dold obstruction. The reusable novelty is that coherent chain-valued data suffice; no actual continuous equivariant map is required.


## Development


Hehui Wu and Ningyuan Yang proved Norine's original non-geodesic antipodal-coloring conjecture in 2026 using a chain-level Borsuk--Ulam obstruction.

The proof architecture relevant to NOR is:

1. a hypothetical counterexample is compressed to a rook labeling \(q(x)=(a,b)\), with antipodality swapping \(a,b\);
2. adjacent cube vertices change at most one rook coordinate;
3. \((a,b)\) is sent to the type-\(A\) root \(e_a-e_b\);
4. the cubical boundary is passed through its Freudenthal subdivision, so maximal simplices become monotone rook galleries;
5. gallery root data are sent to spherical positive-cone sections in a subdivision-invariant polyhedral chain complex;
6. the resulting equivariant augmentation-preserving chain map is ruled out by a purely algebraic chain-level Borsuk--Ulam/Dold obstruction.

The especially reusable point is that no continuous equivariant map is required. Coherent chain-valued data, together with equivariance, augmentation, dimension, and the antipodal norm-operator identity, are enough for the contradiction.

For NOR, this suggests looking for a structured directed label system extracted from failure of the one-change geodesic target, then realizing that system on Freudenthal/Coxeter gallery chains.
