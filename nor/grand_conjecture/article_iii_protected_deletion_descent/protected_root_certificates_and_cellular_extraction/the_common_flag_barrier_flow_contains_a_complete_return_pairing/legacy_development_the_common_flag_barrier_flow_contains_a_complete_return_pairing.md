# The common-flag barrier flow contains a complete return pairing — preserved pre-item development

## Composition

(none yet)

## Development

## The common-flag barrier flow contains a complete return pairing

Continue from §284. A fully-curved barrier realizes the protected square
[
x	o y,quad x	o b,quad a	o y,quad a	o b,
]
and one nested proper-face flag carries an acyclic positive return flow from target shore
[
{y,b}
]
to source shore
[
{x,a},
]
with equal supply at (y,b) and equal demand at (x,a).

Normalize the total supply at each target to (1).

### Path decomposition

Because the return support is a finite acyclic directed graph, decompose the flow into weighted directed source-to-sink paths.

Let
[
M=
egin{pmatrix}
m_{yx} & m_{ya}\
m_{bx} & m_{ba}
end{pmatrix}
]
record the total path weight from each target source (y,b) to each source-shore sink (x,a).

Every row sum and every column sum equals (1). Hence
[
M=
egin{pmatrix}
t & 1-t\
1-t & t
end{pmatrix}
]
for some (0le tle1).

If (t>0), the path decomposition contains:

- an actual monotone canonical path (yleadsto x);
- an actual monotone canonical path (bleadsto a).

If (t<1), it contains:

- an actual monotone canonical path (yleadsto a);
- an actual monotone canonical path (bleadsto x).

Therefore at least one of the two perfect pairings of the barrier shores is realized by two return paths lying in the **same flag-compatible canonical digraph**.

Closing those paths with the corresponding two barrier edges gives two witnessed directed root cycles on one common flag.

### Intersection-switching lemma

Suppose the realized pairing is
[
yleadsto x,qquad bleadsto a
]
and the two paths meet at a vertex (z).

Since both paths are directed forward in the same chamber order, each has a well-defined prefix to (z) and suffix from (z). Swap the two suffixes:
[
yleadsto zleadsto a,qquad
bleadsto zleadsto x.
]
These are also directed paths using the same canonical root edges.

Thus whenever the two paths of one pairing intersect, the opposite pairing is supported as well. The same argument applies starting from the cross pairing.

### Dichotomy

Every fully-curved barrier therefore has one of two strengthened common-flag return forms:

1. **disjoint-pair form:** one barrier pairing has two internally vertex-disjoint monotone canonical return paths;
2. **double-pair form:** both perfect pairings of the (K_{2,2}) barrier shores are supported by monotone canonical return paths in the same flag graph.

This removes fractional branching from the §284 frontier. The remaining realization problem is now a two-path gluing problem on one flag, with the local backward square already fully realized.
