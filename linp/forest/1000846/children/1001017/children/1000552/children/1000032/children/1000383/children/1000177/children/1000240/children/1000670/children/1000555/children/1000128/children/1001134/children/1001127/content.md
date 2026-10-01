# Same-type distinguished overlap gives two lens-free repeated-intersection certificates per label

## Statement

Let H be a finite linear 3-graph. Let v be a vertex with phi(v)=p, and let
  e_i={x_i,v,u_i}, i=1,...,k,
be distinct ascending nonspecial edges terminal at v, where x_i is the unique entrance of e_i. Assume v has minimum vertex rank among the two terminal vertices of every e_i, so phi(u_i)>=p. Order the edges by
  q_1<=...<=q_k,   q_i=phi(e_i),
and choose a canonical maximum source rail R_i of length q_i-1 ending at x_i.

Put h=floor(k/2) and m=k-h. If k>=4, then there exist a,b>h and a set I subset {1,...,h} with
  |I| >= h*floor((m-1)^2/4)/(2*C(m,2)) = k/8-O(1)
such that one of the following holds throughout I:

(X) x_i belongs to V(R_a) intersect V(R_b) for every i in I, and phi(x_i)=q_i-1>=ceil(p/2);

(U) u_i belongs to V(R_a) intersect V(R_b) for every i in I, phi(u_i)>=p, and x_i is absent from V(R_a) union V(R_b). Hence
  e_i intersect V(R_a)=e_i intersect V(R_b)={u_i},
and the first path-edge of each of R_a,R_b containing u_i has index at most q_i-2.

Moreover, write y_i=x_i in case (X) and y_i=u_i in case (U). For every i in I and every maximum endpoint path P_i ending at y_i,
  |V(P_i) intersect V(R_a)|>=2
and
  |V(P_i) intersect V(R_b)|>=2.
In case (X) one may take P_i=R_i.

Thus a common-minimum-terminal family of k ascending edges forces two higher-rank source rails and k/8-O(1) same-type labels, each label carrying two lens-free repeated-intersection certificates.

## Body

Apply the certified rank-ordered distinguished-overlap lemma f9b8f7df1398 to the first h edges and the final m canonical source rails. For each final rail R_j and each coordinate i<=h, encode X if x_i lies on R_j and U otherwise. The U symbol is available because downward completeness, already built into f9b8f7df1398, forces R_j to meet e_i while R_j avoids v.

As in f9b8f7df1398, some two final rails R_a,R_b agree in at least
  A = h*floor((m-1)^2/4)/C(m,2)
coordinates. Split these agreeing coordinates according to common symbol X or U. One class has size at least A/2; call its index set I. This proves the displayed lower bound and the same-type alternative.

In case (X), phi(x_i)=q_i-1 because e_i is ascending. Since v is a terminal of e_i with phi(v)=p, the certified terminal-potential bound a7b7670e955a gives p<=2q_i-2. Hence
  phi(x_i)=q_i-1>=ceil(p/2).

In case (U), the minimum-terminal hypothesis gives phi(u_i)>=p. By the encoding convention, U was chosen only when x_i was absent from the rail. Hence for every i in I,
  x_i notin V(R_a) union V(R_b).
Each canonical source rail also avoids v. Since e_i={x_i,v,u_i}, it follows that
  e_i intersect V(R_a)=e_i intersect V(R_b)={u_i}.
The first-contact localization theorem 813f5b668319 then applies on each host rail. Because the unique contact is the terminal vertex u_i of e_i, its first host occurrence has index at most q_i-2.

It remains to prove the repeated-intersection conclusion without using any endpoint-lens theorem. Fix i in I and let P_i be any maximum endpoint path ending at y_i. The label y_i lies on R_a and is distinct from the endpoint x_a of R_a: indeed i<=h<a, and distinct common-terminal edges have disjoint non-v vertex pairs by linearity. Thus y_i is a non-endpoint vertex of the maximum endpoint path R_a, while it is the endpoint of the maximum endpoint path P_i.

If
  V(P_i) intersect V(R_a)={y_i},
then the certified unique-intersection theorem 5854d853a44b would force y_i to be an internal joint of P_i, contradicting that y_i is the last vertex of P_i. Therefore
  |V(P_i) intersect V(R_a)|>=2.
The same argument with R_b gives
  |V(P_i) intersect V(R_b)|>=2.

In case (X), R_i is itself a maximum endpoint path ending at x_i=y_i, so one may take P_i=R_i.

No endpoint-lens existence or balance statement is used.
