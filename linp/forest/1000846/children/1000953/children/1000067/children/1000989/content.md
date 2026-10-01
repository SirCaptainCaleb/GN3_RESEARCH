# Signed projective normal form one rank above minimum

## Statement

For N=2^n-1, every STS(N) contained in the carrier code of binary rank at most N-n+1 (the t=1 carrier) has the following normal form. There is one distinguished point infinity and, for each nonzero x in F_2^{n-1}, a pair G_x={(x,0),(x,1)}. The block through infinity and G_x is {infinity,(x,0),(x,1)}. For every projective line {x,y,z} with x+y+z=0, the blocks on G_x union G_y union G_z form a TD(3,2); after choosing bit labels in each pair, this TD is described by b_x+b_y+b_z=sigma(x,y,z) for one sign sigma in F_2. Thus the family is encoded by a binary sign on each quotient line, modulo independent swaps of the two points in each G_x. The lower-bound problem asks whether sign patterns can force absence of a spanning linear path even when the all-projective pattern is Hamiltonian.

## Body

This is the specialization t=1 of Jungnickel--Tonchev Theorem 2.8. There T=2^t-1=1, so V_0 consists of one point infinity, every nonzero carrier class G_x has size T+1=2, and the quotient geometry is PG(n-2,2). The one-factorization on a 2-point group is unique, giving {infinity,(x,0),(x,1)}. A TD[3;2] on three specified pairs has four triples and, after bit-labeling the pairs, is exactly one of the two parity systems b_x+b_y+b_z=sigma.

Swapping the two labels in a group G_x toggles sigma on every quotient line through x, so only the switching class of the line-signing matters. This is a compact finite-state parameterization of all carrier-compatible STSs at the first rank above the projective minimum. The projective system is one switching class; PG(4,2) shows that class is Hamiltonian at order 31. The proposed search is to derive a path invariant sensitive to the switching class and exhibit a class forbidding a spanning path, preferably uniformly in n. No such obstruction is proved here.