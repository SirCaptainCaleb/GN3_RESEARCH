# Rooted descent through bounded supports

## Metadata

- ID: line_rooted_small_support_descent_from_deletion_cover_lifts_subsection_a
- Parent Section: line_rooted_small_support_descent_from_deletion_cover_lifts
- Position: 1
- Row version: 8
- Development version: 8
- Composition version: 1
- Composition stale: False

## Composition

Let \(H\) be a minimum counterexample and let \(H-x=P\mid Q\) be a deletion cover. Its singleton lift \(P\mid Q\mid\{x\}\) lies in the three-cover repartition graph. Write
\[
\Phi(R_1\mid R_2\mid R_3)=|R_1|^2+|R_2|^2+|R_3|^2.
\]

### 1. Descent from the singleton lift

The singleton-lift descent proved in the next subsection gives a pairwise repartition that strictly decreases \(\Phi\) and places \(x\) in a Hamiltonian three-support \(T\). If another component has order at least six, the three-component long-neighbor lemma gives further strict descent. If another component has order five, the balanced-cover proposition gives a \(4|4\) repartition of its union with \(T\), decreasing \(\Phi\) by two. The root remains in the union, although its containing component may change.

### 2. Quadratic-minimal states with a three-support

A spanning three-cover minimizing \(\Phi\) in its repartition component has no components of order one or two. If it contains a three-component, the preceding descents exclude all other orders at least five. Since \(|V(H)|>10\), its profile is exactly \(3|4|4\), and \(|V(H)|=11\).

The \(3|4\) analysis in the next subsection gives a neutral endpoint swap or a controlled \(5|2\) detour. The specialized \(3|4|4\) result gives a neutral swap, an order disagreement, or a common terminal pair for two controlled Hamiltonian five-paths. Profiles containing both orders three and five cannot occur at a quadratic minimum.

### 3. Rooted four-supports

Let \(X\) be a Hamiltonian four-support containing the distinguished root, and let \(C=(c_1,\ldots,c_m)\) be a disjoint displayed tight path. If \(m=6\), the balanced-cover proposition gives a strict \(4|6\longrightarrow5|5\) repartition, with change \(-2\) in \(\Phi\). If \(m\ge7\), the four-path long-pair lemma gives strict descent or a non-Hamiltonian endpoint six-set \(X\cup\{c_1,c_m\}\) whose Hamiltonian five-deletions exhibit an order disagreement.

Consequently a quadratic minimum containing a four-component either has profile \(3|4|4\), exhibits that endpoint order disagreement, or has profile \(4|4|4\), \(4|4|5\), or \(4|5|5\). In the last alternative its order is at most fourteen.

### 4. Rooted five-supports

Let (X) be a Hamiltonian five-support containing the root and let (C=(c_1,ldots,c_m)), (mge6). If one endpoint extends (X), then
[
5mid mlongrightarrow6mid(m-1),
]
with quadratic change (12-2m). This is neutral for (m=6) and strict for (mge7).

Assume neither endpoint extends (X). By [[five_side_endpoint_core_m6_01]] and [[toolkit_common_endpoint_core_or_a_two_pair_root_exchange_split]], either a common endpoint-replacement core preserves the root or the non-root vertices of (X) split into two endpoint-specific pairs. In the exceptional split, [[toolkit_forces_four_core_disturbance_or_an_outer_hamiltonian_sixset]] yields a four-core order disagreement, a Hamiltonian four-set, a positioned core reversal, or a Hamiltonian six-set.

Hence failure of numerical descent at support order five already produces a bounded order-theoretic obstruction or a rooted six-support.

### 5. Rooted six-supports

Let (X) be a proper Hamiltonian six-support containing the root, and write the non-Hamiltonian complement as
[
H-X=Pmid Q.
]
By [[rooted_six_support_transfer_or_comparison_disturbance01]], there is a non-root label (din X) such that (X-d) remains Hamiltonian and ((Pcup Q)+d) has path-cover number two. Comparing a two-cover of ((Pcup Q)+d) with the displayed partition
[
Pmid Qmid{d}
]
gives one of three outcomes:

1. (d) attaches to exactly one old support, producing a root-preserving one-label pairwise transfer;
2. one old support is split into two comparison blocks, yielding a split displayed edge or separated blocks;
3. a comparison edge joins (P) directly to (Q).

Thus rooted descent from a deletion-cover lift remains controlled through support order six. The possible outcomes are strict quadratic descent, explicit neutral recurrence, order disagreement or reversal, a bounded Hamiltonian core, or a comparison-cover disturbance.


## Development

Let \(H\) be a minimum counterexample and let \(H-x=P\mid Q\) be a deletion cover. Its singleton lift \(P\mid Q\mid\{x\}\) lies in the three-cover repartition graph. Write
\[
\Phi(R_1\mid R_2\mid R_3)=|R_1|^2+|R_2|^2+|R_3|^2.
\]

### 1. Descent from the singleton lift

The singleton-lift descent proved in the next subsection gives a pairwise repartition that strictly decreases \(\Phi\) and places \(x\) in a Hamiltonian three-support \(T\). If another component has order at least six, the three-component long-neighbor lemma gives further strict descent. If another component has order five, the balanced-cover proposition gives a \(4|4\) repartition of its union with \(T\), decreasing \(\Phi\) by two. The root remains in the union, although its containing component may change.

### 2. Quadratic-minimal states with a three-support

A spanning three-cover minimizing \(\Phi\) in its repartition component has no components of order one or two. If it contains a three-component, the preceding descents exclude all other orders at least five. Since \(|V(H)|>10\), its profile is exactly \(3|4|4\), and \(|V(H)|=11\).

The \(3|4\) analysis in the next subsection gives a neutral endpoint swap or a controlled \(5|2\) detour. The specialized \(3|4|4\) result gives a neutral swap, an order disagreement, or a common terminal pair for two controlled Hamiltonian five-paths. Profiles containing both orders three and five cannot occur at a quadratic minimum.

### 3. Rooted four-supports

Let \(X\) be a Hamiltonian four-support containing the distinguished root, and let \(C=(c_1,\ldots,c_m)\) be a disjoint displayed tight path. If \(m=6\), the balanced-cover proposition gives a strict \(4|6\longrightarrow5|5\) repartition, with change \(-2\) in \(\Phi\). If \(m\ge7\), the four-path long-pair lemma gives strict descent or a non-Hamiltonian endpoint six-set \(X\cup\{c_1,c_m\}\) whose Hamiltonian five-deletions exhibit an order disagreement.

Consequently a quadratic minimum containing a four-component either has profile \(3|4|4\), exhibits that endpoint order disagreement, or has profile \(4|4|4\), \(4|4|5\), or \(4|5|5\). In the last alternative its order is at most fourteen.

### 4. Rooted five-supports

Let (X) be a Hamiltonian five-support containing the root and let (C=(c_1,ldots,c_m)), (mge6). If one endpoint extends (X), then
[
5mid mlongrightarrow6mid(m-1),
]
with quadratic change (12-2m). This is neutral for (m=6) and strict for (mge7).

Assume neither endpoint extends (X). By [[five_side_endpoint_core_m6_01]] and [[toolkit_common_endpoint_core_or_a_two_pair_root_exchange_split]], either a common endpoint-replacement core preserves the root or the non-root vertices of (X) split into two endpoint-specific pairs. In the exceptional split, [[toolkit_forces_four_core_disturbance_or_an_outer_hamiltonian_sixset]] yields a four-core order disagreement, a Hamiltonian four-set, a positioned core reversal, or a Hamiltonian six-set.

Hence failure of numerical descent at support order five already produces a bounded order-theoretic obstruction or a rooted six-support.

### 5. Rooted six-supports

Let (X) be a proper Hamiltonian six-support containing the root, and write the non-Hamiltonian complement as
[
H-X=Pmid Q.
]
By [[rooted_six_support_transfer_or_comparison_disturbance01]], there is a non-root label (din X) such that (X-d) remains Hamiltonian and ((Pcup Q)+d) has path-cover number two. Comparing a two-cover of ((Pcup Q)+d) with the displayed partition
[
Pmid Qmid{d}
]
gives one of three outcomes:

1. (d) attaches to exactly one old support, producing a root-preserving one-label pairwise transfer;
2. one old support is split into two comparison blocks, yielding a split displayed edge or separated blocks;
3. a comparison edge joins (P) directly to (Q).

Thus rooted descent from a deletion-cover lift remains controlled through support order six. The possible outcomes are strict quadratic descent, explicit neutral recurrence, order disagreement or reversal, a bounded Hamiltonian core, or a comparison-cover disturbance.
