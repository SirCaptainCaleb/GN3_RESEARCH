# All connector vertices share one insertion scan on the opposite shore — preserved pre-item development

## The switching split has one universal connector scan

Use the switching-normalized split
[
B	o z	o A	o x.
]

Let
[
P=(b_1,ldots,b_r)
]
be any coordinate order of (B). For every connector-side coordinate
[
ain Acup{x,z},
]
define its insertion scan along (P) by
[
s_i(a)=alpha(a,b_i,b_{i+1}),
qquad 1le ile r-1.
]

Every (B)-vertex dominates every connector-side coordinate. Hence
[
t(a,b_i)=0,qquad t(b_{i+1},a)=1.
]
Therefore
[
s_i(a)
=
t(a,b_i)oplus t(b_i,b_{i+1})oplus t(b_{i+1},a)
=
1oplus t(b_i,b_{i+1}).
]

Thus the scan is independent of (a). Write
[
oxed{e_i:=s_i(a)=1oplus t(b_i,b_{i+1}).}
]

If switching bits (sigma(b_i)) make (P) a directed Hamiltonian path in an equivalent representative, then
[
e_i=sigma(b_i)oplussigma(b_{i+1}),
]
so this is exactly the edge-switching parity sequence of §333.

### Exact insertion packets

Insert any connector coordinate (a) between (b_i,b_{i+1}). The three new ternary windows are
[
oxed{e_{i-1}, 1-e_i, e_{i+1}}
]
with endpoint clipping.

Consequently, for a good shore word (0^p1^q):

- strictly inside the zero phase, a connector insertion is good exactly at a scan pattern
  [
  010;
  ]
- strictly inside the one phase, it is good exactly at
  [
  101;
  ]
- at the unique phase boundary, goodness is determined by the corresponding three-bit monotonicity condition.

These conditions are the same for every coordinate in (Acup{x,z}).

### Hartman interpretation

The connector side therefore behaves as one color class with respect to continuation into (B): all its vertices have identical reachable insertion targets.

A canonical least-unreachable target can be defined directly from the common scan (e), without choosing a distinguished connector vertex.

If one connector coordinate can be inserted at a given gap while preserving the one-change shore order, then every connector coordinate has the same local insertion status there. Failure is likewise common.

Thus the remaining switching-split problem is a genuine one-dimensional connector problem on the common scan (e), with the five-coordinate seed of §344 supplying a realized multi-vertex connector whenever the single-vertex scan alone is insufficient.
