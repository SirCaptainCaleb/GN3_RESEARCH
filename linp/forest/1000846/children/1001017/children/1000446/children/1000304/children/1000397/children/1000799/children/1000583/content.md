# First-contact localization for a nonspecial edge

## Statement

Let f be a nonspecial edge of rank q with unique entrance x. Let R=(r_1,...,r_p) be any linear path not using f, and let i be the first index for which r_i meets f. If r_i∩f={x}, then i<=q-1. If r_i meets f in one of the two terminal vertices of f, then i<=q-2.

## Body

Proof. By the definition of i, f is disjoint from r_1,...,r_{i-1}, while it meets r_i in one vertex. Hence (r_1,...,r_i,f) is a linear path of length i+1 ending in f, with entrance label r_i∩f. If that label is the unique entrance x, then i+1<=q by the definition of q=phi(f), so i<=q-1. If the label is a terminal vertex of f, then i+1 cannot equal q: a q-edge path ending in f through that terminal label would be a longest path with a second entrance label, contradicting nonspecialness. Thus i+1<=q-1 and i<=q-2.