# Common-terminal rank windows add a quadratic source-rank bonus

## Statement

Let v be an active misaligned vertex with phi(v)=p>=8, and let F_v be any switching family from b032348c1a8a. Write k=|F_v| and x_f for the unique entrance of f. Then
  sum_{f in F_v} phi(x_f) >= kp/2 + k(k-1)/8.
More generally the same inequality holds for any k distinct ascending nonspecial edges terminal at a common vertex v of rank p, provided every edge has rank at most p.

Consequently, if eta_v=o(p), then k>=(5/8-o(1))p and
  sum_{f in F_v} phi(x_f) >= (185/512-o(1))p^2.
For simultaneously chosen switching families,
  sum_v [p_v|F_v|/2 + |F_v|(|F_v|-1)/8]
  <= 2 sum_{e ascending} phi(x_e).

## Body

Order the members f_1,...,f_k by nondecreasing edge rank q_i=phi(f_i). Since v has a maximum p-edge path and every switching edge is an ascending nonspecial edge terminal at v with q_i<=p, the path-relative central-window packing theorem 220a14637b5f applies to the family. It gives
  q_i >= ceil((2p+i+3)/4).
For an ascending nonspecial edge the unique entrance x_i satisfies phi(x_i)=q_i-1. Hence
  phi(x_i) >= (2p+i-1)/4,
and summing i=1,...,k yields
  sum_i phi(x_i) >= kp/2 + k(k-1)/8.
No visible-entrance/terminal-only split is needed.

For the switching family of b032348c1a8a, low local defect eta_v=o(p) gives k>=(5/8-o(1))p. The right side is increasing in k, so substitution gives
  (1/2)(5/8)p^2 + (1/8)(25/64)p^2 - o(p^2)
  = (5/16+25/512-o(1))p^2
  = (185/512-o(1))p^2.

Finally an ascending hyperedge has exactly two terminal vertices, so across vertex-indexed families it can occur at most twice, while each occurrence contributes the same source rank. Summing the local inequality over vertices therefore gives the stated global multiplicity bound. This strictly strengthens 94b30079730f.