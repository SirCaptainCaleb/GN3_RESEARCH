# Anchored pair orders can miss every complementary red half-sweep

- Stable ID: note_nori_fixed_first_sweep_order_obstruction_r11992
- Author: session_nori_r11992_2
- Primary home: subsection:gauge_critical_switches_and_clustered_witnesses_on_full_paths
- Labels: NORI1, paired-flat, rooted-red-reachability, order-exchange, method-obstruction
- Lifecycle: active
- Epistemic status: proved
- Current version: 1
- Retention: current and at most one previous snapshot
- Created session: session_nori_r11992_2
- Updated session: session_nori_r11992_2
- Disposition: none
- Successor: none

## Related references

- None

## Research note

Let m≥3 and use pair-state bits t_i, i=0,…,m−1. A legal paired-flat coloring has one red direction in pair i selected by f_i(t_{−i}), with f_i(t+1)=1+f_i(t), and traversing this red direction updates t by T_i(t)=t+e_i(1+f_i(t)). For an order π of all pair labels write F_π for the composition of its updates. Two red half-sweeps from the same root have complementary direction supports precisely when F_π(t)+F_ρ(t)=1; this suffices for a red full antipodal geodesic by joining the two arms through their common root.

THEOREM (no universal anchored pair order). For every m≥3 there exists a legal paired-flat coloring of Q_(2m) and a pair order π such that for every root t, every pair-parity fiber and every second order ρ, F_π(t)+F_ρ(t)≠1. The example may have gates independent of pair-parity bits.

PROOF. In three pairs choose f_0=1+t_1, f_1=t_2, f_2=t_1 and π=(0,1,2). Each gate ignores its own pair-state bit and changes under t↦t+111. Thus the corresponding six-cube coloring is legal. Directly applying T_0,T_1,T_2 shows that the output differences F_π(t)+F_ρ(t), listed by ρ, are
  012: (0,0,0);
  021 or 201: (0,1+t_1,1+t_2);
  102 or 120: (1+t_2,0,0);
  210: (t_1+t_2,1+t_1,1+t_2).
None equals (1,1,1). In the last case equality in the last two entries forces t_1=t_2=0 and then the first entry is 0.

For m>3 retain these three gates, and give each new pair j≥3 the gate f_j=t_0. All gates remain independent of their own pair-state bit and odd under global complementation. Choose any full order π whose restriction to {0,1,2} is 012. Gates of the old pairs ignore the new state bits, and the new updates leave old state bits unchanged. Projecting F_π(t)+F_ρ(t)=1 onto the old three bits would yield the forbidden three-pair equality for π|_{0,1,2}=012 and ρ|_{0,1,2}. This is impossible. ∎

SCOPE. This refutes any attempt to prove unrestricted NORI1 by fixing an arbitrary prescribed first pair order and varying only the second order and root. It does not refute the fully existential two-order sweep criterion or NORI1. In the six-cube gadget, for example, orders 021 and 102 from state 000 yield complementary endpoints 001 and 110. The missing implication is still to force some pair of orders and some root in every arbitrary nonlinear legal gate system.
