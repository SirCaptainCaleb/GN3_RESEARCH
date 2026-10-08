# Two-left flat protected A3 reversal pairs either splice or emit an exterior insertion root — preserved pre-item development

## Composition

(none yet)

## Development

## Two-left flat protected A3 reversal pairs either splice or emit an exterior insertion root

Use the alternating ternary label and mod-two curvature of the preceding splice theorem.

Let P and S be disjoint exterior orders, disjoint from a,b,c,d. Put p=|P|+2>=2 and q=|S|-1>=1. Write S=e f R, so |R|=q-1. Assume
\[
O_c=P\,a\,b\,d\,S,\qquad O_b=P\,d\,c\,a\,S
\]
both have word 0^p1^q, and
\[
\alpha(a,b,c)=1,\qquad \alpha(b,c,d)=0.
\]
These are the deletion witnesses for the reversed A3 chambers when the fixed cut meets the four-block in two coordinates. Require the two additional flat tetrahedra
\[
\kappa(a,b,c,e)=\kappa(b,c,d,e)=0.
\]
No global flatness is needed beyond these two relations.

### Theorem

Define
\[
T=\alpha(a,b,e),\quad H=\alpha(c,e,f),\quad K=\alpha(b,e,f).
\]
Then the following complete words are forced:

- P a b d c S has word 0^{p-1} 1 (1\oplus T) H 1^{q-1}.
- P d c a b S has word 0^{p-1} 1 T K 1^{q-1}.
- The deletion order P a b c S, omitting d, has word 0^{p-2} 1 T H 1^{q-1}.
- The deletion order P d c b S, omitting a, has word 0^{p-2} 1 (1\oplus T) K 1^{q-1}.

If H=1 or K=1, one of these four orders is either a full-support one-change order or a good deletion order with word
\[
0^{p-2}1^{q+2}.
\]
If H=K=0, choose PabdcS for T=0 and PdcabS for T=1. The chosen full-support order has the common word
\[
0^{p-1}1101^{q-1}.
\]
Its displayed 10 transition gives a physical root
\[
e_d-e_f\quad(T=0),\qquad e_a-e_f\quad(T=1).
\]
This is a fixed-insertion root with the original deletion witness retained; its endpoint f is outside the old four-coordinate block.

### Proof of every changed-window formula

The two deletion witnesses give
\[
\alpha(a,b,d)=0,\quad\alpha(b,d,e)=0,\quad\alpha(d,e,f)=1,
\]
and
\[
\alpha(d,c,a)=0,\quad\alpha(c,a,e)=0,\quad\alpha(a,e,f)=1.
\]
Alternation therefore gives alpha(a,c,d)=1 and alpha(a,c,e)=1. Their remaining exterior windows are inherited zeros on the left and inherited ones on the right.

Write B=alpha(b,c,e) and E=alpha(c,d,e). The first required flatness identity is
\[
0=\kappa(a,b,c,e)=1\oplus T\oplus1\oplus B=T\oplus B.
\]
The second is
\[
0=\kappa(b,c,d,e)=0\oplus B\oplus0\oplus E=B\oplus E.
\]
Thus B=E=T.

For PabdcS, left windows through a,b,d are unchanged from O_c. The new three-window continuation is
\[
\alpha(b,d,c)=1,\quad\alpha(d,c,e)=1\oplus T,\quad\alpha(c,e,f)=H.
\]
The suffix from e,f onward is unchanged. This gives its stated word.

For PdcabS, left windows through d,c,a are unchanged from O_b. The continuation is
\[
\alpha(c,a,b)=1,\quad\alpha(a,b,e)=T,\quad\alpha(b,e,f)=K.
\]
Again the suffix from e,f onward is unchanged.

For PabcS, its left attachment pair (a,b) is inherited from O_c. The subsequent colors are alpha(a,b,c)=1, alpha(b,c,e)=T, and alpha(c,e,f)=H. For PdcbS, its left attachment pair (d,c) is inherited from O_b; the next colors are alpha(d,c,b)=1, alpha(c,b,e)=1 xor T, and alpha(b,e,f)=K. The suffix e,f,R is inherited in both cases. These give the two deletion formulas, including p=2 and q=1.

If T=0, H=1 makes PabdcS a full one-change order, while K=1 makes PdcbS an improved deletion. If T=1, K=1 makes PdcabS a full one-change order, while H=1 makes PabcS an improved deletion. Thus all alternatives with H=1 or K=1 are constructive.

If H=K=0, the stated choice gives 0^{p-1}1101^{q-1}. In PabdcS for T=0 the two descent windows are d,c,e and c,e,f; in PdcabS for T=1 they are a,b,e and b,e,f. They drop d or a and enter f, proving the root formulas.

### Witness preservation and rank consequence

In the first residual case, PabdcS is obtained by inserting c immediately after d in the original O_c. In the second, PdcabS is obtained by inserting b immediately after a in the original O_b. The original good deletion witness, its minimum-phase status if assumed, and the entire order of its coordinates are therefore retained literally. Both descent windows meet the omitted coordinate that was just restored. This is genuine protected fixed-insertion provenance in the sense of root §3.

If p is globally minimum among normalized good deletion orders in a full counterexample, the constructive full orders and the p-2 deletion orders are impossible. A p-2=0 monochromatic deletion extends to a one-change full order at an endpoint. Hence such a counterexample necessarily has H=K=0 and the stated exterior insertion root.

Every old internal A3 root lies in
\[
W_B=\{z\in W:\operatorname{supp}z\subseteq B\},\qquad B=\{a,b,c,d\}.
\]
The emitted root has a nonzero f-coordinate, so it lies outside W_B. Adjoining it strictly increases the span of any root family previously contained in W_B.

This is a local rank enlargement, not a global terminating algorithm: a global root span may already contain exterior coordinates. Moreover the new insertion is one gap beyond the canonical switch gap, so the new root must not be called a canonical switch root or assumed to obey the old common-cut cone theorem. It retains an actual original deletion witness, but enlarges the allowed insertion-state class.

### Use with the one-left theorem

In the alternating flat sector, a genuinely witnessed literal A3 reversal two-cycle with common exterior has the following constructive alternatives. Its one-left case gives a full-support splice. Its two-left case gives a full-support splice, a shorter deletion witness, or an actual protected insertion root leaving the old A3 block. This excludes treating such a two-cycle as a self-contained obstruction on its four coordinates. Closing NOR still needs a compatible global mechanism that uses the exterior root rather than silently reapplying a canonical-cut argument to it.
