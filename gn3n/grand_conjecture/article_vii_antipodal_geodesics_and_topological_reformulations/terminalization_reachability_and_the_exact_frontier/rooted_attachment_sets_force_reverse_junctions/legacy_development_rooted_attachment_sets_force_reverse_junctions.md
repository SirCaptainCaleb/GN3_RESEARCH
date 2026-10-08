# Rooted attachment sets force reverse junctions — preserved pre-item development

## Development

## Rooted attachment sets turn connector failure into forced reverse triples

Let
\[
V(H)=S\sqcup V(T)\sqcup V(U),
\]
where
\[
T=(t_1,\ldots,t_p),\qquad U=(u_1,\ldots,u_q),
\]
are tight paths of order at least two, \(|S|\le7\), and \(\kappa_2(H)\ge2\).

Define the rooted attachment sets
\[
L=\{a\in S:h(t_{p-1},t_p,a)=1\},
\qquad
R=\{b\in S:h(b,u_1,u_2)=1\}.
\]
Thus \(a\in L\) means \(a\) can be appended to the displayed end of \(T\), while \(b\in R\) means \(b\) can be prepended to the displayed start of \(U\).

By [[connector_path_exclusion_for_genuine_two_deletion_packets]], no nonempty packet fragment may join \(T\) to \(U\).

**One-label rule.** If \(a\in L\cap R\), then
\[
h(t_p,a,u_1)=0,
\qquad\text{hence}\qquad
h(u_1,a,t_p)=1.
\]

**Proof.** Otherwise \((T,a,U)\) would be a tight path, contradicting connector-path exclusion. Boundary antisymmetry gives the reverse triple. \(\square\)

So every label that attaches on both rooted sides automatically becomes a common reverser of the two inner root vertices \(t_p,u_1\).

**Two-label rule.** Let \(a,b\in S\) be distinct with \(a\in L\) and \(b\in R\). Then the two middle junctions cannot both be tight:
\[
h(t_p,a,b)\,h(a,b,u_1)=0.
\]
Equivalently, at least one of
\[
h(b,a,t_p)=1,
\qquad
h(u_1,b,a)=1
\]
is forced.

**Proof.** If both middle junctions were tight, then every new triple in
\[
(T,a,b,U)
\]
would be tight: the first and last junctions are supplied by \(a\in L\) and \(b\in R\), while the two middle junctions are the displayed hypotheses. Thus \((T,a,b,U)\) would be a packet connector path, again contradicting [[connector_path_exclusion_for_genuine_two_deletion_packets]]. Reverse whichever failed middle triple by boundary antisymmetry. \(\square\)

There is a symmetric pair of rules after exchanging \(T\) and \(U\).

This yields a bounded rooted obstruction calculus for the genuine reflected-double packets. Once \(L\) and \(R\) are known, every ordered pair in \(L\times R\) is forced into one of two reverse-junction types (possibly both), and every label in \(L\cap R\) carries the same rooted reverse triple through \(t_p,u_1\). No Hamiltonicity enumeration is involved.

For the canonical six-packet of the rigid \(010\)-island and for each six-packet arising from a mobile monotone cut, the remaining gluing problem can therefore be phrased as follows: prove that the inherited endpoint reversals and packet Hamiltonicity force either

1. a label or ordered pair violating the rooted reverse-junction rules, which reduces \(\kappa_2\) below two;
2. a Hamiltonian packet support whose complement is one tight path, giving a two-cover; or
3. a coherent reverse-junction chain reaching an exterior position, where the corresponding status change is a strictly farther positive witness or supplies an enlarged-window repair.

The third alternative is not proved here. The point is that a genuine two-deletion residue no longer has arbitrary packet-tail interaction: all possible short joins are converted into explicit reverse triples on a bounded rooted interface.
