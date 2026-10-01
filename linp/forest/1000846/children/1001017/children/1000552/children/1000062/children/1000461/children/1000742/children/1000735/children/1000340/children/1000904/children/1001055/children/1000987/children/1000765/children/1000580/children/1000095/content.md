# Near-saturated terminal-single families force linear balanced endpoint-lens packets in every uniformity

## Statement

Retain the setup of 80e2e6b25cab. Thus H is a finite linear r-graph, r>=3; P is a maximum p-edge endpoint path ending at v, with
  U=V(P)\last(P);
Q is a rank-q ascending anchor path ending at v, q<p; and F is any family of D distinct edges through v such that each f in F has at least two contacts with the anchor precursor R=V(Q)\h but exactly one off-v contact
  c_f in U
with P.

Then the vertices c_f, f in F, are pairwise distinct. For each f, choose any maximum endpoint path P_f ending at c_f. The host path P and P_f contain a clean balanced elementary endpoint lens whose host-side endpoint is c_f.

Hence P supports D balanced endpoint-lens states attached at D distinct host vertices.

In particular, in the near-saturated terminal-single setting of 80e2e6b25cab, if
  t>=J_max(q)-tau,
then one may take
  D >= floor(((r-1)(q-1)-alpha_r(q-3))/2)-tau
    = ((2r-1)/8)q-O_r(1)-tau.
Thus near equality in the arbitrary-r fixed-entrance bound, together with terminal-singleness on a maximum p-path, forces a linear packet of distinct balanced endpoint lenses on that one host path in every uniformity.

For globally unpaid signature-(0,1,...,1) ascending edges, terminal-singleness is automatic on the chosen endpoint path. This gives a uniformity-independent geometric replacement for the r=3 anchor-to-maximum crossing-matching step.

## Body

Distinct members f,f' of F both contain v. By linearity,
  (f\{v}) intersect (f'\{v})=emptyset.
Since c_f belongs to f\{v}, the vertices c_f are pairwise distinct.

Now fix f. The path P is maximum at its endpoint v, and c_f is a vertex of P distinct from v. Let P_f be any maximum endpoint path ending at c_f. Apply the certified endpoint-lens theorem b35b0fd4e4cd with Q there equal to the host path P and y=c_f. It gives a second common vertex z_f such that the relevant z_f-to-c_f pieces of P and P_f form a clean elementary lens with equal edge lengths. Thus c_f is the attachment vertex of a balanced endpoint lens on P.

Because the c_f are pairwise distinct, these are D distinct attachment states, regardless of how the auxiliary sides P_f overlap one another.

The quantitative near-saturation lower bound for D is exactly the switching-family estimate in 80e2e6b25cab. Finally, a globally unpaid signature-(0,1,...,1) edge has contact multiplicity one at every terminal on the globally chosen maximum endpoint paths, so the terminal-single hypothesis required there is automatic.
