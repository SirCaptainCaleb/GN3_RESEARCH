# Correction: adjacent-simple-root minimum-hole faces flip sign or enter the bounded interface — preserved pre-item development

## Development

## Correction: adjacent-simple-root transport flips the root sign

Let X be a minimum two-cover deletion set of order k, and let
H-X=P|Q, |P|=r, |Q|=r+1,
be a Psi-minimal complementary two-cover in the adjacent-simple-root branch. Write P=(p_1,...,p_r), Q=(q_1,...,q_{r+1}).

The previous version incorrectly claimed that a neutral endpoint transfer produces a balanced cover. This is impossible by parity: |V(H)-X|=2r+1 is odd.

### 1. A neutral endpoint transfer flips the simple root

If P union {q_1} is Hamiltonian, then together with the inherited path (q_2,...,q_{r+1}) it gives a new two-cover of H-X with component orders
(r+1)|r.
Thus the exact root changes from
e_{r-1}-e_r
to
e_r-e_{r-1}.
The same holds with q_{r+1} in place of q_1. A transfer therefore negates the adjacent simple root; it does not create a zero-root face.

### 2. If neither endpoint transfers, the bounded four-component conclusion remains valid

Assume H[P union {q_1}] and H[P union {q_{r+1}}] are non-Hamiltonian. Then neither endpoint can prepend or append to the displayed Hamilton path P, so boundary antisymmetry gives
h(p_2,p_1,q)=1 and h(q,p_r,p_{r-1})=1
for q in {q_1,q_{r+1}}.

Every hole x in X satisfies the same two end-reversal relations by minimum-hole four-end synchronization. Partition
R=X union {q_1,q_{r+1}}
by the fixed pair {p_1,p_r}:
R_+={z:h(p_1,z,p_r)=1}, R_-={z:h(p_r,z,p_1)=1}.
Two vertices in the same class complete {p_1,p_r} to a Hamiltonian four-set.

If q_1,q_{r+1} lie in the same class, K_0={p_1,p_r,q_1,q_{r+1}} is Hamiltonian. Together with the inherited interiors (p_2,...,p_{r-1}) and (q_2,...,q_r), this gives a spanning three-cover of H-X with an all-old Hamiltonian four-component.

If q_1,q_{r+1} lie in opposite classes, every hole x agrees with exactly one of them, say q(x), and K_x={p_1,p_r,q(x),x} is Hamiltonian. In G_x=H-(X-{x}), minimum-hole heredity gives kappa_2(G_x)=1, while K_x, the interior of P, and Q with q(x) removed give a spanning three-cover of G_x. Hence this branch enters the bounded deletion-distance-one four-component interface.

Therefore the valid dichotomy is:

**Simple-root transport dichotomy.** A Psi-normalized minimum-hole face of adjacent-simple-root type either admits a neutral endpoint transfer to another minimum-hole face with the opposite adjacent simple root, or it already lies in the bounded four-component/deletion-distance-one interface.

Consequently the unbounded adjacent-simple-root regime, if it exists, is a finite transport system whose states carry the two root signs and whose neutral endpoint-transfer edges interchange those signs. Zero root is not obtained by cardinality transfer alone.
