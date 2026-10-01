# Persistent pair-order disagreement has even parity around a deletion-cover cycle

## Statement

Let F_1,...,F_k,F_{k+1}=F_1 be a cyclic sequence of deletion covers whose support partitions agree on the relevant common domains. Fix two vertices u,v that survive every cover and lie in one common support class in every F_i. For each transition i, let epsilon_i(u,v)=1 when F_i and F_{i+1} give u,v opposite relative orders and 0 otherwise. Then sum_i epsilon_i(u,v)=0 mod 2. Hence a nontrivial order-cocycle cannot be carried by any fixed pair surviving the entire cycle; any nontrivial monodromy must use pairs involving labels omitted somewhere along the cycle or a richer datum than pairwise order parity.

## Body

For each i encode the order of u,v in F_i by a bit s_i, with s_i=0 for u before v and s_i=1 for v before u. Then epsilon_i=s_i xor s_{i+1}. XORing around the cycle telescopes: epsilon_1 xor ... xor epsilon_k=(s_1 xor s_2) xor ... xor (s_k xor s_1)=0. Equivalently the number of reversals is even. Combined with trivial support monodromy, this localizes any genuinely new cocycle obstruction to order information involving labels that disappear from at least one comparison.