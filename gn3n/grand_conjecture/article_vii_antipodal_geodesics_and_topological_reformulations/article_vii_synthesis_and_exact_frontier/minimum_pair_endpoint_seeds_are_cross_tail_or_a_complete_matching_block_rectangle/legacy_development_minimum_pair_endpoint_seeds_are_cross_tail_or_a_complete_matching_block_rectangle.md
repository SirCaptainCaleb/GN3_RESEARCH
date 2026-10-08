# Minimum-pair endpoint seeds are cross-tail or a complete matching-block rectangle — preserved pre-item development

## Composition

(none yet)

## Development

## Exposed minimum-pair seeds are cross-tail or form a complete matching-block rectangle

Let
\[
X=\{x,y\}
\]
be a minimum deletion pair and let
\[
H-X=P\mid Q,
\qquad
P=(p_1,\ldots,p_m),\quad Q=(q_1,\ldots,q_t),
\]
with \(m,t\ge2\). Put
\[
E_P=\{p_1,p_m\},\qquad E_Q=\{q_1,q_t\}.
\]

Partition the four exposed endpoints by orientation through the fixed pair \(\{x,y\}\):
\[
E_+=\{z:h(x,z,y)=1\},
\qquad
E_-=\{z:h(y,z,x)=1\}.
\]

Then exactly one of the following structural alternatives occurs.

### Cross-tail seed

There exist
\[
p\in E_P,\qquad q\in E_Q
\]
such that
\[
\{x,y,p,q\}
\]
is Hamiltonian. Its complement is covered by the inherited truncations of \(P,Q\), so this is a hole-containing cross-tail four-seed with inherited two-interval complement.

### Complete matching-block residue

Assume no cross-tail four-set
\[
\{x,y,p,q\},\qquad p\in E_P,\ q\in E_Q,
\]
is Hamiltonian.

Then the two endpoints of \(P\) must lie in one fixed-pair orientation class and the two endpoints of \(Q\) in the other. Indeed, if the two endpoints of \(P\) belonged to different classes, every \(q\in E_Q\) would agree with one of them and the fixed-pair same-class theorem would give a cross-tail Hamiltonian four-set. The same argument applies to \(Q\).

After exchanging \(x,y\) if necessary,
\[
E_P\subseteq E_+,\qquad E_Q\subseteq E_-.
\]
Hence the same-rail supports
\[
\boxed{\{x,y,p_1,p_m\}\text{ Hamiltonian}},
\qquad
\boxed{\{x,y,q_1,q_t\}\text{ Hamiltonian}}
\]
by the fixed-pair same-class theorem.

By assumption every cross pair \(p\in E_P,q\in E_Q\) is bad. Thus the fixed-pair bad-extension graph on the four exposed endpoints is exactly
\[
K_{2,2}=E_P\times E_Q,
\]
the extremal complete-bipartite case.

The fixed-pair hook theorem therefore gives, for every
\[
p\in E_P,\qquad q\in E_Q,
\]
the matching-block rectangle
\[
h(x,p,y)=1,\qquad
h(y,q,x)=1,
\]
\[
\boxed{h(p,x,q)=1,\qquad h(q,y,p)=1.}
\]

Thus failure of a cross-tail hole seed does not leave an arbitrary same-rail alternative. It forces two opposite same-rail hole-containing four-seeds and a complete four-by-four family of cross-tail hook relations through the two holes.

Each same-rail seed has inherited two-interval complement: deleting both endpoints of one displayed path leaves its interior interval together with the other path. Hence either branch is compatible with interval-preserving seed maximalization.
