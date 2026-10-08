# Neighboring shared bridges have a sharp orientation and deletion fork

## Composition

(none yet)

## Development

Use the neighboring-cut notation from [[a_shared_bridge_at_neighboring_cuts_exposes_four_new_repair_labels]]:
A={x,y,c_1,c_2}, r=c_{j+1}, v=c_{j+2}, s=c_{j+3},
T=(c_3,...,c_j), U=(c_N,...,c_{j+4}), with j=u or u+1 in a monotone corridor 1^u0^v_status, u,v_status>=4.

Suppose v bridges both neighboring tests and neither test supplies a two-cover. Thus A+r and A+s are non-Hamiltonian, and every (A-w)+r+s, w in A, is Hamiltonian. By [[one_shared_bridge_orientation_at_neighboring_cuts_closes_automatically]], the first bridge cannot be (T,v,U,s); it must be (U,s,v,T).

If the second bridge has orientation (T,r,v,U), then either the span has a two-cover or the four-set
B=(A-{c_2}) union {s}
is non-Hamiltonian.

Proof. The original corridor triple (c_2,c_3,c_4) is tight. Therefore (c_2,T,r,v,U) is tight whenever (T,r,v,U) is. Its complement is exactly B. If B is Hamiltonian these two paths cover the span. QED.

In the residual case B is non-Hamiltonian while A+s is a non-Hamiltonian five-set. The non-Hamiltonian-five-set theorem allows at most one non-Hamiltonian four-subset, so A is Hamiltonian. Together with the already known bad extensions A+r and A+s, this activates [[two_bad_five_extensions_adjacent_four01]]: among the four-sets {r,s,a,b}, a,b in A, at least two are Hamiltonian and their pairs {a,b} share a vertex. This provides overlapping Hamiltonian four-supports, not an automatic attachment to the remaining tails.

There is also a position restriction. The second forward bridge contains the triple
(c_j,c_{j+1},c_{j+2}).
At j=u+1 this has status zero, so that orientation is impossible. It can occur only at the earlier neighboring-cut pair j=u. Thus the later pair j=u+1, if it has the same bridge in both tests and fails to close, must have reverse orientations in both tests.

The remaining reverse/reverse case is
(U,s,v,T) and (U,v,T,r).
Its contiguous subpath R=(U,v,T) is tight and covers the complement of S=A+r+s. Hence this branch has one long tight path beside a six-vertex packet, rather than two unjoined tails. Its resulting absorption conditions are stated in [[reverse_shared_bridges_reduce_to_one_tight_path_and_a_six_vertex_packet]].

These conclusions are conditional on the shared bridge existing. They do not guarantee its presence, rule out the Hamiltonian-common-core residue, or supply global protected-carrier compatibility.
