# Two labels using one endpoint collapse the third transport interval to width one

## Statement

In the common-core-order branch of compattripletransport13, let L=(r_1,...,r_m) be the common core, m>=2, and let a,b,c be the three special labels, each having two distinct insertion gaps. If two of the labels use the left endpoint gap 0 in any of their occurrences, then the remaining label has insertion-gap set exactly {0,1}; hence its transport interval has width one at the left endpoint. Symmetrically, if two labels use the right endpoint gap m, the remaining label has insertion-gap set exactly {m-1,m}.

## Body

Let X be the critical support carrying the three deletion paths, and Q the fixed Hamiltonian opposite support supplied by compattripletransport13. Since H is a counterexample, H[X] is non-Hamiltonian; otherwise a Hamilton path on X together with Q would two-cover H.

Suppose two labels, say a and b, use the left endpoint gap 0 in their respective occurrences. Then both (a,L) and (b,L) are tight paths.

The third label c occurs in two deletion paths at two distinct insertion gaps of L. Apply the preceding endpoint-extender localization lemma. Since H[X] is non-Hamiltonian and a,b both left-extend L, every insertion gap of c belongs to {0,1}. The two gaps for c are distinct by the order-incompatible common-core normal form, so they are exactly
{0,1}.
Thus I_c is the single-step interval at the left endpoint.

The right-end statement is identical after reversing the role of the two ends: if two labels right-extend L, every insertion of the third lies in {m-1,m}, and distinctness forces exactly those two gaps. ∎
