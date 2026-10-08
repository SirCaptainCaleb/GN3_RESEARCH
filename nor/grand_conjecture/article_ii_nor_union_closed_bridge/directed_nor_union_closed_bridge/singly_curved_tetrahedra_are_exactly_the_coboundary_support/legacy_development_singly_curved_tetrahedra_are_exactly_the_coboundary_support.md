# Singly curved tetrahedra are exactly the coboundary support — preserved pre-item development

## Singly curved tetrahedra are exactly the coboundary support

Fix a global linear order on (V). Encode the alternating triangle orientation by an unordered face bit
[
f({a,b,c})=alpha(a,b,c)
]
when (a<b<c). Ordered values of (alpha) are recovered by adding permutation parity.

For a four-set
[
Q={0,1,2,3},
]
write
[
A=f(012),quad B=f(013),quad C=f(023),quad D=f(123).
]
Define its mod-2 tetrahedral coboundary
[
(delta f)(Q)=Aoplus Boplus Coplus D.
]

From the link-curvature classification, a tetrahedron is:
- singly curved exactly when one of its four face bits differs from the other three;
- fully curved when the face pattern is a (2)-(2) split of the form (A=C
e B=D) up to relabeling;
- otherwise flat.

Therefore:

### Theorem
[
(delta f)(Q)=1
quadLongleftrightarrowquad
Q	ext{ has exactly one curved pivot}.
]

Indeed odd face parity on four bits means a (3)-(1) split, which is precisely the singly-curved case. Flat and fully-curved tetrahedra both have even face parity.

### Corollary: five-set parity conservation

For every five-set (Wsubseteq V),
[
igoplus_{substack{Qsubset W\|Q|=4}} (delta f)(Q)=0.
]
Equivalently, the number of singly-curved tetrahedra among the five 4-faces of (W) is even.

This is simply (delta^2 f=0): each triangle of (W) occurs in exactly two tetrahedral faces, so all triangle bits cancel mod (2).

### Interpretation

The local failure of pivot-link transitivity has two qualitatively different pieces.

1. **Coboundary curvature:** singly-curved tetrahedra, detected exactly by (delta f). These defects satisfy an automatic parity conservation law on every 5-set.
2. **Even curvature:** fully-curved tetrahedra, invisible to (delta f), where all four pivot links are cyclic.

Thus the pure-orientation obstruction has a natural two-level decomposition. The singly-curved part is not arbitrary marked data; it is the support of a genuine simplicial coboundary. Any connector/Sperner formulation that works on simplex faces should exploit this conservation law rather than labeling tetrahedra independently.
