# Matched-prefix peeling terminates at a hole frontier or an alternating order cycle

## Composition

(none yet)

## Development

## Matched-prefix peeling terminates at a hole frontier or an alternating order cycle

Let
\[
F_a=P_1\mid P_2,\qquad F_b=R_1\mid R_2
\]
be deletion covers of \(H-a\) and \(H-b\), and suppose cuts
\[
P_i=L_iT_i,\qquad R_i=M_iN_i
\]
satisfy the matched-prefix identity
\[
V(L_1)\cup V(L_2)=\bigl(V(M_1)\cup V(M_2)\bigr)\cup\{b\}.
\]
Put
\[
B=V(M_1)\cup V(M_2).
\]

Call \(x\in B\) peelable if \(x\) is simultaneously the last vertex of a nonempty \(L_i\) and the last vertex of a nonempty \(M_j\). If \(x\) is peelable, move both cuts immediately before \(x\). Equivalently, replace
\[
L_i=L_i'x,\quad M_j=M_j'x
\]
by \(L_i',M_j'\), moving \(x\) to the corresponding two tails. The matched-prefix identity is preserved:
\[
\bigcup V(L_i')=\left(\bigcup V(M_i')\right)\cup\{b\},
\]
and \(|B|\) decreases by one.

Hence repeated peeling terminates after at most the initial \(|B|\) steps.

At a terminal matched cut one of the following holds.

1. \(B=\varnothing\). Then the \(P\)-prefix side is exactly the singleton hole label \(\{b\}\).
2. \(b\) is the last vertex of one of the nonempty \(P\)-prefixes \(L_i\).
3. The union of the two prefix orders contains a directed alternating order cycle: a cyclic sequence of distinct labels in \(B\cup\{b\}\) obtained by moving forward along an \(R\)-prefix order to an \(R\)-terminal label, then forward along a \(P\)-prefix order to a \(P\)-terminal label, and repeating. Every change from one cover order to the other occurs at a frontier label.

Proof of the terminal trichotomy. Assume \(B\neq\varnothing\), \(b\) is not a \(P\)-prefix terminal, and no peelable label remains. Choose a \(P\)-prefix terminal \(x\). Then \(x\in B\), and because \(x\) is not peelable it is not an \(R\)-prefix terminal. Follow its \(R\)-path forward inside the prefix until the corresponding \(R\)-terminal label \(y\). Again \(y\) cannot be a \(P\)-prefix terminal, so follow its \(P\)-path forward inside the prefix to a \(P\)-terminal label \(z\). Because \(b\) is not terminal, \(z\in B\). Repeating gives an infinite alternating sequence of frontier labels in the finite prefix set, hence a repeated frontier label and therefore a directed cycle in the union of the two strict path orders. The intervening directed segments concatenate to the asserted alternating order cycle.

This is a terminating normalization of a matched cut. It does not claim that the terminal cycle itself is already a two-cover. Its value is that endpoint-transfer/Hall analysis need only be run after all common terminal labels have been removed: the residual obstruction is forced either onto the hole frontier or into a cyclic disagreement of the two actual path orders. No bounded-order cutoff or bare bounded Hamiltonian support is used.
