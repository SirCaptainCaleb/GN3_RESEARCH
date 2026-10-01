# Large entrance-prefix excess converts into early triangle-or-superlevel certificate mass

## Statement

Let P=(g_1,...,g_p) be a maximum p-edge path with last vertex v. Let F be a family of distinct selected switching edges
  f={x_f,v,u_f}
from the local D+Y certificate system of 9586a4d2317f / c8d14f7306ab at v. Assume that for every f in F the unique off-v contact with P is its entrance x_f. Let a_f be the first host-edge index containing x_f, and put
  sigma_f=phi(x_f)-a_f.

Fix s>=0 and let
  F_{>s}={f in F:sigma_f>s}.
Then the contact cells of F_{>s} contain at least ceil(|F_{>s}|/2) distinct interior cells. Every such cell lies strictly before host output index
  phi(f)-s+1 <= p-s,
and each such certificate cell contributes at least one of the following:
(1) a doubly occupied switcher cell, hence a linear switcher triangle;
(2) a paid cell whose standard output edge is contained in V_{>=p}.

More concretely, if m=|F_{>s}|, then there are at least ceil(m/2) distinct early certificate cells, each carrying a triangle or a distinct superlevel output edge. Thus a linear family of entrance-retained switchers with linear host-prefix excess forces linear early progress-or-obstruction mass on the common host.

## Body

For f in F write q_f=phi(f). Since f is ascending with unique entrance x_f,
  phi(x_f)=q_f-1.
If sigma_f>s, then
  q_f-1-a_f>s,
so
  a_f <= q_f-s-2.                                      (1)

Each selected switcher has its unique precursor contact in one two-slot interior cell
  C_i={b_i,z_i},
and both possible vertices of C_i have first host occurrence i. Hence for f in F_{>s}, its cell index is
  i=a_f<=q_f-s-2.
The standard output of C_i is g_{i+2}, so its output index satisfies
  i+2<=q_f-s<=p-1-s,
because q_f<p in the strict-gap application. In particular the output lies in the early host prefix, certainly no later than g_{p-s}.

A cell has only two possible contact vertices. Distinct edges through v have distinct non-v contact vertices by linearity. Therefore at most two members of F occupy one cell, and the m members of F_{>s} occupy at least ceil(m/2) distinct cells.

Now use the defining D+Y certificate selection. Every selected switcher witnesses one of the two local currencies:
- a D-unit comes from a doubly occupied cell; its two switchers together with the corresponding host edge form the certified linear switcher triangle;
- a Y-unit comes from a paid occupied cell. By the potential-cut characterization 39d0d99258db, the standard output edge of a paid cell lies entirely in V_{>=p}.
Distinct occupied cells have distinct standard output edges.

Thus every distinct cell represented by F_{>s} carries at least one of the two displayed outcomes, and there are at least ceil(m/2) such cells. The argument uses only the local selected-certificate semantics, ascendingness, strict edge-rank gap q_f<p for the final early-index bound, and linearity. It does not use source-cleanliness or terminal-singleness at the opposite terminal.