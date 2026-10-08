# A shortcut-free switching split with shore imbalance at most three closes monochromatically — preserved pre-item development

## Development

## Balanced cuts eliminate all nearly balanced switching splits

Use the switching-normalized shortcut-free split
[
B	o z	o A	o x,
]
with every (B)-vertex dominating every (A)-vertex.

Let
[
a=|A|,qquad b=|B|.
]

The following are homogeneous tournament cuts:

[
B ig| {z}cup Acup{x},
]
because every (B)-vertex dominates (z,A,x);

and
[
Bcup{z} ig| Acup{x},
]
because (B	o A,x) and (z	o A,x).

The two left-side sizes are
[
b,qquad b+1,
]
while
[
n=a+b+2.
]

By the balanced homogeneous-cut theorem, NOR closes monochromatically whenever either (b) or (b+1) equals one of
[
lfloor n/2floor,qquad lceil n/2ceil.
]

Equivalently, writing (d=a-b), the two displayed cuts close whenever
[
din{-3,-2,-1,0,1}.
]

Now reverse the connector pair (x,z). Its signature shores are exchanged, so the same argument with (a,b) interchanged covers
[
din{-1,0,1,2,3}.
]

Therefore every shortcut-free split with
[
oxed{|a-b|le3}
]
has a spanning monochromatic NOR order.

### Consequence for a minimum shore

Choose (A) to be the smaller shore. In any unresolved minimum counterexample,
[
oxed{|B|ge |A|+4.}
]

Since the connector block
[
Acup{x,z}
]
has size
[
|A|+2,
]
the larger shore (B) has at least two more vertices than the entire connector block.

Thus there are enough (B)-gaps to interleave every connector coordinate without forcing two connector vertices to be consecutive for cardinality reasons. The remaining obstruction is purely the finite orientation/parity compatibility described by §346, not a shortage of separator positions.
