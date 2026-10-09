# Dead-prefix rigidity forces a two-mark-like alternating seed in Q6

# Alternating-tail rigidity in a reversal-even six-coordinate residual

Let \(B\) be a six-element coordinate set and let \(H(a,b,c)\in\mathbb F_2\) be a position-independent coloring of ordered *distinct* triples satisfying reversal-evenness
\[
H(a,b,c)=H(c,b,a).
\]
Call an ordered triple \((a,b,c)\) a **dead prefix** if, for every permutation \((d,e,f)\) of \(D=B\setminus\{a,b,c\}\), the three-color tail
\[
\bigl(H(b,c,d),\,H(c,d,e),\,H(d,e,f)\bigr)
\]
has two changes, equivalently it alternates.

**Lemma (rigid alternating-tail seed).** For a fixed ordered triple \((a,b,c)\) and \(D=B\setminus\{a,b,c\}\), the dead-prefix condition holds **if and only if** there is a bit \(K\) such that
\[
\begin{aligned}
H(b,c,d)&=K &&(d\in D),\\
H(c,d,e)&=1\oplus K &&(d,e\in D,\ d\ne e),\\
H(d,e,f)&=K &&((d,e,f)\text{ any permutation of }D).
\end{aligned}\tag{1}
\]
Thus a single dead prefix forces the colors of all six permutations on \(D\), all six \(c\)-to-\(D\)-to-\(D\) triples, and all three \(b,c,D\) triples from one bit.

**Proof.** Assume every tail alternates. Fix an element \(d\in D\) and write \(e,f\) for the other two. Reversal-evenness implies that \(H(d,e,f)=H(f,e,d)\), so the color of a triple whose three coordinates are exactly \(D\) depends only on its middle coordinate; call it \(W_e\). Put \(U_d=H(b,c,d)\). Alternation for the permutation \((d,e,f)\) says
\[
U_d=W_e,\qquad H(c,d,e)=1\oplus W_e\qquad(d,e\in D,\ d\ne e).\tag{2}
\]
For any distinct \(e,e'\in D\), take the remaining \(d\in D\). Then \(W_e=U_d=W_{e'}\). Therefore all \(W_e\) equal some \(K\); (2) gives all \(U_d=K\) and \(H(c,d,e)=1\oplus K\), proving (1). Conversely, (1) makes every tail word \((K,1\oplus K,K)\), so the prefix is dead. \(\square\)

**Necessary structural consequence for one-flipper Q7.** Let \(c\) be a hypothetical NORI counterexample on \(Q_7\) with a universal exterior flipper \(g\), whose induced reversal-even six-coordinate coloring is position-independent, \(h(F,\pi)=H(\pi)\). The uniform good-tail theorem implies that *some* ordered triple \((a,b,c)\) is a dead prefix. Consequently the induced \(H\) contains an alternating-tail seed of the exact form (1), up to coordinate relabeling and global color complementation.

The known reversal-even two-mark obstruction realizes such a seed by taking \(b,c\) to be its marked directions, \(a\) an unmarked direction, and the three elements of \(D\) unmarked. Formula (1) is a necessary seed for every possible coordinate-only residual obstruction to one-flipper closure, without assuming the entire two-mark template. It is a rigidity mechanism, not by itself closure.
