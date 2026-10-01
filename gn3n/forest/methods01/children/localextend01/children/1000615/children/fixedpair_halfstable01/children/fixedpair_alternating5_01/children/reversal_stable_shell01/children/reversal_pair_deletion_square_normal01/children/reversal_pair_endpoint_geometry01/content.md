# An exposed reversed pair yields disagreement, a bounded Hamiltonian window, or a same-component reverse cross

## Statement

Let H be a minimum counterexample and let u,v,a,x be supplied by reversal_pair_deletion_square_normal01. Suppose its simultaneous-endpoint outcome occurs, and let H-x=P|Q be a displayed two-cover in which u and v are both displayed endpoints. Then at least one of the following holds: (1) H has relative-order disagreement between the original tight path containing the ordered edge (u,v) and a component of P|Q; (2) H contains a proper Hamiltonian set W of order four or five containing x,u,v and neighboring endpoint data from the cover, with H-W non-Hamiltonian of path-cover number two; (3) u and v are the two displayed endpoints of one component, that component orders u before v, and (v,x,u) is tight.

## Body

Let R be the tight three-vertex path from reversal_pair_deletion_square_normal01, so R is either (u,x,v) or (v,x,u). Some tight path S contains the ordered edge (u,v), hence orders u before v.

If u,v are the two endpoints of one component P and P orders v before u, then P and S give relative-order disagreement, yielding (1). Otherwise write P=(p_0,...,p_m) with p_0=u,p_m=v. If (u,x,v) is tight, then for m=2 the hook (p_1,u,x) gives the tight four-path (p_1,u,x,v), while for m>=3 theorem 1000084 gives the canonical tight five-path (p_1,u,x,v,p_{m-1}); in either case its proper Hamiltonian support has non-Hamiltonian pc2 complement, yielding (2). If instead (v,x,u) is tight, this is the residual same-component reverse cross (3).

Suppose u,v lie on different components. If they are a facing pair, theorem 1000305 directly gives a positioned Hamiltonian support of order four or five containing x,u,v with non-Hamiltonian pc2 complement, regardless of which of (u,x,v),(v,x,u) is tight. If they occupy the same displayed end, endpoint hooks plus the known middle triple give a tight four-path: for initial-initial endpoints either (p_1,u,x,v) or (q_1,v,x,u), and for terminal-terminal endpoints either (u,x,v,q_{s-1}) or (v,x,u,p_{m-1}). Thus every different-component placement yields (2), leaving only the same-component reverse cross in (3).