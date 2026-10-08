# Both-hole seed maximalization yields a saturated deletion-critical complement — preserved pre-item development

## Both-hole seed maximalization yields a saturated deletion-critical complement

Let \(H\) satisfy \(\kappa_2(H)=2\). Suppose \(S_0\) is a Hamiltonian support containing a distinguished minimum deletion pair
\[
X=\{x,y\}
\]
and satisfying
\[
\operatorname{pc}(H-S_0)\le2.
\]
Among Hamiltonian supports \(S\supseteq S_0\) with \(\operatorname{pc}(H-S)\le2\), choose one of maximum cardinality. Write
\[
H-S=P\mid Q,
\qquad
P=(p_1,\ldots,p_m),\quad Q=(q_1,\ldots,q_t).
\]

Then three independent structures hold simultaneously.

### 1. Hole provenance is retained

Because \(S\supseteq S_0\),
\[
\{x,y\}\subseteq S.
\]
Thus every complementary label lies outside the selected minimum pair. The maximal-support normalization has not forgotten which bounded seed came from the genuine two-deletion state.

### 2. Absolute exposed-endpoint nonaugmentability

For every nonempty subset
\[
E\subseteq\{p_1,p_m,q_1,q_t\}
\]
of the displayed complementary endpoints,
\[
H[S\cup E]
\]
is non-Hamiltonian. Deleting \(E\) from the displayed paths leaves at most two inherited tight intervals, so \(S\cup E\) would otherwise be a larger admissible Hamiltonian support still containing \(S_0\).

In particular, for any Hamilton order
\[
S=(s_1,\ldots,s_k),
\]
each exposed endpoint \(e\) satisfies the literal boundary-flip relations
\[
h(s_2,s_1,e)=1,
\qquad
h(e,s_k,s_{k-1})=1.
\]

### 3. The complementary two-cover is Hamiltonian-deletion-critical

Put
\[
G=H-S.
\]
For every \(v\in V(G)\),
\[
G-v
\]
is non-Hamiltonian. Indeed, if \(G-v\) were Hamiltonian, then a Hamilton path on \(S\) together with one on \(G-v\) would two-cover \(H-v\), contradicting \(\kappa_2(H)=2\).

Hence, whenever \(m,t\ge3\), the four endpoint deletions give the second-layer junction forks of [[deletion_critical_complements_force_second_layer_junction_forks]]. For example
\[
h(q_1,p_{m-1},p_{m-2})=1
\quad\text{or}\quad
h(q_2,q_1,p_{m-1})=1,
\]
and
\[
h(q_2,p_m,p_{m-1})=1
\quad\text{or}\quad
h(q_3,q_2,p_m)=1,
\]
with the two opposite-end analogues obtained by symmetry.

Thus a both-hole seed does not merely enter maximal-support theory. It enters a **hole-preserving saturated state** in which:
- the minimum pair remains inside the Hamiltonian support;
- every subset of exposed complementary endpoints is jointly nonaugmenting;
- the complement is one-vertex Hamiltonian-deletion-critical;
- each boundary therefore carries an audit-safe one-layer inward reversal fork.

If one complementary path has order at most two, that side is already a bounded interface. Otherwise all four second-layer forks are available.

### Frontier consequence

The strengthened twelve-label survivor of [[twelve_label_sat_remains_feasible_after_both_hole_seed_selectors_and_immediate_rooted_conversions]] should not be attacked by adding further unconditional local seed clauses. Each both-hole seam seed can instead be maximalized while retaining both holes, and the next obstruction is the compatibility of the four exposed-endpoint nonaugmentability relations with these four deletion-critical second-layer forks.

This imports genuinely new ambient information absent from the twelve-label SAT model while using no minimum-counterexample induction, cyclic rotation, or path reversal.
