# The reversal-linked cube has a middle-label endpoint-or-internal dichotomy

## Statement

Let H be a minimum counterexample and choose u,v,a,x,y,z as in reversal_stable_shell01, so one of (y,u,x,v,z) and (y,v,x,u,z) is a tight Hamiltonian five-path and, with G=H-{u,v}, every state G-S for S subseteq {x,y,z} is non-Hamiltonian with path-cover number two. Then at least one of the following holds: (1) some two-cover of G has x and one of y,z simultaneously as displayed endpoints; (2) two two-covers of G have different unordered support partitions; (3) two Hamilton paths on one common component support of two covers of G exhibit relative-order disagreement; (4) x is internal in every two-cover of G; (5) both y and z are internal in every two-cover of G.

## Body

Apply pc2_square_topcover_normal01 to the full square on labels {x,y}. If it yields simultaneous displayed endpoints, outcome (1) holds. If it yields support-partition disagreement or order disagreement, outcome (2) or (3) holds. Otherwise one of x,y is internal in every two-cover of G.

Apply the same theorem to the square on labels {x,z}. Again, its endpoint outcome gives (1), and its two disagreement outcomes give (2) or (3). If none of (1)-(3) occurs, then one of x,z is internal in every two-cover of G.

If x is internal in every two-cover, outcome (4) holds. Otherwise the first face forces y to be internal in every two-cover and the second face forces z to be internal in every two-cover, giving outcome (5). The reversal and alternating five-path data are inherited unchanged from reversal_stable_shell01.
