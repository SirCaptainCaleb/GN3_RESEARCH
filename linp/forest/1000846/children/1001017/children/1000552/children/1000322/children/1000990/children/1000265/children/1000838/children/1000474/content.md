# Exact-density nonspecial obstructions have average endpoint potential d plus five-sixths

## Statement

Let H be a P_ell-free linear 3-graph with exact density |E(H)|=d|V(H)|, where d=floor(2ell/3), and suppose the contact-snake setup yields the unpaid 0-1-1 transition count U as in bbcfa1f0ff1d. Then the average endpoint potential satisfies
(1/n) sum_v phi(v) >= d+5/6.
Equivalently,
A_phi=sum_v((ell-1)-phi(v)) <= (ell-1-d-5/6)n.
This bound is residue-independent despite the residue-dependent transition surplus gamma_ell.

## Body

From bbcfa1f0ff1d,
U >= gamma_ell n + 2A_phi
and
2U <= (2ell-5)n - 2A_phi.
The second inequality gives
U <= (ell-5/2)n - A_phi.
Combining,
gamma_ell n + 2A_phi
 <= (ell-5/2)n - A_phi,
so
3A_phi <= (ell-5/2-gamma_ell)n.

Hence
(1/n)sum_v phi(v)
 = ell-1 - A_phi/n
 >= ell-1 - (ell-5/2-gamma_ell)/3
 = (2ell+gamma_ell-1/2)/3.

Now evaluate by residue.

If ell=3r, then d=2r and gamma_ell=3, so
(2ell+gamma_ell-1/2)/3
=(6r+5/2)/3
=2r+5/6=d+5/6.

If ell=3r+1, then d=2r and gamma_ell=1, giving again
(6r+2+1-1/2)/3
=2r+5/6=d+5/6.

If ell=3r+2, then d=2r+1 and gamma_ell=2, so
(6r+4+2-1/2)/3
=2r+11/6
=d+5/6.

Thus the same lower bound d+5/6 holds in all three residue classes.

This says exact-density equality obstructions are globally high-potential: although phi(v) can range up to ell-1, their mean already lies strictly above the Turan coefficient d by a fixed additive amount. Combined with the fact that every unpaid 0-1-1 edge strictly raises potential, this turns the equality layer into a finite-height acyclic branching problem with very little low-level mass available.
