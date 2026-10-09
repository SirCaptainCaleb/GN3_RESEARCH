# Three nonlinear exceptional directions force all six terminal suffixes to synchronize under hypothetical NORI failure

# Three-coordinate nonlinear fault rigidity: all six terminal orders synchronize to one alternating pattern

Fix n>=8 and distinct exceptional directions K={a,b,c}⊂[n], with D=[n]\K of size m=n-3>=5. Let C be a binary coloring of physical ORDERED three-faces satisfying the active NORI law C(bar F,rev π)=1-C(F,π). Assume that whenever an ordered triple π has all three free directions INSIDE D, C coincides with a full-exterior-parity baseline
\[
C(F,\pi)=h(\pi)+\bigoplus_{t\notin\operatorname{free}(F)} z_t(F).
\]
On ordered three-faces whose free triples MEET K, C is COMPLETELY ARBITRARY, including arbitrary nonlinear dependence on exterior bits, subject only to the NORI axiom.

Fix ANY order p=(p_1,...,p_m) of D. The first m-2 ordered-three-face windows of any full permutation (p,σ) with σ∈S(K) agree with the parity baseline. Define G_p⊆Q_n to be the set of roots at which these m-2 prefix windows are all of a single color. Their successive change equations are
\[
0=\delta_j=h(p_j,p_{j+1},p_{j+2})+h(p_{j+1},p_{j+2},p_{j+3})+1+x_{p_j}+x_{p_{j+3}}
\qquad(1\le j\le m-3).
\]
The equations are independent, so |G_p|=2^(n-(m-3))=2^6=64. Membership depends ONLY on the D-bits x_D, not on the three K-bits; also if x∈G_p then x⊕D∈G_p.

For every x∈G_p and t∈K define the FIRST exceptional-window color
\[
L_t(x)=C(\text{physical window along }(p,t,\ldots),\ (p_{m-1},p_m,t)).
\]
Its physical face is uniquely determined by x and p, and is independent of the order of the other two K coordinates. For σ=(s_1,s_2,s_3), denote its three successive exceptional window colors by
\[
W_\sigma(x)=(L_{s_1}(x),\ M_{s_1s_2}(x),\ V_\sigma(x)).
\]
The last window is the ordered K-face obtained after traversing every direction of D.

**THEOREM (strong 3-exception synchronization).** Suppose that the active NORI GRAND CONJECTURE FAILS for C, so no full order admits a one-switch path. Then for every fixed p and every x∈G_p:
1. All SIX suffix words are ALTERNATING:
\[
W_\sigma(x)=(t(x_D),1-t(x_D),t(x_D))
\quad\text{for all }\sigma\in S(K).
\]
2. The bit t depends ONLY on x_D, not on any K starting bit. Thus all three first-window colors L_a,L_b,L_c agree and all six middle-window colors M_ab, M_ac, M_ba, M_bc, M_ca, M_cb agree with their complement.
3. The six ordered-color values on the SAME physical K-face reached after traversing D are EQUAL: C(F,σ)=t(x_D) for every ordering σ of K. This is genuine ORIENTATION BLINDNESS of the exceptional K-face on the 8 outside-root patterns x_D satisfying the early-prefix equations. For the antipodal physical K-face, t((x⊕D)_D)=1-t(x_D).

**PROOF.** The existing arbitrary-three-terminal-fault theorem applies separately to EACH σ: since the first m-2 actual windows equal the full exterior-parity baseline and x∈G_p, the full word is q(x)^(m-2) followed by W_σ(x). The coordinate t_0=s_1=p_{m+1} lies in all three exceptional free direction triples and in none of the early free triples. Flipping x_{s_1} preserves all three arbitrary exceptional physical face colors and complements every early parity window. Both paired roots remain in G_p. Unless W_σ itself has at least TWO internal switches, one of these paired full paths has at most ONE total switch. Since by hypothesis neither is good, every W_σ alternates:
\[
M_{s_1s_2}(x)=1-L_{s_1}(x),\qquad V_\sigma(x)=L_{s_1}(x).   (1)
\]

Now put x'=x⊕D. As the early change equations involve only XORs of pairs of D-bits, they are invariant under complementing ALL D-bits, so x'∈G_p. The last K-face reached from x has exterior bit vector x_D⊕1_D, whereas the last K-face reached from x' has exterior bits x_D. Hence these two physical K-faces are antipodal. For σ=(s_1,s_2,s_3), apply NORI reversal oddness to their reversed orders:
\[
V_{\operatorname{rev}\sigma}(x')=1-V_\sigma(x).
\]
Using (1) at both x and x' gives
\[
L_{s_3}(x')=1-L_{s_1}(x)\quad
\text{for EVERY distinct }s_1,s_3\in K.
\]
Fix s_3 and compare the two choices of s_1≠s_3. It follows L_{s_1}(x)=L_{s'_1}(x). Vary s_3 to conclude L_a(x)=L_b(x)=L_c(x), say t(x). Likewise L_a(x')=L_b(x')=L_c(x')=1-t(x). Formula (1) now gives the uniform alternating suffix for all σ.

Finally G_p-membership depends only on x_D and allows ALL eight assignments of x_K. For each s∈K, the actual ordered face of the first exceptional window has s as a FREE direction, so L_s(x) is independent of the starting bit x_s. But for every assignment of x_K the three functions L_a,L_b,L_c are equal. Their common value is therefore independent of x_a,x_b,x_c separately, hence depends ONLY on x_D. Formula (1) shows every middle exceptional window color is 1-t(x_D) and every final physical K-face orientation has value t(x_D). The complementary relation for x' was established above. QED.

**Interpretation and unproved step.** The standard three-terminal-fault argument only forces each individual suffix to alternate; the new result proves CROSS-ORDER and ACROSS-ROOT synchronization using NORI's actual reversal-odd law and freedom in the physical K-coordinates. It is a necessary obstruction for a potentially grand-counterexample coloring in the broad class of arbitrary nonlinear three-coordinate faults of a full-parity reference. It does NOT yet refute that obstruction: globally consistent orientation-blind K-face data may exist, and a proof must also constrain permutations that mix K with D. This is a concrete exchange/repair frontier.
