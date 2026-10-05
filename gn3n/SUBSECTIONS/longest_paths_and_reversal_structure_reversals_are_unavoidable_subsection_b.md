# Neutral internalization of a double reversal

## Metadata

- ID: longest_paths_and_reversal_structure_reversals_are_unavoidable_subsection_b
- Parent Section: longest_paths_and_reversal_structure_reversals_are_unavoidable
- Position: 2
- Row version: 3
- Development version: 3
- Composition version: 1
- Composition stale: False

## Composition

### Every terminal witness has two neutral swaps into either four-component

**Lemma 9 (two neutral witness swaps).** Let
[
Tmid Amid B
]
be a spanning (3|4|4) three-cover, and let (win T). Then there are at least two distinct vertices
[
a,a'in A
]
such that
[
(A-a)+w
qquad	ext{and}qquad
(A-a')+w
]
are Hamiltonian four-sets.

For every such (a), the three-set
[
(T-w)+a
]
is Hamiltonian. Hence
[
Tmid Amid B
longrightarrow
igl((T-w)+aigr)midigl((A-a)+wigr)mid B
]
is a neutral (3|4|4) pairwise repartition.

The same conclusion holds with (A,B) interchanged.

**Proof.** Consider the five-set
[
F=Acup{w}.
]
Every five-vertex boundary tournament has at least three Hamiltonian four-subsets. One of them is (A=F-{w}). Therefore at least two of the remaining four deletions
[
F-{a}=(A-a)+w,qquad ain A,
]
are Hamiltonian.

For every such (a), the set ((T-w)+a) has order three, and every three-vertex boundary tournament has a Hamilton tight path. Thus the displayed repartition is legal. Both sides have profile (3|4), so the quadratic potential is unchanged. (square)

This neutral mobility is independent of the reversal certificate: every distinguished vertex of the three-component has at least two ways to enter either four-component.

**Corollary 10 (double reversal internalization).** Suppose additionally that
[
A=(a_1,a_2,a_3,a_4)
]
and that (w) reverses both displayed end edges:
[
(a_2,a_1,w),
qquad
(w,a_4,a_3)
]
are tight. Then there is a neutral witness swap as in Lemma 9 whose new four-component contains (w) together with an entire reversed end edge and its reversing tight triple.

More precisely, for every swappable (ain A):

- if (ain{a_1,a_2}), the new four-component contains
  [
  {w,a_3,a_4}
  ]
  and retains the tight reversal
  [
  (w,a_4,a_3);
  ]

- if (ain{a_3,a_4}), the new four-component contains
  [
  {a_1,a_2,w}
  ]
  and retains the tight reversal
  [
  (a_2,a_1,w).
  ]

Since Lemma 9 supplies at least two swappable vertices, at least one such neutral internalization always exists. (square)

Thus the difficult double-reversal branch can be moved, without changing the terminal (3|4|4) profile, to a state in which the reversing vertex and a complete reversed edge lie inside one Hamiltonian four-component. This is stronger than preserving only the witness and one old endpoint: the full local reversal certificate survives the neutral move.

## Development

### Every terminal witness has two neutral swaps into either four-component

**Lemma 9 (two neutral witness swaps).** Let
[
Tmid Amid B
]
be a spanning (3|4|4) three-cover, and let (win T). Then there are at least two distinct vertices
[
a,a'in A
]
such that
[
(A-a)+w
qquad	ext{and}qquad
(A-a')+w
]
are Hamiltonian four-sets.

For every such (a), the three-set
[
(T-w)+a
]
is Hamiltonian. Hence
[
Tmid Amid B
longrightarrow
igl((T-w)+aigr)midigl((A-a)+wigr)mid B
]
is a neutral (3|4|4) pairwise repartition.

The same conclusion holds with (A,B) interchanged.

**Proof.** Consider the five-set
[
F=Acup{w}.
]
Every five-vertex boundary tournament has at least three Hamiltonian four-subsets. One of them is (A=F-{w}). Therefore at least two of the remaining four deletions
[
F-{a}=(A-a)+w,qquad ain A,
]
are Hamiltonian.

For every such (a), the set ((T-w)+a) has order three, and every three-vertex boundary tournament has a Hamilton tight path. Thus the displayed repartition is legal. Both sides have profile (3|4), so the quadratic potential is unchanged. (square)

This neutral mobility is independent of the reversal certificate: every distinguished vertex of the three-component has at least two ways to enter either four-component.

**Corollary 10 (double reversal internalization).** Suppose additionally that
[
A=(a_1,a_2,a_3,a_4)
]
and that (w) reverses both displayed end edges:
[
(a_2,a_1,w),
qquad
(w,a_4,a_3)
]
are tight. Then there is a neutral witness swap as in Lemma 9 whose new four-component contains (w) together with an entire reversed end edge and its reversing tight triple.

More precisely, for every swappable (ain A):

- if (ain{a_1,a_2}), the new four-component contains
  [
  {w,a_3,a_4}
  ]
  and retains the tight reversal
  [
  (w,a_4,a_3);
  ]

- if (ain{a_3,a_4}), the new four-component contains
  [
  {a_1,a_2,w}
  ]
  and retains the tight reversal
  [
  (a_2,a_1,w).
  ]

Since Lemma 9 supplies at least two swappable vertices, at least one such neutral internalization always exists. (square)

Thus the difficult double-reversal branch can be moved, without changing the terminal (3|4|4) profile, to a state in which the reversing vertex and a complete reversed edge lie inside one Hamiltonian four-component. This is stronger than preserving only the witness and one old endpoint: the full local reversal certificate survives the neutral move.
