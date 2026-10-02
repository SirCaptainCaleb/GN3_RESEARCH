# Every globally minimum-side deletion cover has a cross-end four-vertex connector

## Statement

Let H be a minimum counterexample. Let mu be the minimum smaller-component order among all two-covers of one-vertex deletions, and choose any deletion cover
H-x=P|Q
with |P|=mu<=|Q|, displayed as P=(p_0,...,p_r), Q=(q_0,...,q_s). Then at least one of the two facing cross-end four-tuples supplied by ab8c0e2136f9 is a tight path. Equivalently, the simultaneous connector-free endpoint-peel branch of fe98a0b8adf0 is impossible.

## Body

Assume for contradiction that neither facing endpoint pair gives the four-vertex connector of ab8c0e2136f9.

Because P has globally minimum deletion-side order mu, neither application of ab8c0e2136f9 can use the alternative that transfers an endpoint out of P: that would create a deletion two-cover with a component of order mu-1.

Hence both transfers from Q into P are forced. The proof of fe98a0b8adf0 then gives both tight join triples
(q_s,p_0,p_1)
and
(p_{r-1},p_r,q_0).
Together with the inherited triples of P, these make
T=(q_s,p_0,p_1,...,p_r,q_0)
a tight path.

The original displayed path
Q=(q_0,q_1,...,q_s)
is also tight. The two paths T and Q have exactly the two endpoints q_s,q_0 in common and have disjoint interiors: the interior of T is V(P), while the interior of Q is {q_1,...,q_{s-1}}. Traversing T from q_s to q_0 and then Q from q_0 back to q_s therefore gives a vertex-simple tight cycle on
V(P) union V(Q)=V(H)-{x}.

Opening this cycle at any cyclic edge yields a Hamilton tight path on H-x. Together with the singleton path {x}, this is a spanning two-cover of H, contradicting that H is a counterexample.

Therefore at least one facing cross-end connector must occur.