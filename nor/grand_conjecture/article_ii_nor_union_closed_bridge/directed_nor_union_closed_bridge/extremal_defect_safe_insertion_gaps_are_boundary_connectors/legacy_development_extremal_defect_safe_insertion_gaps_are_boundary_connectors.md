# Extremal defect-safe insertion gaps are boundary connectors — preserved pre-item development


## Extremal defect-safe insertion gaps are boundary connectors

Use the triangle-orientation plus defect-vertex decomposition. Let
O=(v_1,...,v_m)
be defect-free, fix a new vertex x, and for 1<=i<m classify the marked vertex of {x,v_i,v_{i+1}} by

L if it is v_i,
R if it is v_{i+1},
X if it is x,
N if there is no mark.

Call this symbol e_i.

For an interior insertion of x between v_i and v_{i+1}, the exact defect-safety criterion is

e_{i-1} != R,   e_i != X,   e_{i+1} != L,

with nonexistent boundary terms omitted. Prepending is safe exactly when e_1 != L, and appending is safe exactly when e_{m-1} != R.

### Proposition: leftmost safe insertion

If e_1 != L, the leftmost safe position is before v_1.

Otherwise let k be the length of the initial L-run:
e_1=...=e_k=L,
with either k=m-1 or e_{k+1} != L.

Then inserting x between v_k and v_{k+1} is defect-safe, and every position strictly to its left is unsafe.

Proof. Prepending is blocked by e_1=L. For i<k, the gap after v_i is blocked by e_{i+1}=L. At i=k, one has e_k=L != X, the preceding symbol when present is L != R, and the following symbol when present is not L. Thus the gap is safe.

### Proposition: rightmost safe insertion

Dually, if e_{m-1} != R, the rightmost safe position is after v_m.

Otherwise let k be the first index of the terminal R-run:
e_k=...=e_{m-1}=R,
with either k=1 or e_{k-1} != R.

Then inserting x between v_k and v_{k+1} is defect-safe, and every position strictly to its right is unsafe.

The proof is the reversed argument.

### Connector interpretation

For every x and every defect-free order O there are canonical extremal safe insertions:

- a left connector determined by the initial L-wall;
- a right connector determined by the terminal R-wall.

Thus the defect field does not create an arbitrary set of admissible insertion positions. It creates a one-dimensional carrier with forced access from both ends. Any failure to insert x while preserving a desired alpha-word property must already fail at both canonical connectors.

If the alpha-word of O is fixed, the orientation signs
s_i=alpha(x,v_i,v_{i+1})
therefore need only be analyzed at these extremal safe positions and along the finite interval between them. A discrete Connector/Hex argument can be sought by labeling safe gaps according to the direction of their orientation failure. A first change from left-type to right-type failure is necessarily local and is a candidate source of the shifted two-circuit / centered-triangle blockers already isolated elsewhere in Article II.

This is not yet a closure theorem: the orientation-failure labels on safe gaps have not been shown to satisfy the needed adjacency rule. The point is that the defect side of that connector construction is now exact and canonical.
