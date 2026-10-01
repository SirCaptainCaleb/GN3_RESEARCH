# Canonical source rails are downward-complete against common-terminal competitors

## Statement

Let e={x,v,u} be an ascending nonspecial edge of rank r>=2, with unique entrance x and terminal v. Let
R=(g_1,...,g_{r-1})
be any canonical maximum source rail ending at x such that R,e is a longest r-edge path ending in e through x; in particular R avoids v and u.

Let f be any distinct nonspecial edge through v for which v is a terminal, and suppose phi(f)<=r+1. Then f meets V(R).

Consequently, for any family e_1,...,e_k of ascending nonspecial edges terminal at the same vertex v, ordered by nondecreasing ranks r_1<=...<=r_k, every canonical source rail R_j of e_j meets every earlier edge e_i, i<j. More generally R_j meets every family edge of rank at most r_j+1.

## Body

Suppose f is disjoint from V(R). Since e and f are distinct edges through v, linearity gives e∩f={v}. Also R avoids v and the other terminal u of e, so
R,e,f
is a linear path of length r+1 ending in f and entering f through v.

If phi(f)<=r, this path is longer than the rank of f, impossible. If phi(f)=r+1, it is a longest path ending in f whose entrance label is v. But v is assumed to be a terminal vertex of the nonspecial edge f, contradicting the uniqueness of its longest-path entrance. Hence f must meet R.

The ordered-family assertion is immediate because r_i<=r_j<=r_j+1 for i<j.
