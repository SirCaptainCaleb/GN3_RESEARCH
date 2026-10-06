# Lemma 8

## Metadata

- ID: snake_accounting_and_the_4348_equality_problem_the_interior_pair_count_subsection_b
- Parent Section: snake_accounting_and_the_4348_equality_problem_the_interior_pair_count
- Position: 2
- Row version: 1
- Development version: 1
- Composition version: None
- Composition stale: False

## Composition

(none yet)

## Development

\[
D'_v+I_v
\ge
s_v-\left\lceil\frac{p-3}{2}\right\rceil. \tag{27}
\]
Consequently
\[
D'_v+I_v
\ge
\frac18p-\eta_v-O(1). \tag{28}
\]

#### Proof
Let \(C_v\) be the number of occupied interior pairs. Since each occupied pair contains one or two intersections,
\[
s_v=C_v+D'_v. \tag{29}
\]

Consider an occupied \(B_i\) that is not counted by \(I_v\). By (26), \(\phi(g_{i+2})\ge p\). Since some vertex of \(g_{i+2}\) has rank below \(p\), the edge \(g_{i+2}\) must have edge rank exactly \(p\), must be nonspecial ascending, and its unique entrance is its forward joint
\[
g_{i+2}\cap g_{i+3},
\]
which has vertex rank \(p-1\).

Two consecutive output edges cannot both have this form. Indeed, if \(g_j\) has unique entrance
\[
z_j=g_j\cap g_{j+1}
\]
with \(\phi(z_j)=p-1\), and \(g_{j+1}\) has the analogous form, then \(z_j\) is a terminal vertex of the rank-\(p\) edge \(g_{j+1}\), forcing \(\phi(z_j)\ge p\), a contradiction.

Thus the occupied interior pairs that are neither doubly occupied nor counted by \(I_v\) form an independent set in the path of \(p-3\) interior indices. There are at most
\[
\left\lceil\frac{p-3}{2}\right\rceil
\]
of them. Using (29) gives (27), and (25) gives (28). ∎

If \(B_i\) is doubly occupied, the edge \(g_i\) and the two members of \(F_v\) using \(b_i,z_i\) form a \(3\)-edge linear cycle. Distinct doubly occupied interior pairs yield edge-disjoint such cycles apart from the common vertex \(v\) in their two nonpath edges. Distinct indices counted by \(I_v\) yield distinct path edges \(g_{i+2}\) contained in the rank superlevel
\[
V_{\ge p}=\{w:\phi(w)\ge p\}. \tag{30}
\]

Thus every low-\(\eta_v\) high-rank vertex produces linearly many local cycles or linearly many distinct edges in its rank superlevel.

## Frontier

- Development version when composed: None
- Development version now: 1
