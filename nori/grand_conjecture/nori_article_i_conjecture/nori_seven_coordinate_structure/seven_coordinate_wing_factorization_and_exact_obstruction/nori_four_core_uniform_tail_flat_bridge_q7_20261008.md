# Four-core flat bridge forces one-flipper Q7 closure with arbitrary exterior dependence

# Four-core flat bridge: generalized seven-dimensional one-flipper closure

Let \(B=A\sqcup M\), \(|A|=4\), \(M=\{u,v\}\), and \(V=B\sqcup\{g\}\). Let \(c\) be an antipodal-reversal-odd ordered-three-face coloring of \(Q_7\), and suppose \(g\) is a universal exterior flipper. Write \(c(F,\pi)=x_g(F)\oplus h(F_B,\pi)\) on every ordered face avoiding \(g\), where \(h\) is an induced, completely arbitrary ordered-three-face coloring of \(Q_B\), satisfying antipodal-reversal *evenness* by the symmetry transfer. No position independence is assumed for \(h\).

**Theorem (four-core flat-bridge closure).** Suppose the residual coloring \(h\) has both properties:

(T) **Uniform good tails on the four-core.** For every pairwise distinct \(a,b,c\in A\) and every \(B\)-starting vertex \(x\in Q_B\), there is a permutation \((d,e,f)\) of \(B\setminus\{a,b,c\}\) such that the last three window colors of the six-direction geodesic with order \((a,b,c,d,e,f)\) and start \(x\) have at most one change.

(F) **One universally flat four-core prefix.** There is some permutation \((a,b,c,d)\) of \(A\) such that for every \(B\)-starting vertex \(x\), the first and second window colors of the six-direction geodesic with order \((a,b,c,d,u,v)\) agree. Their common value \(\lambda(x)\) may depend arbitrarily on \(x\).

Then \(c\) admits a full seven-coordinate antipodal geodesic with at most one color change. All colors on faces containing \(g\) may depend arbitrarily on their four fixed exterior bits.

**Proof.** Suppose every full \(Q_7\) geodesic has at least two changes.

First, the exact universal-flipper lifting lemma implies that every six-direction geodesic of \(h\) has at least two changes: a one-change residual geodesic would lift to a good full geodesic.

For distinct \(a,b,c\in A\), apply (T) and consider the full order \((a,g,b,c,d,e,f)\), with \((d,e,f)\) a good-tail completion. The first two window colors \(P=c(a,g,b)\) and \(Q=c(g,b,c)\), at the reached face positions, are independent of the initial \(g\)-bit. The last three windows avoid \(g\), so toggling that starting bit complements all three simultaneously, preserving their at-most-one changes. We may arrange for the third color to agree with \(Q\). Global failure therefore forces \(P\ne Q\) for every assignment of starting \(B\)-bits, every distinct \(a,b,c\in A\), and whichever completion (T) supplies.

For fixed \(a,b\), vary the initial bit \(x_c\): the \((g,b,c)\)-face has direction \(c\) free, so its color is independent of \(x_c\); the forced inequality implies the \((a,g,b)\)-color is also independent of \(x_c\). Taking both choices \(c\in A\setminus\{a,b\}\) shows that \((a,g,b)\) depends on no exterior \(A\)-bits. Write its value \(F_{ab}(m)\), where \(m=(x_u,x_v)\). Dually, varying \(a\in A\setminus\{b,c\}\) shows that \((g,b,c)\) depends on no exterior \(A\)-bits; write it \(G_{bc}(m)\). Thus
\[
F_{ab}(m)=1\oplus G_{bc}(m)\qquad(a,b,c\in A\text{ distinct}).
\tag{1}
\]
As \(|A|=4\), comparison through a common third direction shows that \(F_{ab}(m)=K_b(m)\) is independent of \(a\), and \(G_{bc}(m)=1\oplus K_b(m)\) is independent of \(c\). Applying oddness to the reversal of the \((a,g,b)\)-face gives
\[
K_a(\bar m)=1\oplus K_b(m)\quad(a\ne b).
\]
Comparing three distinct indices in \(A\) forces a common function \(K\) for all subscripts, with
\[
K(\bar m)=1\oplus K(m).
\tag{2}
\]
Hence, at the relevant face positions and for any distinct \(r,s\in A\),
\[
c(r,g,s)=K(m),\quad c(g,r,s)=1\oplus K(m),\quad c(r,s,g)=1\oplus K(m).
\tag{3}
\]
The final identity follows by antipodal reversal and (2). In all three formulas \(m\) is the marked exterior-bit pair *at that face*. These bits have not been traversed in any of the subsequent paths using (3).

Now choose the four-core order \((a,b,c,d)\) provided by (F), and fix arbitrary initial \(B\)-bits \(x\). Denote the common first-two residual colors in the order \((a,b,c,d,u,v)\) by \(\lambda(x)\). Because every complete residual \(h\)-geodesic is bad, its four-color word must be
\[
(\lambda,\lambda,1\oplus\lambda,\lambda);
\tag{4}
\]
indeed, when the first two entries agree, at least two changes require both remaining comparisons to change. Therefore the residual color of its final \((d,u,v)\)-window equals \(\lambda(x)\). The same holds for the complete residual order \((a,b,c,d,v,u)\): its first two window faces and their positions are unchanged, so its final \((d,v,u)\)-color also equals \(\lambda(x)\).

Consider next the full \(Q_7\) order
\[
(a,b,c,g,d,u,v).
\]
Its five-window word, with \(z=x_g\), is
\[
\bigl(z\oplus\lambda,\;1\oplus K(m),\;K(m),\;T_u,\;(1\oplus z)\oplus\lambda\bigr),
\tag{5}
\]
where \(T_u\) denotes the color of the fourth ordered face \((g,d,u)\), reached after the first three \(A\)-moves and the \(g\)-move. Formula (4) justifies the final entry of (5): the \(B\)-face \((d,u,v)\) is reached after precisely the same \(a,b,c\)-moves in both the residual path and the full path.

Choose \(z=1\oplus K(m)\oplus\lambda\). Then (5) becomes
\[
(1\oplus K,\;1\oplus K,\;K,\;T_u,\;K).
\tag{6}
\]
If \(T_u=K(m)\), the word has exactly one change. Thus global failure forces \(T_u=1\oplus K(m)\) for every \(x\). Since \(u\) is *free* in \((g,d,u)\), changing the initial bit \(x_u\) leaves \(T_u\) unchanged, and all the other exterior face bits are unchanged. Therefore \(K(x_u,x_v)\) is independent of \(x_u\).

Repeating the same argument with the order \((a,b,c,g,d,v,u)\), using the second consequence of (4), forces \(K(x_u,x_v)\) independent of \(x_v\). Thus \(K\) is constant, contradicting (2). This proves closure. \(\square\)

**Scope and significance.** Conditions (T) and (F) are structural hypotheses on the six-dimensional reversal-even residual. The theorem tolerates arbitrary nonlinear dependence on all exterior bits in that residual, provided (T) and (F) hold, and *complete* arbitrary dependence on exterior bits for every \(g\)-containing face. It strengthens the earlier prescribed sparse two-mark template: that template has a four-core \(A\) with its AAA-prefix colors both zero, and the explicit marked-tail pattern makes (T) hold. In an unresolved one-flipper counterexample, for every four-set \(A\) satisfying (T), **every** permutation of \(A\) must have at least one residual start whose two first-window colors differ; otherwise (F) would hold and the counterexample would collapse. This leaves an explicit residual dichotomy to attack.
