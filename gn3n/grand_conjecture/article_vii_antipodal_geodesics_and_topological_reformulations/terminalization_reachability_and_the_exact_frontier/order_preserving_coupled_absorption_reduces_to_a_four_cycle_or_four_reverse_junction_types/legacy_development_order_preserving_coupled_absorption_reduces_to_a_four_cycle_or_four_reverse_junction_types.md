# Order-preserving coupled absorption reduces to a four-cycle or four reverse-junction types — preserved pre-item development

## Order-preserving coupled absorption has only two bounded obstruction types

Let
\[
B=(b_1,\ldots,b_m)
\]
be a tight path and let \(x,y\notin V(B)\). Assume neither \(x\) nor \(y\) can be inserted individually into any slot of the inherited order of \(B\). Suppose nevertheless that there is a tight order \(R\) on \(V(B)\cup\{x,y\}\) whose restriction to \(V(B)\) is exactly the displayed order \(B\).

By [[minimum_pair_coupled_insertions_have_range_at_most_two]], the two new labels are either adjacent in \(R\), or exactly one old vertex lies between them.

The one-separator case is already handled by [[one_separator_coupled_insertion_forces_the_carrier_four_cycle]]: if
\[
(\ldots,b_i,x,b_{i+1},y,b_{i+2},\ldots)
\]
is tight, then in the local tournament at \(b_{i+1}\) the four labels
\[
\{b_i,b_{i+2},x,y\}
\]
contain the directed cycle
\[
b_i\to b_{i+2}\to x\to y\to b_i.
\]

It remains to localize the adjacent case. Assume, away from the two end slots,
\[
(\ldots,b_{i-1},b_i,x,y,b_{i+1},b_{i+2},\ldots)
\]
is tight. Then
\[
h(b_{i-1},b_i,x)=1,\qquad
h(b_i,x,y)=1,\qquad
h(x,y,b_{i+1})=1,\qquad
h(y,b_{i+1},b_{i+2})=1.
\]

Insert \(x\) alone between \(b_i\) and \(b_{i+1}\). The left junction is already certified:
\[
h(b_{i-1},b_i,x)=1.
\]
Since this one-label insertion fails, at least one of the remaining two junctions fails:
\[
h(b_i,x,b_{i+1})=0
\quad\text{or}\quad
h(x,b_{i+1},b_{i+2})=0.
\]
By boundary antisymmetry,
\[
\boxed{h(b_{i+1},x,b_i)=1}
\quad\text{or}\quad
\boxed{h(b_{i+2},b_{i+1},x)=1}.
\]

Likewise insert \(y\) alone in the same inherited slot. The right junction is already certified:
\[
h(y,b_{i+1},b_{i+2})=1.
\]
Hence failure of this insertion forces
\[
h(b_{i-1},b_i,y)=0
\quad\text{or}\quad
h(b_i,y,b_{i+1})=0,
\]
equivalently
\[
\boxed{h(y,b_i,b_{i-1})=1}
\quad\text{or}\quad
\boxed{h(b_{i+1},y,b_i)=1}.
\]

Therefore an adjacent coupled insertion is completely described, beyond its two certified middle triples, by one choice from each of two binary reverse-junction alternatives. There are only four possible obstruction types, all supported on
\[
\{b_{i-1},b_i,b_{i+1},b_{i+2},x,y\}.
\]

At an endpoint slot one of the outer junction tests disappears, so the corresponding conclusion is strictly simpler.

### Coupled-routing dichotomy

For a genuine minimum deletion pair \(\{x,y\}\) and either inherited complementary path \(B\), minimum-pair nonaugmentability supplies the individual noninsertability hypothesis. Hence every order-preserving absorption of both holes into \(B\) has exactly one of two forms:

1. **one-separator form:** a canonical directed four-cycle appears in one local tournament;
2. **adjacent form:** the obstruction is one of four explicit two-sided reverse-junction types on at most six consecutive anchor labels.

Thus coupled two-hole routing introduces no new unbounded interface. The only nontrivial order-preserving routing phenomena are a four-cycle or a bounded reverse-junction packet. This places the combinatorial two-deletion handoff on the same finite scale as the protected carrier \(C_4\) obstruction; the remaining work is to identify which reverse-junction types either generate the terminal-pair mutual \(C_4\), fill it by protected exterior labels, or force a rooted endpoint handoff.
