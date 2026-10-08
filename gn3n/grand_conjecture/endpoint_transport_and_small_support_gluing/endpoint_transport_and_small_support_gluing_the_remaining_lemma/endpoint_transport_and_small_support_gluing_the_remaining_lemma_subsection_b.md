# Half-order maximal support

## Composition

### A maximal support contains at least half the tournament

**Lemma 13 (half-order bound).** Let (H) be a minimum counterexample on (n) vertices, and let
[
Ssubsetneq V(H)
]
be a maximum-cardinality Hamiltonian support satisfying
[
operatorname{pc}(H-S)=2.
]
Put
[
k=|S|.
]
Then
[
n-1le 2k.
]
Equivalently,
[
kge leftlceilrac{n-1}{2}ightceil.
]

**Proof.** Fix any vertex (xin V(H)). Since (H) is a minimum counterexample,
[
operatorname{pc}(H-x)le2.
]
The tournament (H-x) cannot be Hamiltonian, because then a Hamilton path on (H-x) together with the singleton path ({x}) would two-cover (H). Hence
[
H-x=Amid B
]
for two nonempty Hamiltonian paths (A,B).

Now (A) itself is a proper Hamiltonian support whose complement is two-coverable:
[
H-A=Bmid{x}.
]
By maximality of (S),
[
|A|le k.
]
Similarly,
[
H-B=Amid{x}
]
is two-coverable, so
[
|B|le k.
]
Therefore
[
n-1=|A|+|B|le2k.
]
(square)

Thus the maximal-support normalization controls at least half of the ground set. If
[
H-S=Pmid Q,
]
then
[
|P|+|Q|=n-kle k+1.
]
In particular the absorption problem is a majority-support problem: the fixed Hamiltonian support is at least as large as its entire complement up to one vertex.

This quantitative fact is independent of the displayed cover (Pmid Q) and should be used together with the sandwich-splice thresholds above.

## Development

### A maximal support contains at least half the tournament

**Lemma 13 (half-order bound).** Let (H) be a minimum counterexample on (n) vertices, and let
[
Ssubsetneq V(H)
]
be a maximum-cardinality Hamiltonian support satisfying
[
operatorname{pc}(H-S)=2.
]
Put
[
k=|S|.
]
Then
[
n-1le 2k.
]
Equivalently,
[
kge leftlceilrac{n-1}{2}ightceil.
]

**Proof.** Fix any vertex (xin V(H)). Since (H) is a minimum counterexample,
[
operatorname{pc}(H-x)le2.
]
The tournament (H-x) cannot be Hamiltonian, because then a Hamilton path on (H-x) together with the singleton path ({x}) would two-cover (H). Hence
[
H-x=Amid B
]
for two nonempty Hamiltonian paths (A,B).

Now (A) itself is a proper Hamiltonian support whose complement is two-coverable:
[
H-A=Bmid{x}.
]
By maximality of (S),
[
|A|le k.
]
Similarly,
[
H-B=Amid{x}
]
is two-coverable, so
[
|B|le k.
]
Therefore
[
n-1=|A|+|B|le2k.
]
(square)

Thus the maximal-support normalization controls at least half of the ground set. If
[
H-S=Pmid Q,
]
then
[
|P|+|Q|=n-kle k+1.
]
In particular the absorption problem is a majority-support problem: the fixed Hamiltonian support is at least as large as its entire complement up to one vertex.

This quantitative fact is independent of the displayed cover (Pmid Q) and should be used together with the sandwich-splice thresholds above.
