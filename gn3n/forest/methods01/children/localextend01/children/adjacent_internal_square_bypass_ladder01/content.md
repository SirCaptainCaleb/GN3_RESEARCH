# An adjacent universally-internal square pair has a three-state local bypass ladder

## Statement


Let G be a boundary tournament and let x,y be distinct vertices such that all four states
G, G-x, G-y, G-{x,y}
are non-Hamiltonian with path-cover number two. Suppose x and y are internal in every two-cover of G.

Fix a displayed two-cover
P|Q
of G in which x,y are consecutive on P, and write
P=(A,x,y,B),
where A and B are nonempty inherited tight paths.

Then the following hold.

(1) In every two-cover of G-x, relative to the three nonempty inherited classes
V(A) | ( {y} union V(B) ) | V(Q),
there is at least one cross-class ordinary edge. If there is exactly one, it joins V(A) to {y} union V(B), and the other component has support exactly V(Q).

(2) In every two-cover of G-y, relative to
( V(A) union {x} ) | V(B) | V(Q),
there is at least one cross-class ordinary edge. If there is exactly one, it joins V(A) union {x} to V(B), and the other component has support exactly V(Q).

(3) In every two-cover of G-{x,y}, relative to
V(A) | V(B) | V(Q),
there is at least one cross-class ordinary edge. If there is exactly one, it joins V(A) to V(B), and the other component has support exactly V(Q).

Thus across the three lower states of the full square, every minimum-crossing cover bypasses the deleted position locally while leaving the opposite top component Q intact:
A <-> (yB), (Ax) <-> B, and A <-> B, respectively.


## Body


Each displayed partition in the statement consists of three nonempty Hamiltonian classes. Hence any two-cover of the corresponding lower state has at least one ordinary edge joining distinct classes: if a two-cover had no such edge, its two components could occupy at most two of the three nonempty classes.

For (1), let T be a two-cover of G-x with exactly one cross-class edge. Equality in the three-class transition count means each class occurs as one contiguous T-block: one component merges exactly two classes and the other component is supported exactly on the third.

Suppose the merged pair were A and Q, leaving {y} union B as the isolated component. Replace that isolated component by the inherited tight path (y,B). The path (x,y,B) is then tight, being a terminal segment of the original P. Together with the unchanged A-union-Q component, this gives a two-cover of G in which x is a displayed endpoint, contradicting universal internality of x.

Suppose instead the merged pair were ({y} union B) and Q, leaving A isolated. Replace the isolated component by the inherited path A. Then (A,x) is a tight path, being a prefix of P (vacuously so when |A|=1). Together with the unchanged ({y} union B)-union-Q component, this gives a two-cover of G in which x is again a displayed endpoint. Thus both merges involving Q are impossible. The unique equality merge must be A with {y} union B, leaving Q intact. This proves (1).

For (2), the argument is symmetric. A one-crossing cover of G-y has three intact class-blocks. If it merges (A union {x}) with Q and leaves B isolated, replace B by its inherited order and use the tight path (y,B); this gives a two-cover of G with y as an endpoint. If it merges B with Q and leaves A union {x} isolated, replace that isolated component by the inherited path (A,x) and append y, obtaining the tight path (A,x,y) and again exposing y as an endpoint. Hence the only equality merge is (A union {x}) with B, leaving Q intact.

For (3), a one-crossing cover of G-{x,y} likewise has one merged pair and one isolated class. If it merges A with Q and leaves B isolated, replacing B by its inherited path and restoring (x,y,B) produces a two-cover of G with x as an endpoint. If it merges B with Q and leaves A isolated, replacing A by its inherited path and restoring (A,x,y) produces a two-cover of G with y as an endpoint. Therefore the unique equality merge is A with B, leaving Q intact.

These are precisely the three stated local bypasses.
