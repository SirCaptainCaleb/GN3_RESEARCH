# Large minimum balanced holes force uniform one-hole imbalance — preserved pre-item development

## Large minimum balanced holes force uniform one-hole imbalance

Let H be a boundary 3-tournament with at least one one-hole deletion cover. Define
\[
\zeta_2(H)=\min\{|Y|: H-Y=A\mid B,\ |A|=|B|\},
\]
and let
\[
\mu_1(H)=\min\bigl\{\bigl||A|-|B|\bigr|:
H-x=A\mid B\text{ is a one-hole deletion cover}\bigr\}.
\]

### Proposition
\[
\boxed{\zeta_2(H)\le 1+\mu_1(H).}
\]

More strongly, for every one-hole deletion cover
\[
H-x=A\mid B,\qquad |A|=a\le b=|B|,
\]
one has
\[
\zeta_2(H)\le 1+(b-a).
\]

Proof. Choose a displayed Hamilton order on B and delete b-a vertices from one end of that path. The surviving subpath B' has order a and is Hamiltonian. Then
\[
H-\bigl(\{x\}\cup(B-B')\bigr)=A\mid B'
\]
is a balanced deletion cover with hole order 1+b-a. Taking the minimum proves the claim. QED.

Hence if \(\zeta_2(H)=z\), every one-hole deletion cover has imbalance at least
\[
\bigl||A|-|B|\bigr|\ge z-1.
\]

### Minimum-counterexample consequence
Let H be a minimum-order counterexample. Then \(\kappa_2(H)=1\), so H-x has a two-cover for every vertex x. If \(\zeta_2(H)\ge3\), then every one-hole deletion cover of every H-x has support-size imbalance at least two. In particular every \(\Psi\)-minimal deletion cover
\[
H-x=P\mid Q,\qquad |Q|\ge |P|+2,
\]
lies in the imbalanced minimum-hole regime.

Write
\[
P=(p_1,\ldots,p_s),\qquad Q=(q_1,\ldots,q_t).
\]
Use the fixed-pair orientation classes through \(\{p_1,p_s\}\) on
\[
\{x,q_1,q_t\}.
\]

### One-hole specialization
For every x, one of the following holds.

1. **Rooted four-component three-cover.** H has a spanning three-cover
\[
K\mid P^\circ\mid Q'
\]
where K is a Hamiltonian four-set containing x and two exposed endpoints of the displayed deletion cover, and the other two components are inherited contiguous subpaths.

2. **Minority-hole signature.** The long-side endpoints q_1,q_t lie in the same fixed-pair orientation class and x lies in the opposite class.

Proof. If q_1,q_t lie in opposite classes, x agrees with exactly one endpoint q(x). Then
\[
K=\{p_1,p_s,q(x),x\}
\]
is Hamiltonian by the fixed-pair same-class theorem, and the inherited interiors give the spanning three-cover already recorded in the imbalanced minimum-hole theorem.

If q_1,q_t lie in the same class and x lies in that same class, then
\[
K=\{p_1,p_s,q_1,x\}
\]
is Hamiltonian. Removing these four vertices leaves the inherited path
\[
(p_2,\ldots,p_{s-1})
\]
and inherited tail
\[
(q_2,\ldots,q_t),
\]
so again H has the required spanning three-cover.

The only remaining case is exactly the minority-hole signature. QED.

### Strategic meaning
Thus a large minimum balanced hole cannot remain an isolated zero-root phenomenon. It forces a global deletion-by-deletion dichotomy: every vertex is either carried by an anchored four-component spanning three-cover, or is the unique minority label against both exposed endpoints of the long side of a \(\Psi\)-minimal deletion cover.

A single bounded four-support is not claimed as closure. The useful content is the simultaneous constraint over every deleted label.
