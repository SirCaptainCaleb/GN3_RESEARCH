# High entrance rails have exact clean interior bands and double-only terminal cells

## Statement

Let e={x,v,u} have rank q and let h_1,h_2,h_3 have rank q+1 in a q,(q+1)^3 charged configuration at the common terminal v. Fix i and a canonical q-edge entrance rail Q_i=(r_1,...,r_q) for h_i.

Then every foreign charged edge meets Q_i, with the following exact one-contact bands:

- for j!=i, if h_j has exactly one contact on Q_i, its contact occurs in r_2,...,r_{q-2};
- if e has exactly one contact on Q_i, its contact occurs in r_3,...,r_{q-2}.

Consequently any foreign charged edge meeting r_{q-1} or r_q is necessarily a double blocker on Q_i.

## Body

For h_j with j!=i, apply the certified terminal tail-blocker lemma to h_j, whose rank is q+1, against the (q+1)-edge path Q_i,h_i ending at the common terminal v. Since h_j is not the last edge h_i, it must meet one of the final (q+1)-2=q-1 precursor edges, namely r_2,...,r_q.

If h_j has exactly one Q_i-contact, f4011e425d67 gives that its last contact index is at most q-2. Hence its unique contact lies in r_2,...,r_{q-2}.

For the low edge e, the terminal tail-blocker lemma gives a contact among the final q-2 precursor edges r_3,...,r_q. If this contact is unique, 1e74ab7b5498 gives last index at most q-2. Thus the unique low-edge contact lies in r_3,...,r_{q-2}.

Therefore every foreign charged edge that reaches either r_{q-1} or r_q must use both of its non-v vertices on Q_i.