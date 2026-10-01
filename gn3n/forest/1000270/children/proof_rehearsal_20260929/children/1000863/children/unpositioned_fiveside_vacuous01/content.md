# An unpositioned Hamiltonian five-side does not consume the bounded-square obstruction

## Statement


In the bounded-square setting of 1000863, suppose the top two-cover is
P|Q with P=(L,y,M,z,R),
where y,z are internal on P and M is nonempty.

Then the bare conclusion
"there exists a proper Hamiltonian five-set W whose complement has path-cover number two"
is automatic before using any lower-square crossing data.

Indeed P has order at least five, so any five consecutive vertices of P form a Hamiltonian five-set; by minimum-counterexample calculus its complement is non-Hamiltonian with path-cover number two.

Therefore a five-side branch can serve as genuine obstruction consumption only if it retains additional positioning information, such as prescribed local crossing/reversal vertices, a prescribed fixed core, or an ordered attachment condition. Mere existence of some Hamiltonian five-set is not a discriminating outcome in this setting.


## Body


Because y and z are internal on the displayed path P and the middle segment M is nonempty, each of L,M,R is nonempty. Hence
|P| >= |L|+1+|M|+1+|R| >= 5.
Choose any five consecutive vertices of the tight path P. Their induced subtournament is Hamiltonian, witnessed by that displayed five-vertex subpath.

This five-set is proper because a minimum counterexample has order greater than ten. By minimum-counterexample calculus, its complement has path-cover number at most two. The complement cannot be Hamiltonian: otherwise the Hamiltonian five-set and a Hamilton path on its complement would be a spanning two-cover of H. Hence the complement is non-Hamiltonian with path-cover number exactly two.

No property of a two-cover of G-{y,z}, no crossing edge, and no order/reversal information is used. Thus an unpositioned five-side disjunct is automatically satisfied and cannot certify progress on the bounded crossing. A useful replacement must encode which local obstruction vertices are retained. The fixed-two-core lifting lemma fixed_two_core_triple_lift01 supplies one systematic way to retain any prescribed local triple while entering a Hamiltonian five-side.
