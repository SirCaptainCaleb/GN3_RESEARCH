# Audit: the canonical full-permutahedron root map has a trivial central zero — preserved pre-item development

## Development


Audit correction to the preceding full-permutahedron descent-root-map construction.

The vertex formula

R(pi)=sum_{10 descents i}(e_{pi_i}-e_{pi_{i+r}})

is valid, nonzero at every permutation vertex, and satisfies

R(pi^rev)=-R(pi).

However the claimed topological extraction consequence is not useful as stated.

The centered permutahedron has a fixed point under central inversion: its geometric center 0. Any continuous odd extension F on the whole permutahedral ball necessarily satisfies

F(0)=-F(0),

hence F(0)=0.

For the specific barycentric extension in the preceding subsection, this trivial zero is completely explicit. The barycenter vertex associated with the top face P_V is labeled by

|Vert(P_V)|^{-1} sum_pi R(pi)=0,

because permutation vertices pair as pi,pi^rev with opposite root sums.

Thus the degree argument does not force a nontrivial local carrier: it may return only the whole-permutahedron center zero. Expanding that zero gives the tautological global cancellation between reversed orders, with carrier equal to the entire top face. Coxeter-block localization then gives no useful small outside-fixed packet because the top face has one block containing every coordinate.

What remains valid and potentially useful from the construction is:

1. R(pi) is a canonical nonzero no-tie-breaking physical-root label on every bad full order;
2. reversal negates it exactly;
3. on any proper face whose averaged label or affine interpolation vanishes, the zero does expand into a positive dependence of genuine descent roots carried by that proper face.

But a separate argument is required to force a zero on a proper free-antipodal carrier, or to remove/factor out the unavoidable central zero while retaining a nontrivial degree obstruction.

Therefore the full-permutahedron construction does NOT by itself supply the missing global protected carrier/extraction theorem and must not be cited as closure progress without an additional noncentral-zero argument.
