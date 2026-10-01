# Nonascending bad-load blocker bound

## Statement

Let H be a linear 3-graph and x a vertex with endpoint rank a=a(x). Among nonspecial edges e whose unique entrance is x and which are nonascending, there are at most 2a-2. More sharply, among those satisfying a>2(phi(e)-1), there are at most a-1.

## Body

Proof. Fix one a-edge linear path P ending physically at x. By the entrance-rank blocker lemma d873cc1eb545, every nonascending nonspecial edge e bad at x meets P in at least one terminal vertex of e in addition to x. Since e and the last edge of P both contain x, linearity forbids e from meeting any other vertex of the last edge, so such a blocker lies in V(P)\V(f_a), a set of size 2a-2. Distinct bad edges through x are otherwise disjoint by linearity, so choosing one blocker for each gives an injection into V(P)\V(f_a), proving the first bound. For the sharper subfamily a>2(phi(e)-1), d873cc1eb545 forces both terminal vertices of e to lie on P as blockers. Distinct edges again have disjoint terminal pairs, so each consumes two distinct vertices of V(P)\V(f_a), giving at most (2a-2)/2=a-1 such edges.