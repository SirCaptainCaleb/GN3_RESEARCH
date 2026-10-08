# Two-window root synchronization and explicit Q7 forcing-table obstruction

TWO-WINDOW ROOT-SYNCHRONIZATION CRITERION AND THE Q7 TABLE HOLONOMY OBSTRUCTION.

Fix two complete coordinate orders p,q. Suppose ordered triples T=(a,b,c) and U=(d,e,f) occur consecutively in both orders, in identical orientation. For each external direction z outside both triples, let t_p(T,z) in {0,1} indicate that z occurs BEFORE the T window in p; similarly define t_p(U,z), t_q(T,z),t_q(U,z). Let x and y be the two starting vertices. The physical fixed z-bit at a window T is x_z XOR t_p(T,z) for path p, and y_z XOR t_q(T,z) for path q.

THEOREM. There exist starting z-bits x_z,y_z making both actual ordered faces T and U coincide at coordinate z if and only if
 t_p(T,z) XOR t_p(U,z) = t_q(T,z) XOR t_q(U,z).
When this equality holds, one chooses y_z=x_z XOR t_p(T,z) XOR t_q(T,z). The statement extends independently over every common external coordinate, and to k designated shared windows by requiring the same relative prefix parity for every pair. The criterion does NOT require NORI symmetry.

PROOF. Equality of physical exterior z-bits for T gives x_z XOR y_z=t_p(T,z) XOR t_q(T,z). Equality for U gives the same with U. These two linear equations are simultaneously solvable precisely when their right-hand sides agree. QED.

EXACT TWO-ROW OBSTRUCTION TO THE EXISTING COORDINATE-ONLY Q7 FORCING TABLE. The certificate in Item nori_seven_coordinate_only_closure_from_facet_transfer_20261008 uses both direction orders
 p=(b,c,d,a,g,f,e), q=(b,c,d,e,a,g,f)
and identifies the ordered triples T=(b,c,d) and U=(a,g,f) across these rows. The direction e is exterior to both triples. In p, e follows BOTH windows, so t_p(T,e)=t_p(U,e)=0. In q, e follows T but precedes U, so t_q(T,e)=0 and t_q(U,e)=1. Hence the synchronization equation reads 0=1, impossible. Explicitly, to match the T-face one needs x_e=y_e; to match the U-face one needs x_e=1 XOR y_e.

This is a four-constraint holonomy certificate proving that these two specific rows cannot simultaneously reuse both ordered faces as identical actual faces in arbitrary face-dependent NORI. Coordinate-only triple labels suppress exterior dependence and therefore allow their equality, explaining why the original Q7 forcing table is valid precisely in that restricted setting.

RESEARCH CONSEQUENCE. An attempted all-root face-dependent forcing table must use window comparisons obeying the signed prefix-parity cycle equations. A path exchange that changes whether an exterior coordinate lies between two compared windows creates a nonzero obstruction, unless one can exploit sensitivity to that exterior coordinate to produce a new good path or a valid alternative witness. Root matching and color forcing must be designed together. This is a structural barrier to verbatim table lifting, NOT a proof that every alternative forcing table fails.
