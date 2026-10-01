# Same-type distinguished overlap yields two balanced endpoint lenses per label

## Statement

Let H be a finite linear 3-graph. Let v be a vertex with \(\phi(v)=p\), and let
\[
e_i=\{x_i,v,u_i\},\qquad i=1,\dots,k,
\]
be distinct ascending nonspecial edges terminal at \(v\), where \(x_i\) is the unique entrance of \(e_i\). Assume that \(v\) has minimum vertex rank among the two terminal vertices of every \(e_i\), so \(\phi(u_i)\ge p\). Order the edges so that \(q_1\le\cdots\le q_k\), where \(q_i=\phi(e_i)\), and choose a canonical maximum source rail \(R_i\) of length \(q_i-1\) ending at \(x_i\).

Put \(h=\lfloor k/2\rfloor\) and \(m=k-h\). If \(k\ge4\), then there are two indices \(a,b>h\) and a set \(I\subseteq\{1,\dots,h\}\) with
\[
|I|\ \ge\ \frac{h\,\lfloor (m-1)^2/4\rfloor}{2\binom m2}
\ =\ \frac{k}{8}-O(1)
\]
such that one of the following holds throughout \(I\):

(i) \(x_i\in V(R_a)\cap V(R_b)\) for every \(i\in I\), and \(\phi(x_i)\ge\lceil p/2\rceil\);

(ii) \(u_i\in V(R_a)\cap V(R_b)\) for every \(i\in I\), and \(\phi(u_i)\ge p\). In this case
\[
e_i\cap V(R_a)=e_i\cap V(R_b)=\{u_i\}.
\]
Consequently, on each of \(R_a,R_b\), the first path edge containing \(u_i\) has index at most \(q_i-2\).

Moreover, writing \(y_i=x_i\) in case (i) and \(y_i=u_i\) in case (ii), for any maximum endpoint path \(P_i\) ending at \(y_i\), each pair \(R_a,P_i\) and \(R_b,P_i\) contains a clean balanced elementary endpoint lens ending at \(y_i\). In case (i) one may take \(P_i=R_i\).

## Body

Apply the rank-ordered distinguished-overlap lemma f9b8f7df1398 to the first \(h\) edges and the final \(m\) source rails. In its binary encoding, each final rail \(R_j\), \(j>h\), chooses at each coordinate \(i\le h\) the symbol \(X\) if it contains \(x_i\), and otherwise the symbol \(U\); the latter is available because downward-completeness forces \(R_j\) to meet \(e_i\), while \(R_j\) avoids the common terminal \(v\).

Hence some two final rails \(R_a,R_b\) agree in at least
\[
A:=\frac{h\,\lfloor (m-1)^2/4\rfloor}{\binom m2}
\]
coordinates. Partition these agreeing coordinates according to whether the common chosen vertex is \(x_i\) or \(u_i\). One class has size at least \(A/2\); call its index set \(I\). This gives the asserted common-label alternative and the displayed lower bound.

For case (ii), the minimum-terminal hypothesis directly gives \(\phi(u_i)\ge p\). More is true because of the convention in the binary encoding: a rail receives the symbol \(U\) at coordinate \(i\) only when \(x_i\) is absent from that rail. Thus \(x_i\notin V(R_a)\cup V(R_b)\) for every \(i\in I\). Every canonical source rail at the common terminal \(v\) also avoids \(v\). Since \(e_i=\{x_i,v,u_i\}\), it follows that
\[
e_i\cap V(R_a)=e_i\cap V(R_b)=\{u_i\}.
\]
Neither host rail uses \(e_i\), so first-contact localization 813f5b668319 applies. The unique contact is a terminal vertex of \(e_i\), hence the first edge of either host rail containing \(u_i\) has index at most \(q_i-2\).

For case (i), since \(e_i\) is ascending of edge rank \(q_i\), \(\phi(x_i)=q_i-1\). The certified terminal-rank bound a7b7670e955a gives
\[
p=\phi(v)\le 2q_i-2,
\]
so
\[
\phi(x_i)=q_i-1\ge \left\lceil\frac p2\right\rceil.
\]

It remains to record the geometric consequence of a common label. By linearity, the off-\(v\) vertices of the distinct edges \(e_i\) are pairwise distinct. Since \(i\le h<a,b\), the selected label \(y_i\) is distinct from the last vertices \(x_a,x_b\) of \(R_a,R_b\). Thus \(y_i\) is a non-last vertex on each of the two maximum endpoint paths \(R_a,R_b\). Apply b35b0fd4e4cd to \(R_a\) and any maximum endpoint path \(P_i\) ending at \(y_i\), and again to \(R_b\) and the same \(P_i\). Each application produces a clean balanced elementary endpoint lens ending at \(y_i\). In case (i), the canonical source rail \(R_i\) is itself a maximum endpoint path ending at \(x_i\), so \(P_i=R_i\) is admissible.

Finally, with \(h=\lfloor k/2\rfloor\) and \(m=\lceil k/2\rceil\), the exact bound above is \(k/8-O(1)\).
