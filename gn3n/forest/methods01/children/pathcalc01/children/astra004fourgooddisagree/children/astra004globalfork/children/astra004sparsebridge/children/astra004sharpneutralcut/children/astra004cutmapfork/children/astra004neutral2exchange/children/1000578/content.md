# The neutral deletion-sparse cut map cannot be disturbance-free

## Statement

Keep the sharp-shell setup A=(a_0,...,a_{lambda-1}), U=V(H)-V(A), D={u in U:U-u is Hamiltonian}, with |D|<=2. Suppose every bad label u in U-D has a chosen exact cover of H-u attaining exactly two A|(U-u) crossings and lying in the completely order-neutral cut form of astra004sharpneutralcut. Then explicit double-deletion crossing or relative-order disagreement necessarily occurs. Equivalently, there is no fully disturbance-free neutral cut-map realization of the deletion-sparse sharp shell.

## Body

Let k:U-D -> {1,...,lambda-1} be the neutral cut map. If k is not injective, choose distinct bad labels u,v with k(u)=k(v). By astra004repeatcutdisturb, every repeated neutral cut forces explicit common-double-deletion crossing or relative-order disagreement. This is the desired disturbance.

Assume therefore that k is injective. The domain has size |U-D|=lambda+1-|D| and the codomain has size lambda-1. Injectivity gives lambda+1-|D|<=lambda-1, hence |D|>=2. Since |D|<=2, one has |D|=2, and the domain and codomain both have size lambda-1. Thus k is bijective.

In particular there are bad labels u_L,u_R with cuts 1 and lambda-1. Apply astra004extremecutdisturb to the corresponding normalized extreme covers. It gives either an inherited three-part crossing in the common double deletion or different support partitions for the two induced exact covers, hence explicit support/order disturbance.

Thus both the repeated-cut and injective cases force disturbance. No fully neutral deletion-sparse cut map exists. ∎
