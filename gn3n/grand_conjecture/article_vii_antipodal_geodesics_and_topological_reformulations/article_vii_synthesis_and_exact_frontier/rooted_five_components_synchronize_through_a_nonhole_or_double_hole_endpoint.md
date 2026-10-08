# Rooted five-components synchronize through a nonhole or double-hole endpoint

## Composition

(none yet)

## Development

## Rooted five-components synchronize through a nonhole or a double-hole endpoint

Let
\[
Y
\]
be a Hamiltonian five-set containing two distinguished labels \(x,y\), and write
\[
N=Y-\{x,y\},\qquad |N|=3.
\]
Let \(T=(t_1,\ldots,t_m)\) be a disjoint tight path, \(m\ge6\). Assume both six-sets
\[
Y\cup\{t_1\},\qquad Y\cup\{t_m\}
\]
are non-Hamiltonian.

For \(e\in\{t_1,t_m\}\), define
\[
G_e=\{r\in Y:(Y-\{r\})\cup\{e\}\text{ is Hamiltonian}\}.
\]
By the four-of-six theorem,
\[
|G_e|\ge3.
\]

Then at least one of the following holds.

1. **Hole-preserving common core.** There is
\[
r\in N
\]
with
\[
r\in G_{t_1}\cap G_{t_m}.
\]
Hence the same four-label core \(Y-\{r\}\), which still contains both distinguished labels \(x,y\), accepts both endpoints of \(T\).

2. **Double-hole endpoint.** For one endpoint \(e\in\{t_1,t_m\}\),
\[
\{x,y\}\subseteq G_e.
\]
Equivalently, both
\[
(Y-\{x\})\cup\{e\},
\qquad
(Y-\{y\})\cup\{e\}
\]
are Hamiltonian.

**Proof.**
Assume no nonhole lies in both good sets. Then
\[
(G_{t_1}\cap N)\cap(G_{t_m}\cap N)=\varnothing.
\]
If neither good set contained both \(x\) and \(y\), each would contain at most one distinguished label. Since each has order at least three, each would then contain at least two labels of the three-set \(N\). Two disjoint subsets of a three-set cannot both have order at least two, contradiction. Therefore one endpoint good set contains both \(x,y\). ∎

For a rooted five-component produced from a minimum deletion pair, the first branch permits endpoint transport while retaining the entire minimum pair inside the moving four-core. The second branch is even more rigid: at one tail endpoint, deleting either hole from the five-component gives a Hamiltonian replacement with the same three ordinary labels and the same endpoint. Applying the dichotomy to both complementary tails reduces the rooted five-component handoff to a hole-preserving transport branch or two explicit double-hole endpoint certificates.
