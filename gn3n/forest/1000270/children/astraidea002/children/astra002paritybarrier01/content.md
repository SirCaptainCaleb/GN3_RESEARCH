# Minimum balanced-cover failures force parity-specific noninsertability

## Statement

Let H be a minimum-order counterexample to the balanced two-cover conjecture. If |V(H)|=2k+1, then for every vertex x and every balanced deletion cover H-x=P|Q with |P|=|Q|=k, the omitted vertex x cannot be inserted into any position of either displayed path P or Q. If |V(H)|=2k, then for every x and every balanced deletion cover H-x=P|Q with {|P|,|Q|}={k,k-1}, x cannot be inserted into any position of the smaller (k-1)-vertex component. Consequently, in odd order both deletion components force the two reversed endpoint triples supplied by failed prepend/append, while in even order the smaller component does.

## Body

# Proof

Let H have minimum order among boundary tournaments with no balanced two-cover. Every proper induced subtournament therefore has a balanced two-cover.

Fix x in V(H) and choose a balanced two-cover of H-x.

## Odd order

Let |V(H)|=2k+1. Then H-x has order 2k, so its balanced cover has component orders k and k. Write it as P|Q.

Suppose x can be inserted into some position of the displayed tight path P. Then P+x is a tight path on k+1 vertices, while Q remains a tight path on k vertices. These two paths are disjoint and span H, giving component orders k+1 and k, exactly the balanced target for order 2k+1. This contradicts the choice of H.

Thus x is noninsertable into P. The same argument applies to Q.

In particular x cannot be appended or prepended to either component. If P=(p_0,...,p_{k-1}), failure of append/prepend gives the two outer triples
(p_{k-2},p_{k-1},x) and (x,p_0,p_1)
non-tight, so boundary antisymmetry forces
(x,p_{k-1},p_{k-2}) and (p_1,p_0,x)
tight. The same holds for Q.

## Even order

Let |V(H)|=2k. Then H-x has order 2k-1, so every balanced cover has component orders k and k-1. Write P|Q with |P|=k and |Q|=k-1.

If x could be inserted anywhere into Q, then Q+x would have order k and together with P would give a balanced k|k cover of H, contradiction.

Therefore x is noninsertable into the smaller component Q. In particular it cannot be attached at either end, and boundary antisymmetry forces the corresponding reversed endpoint triples on Q.

Insertion into the larger k-vertex component need not contradict balancedness, because it would produce sizes k+1 and k-1. Hence no corresponding universal noninsertability statement is claimed there.

The argument uses only minimality for the balanced-cover conjecture, not the grand two-cover conjecture.
