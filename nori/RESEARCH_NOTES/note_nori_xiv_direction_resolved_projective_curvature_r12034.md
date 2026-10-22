# Direction-resolved projective square curvature in every dimension

- Stable ID: note_nori_xiv_direction_resolved_projective_curvature_r12034
- Author: session_nori_r12034_1
- Primary home: subsection:projective_square_curvature_and_the_antipodal_exchange_disk_identity
- Labels: NORI1, topology, proved
- Lifecycle: active
- Epistemic status: proved
- Current version: 2
- Retention: current and at most one previous snapshot
- Created session: session_nori_r12034_1
- Updated session: session_nori_r12035_1
- Disposition: none
- Successor: none

## Related references

- None

## Research note

For n>=3 let B be the boundary of the n-cube and Y=B/tau=RP^(n-1). Given an antipodally odd edge coloring c, let b_i be the 1-cochain equal to c on edges of direction i and zero elsewhere. Its differential beta_i=db_i is antipodally invariant and closed; on an (i,j)-square it equals Delta_j c_i and it vanishes on other squares. Let Sigma_P be the canonical exchange disk of any full antipodal geodesic P, established in the associated manuscript: boundary Sigma_P=P+tau P, with one (i,j)-square for each unordered pair. Stokes gives <beta_i,Sigma_P>=<b_i,P+tau P>=c(e_i(P))+c(tau e_i(P))=1, for EVERY direction i, on the SAME disk. Since the projected Sigma_P generates H_2(Y;F2), each descended beta_i represents u^2 (u=w_1 of the double cover) IN EVERY DIMENSION n>=3. Consequently the cup product of k distinct directional beta classes equals u^(2k), nonzero whenever 2k<=n-1. At least ceil(n/2) squares on every canonical disk are sensitive in at least one free direction. The total curvature kappa=sum_i beta_i has class (n mod2)u^2, recovering the known parity-dependent theorem. This yields color-dependent nontrivial degree-two classes in even dimensions, where total curvature is cohomologically zero. No geodesic forcing or decoding from these cup classes has been established.

## Bounded-support repair obstruction and curvature decoupling

Let P be a full antipodal geodesic with twisted color word w and let delta be the least cyclic spacing between its odd-numbered seam positions. Permuting a contiguous cyclic interval of ell<delta successive dimensions, while fixing all other cyclic positions, cannot decrease its twisted seam count D. Choose a root immediately before the affected interval. All original edges outside this interval are unchanged, and the only affected seam positions are the ell+1 boundaries around and within it. They contain at most one original seam. Their seam count has a fixed parity, determined by the two unchanged exterior edge colors, so a new count cannot be smaller. Root slides preserve D and simply move the chosen cut.

For arbitrarily large n=3m with m>=3 this has a full-class realization whose sensitive squares never cross the three runs. Partition [n]=A union B union C into consecutive blocks of size m and set pi=(1,...,n). Let sigma be any fixed-point-free cyclic permutation preserving each block. Put q_i=1 on B and q_i=0 elsewhere, and p_i=1 if sigma(i) precedes i in pi. Define the original undirected edge coloring by c_i(x)=x_(sigma(i)) + p_i + q_i modulo two. Since sigma(i)!=i, this is well-defined on i-edges; because sigma(i) is a single other bit, antipodality complements every edge color. At root 0 and order pi the color word is 0^m 1^m 0^m, giving D=3 and cyclic seam spacing m. No reordering of fewer than m contiguous directions can reduce D, even after choosing another cyclic cut of the same projective geodesic.

For every square of dimensions i,j the directional sensitivity Delta_j c_i is one iff j=sigma(i). Thus the direction-resolved sensitivity digraph on EVERY exchange disk is the disjoint union of the three directed sigma-cycles, entirely inside A,B,C. Every directional projective curvature class beta_i remains the nonzero class u^2, and every product allowed by dimension remains nonzero. In particular these cohomological obligations alone do not impose a sensitivity connection between any two seam runs.

Nevertheless this legal coloring has a red full geodesic of order pi rooted at x=1_B: for each i its color in that order equals x_(sigma(i))+q_i=0. Hence a globally successful coloring can contain an arbitrarily wide locally stable three-seam geodesic, with all directional curvature contained within its runs. The necessary repair uses a different root or a nonlocal exchange, and cannot follow from the individual projective curvature classes, their cup products, and bounded-width variations around that geodesic alone.

This is a limitation of such local forcing mechanisms. A theorem exploiting global minimality over all roots and all orders, or jointly witnessed root transfer, remains open.
