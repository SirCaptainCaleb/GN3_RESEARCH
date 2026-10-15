# Boundary overlap cocycles and the shared antipodal covering class

# Boundary triple-overlap cocycles and the common antipodal cover

For \(n\ge5\), define the graph \(O_n\) on injective ordered triples of \(n\) original vertices, with adjacency \(abc\sim bcd\) when \(a,b,c,d\) are distinct. Triple reversal \(R(abc)=cba\) is a free graph involution.

**Lemma 1 (connectivity).** The graph \(O_n\) is connected.

*Proof.* Given five distinct symbols \(a,b,c,d,e\), the paths
\[
abc\sim bcd\sim cde\sim acd\sim bac,
\qquad
abc\sim dab\sim eda\sim dac\sim acb
\]
exchange the first two or last two positions. Furthermore \(abc\sim eab\sim abd\) replaces the third entry \(c\) by an unused \(d\). Adjacent exchanges allow the replacement to occur in any position. Thus all injective triples are connected. Reversal sends the first overlap edge \(abc\sim bcd\) to \(dcb\sim cba\); no triple or undirected overlap edge is fixed, by injectivity. \(\square\)

Let \(b\) be an arbitrary reversal-odd boundary 3-tournament, so \(b(c,h,a)=1-b(a,h,c)\). Set
\[
\epsilon_b(t,u)=b(t)+b(u)\pmod2
\]
on adjacent triples. The cochain is invariant under reversal, so descends to \(\bar\epsilon_b\) on the quotient \(O_n/R\).

**Theorem 2.** If \(p:O_n\to O_n/R\) is the double covering, then
\[
\boxed{[\bar\epsilon_b]=w_1(p)\in H^1(O_n/R;\mathbb F_2).}
\]
The assignment \(b\mapsto\bar\epsilon_b\) also gives a bijection
\[
\boxed{
\{\text{reversal-odd boundary tournaments}\}/(b\sim1-b)
\cong
\{\eta\in Z^1(O_n/R;\mathbb F_2):[\eta]=w_1(p)\}.
}
\]

*Proof.* Lift any closed walk in the quotient to a path \(t_0,\ldots,t_m\) ending at \(R^h t_0\), where \(h\in\mathbb F_2\) is its covering monodromy. Summing its comparison bits telescopes to \(b(t_0)+b(R^h t_0)=h\). Thus the comparison class evaluates on every loop as the covering class.

If two legal triple colorings have the same comparison bits, their difference is constant on the connected graph \(O_n\), giving uniqueness modulo complement. Conversely, a quotient cocycle in class \(w_1(p)\) pulls back to a coboundary on \(O_n\). Integrate it to a triple-color function \(b\). Its integral from \(t\) to \(Rt\) is one, hence it obeys reversal oddness. \(\square\)

**Common structure with NORI1.** The earlier cube-edge incidence cocycle theorem uses the line graph \(L(Q_n)\), whose vertices are undirected cube edges; its involution is antipodal edge translation. For a cube coloring \(c\), the comparison bit on adjacent edges is \(\epsilon_c(e,f)=c(e)+c(f)\). It obeys the same two theorems. Accordingly both unrestricted colorings, modulo global color exchange, correspond to cocycle representatives of the canonical first Stiefel–Whitney class of a connected local-incidence double cover.

The **full-rank path constraint is indispensable**. Hamilton tight paths advance through *directed* overlapping triples using each original vertex once. Cube geodesics advance through consistently concatenated edges using each dimension once. Their switch counts equal sums of the respective comparison cocycle along the associated incidence sequence. Arbitrary walks in either incidence graph need not decode into admissible full paths. The next Wu–Yang-style argument must use the particular cocycle representative and its support-preserving higher path geometry; the covering class alone is independent of the coloring and insufficient.
