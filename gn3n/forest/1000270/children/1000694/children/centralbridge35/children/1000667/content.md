# The grand theorem reduces to no trapping of canonical three-or-five bridge states

## Statement

Let H be a minimum counterexample. For every exact deletion two-cover H-x=P|Q, the canonical central-bridge three-cover supplied by centralbridge35 lies in an Astra-003 connected component containing no cover with at most two components. Consequently the grand two-cover conjecture follows from the order-independent closure statement that no canonical central-bridge state of either the 3-bridge or 5-bridge form can lie in a trapped Astra-003 component.

## Body

# Canonical-bridge reduction of the grand theorem

Assume the grand two-cover conjecture is false and let H be a minimum-order counterexample.

Fix an arbitrary vertex x. By the minimum-counterexample calculus, H-x has an exact two-path cover

P|Q,

with P=(p_0,...,p_m) and Q=(q_0,...,q_s).

By centralbridge35, this deletion state canonically produces one of two spanning three-path covers of H.

If (p_m,x,q_0) is tight, the state is

P^- | (p_m,x,q_0) | Q^+,

where P^-=(p_0,...,p_{m-1}) and Q^+=(q_1,...,q_s).

If (p_m,x,q_0) is non-tight, the state is

P^{--} | (q_1,q_0,x,p_m,p_{m-1}) | Q^{++},

where P^{--}=(p_0,...,p_{m-2}) and Q^{++}=(q_2,...,q_s).

In both cases the middle component is a checked tight path of order 3 or 5 supported entirely on the canonical width-three join window and its forced reversals.

Now consider the Astra-003 connected component K of this three-cover under pairwise repartition moves.

If K contained a spanning cover with at most two components, then H itself would have path-cover number at most two, contradicting the assumption that H is a counterexample. Therefore K is trapped: every state in K has exactly three nonempty components.

Since x and the exact deletion cover P|Q were arbitrary, every exact deletion state of a minimum counterexample supplies such a trapped canonical bridge component.

Hence it is enough to prove the following order-independent closure statement:

> No canonical central-bridge state arising from an exact deletion two-cover can belong to a trapped Astra-003 component.

Indeed, if that closure statement held for all finite boundary tournaments, applying it to any exact deletion cover of a minimum counterexample would contradict the preceding paragraph.

Equivalently, the grand theorem reduces to proving that from either canonical bridge form above, repeated legal pairwise repartitions must eventually merge two components.

This reduction is independent of the order of H. The bounded object is not the ambient tournament but only the central interface: an order-3 or order-5 tight bridge tied to two inherited outer subpaths from one exact deletion cover.
