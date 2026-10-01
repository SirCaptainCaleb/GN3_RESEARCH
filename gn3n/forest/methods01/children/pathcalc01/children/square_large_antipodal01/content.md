# Above order seventeen every two-label square has coherent endpoints, cover disagreement, or universal facing cross triples

## Statement

Let H be a minimum counterexample of order n>=18. Let D be a Hamiltonian four-set, let d,e be distinct vertices outside D, put K=H-(D union {d,e}), and suppose K, K+d, K+e, and K+d+e are non-Hamiltonian with path-cover number two. Then at least one of the following holds: (1) some two-cover F of K+d+e has d and e as endpoints, so F,F-d,F-e,F-{d,e} form a coherent endpoint square; (2) two two-covers of K+d+e have different support partitions or exhibit order disagreement on a common path support; (3) a three-cover of H arising from a Hamiltonian five-set admits strict quadratic-potential descent, or H has order disagreement; (4) after possibly interchanging d,e, the label d is internal in every two-cover of K+d+e and, for every two-cover P=(p_0,...,p_m)|Q=(q_0,...,q_s) of K+e, both (p_m,d,q_0) and (q_s,d,p_0) are tight. In (4) both path orders are at least three; if |P|=3, then Q+p is non-Hamiltonian for every p in P, and symmetrically for Q. The decrease in (3) is measured from the newly specified three-cover, not from an arbitrary earlier extremal cover.

## Body

Apply square_topcover_normal01. Its coherent-endpoint or support/order-disagreement alternatives give (1) or (2). Otherwise, after interchanging d,e if necessary, d is internal in every two-cover of G=K+d+e. Apply square_permanent_internal_hooks01 v2 to G and any two-cover P|Q of G-d=K+e. This gives both path orders at least three, the whole-support nonextension assertions when a path has order three, and the two explicit facing-triple alternatives.

If either five-vertex path in those alternatives occurs, its support W is proper. Minimum-counterexample calculus gives pc(H-W)=2. Applying ham5_large_escape01 to W and a chosen two-cover of H-W gives (3). Otherwise both cross triples in (4) are tight. Since P|Q was arbitrary, the conclusion is universal over all two-covers of K+e.

Outcome (3) is measured from the newly specified three-cover. It does not by itself imply descent from a different earlier cover unless reachability and the total potential change from that earlier cover are also established.
