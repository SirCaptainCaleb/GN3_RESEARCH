# Certified seven- and eight-vertex boundary spanning one-turn closure

- Stable ID: note_nori_xi_certified_boundary_one_turn_orders_seven_eight
- Author: Astra
- Primary home: section:nori_matroid_generalizations_conjectures
- Labels: computer-assisted-proof, boundary-tournament, one-turn, graphic-matroid, seven-vertices, eight-vertices, verified-certificate
- Lifecycle: active
- Epistemic status: proved
- Current version: 1
- Retention: current and at most one previous snapshot
- Created session: session_nori_r6661_1
- Updated session: session_nori_r6661_1
- Disposition: none
- Successor: none

## Related references

- subsection:common_terminal_monochromatic_arm_bases_and_rooted_boolean_complement_intersection, exact version 2

## Research note

# Certified boundary spanning one-turn closure at orders seven and eight

**Computer-assisted theorem.** Let \(n\in\{7,8\}\), and let \(b:V^{\underline 3}\to\{0,1\}\), \(|V|=n\), satisfy
\[
b(c,v,a)=1-b(a,v,c).
\]
Then some permutation \(W=(v_1,\ldots,v_n)\) has at most one change in its consecutive triple-color word. The hypothesis allows independent, arbitrary local tournaments at the middle vertices.

## Propositional reduction

Order the triples \((a,b,c)\) with \(a<c\) by increasing middle \(b\), then increasing outer pair \((a,c)\). Assign one Boolean variable to each of these \(n(n-1)(n-2)/2\) reversal orbits. An oriented window has signed variable \(x_{a,b,c}\) when \(a<c\), and the negative variable for its reversed representative when \(a>c\).

Color complementation preserves every switch count, so impose \(x_1=0\). For each permutation \(p\) with \(p_1<p_n\), let \(L_1,\ldots,L_m\), \(m=n-2\), be its signed window variables. For each \(q\in\{0,1\}\) and \(1\le k\le m\), prohibit the word \(q^k(1-q)^{m-k}\) by the clause
\[
\bigvee_{j=1}^{m}
\begin{cases}
L_j,&w_j=0,\\
\neg L_j,&w_j=1.
\end{cases}
\]
These are all \(2m\) words with at most one change, including both constant words. Reversal of a vertex permutation complements and reverses its color word, preserving the number of changes; hence the selected half of the permutations suffices.

The resulting formula is satisfiable if and only if there is a boundary tournament of order \(n\) without a spanning one-turn word. It has
\[
N_n=n(n-1)(n-2)/2,\qquad C_n=1+n!(n-2)
\]
variables and clauses, respectively.

## Checked refutations

Both formulas have retained clausal refutations:

| Order | Variables | Clauses | Retained reverse-unit-propagation additions |
|---|---:|---:|---:|
| 7 | 105 | 25,201 | 1,446 |
| 8 | 168 | 241,921 | 130,753 |

CaDiCaL 1.9.5 through python-sat 1.9.dev15 produced DRAT refutations. DRAT-trim verified both and converted them to LRAT. Its C LRAT checker independently accepted both. All retained proof additions are reverse unit propagation; no RAT inference is used.

A separate standard-library Python verifier performs two checks. First it reconstructs every original clause using enumeration of binary window words and direct switch counting, independently of the generator's seam loop, and compares the clause multisets. Second it verifies each LRAT addition: negate the proposed clause, follow its positive antecedent hints, check each unit propagation, and require a conflict. Both files finish with a derived empty clause. This verifier accepted the order-seven proof with 1,446 additions and the order-eight proof with 130,753 additions. The solver is unnecessary for verification.

## Certificates and reproduction

Persistent proof archive: **nori_boundary_seven_eight_vertex_proofs.zip**, Library ID **libfile_9dd0a10c390081919915cd588595e674**.

Archive SHA256:
\[
\texttt{363db4116b1a077be79e421f2d6be7106a7582804070570c1552c385d78405b8}.
\]

The archive contains the two CNF formulas, original DRAT proofs, positive-hint LRAT proofs, all checker logs, the generator, the independent Python verifier, checker C sources, their license, a mathematical README, and SHA256SUMS. After unpacking, verification is:

    python verify_boundary.py 7 certificate_n7
    python verify_boundary.py 8 certificate_n8

CNF hashes:

- Order 7: ad4cc57fb0dae8fa84e7c199993fae0159b85945507a5bb0cfea26b865622ce3.
- Order 8: af6c4a5da45a83e0ae9740cb1bd035dea7f29dc92072ba289579e6ddef919acb.

Original DRAT hashes:

- Order 7: baa62799f6be421056c677904606225ce6cf465cd00e74b37891ea5bebd4a26a.
- Order 8: c16f1c48bbc77204ea864d98a7d68e06b1198ccac29826a7b87667c3f6737264.

DRAT-trim source revision: 2e3b2dc0ecf938addbd779d42877b6ed69d9a985, https://github.com/marijnheule/drat-trim.

## Graphic-matroid consequence

For each of these two orders, there exist a vertex \(v\), a color \(\varepsilon\), and two \(\varepsilon\)-monochromatic injective arms \(P,Q\) ending at \(v\), with \(V(P)\cap V(Q)=\{v\}\) and \(V(P)\cup V(Q)=V\). To obtain them, split a one-turn word at the vertex in position \(i+2\) when its change lies between windows \(i\) and \(i+1\), and reverse the suffix. For a monochromatic word, use its terminal singleton as the second arm. Their edge union in separate parallel copies of \(K_n\) is a basis of \(M(2K_n)\), of rank \(n-1\).

This proves the same-terminal complementary-arm basis assertion at orders seven and eight. The all-order boundary assertion and unrestricted NORI1 remain open.
