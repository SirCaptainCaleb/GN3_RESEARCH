# The recurrent flat A2 cycle contains a perfect seven coordinate threshold weave

## Metadata

- ID: the_recurrent_flat_a2_cycle_contains_a_perfect_seven_coordinate_threshold_weave
- Parent Section: ternary_protected_bridges_and_scan_obstructions
- Position: 4
- Row version: 1
- Development version: 1
- Composition version: None
- Composition stale: False

## Composition

(none yet)

## Development

## The recurrent flat A2 cycle contains a perfect seven-coordinate threshold weave

Assume the nontrivial (d=e=2) same-profile flat replacement cycle. Use the notation
[
ldots,A,B,z,y,C,D,ldots qquad(	ext{omit }x),
]
[
ldots,A,B,y,x,C,D,ldots qquad(	ext{omit }z),
]
[
ldots,A,B,x,z,C,D,ldots qquad(	ext{omit }y),
]
where all three deletion carriers have the same word (0^p1^q), with the switch between the windows
[
alpha(A,B,cdot)=0
]
and
[
alpha(B,cdot,cdot)=1.
]

The shared carriers give
[
alpha(A,B,x)=alpha(A,B,y)=alpha(A,B,z)=0,
]
[
alpha(B,x,z)=alpha(B,z,y)=alpha(B,y,x)=1,
]
[
alpha(x,z,C)=alpha(z,y,C)=alpha(y,x,C)=1,
]
and, because the next suffix window is still in the 1-phase,
[
alpha(x,C,D)=alpha(y,C,D)=alpha(z,C,D)=1.
]

### Proposition

The full seven-coordinate order
[
oxed{
(A,B,x,z,C,D,y)
}
]
has threshold word
[
oxed{
0,1,1,1,1.
}
]

### Proof

Its consecutive statuses are
[
alpha(A,B,x)=0,
]
[
alpha(B,x,z)=1,
]
[
alpha(x,z,C)=1,
]
[
alpha(z,C,D)=1,
]
and
[
alpha(C,D,y)=alpha(y,C,D)=1
]
by cyclic invariance. QED.

Cyclically rotating the residual names gives two companion weaves:
[
(A,B,z,y,C,D,x),
]
[
(A,B,y,x,C,D,z),
]
again with word (0,1,1,1,1).

### Boundary consequence

This weave keeps the left ordered boundary pair ((A,B)) exactly fixed and absorbs all three residual vertices into a perfect local (0	o1) threshold block.

Only the right boundary changes: the original protected suffix begins with
[
(C,D,E,F,ldots),
]
whereas the weave ends in
[
(C,D,y,E,F,ldots).
]

Thus after substitution the only new statuses not already controlled are
[
alpha(D,y,E),
qquad
alpha(y,E,F).
]
After those two windows, the untouched color-1 suffix resumes.

Therefore the recurrent (A_2) exchange cycle has been reduced to a **two-window right-boundary reconnection problem**. No internal switch obstruction remains.

Moreover
[
alpha(D,y,E)=1-alpha(y,D,E),
qquad
alpha(y,E,F)=s_y(E,F),
]
so the two-window boundary packet is exactly a local two-bit function of the omitted-vertex suffix scan. If both bits are (1), the weave closes NOR immediately; every surviving counterexample must force at least one of them to be (0).

This is a protected full-support surgery: no prefix coordinate is reordered, and every suffix coordinate is retained.

## Frontier

- Development version when composed: None
- Development version now: 1
