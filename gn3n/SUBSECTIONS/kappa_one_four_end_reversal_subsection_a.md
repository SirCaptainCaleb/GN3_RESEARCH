# kappa_one_four_end_reversal_subsection_a

## Metadata

- ID: kappa_one_four_end_reversal_subsection_a
- Parent Section: kappa_one_four_end_reversal
- Position: 1
- Row version: 1
- Development version: 1
- Composition version: None
- Composition stale: True

## Cold composition

(none yet)

## Development

Assume H has no spanning two-cover and kappa_2(H)=1. Let
H-x=P|Q,
where P=(p_1,...,p_r) and Q=(q_1,...,q_s) are tight paths. Both r and s are at least three: if one component had order at most two, adjoining x gives a Hamiltonian set of order at most three, which together with the other component two-covers H.

Minimum-hole synchronization gives the terminal reversals
(x,p_r,p_{r-1}) and (x,q_s,q_{s-1}) tight.

Use the exact cyclic formulation
pc(H)=min_Z max{1,tau(D_Z)}.
Since H has no two-cover, every spanning cycle Z has tau(D_Z)>=3.

Take the oriented Hamilton cycle
Z_1=(P,Q,x).
Every triple wholly inside P or Q is tight. The only possible defect positions form two separated path components in D_{Z_1}: a component of at most two edges at the P|Q seam and a component of at most three edges at the Q|x|P seam. The first status in the latter component is
(q_{s-1},q_s,x),
which is non-tight because its reverse (x,q_s,q_{s-1}) is tight. If the last status
(x,p_1,p_2)
were tight, the Q|x|P component would have vertex-cover number at most one, while the P|Q component also has vertex-cover number at most one. Then tau(D_{Z_1})<=2, contradiction. Hence
(x,p_1,p_2)
is non-tight, and boundary reversal gives
(p_2,p_1,x)
tight.

Now take
Z_2=(P,x,Q).
Again the two seam clusters have vertex-cover numbers at most one and two. The first status in the three-edge P|x|Q cluster,
(p_{r-1},p_r,x),
is non-tight because (x,p_r,p_{r-1}) is tight. Therefore the last status
(x,q_1,q_2)
must also be non-tight, or tau(D_{Z_2})<=2. Reversal gives
(q_2,q_1,x)
tight.

Thus
(x,p_r,p_{r-1}), (p_2,p_1,x),
(x,q_s,q_{s-1}), (q_2,q_1,x)
are all tight.

This conclusion uses only deletion-distance one, minimum-hole synchronization inside the fixed graph, and the exact cyclic defect-cover identity. It uses neither minimum-counterexample induction nor path-disturbance descent.
