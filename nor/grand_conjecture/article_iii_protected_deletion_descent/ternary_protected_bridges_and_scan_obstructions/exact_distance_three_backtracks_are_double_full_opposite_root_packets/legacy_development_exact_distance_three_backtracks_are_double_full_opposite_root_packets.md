# Exact distance three backtracks are double full opposite root packets — preserved pre-item development

## Composition

(none yet)

## Development

## Exact distance-three backtracks are double-full opposite-root packets

Work in the coboundary-flat alternating ternary sector. Choose a one-change deletion carrier
[
O=(v_1,ldots,v_m)
]
with normalized word
[
0^p1^q
]
whose first run (p) is globally minimum over all deletion carriers, reversals, and color complements. Let (x) be omitted.

Assume the minimum-run replacement dynamics take the exact distance-three backtrack branch
[
d=e=3.
]
Thus the forced right replacement omits
[
y=v_{p+3}
]
and inserts (x) in its position, producing
[
O'
]
with profile
[
0^{p+3}1^{q-3},
]
and the forced left replacement from (O') restores (O) exactly.

Put
[
a=v_{p+1},qquad z=v_{p+2},qquad b=v_{p+4},qquad c=v_{p+5}
]
when (c) exists.

### Local scan data

Distance (d=3) gives
[
alpha(x,a,z)=
alpha(x,z,y)=
alpha(x,y,b)=
alpha(x,b,c)=0
]
through the relevant protected scan positions.

The original carrier gives
[
alpha(a,z,y)=1,qquad
alpha(z,y,b)=1,qquad
alpha(y,b,c)=1.
]

The intermediate carrier (O') has bridge (000). Hence
[
alpha(a,z,x)=0,qquad
alpha(z,x,b)=0,qquad
alpha(x,b,c)=0.
]

### The pair-insertion packet

Insert both exchanged coordinates and consider
[
(a,z,x,y,b).
]
Its three statuses are
[
alpha(a,z,x)=0,
]
[
alpha(z,x,y)=1-alpha(x,z,y)=1,
]
[
alpha(x,y,b)=0.
]
Thus the exact backtrack canonically contains the singleton packet
[
oxed{0,1,0}.
]

### Both bounding tetrahedra are fully curved

For
[
Q_L={a,z,x,y},
]
the ordered quadruple ((a,z,x,y)) has consecutive colors (0,1), while the opposite face
[
alpha(a,z,y)=1.
]
In the coboundary-flat transition classification this is the fully-curved alternative. Hence (Q_L) is fully curved.

Similarly
[
Q_R={z,x,y,b}
]
has ordered consecutive colors
[
alpha(z,x,y)=1,qquad alpha(x,y,b)=0,
]
and opposite face
[
alpha(z,y,b)=1,
]
so (Q_R) is fully curved.

Therefore every literal distance-three backtrack is a double-full singleton packet on the five physical coordinates
[
{a,z,x,y,b}.
]

Equivalently, the opposite protected-root two-cycle associated with the exchange (xleftrightarrow y) always carries the standard two-full-switch five-set geometry.

### Phase-gap constraint

The intermediate deletion carrier (O') has run profile
[
(p+3,q-3).
]
Reverse it and globally complement colors. This gives another normalized deletion carrier with first run
[
q-3.
]
Since (p) was globally minimum,
[
q-3ge p.
]
Hence
[
oxed{qge p+3.}
]

So an exact distance-three backtrack can occur only when the second phase exceeds the globally minimum first phase by at least three.

### Current elimination target

The flat ternary applicability and recurrence analysis is now reduced to eliminating this packet:
- the short phases (p,qle2) are closed separately;
- the nontrivial distance-two A2 recurrence is killed by the boundary-compatible five-set weave;
- residual drift is finite;
- an exact distance-three return is precisely the double-full opposite-root packet above.

A final flat-sector proof may therefore be phrased either as:
1. a boundary-compatible surgery for this double-full packet across a genuine (0	o1) phase boundary; or
2. an elimination lemma for a protected-root two-cycle with fixed outside order.

The residual five-set holonomy bit remains the only internal local degree of freedom; all other five-set faces are forced by the two full tetrahedra.
