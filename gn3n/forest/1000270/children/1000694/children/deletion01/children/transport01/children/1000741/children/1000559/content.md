# A reversed component-end edge gives a two-cover, neutral singleton transfer, or strict quadratic descent

## Statement

Let H be a minimum counterexample and let H-x=P|Q be a deletion two-cover, where P=(p_0,...,p_m) has order N=m+1>=2. Let R be any Hamilton tight order on V(P). If R contains the reversed terminal edge (p_m,p_{m-1}), write R=A,p_m,p_{m-1},B and put t=|A|. Then (x,p_m,p_{m-1},B) is tight, so A | (x,p_m,p_{m-1},B) | Q is a spanning path cover whenever A is nonempty. If t=0, (x,R)|Q is a spanning two-cover. If t=1, the new three-cover has the same quadratic potential as P|{x}|Q. If 2<=t<=N-2, it has strictly smaller quadratic potential, with drop 2(t-1)(N-t). Symmetrically, if R contains the reversed initial edge (p_1,p_0), splitting immediately after p_0 gives the corresponding two-cover / neutral / strict-descent trichotomy according to the size of the suffix after p_0.

## Body

Because H is a counterexample, x cannot be appended to the displayed order P. Hence
(p_{m-1},p_m,x)
is non-tight. Boundary antisymmetry gives the tight reverse
(x,p_m,p_{m-1}).                                    (1)

Let R be a Hamilton order of V(P) containing the ordered edge
(p_m,p_{m-1}).
Write
R=(A,p_m,p_{m-1},B),
where A is the possibly empty prefix before p_m and B the possibly empty suffix after p_{m-1}. Put t=|A|. Since R uses all N vertices of P, the suffix beginning at p_m has order N-t.

By (1), prepending x to that suffix gives the tight path
S=(x,p_m,p_{m-1},B):
its first triple is (1), and every subsequent triple is inherited from the Hamilton order R.

If t=0, then A is empty and S=(x,R) is a Hamilton path on V(P) union {x}. Together with Q it is a spanning two-cover of H, impossible in a counterexample.

Assume t>=1. The prefix A is an initial subpath of R and hence tight. Therefore
A | S | Q
is a legal spanning three-cover obtained by repartitioning the pair P|{x}; the unchanged component Q is untouched. The old changed pair has component orders N and 1, while the new pair has orders
t and N-t+1.

The change in quadratic potential is
t^2+(N-t+1)^2-(N^2+1)
=2(t-1)(t-N)
=-2(t-1)(N-t).

Thus t=1 is Phi-neutral, while every 2<=t<=N-2 gives a strict drop
2(t-1)(N-t)>0.
(The edge p_m,p_{m-1} occupies two vertices, so t<=N-2.)

For the initial edge, x cannot be prepended to P, so
(x,p_0,p_1)
is non-tight and hence
(p_1,p_0,x)
is tight. If a Hamilton order R contains (p_1,p_0), write
R=(A,p_1,p_0,B)
and append x to the prefix ending at p_0. Splitting after p_0 gives the symmetric repartition; the same calculation, with |B| in place of t, gives the identical two-cover / neutral / strict-descent trichotomy. ∎