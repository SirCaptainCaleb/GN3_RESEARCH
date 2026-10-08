# Three common reversers force a three-cover by finite root advance — preserved pre-item development

## Composition

(none yet)

## Development

## Three common reversers force a three-cover by finite root advance

Let
\[
P=(p_1,\ldots,p_m),\qquad Q=(q_1,\ldots,q_n)
\]
be disjoint tight paths with \(m,n\ge2\), and let
\[
U=\{u,v,w\}
\]
be disjoint from them. Assume every \(z\in U\) reverses both initial exposed edges:
\[
h(p_2,p_1,z)=h(q_2,q_1,z)=1.
\]

**Theorem (finite root-advance three-cover).**
The induced tournament on
\[
V(P)\cup V(Q)\cup U
\]
has a cover by at most three tight paths.

More precisely, the proof either produces a Hamiltonian support of order five or six together with the two untouched corridor tails, or advances to a strictly shorter pair of corridor tails with the same three common reversers.

**Proof.**
Apply [[three_common_initial_reversers_force_a_root_advancing_five_path]]. Up to exchanging \(P,Q\), there are distinct \(u,v\in U\) such that
\[
X=(p_2,p_1,u,q_1,v)
\]
is a tight five-path. Let \(w\) be the third element of \(U\) and put
\[
S=\{p_2,p_1,q_1,u,v,w\}.
\]

If \(H[S]\) is Hamiltonian, then
\[
S\mid(p_3,\ldots,p_m)\mid(q_2,\ldots,q_n)
\]
is a three-cover, omitting empty tails.

Assume \(H[S]\) is non-Hamiltonian. By four-of-six, at least four of the six vertex-deleted five-subsets of \(S\) are Hamiltonian. As in [[root_advance_plus_four_of_six_leaves_one_wrong_root_exception]], if \(S-\{p_2\}\) or \(S-\{q_1\}\) is Hamiltonian, we obtain a three-cover immediately:
\[
(S-\{p_2\})\mid(p_2,\ldots,p_m)\mid(q_2,\ldots,q_n),
\]
or
\[
(S-\{q_1\})\mid(p_3,\ldots,p_m)\mid(q_1,\ldots,q_n).
\]

Hence suppose neither favorable deletion is Hamiltonian. Since at least four deletions are Hamiltonian and there are only four remaining labels
\[
p_1,u,v,w,
\]
all four corresponding deletions are Hamiltonian. In particular, for every \(z\in U\),
\[
K_z:=S-\{z\}
\]
is a Hamiltonian five-set.

Put
\[
P'=(p_3,\ldots,p_m),\qquad Q'=(q_2,\ldots,q_n).
\]
Fix \(z\in U\). If \(z\) prepends \(P'\), i.e. if \(P'\) is empty or has one vertex, or
\[
h(z,p_3,p_4)=1
\]
when \(|P'|\ge2\), then \(K_z\), the resulting path \(zP'\), and \(Q'\) give a three-cover. The same holds if \(z\) prepends \(Q'\).

Therefore, if no three-cover has yet appeared and both shortened tails have order at least two, every \(z\in U\) satisfies
\[
h(z,p_3,p_4)=0,\qquad h(z,q_2,q_3)=0.
\]
Boundary antisymmetry gives
\[
h(p_4,p_3,z)=1,\qquad h(q_3,q_2,z)=1.
\]
Thus the same three labels \(U\) are common reversers of the initial exposed edges of the strictly shorter tight paths
\[
\widetilde P=(p_3,p_4,\ldots,p_m),\qquad
\widetilde Q=(q_2,q_3,\ldots,q_n).
\]
Apply the theorem recursively to \(\widetilde P,\widetilde Q,U\).

At each recursive step the sum of the two tail orders decreases by three, so the process terminates. If one shortened tail has order at most one before another recursive application is possible, choose any Hamiltonian \(K_z\); the leftover \(z\) together with that tail is a tight path of order at most two, and the other tail is tight, again giving a three-cover. \(\square\)

### Consequence for the blocked double-persistent branch

In the common-reverser alternative of [[blocked_exterior_vertices_either_extend_the_opposite_tail_or_force_root_advance]], the three labels are precisely the two deleted endpoint vertices \(x,y\) and one blocked exterior label \(z\). Therefore
\[
P\cup Q\cup\{x,y,z\}
\]
always has path-cover number at most three.

So a blocked exterior label has a stronger transport consequence than the single five-path statement:

\[
\boxed{
\text{opposite-tail extension}
\quad\text{or}\quad
\text{an enlarged local three-cover obtained by finite root advance}.
}
\]

This still does not by itself give the required two-cover/outward replacement. But it removes the orientation-handoff dead end: the root-advance process cannot continue indefinitely or strand an uncontrolled bounded packet. The next step may invoke the established three-cover repartition machinery on this enlarged local cover, rather than solving a new fixed-junction problem from scratch.
