# Two selected same-end replacements force four tight endpoint triples

## Statement

Let H be a minimum counterexample and let H-b=P|Q be a deletion cover with displayed paths P and Q, each of order at least three. Choose an endpoint a of P and an endpoint c of Q that occupy the same displayed end. Suppose H-a has a deletion cover obtained by replacing a with b at that same end of P while leaving Q unchanged, and H-c has a deletion cover obtained by replacing c with b at that same end of Q while leaving P unchanged. Let u and v be the neighbors of a and c on P and Q. If a,c are terminal, then (b,a,u),(a,b,u),(b,c,v),(c,b,v) are tight. If a,c are initial, then (u,a,b),(u,b,a),(v,c,b),(v,b,c) are tight.

## Body

Treat the terminal-terminal case; the initial-initial case is symmetric. Write P=(p_0,...,u,a) and let R_P=(p_0,...,u). The original deletion cover H-b contains the tight path (R_P,a), while the same-end replacement cover of H-a contains (R_P,b). Let R=(p_1,...,u), so p_0 is a left extender of R and a,b are two right extenders. Apply 7b9f6ae39813 in its symmetric form to R with right extenders a,b and left extender p_0. If H[V(P) union {b}] were Hamiltonian, a Hamilton path on that support together with Q would be a spanning two-cover of H, impossible. Hence the non-Hamiltonian alternative holds, giving both (b,a,u) and (a,b,u) tight. Apply the identical argument to Q and its same-end replacement at c, obtaining both (b,c,v) and (c,b,v) tight. No cyclic rotation or path reversal is used.
