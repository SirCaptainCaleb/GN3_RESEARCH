# The pure cycle residue forces a genuine reversed pair or a complement endpoint hook

## Statement

Let H be a minimum counterexample and let C=(u_0,...,u_{r-1}) be a proper vertex-simple tight cycle, with indices modulo r. Put K=H-V(C) and choose any displayed two-cover A|B of K. Fix a cycle edge u_i u_{i+1}. Then at least one of the following holds:

(1) some tight triple of H contains the consecutive pair (u_{i+1},u_i), genuinely reversing the cycle edge u_i u_{i+1};

(2) for every non-singleton displayed component R=(r_0,...,r_m) of A|B, the reverse endpoint hook (u_i,r_m,r_{m-1}) is tight.

Thus the pure-cycle branch of minimal order disagreement always localizes to nonvacuous tight-triple reversal data: either directly on the chosen cycle edge, or on the terminal edge of every nontrivial component of a two-cover of the cycle complement.

## Body

Assume outcome (1) fails. Let w be any vertex distinct from u_i,u_{i+1}. Since no tight triple contains (u_{i+1},u_i) consecutively, both ordered triples
(w,u_{i+1},u_i) and (u_{i+1},u_i,w)
are non-tight. By boundary reversal antisymmetry their reverses
(u_i,u_{i+1},w) and (w,u_i,u_{i+1})
are tight. Hence the cycle edge u_i u_{i+1} is universally two-sided extendable: every exterior vertex w extends it on either side.

Now let R=(r_0,...,r_m), m>=1, be either non-singleton component of the displayed complement cover A|B, and let S denote the other component. Open the tight cycle at the cut u_{i-1}|u_i:
P_C=(u_i,u_{i+1},...,u_{i-1}).
By universal two-sided extension,
(r_m,u_i,u_{i+1})
is tight.

If (r_{m-1},r_m,u_i) were also tight, then concatenating R with P_C would give a tight Hamilton path on V(R) union V(C): the first cross-boundary triple would be (r_{m-1},r_m,u_i), the second would be (r_m,u_i,u_{i+1}), and all later triples are inherited from the opened cycle. Together with the unchanged path S this would be a spanning two-cover of H, impossible.

Therefore (r_{m-1},r_m,u_i) is non-tight. Boundary reversal antisymmetry gives
(u_i,r_m,r_{m-1})
tight, which is exactly the claimed reverse hook on the terminal edge of R.

The argument applies independently to every non-singleton component of A|B. No two-vertex path is used as reversal evidence.