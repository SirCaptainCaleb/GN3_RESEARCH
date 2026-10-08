# One-left protected A3 reversal pairs have a boundary-safe full-support splice — preserved pre-item development

## One-left protected A3 reversal pairs have a boundary-safe full-support splice

Work with an alternating ternary binary label alpha: cyclic permutations preserve its value and odd permutations complement it. Reversal oddness alone is not enough for this lemma. For distinct a,b,c,d define
\[
\kappa(a,b,c,d)=\alpha(a,b,c)\oplus\alpha(a,b,d)
 \oplus\alpha(a,c,d)\oplus\alpha(b,c,d).
\]
This mod-two tetrahedral curvature is independent of the ordering used to name the four-set.

### Theorem

Let P and S be disjoint coordinate orders, also disjoint from a,b,c,d. Put p=|P|+1>=1 and q=|S|>=1, and write e for the first coordinate of S. Assume the deletion orders
\[
O_b=P\,a\,c\,d\,S,\qquad O_c=P\,d\,b\,a\,S
\]
both have ternary word 0^p1^q. Assume also
\[
\alpha(a,b,c)=1,\qquad \alpha(b,c,d)=0.
\]
These are the two minimum-phase deletion witnesses underlying a genuine reversed A3 root pair when the cut meets the four-block in its first coordinate: restoring b or c at the canonical gap gives PabcdS or Pd c b a S. Minimality is not needed for the splice itself.

Set
\[
U=\alpha(b,d,e),\qquad V=\alpha(c,a,e).
\]
Then the two full-support orders
\[
F_1=P\,a\,c\,b\,d\,S,\qquad F_2=P\,d\,b\,c\,a\,S
\]
have words
\[
0^p\,1\,U\,1^{q-1},\qquad 0^p\,1\,V\,1^{q-1},
\]
respectively, and
\[
U\oplus V=1\oplus\kappa(a,b,d,e)\oplus\kappa(a,c,d,e).
\]
Consequently, if the two displayed boundary curvatures agree, at least one of F_1,F_2 is a full-support one-change order, with word 0^p1^{q+1}.

In particular every such genuinely witnessed one-left reversal pair closes in the globally coboundary-flat alternating sector.

### Complete window check

The word of O_b forces alpha(a,c,d)=0 and alpha(c,d,e)=1. Its windows before the internal triple a,c,d are all zero, including every existing left attachment to the pair (a,c). Its windows after c,d,e are all one.

The word of O_c forces alpha(d,b,a)=0 and alpha(b,a,e)=1. Thus, by alternation,
\[
\alpha(a,b,d)=1,\qquad\alpha(a,b,e)=0.
\]
Its existing left attachment windows to (d,b) are all zero, and its right continuation through a,e is all one.

In F_1, every window preceding the first internal triple is inherited from O_b. Alternation gives
\[
\alpha(a,c,b)=0,\qquad\alpha(c,b,d)=1.
\]
The next window is b,d,e, with color U. Every subsequent window is inherited from O_b and is one. This proves the first word formula, including q=1, where the terminal 1^{q-1} is empty.

In F_2 the left attachments are inherited from O_c. The two internal colors are
\[
\alpha(d,b,c)=0,\qquad\alpha(b,c,a)=1.
\]
The next window is c,a,e, with color V, and the remaining right windows are inherited from O_c and are one. This proves the second formula.

Neither argument assumes unverified old boundary pairs for a changed order: all windows meeting P or S have been listed or identified as literal inherited windows. Both permutations retain every coordinate and the entire relative order inside P and S.

### Boundary identity

Put D=alpha(a,d,e). Since alpha(a,b,d)=1 and alpha(a,b,e)=0,
\[
\kappa(a,b,d,e)=1\oplus D\oplus U.
\]
Also alpha(a,c,d)=0, alpha(a,c,e)=1\oplus V, and alpha(c,d,e)=1, so
\[
\kappa(a,c,d,e)=D\oplus V.
\]
Taking their xor proves the claimed identity.

### Curvature separation in an unresolved instance

If the full instance is a counterexample, both candidates must fail. Their complete word formulas force U=V=0, hence
\[
\kappa(a,b,d,e)\ne\kappa(a,c,d,e),\qquad
\alpha(a,d,e)=\kappa(a,c,d,e).
\]
Thus simultaneous genuinely protected opposite roots do impose a new coupling on the reconnection data: the coupling comes from BOTH deletion witnesses, not flatness alone. This does not contradict the independent four-bit assignments in ternary §39, whose weaker local hypotheses do not include this pair of full deletion witnesses with common exterior order.

### Scope for Article III

Root §33 reduces a canonical protected A3 reversal two-cycle to one or two Johnson cut exchanges. This theorem resolves its one-exchange case whenever the two specified boundary curvatures agree. In the flat alternating sector, an unresolved genuinely witnessed reversed A3 two-cycle must therefore be in the two-left-coordinate case, or fail the stated common-exterior/canonical-provenance hypotheses. Raw opposite chamber roots alone do not supply the two witnesses. Arbitrary opposite-endpoint chambers need not be literal block reversals.

No theorem here concerns the full basepoint-dependent NOR coloring, or general reversal-odd coordinate labels lacking alternation.
