# Minimum directed N_4 counterexamples yield four-change extremal cycles — preserved pre-item development

## Development

## Four-change extremal cycle at directed N_4

Work in the directed translation-invariant sector of (N_4), so the coordinate label has arity (r=3):
[
h(a,b,c)in{0,1},qquad h(c,b,a)=1-h(a,b,c).
]

Assume a counterexample exists and choose one on a ground set (V) of minimum size (n). Put
[
s=n-3.
]
Fix (xin V), and let
[
sigma=(x_1,ldots,x_{n-1})
]
be any one-change ordering of (Vsetminus{x}). By minimum-counterexample endpoint blocking its triple-status word has the form
[
a^p(1-a)^q,qquad p,qge1,qquad p+q=s.
]

Close (x,sigma) into the cyclic coordinate order
[
C=(x,x_1,ldots,x_{n-1}).
]
Write its cyclic triple-status word as (u_0,ldots,u_{n-1}). With the natural indexing,
[
u_0=1-a,
]
[
(u_1,ldots,u_s)=a^p(1-a)^q,
]
and endpoint blocking at the other end gives
[
u_{s+1}=a.
]
Because (n=s+3), there is only one remaining cyclic status,
[
u_{s+2}=w:=h(x_{n-1},x,x_1).
]

### Lemma
The cyclic status word of (C) has exactly four changes.

### Proof
Along
[
u_0,u_1,ldots,u_{s+1}
]
there are exactly three changes: one from (u_0=1-a) to (u_1=a), the unique change inside the deletion word, and one from (u_s=1-a) to (u_{s+1}=a).

The two remaining cyclic transitions run
[
a=u_{s+1}longrightarrow w=u_{s+2}longrightarrow u_0=1-a.
]
Since their endpoints differ, exactly one of these two transitions changes color. Hence the total cyclic variation is exactly
[
q(C)=4.
]
(square)

### Extremality
In any directed (N_4) counterexample, every cut of every cyclic coordinate order is bad. If (d_i=u_ioplus u_{i+1}) is the cyclic transition word, each cut retains a block of (s=n-3) consecutive transition bits and therefore
[
d_i+cdots+d_{i+s-1}ge2.
]
Summing over all (n) cuts gives
[
s,q(C)ge2n.
]
A cyclic binary word has even variation, and
[
rac{2n}{n-3}>2,
]
so every cyclic coordinate order in a counterexample has (q(C)ge4). Thus the cycle constructed above is globally minimum-variation.

Because this particular cycle has total transition weight four, the bad-cut condition is also equivalent to saying that no three consecutive cyclic transition bits are all (1): a retained block of (n-3) transitions has weight at least two exactly when its complementary block of three transitions has weight at most two.

Finally, the full cyclic status word is
[
(1-a),,a^p,,(1-a)^q,,a,,w.
]
If (w=a), its four cyclic run lengths are
[
1,p,q,2;
]
if (w=1-a), they are
[
2,p,q,1
]
up to cyclic rotation. Hence every deleted-vertex one-change order in a minimum directed (N_4) counterexample closes to a globally minimum four-run cycle having a singleton run and a length-two run adjacent to the reinserted vertex.

### Closure significance
This replaces the weaker two-tight-window normalization at (r=3) by a complete extremal cyclic profile. A closure proof may therefore start from a minimum-variation four-run cycle and target the forced singleton run by a local reversal, transposition, or recentering exchange. Any such move producing variation (0) or (2) contradicts the universal lower bound (qge4).
