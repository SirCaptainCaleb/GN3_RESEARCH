# Selected strict-gap edges split into same-terminal and uphill certificate classes

## Statement

Retain the strict-gap family Epp from e2dcd798f528. For each edge e with terminal vertices u,v, choose one selected common-anchor D+Y certificate terminal c(e), and assign e to a terminal m(e) of minimum vertex rank.

Then every edge belongs to exactly one of the following two classes after choosing c(e) optimally:
(S) same-terminal certified: some selected certificate terminal has vertex rank equal to min{phi(u),phi(v)}, so e may be assigned to a minimum-rank terminal at which it carries its selected certificate;
(H) uphill certified: every selected certificate terminal has vertex rank strictly larger than min{phi(u),phi(v)}.

In class (H), if m(e)=v and c(e)=u, then
  phi(e)<phi(v)<phi(u).
Thus the certificate orientation is a strict rise in terminal potential away from the counting terminal.

Consequently, for every near-43/48 member, at least half of the Omega(S) distinct strict-gap edges lie in one of the two classes. To contradict 43/48 it is enough to prove an o(p) assigned local bound separately for class (S) and class (H).

## Body

For an edge e with terminal ranks a<=b, consider the set of its selected certificate terminals supplied by e2dcd798f528.

If one certificate terminal has rank a, choose that terminal for both the certificate and minimum-rank assignment. This is class (S). In particular, if a=b, every certificate terminal is minimum-rank, so the edge is necessarily in (S).

Otherwise every certificate terminal has rank strictly larger than a. Since there are only the two terminal vertices, this forces a<b and every selected certificate to lie at the unique higher-rank terminal. Assign e to the unique lower-rank terminal. This is class (H), and strict two-terminal edge-rank gap from e2dcd798f528 gives
  phi(e)<a<b.

The two classes partition Epp. Hence one contains at least |Epp|/2 distinct edges. The proof of a54a1a6159e1 applies to any subfamily of Epp: if each class separately has assigned degree o(p) at rank-p vertices, their union does as well; more weakly, it is enough to derive the contradiction from whichever class has linear global size.
