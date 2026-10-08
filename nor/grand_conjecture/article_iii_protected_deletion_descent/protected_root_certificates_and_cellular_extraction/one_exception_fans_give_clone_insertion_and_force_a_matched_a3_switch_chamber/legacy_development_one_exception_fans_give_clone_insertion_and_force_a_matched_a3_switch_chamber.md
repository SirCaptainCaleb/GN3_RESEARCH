# One-exception fans give exact clone insertion — preserved pre-item development

## One-exception fans give exact clone insertion

Assume the one-exception fan branch of the preceding fixed-cut A3 dichotomy actually occurs.

Suppose a pre-side label is carried by
[
(a,b,c),
]
with pre target (eta), and its fan is
[
alpha(a,b,c)=1-eta,
qquad
alpha(b,c,x)=eta
quad
(x
otin{a,b,c}).
]

### Clone identity

For distinct (x,y
otin{b,c}), coboundary flatness on ({x,y,b,c}) gives
[
alpha(x,y,b)oplusalpha(x,y,c)
=
alpha(x,b,c)oplusalpha(y,b,c).
]
By cyclic invariance,
[
alpha(x,b,c)=alpha(b,c,x).
]
Hence
[
alpha(x,y,b)=alpha(x,y,c)
]
whenever neither (x) nor (y) equals (a), while the two values are opposite whenever exactly one of (x,y) equals (a).

Thus (b) and (c) are exact ternary clones in every context avoiding the unique exceptional coordinate (a).

### Exact deletion insertion away from the exception

Let a one-change order of (Vsetminus{b}) contain
[
cdots,x,y,c,z,w,cdots
]
and put
[
B=alpha(y,c,z).
]

If (B=eta) and (a
otin{x,y,z}), insert (b) immediately before (c):
[
cdots,x,y,b,c,z,w,cdots.
]
Then
[
alpha(x,y,b)=alpha(x,y,c),
]
and
[
alpha(y,b,c)=eta=B,
qquad
alpha(b,c,z)=eta=B.
]
So the new status word is exactly the old one with the bit (B) duplicated.

If (B=1-eta) and (a
otin{y,z,w}), insert (b) immediately after (c):
[
cdots,x,y,c,b,z,w,cdots.
]
Then
[
alpha(y,c,b)=1-eta=B,
qquad
alpha(c,b,z)=1-eta=B,
]
and the clone identity gives
[
alpha(b,z,w)=alpha(c,z,w).
]
Again the new word is exactly the old word with (B) duplicated.

Therefore either insertion gives an ACTUAL spanning one-change order whenever the side matching (B) avoids the exceptional coordinate (a).

Consequently, in a counterexample, any one-change deletion order of (Vsetminus{b}) to which this fan applies must obey the local positional obstruction
[
B=etaLongrightarrow ain{x,y,z},
]
or
[
B=1-etaLongrightarrow ain{y,z,w},
]
respectively. Endpoint versions have weaker exceptional sets because fewer outer windows are changed.

### Post-side symmetry

For the post-side fan branch of a label ((a,b,c)), the leading pair ((a,b)) has the analogous clone property outside the exceptional coordinate (c), and the same deletion-insertion statement holds after reversal.

### Conditional repeated-middle observation

If one additionally has a **valid** sign-separated-middle reduction for the same carrier, then the (n+1)-label pigeonhole supplies two support labels with the same middle and same side sign. Under their fan branches, two distinct pre-side labels
[
(a,b,c),qquad(d,b,e)
]
cannot have disjoint/nonconcatenating physical roots: if (e
otin{a,b,c}) and (c
otin{d,b,e}), the two fans give
[
alpha(b,c,e)=eta=alpha(b,e,c),
]
contradicting alternation. Hence (e=a) or (d=c). The post-side case is symmetric.

For a concatenating pair
[
(a,b,c),qquad(c,b,e),
]
the two fans imply
[
alpha(a,b,e)=eta,qquad
alpha(b,e,c)=1-eta,
]
so the exact A3 chamber
[
a,b,e,c
]
has a matched central switch pair.

This repeated-middle paragraph is **conditional**. The later four-window neighbor-replacement audit shows that the previous proof of unrestricted complementary-cell termination is insufficient, so the existing sign-separated-middle theorem cannot presently be used as an unconditional counterexample reduction until its extraction step is repaired.

### Consequence

The unconditional output here is the clone-insertion theorem: whenever the one-exception fan branch occurs, the spanning extension problem collapses to a bounded positional obstruction involving the single exceptional coordinate. This is independent of the disputed arbitrary complementary-cell path potential.
