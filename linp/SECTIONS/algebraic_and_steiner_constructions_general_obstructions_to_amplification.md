# General obstructions to amplification

## Cold composition

Several natural ways to enlarge the exceptional small systems do not improve the asymptotic coefficient.

## Proposition 9

A fixed number of full two-bit Boolean fibre extensions cannot increase the limiting normalized density
\[
\frac{|E(H)|}{|V(H)|(L(H)+1)},
\]
where \(L(H)\) is the maximum linear-path length.

#### Proof
If a Boolean domain has \(v\) vertices and \(m\) additive triples, a full two-bit extension has
\[
4v+3
\]
vertices and
\[
16m+6v+1
\]
edges. If the original maximum path length is \(L\), the extended system contains a path of length at least
\[
4L-1,
\]
and when \(L\) is even, at least \(4L+3\). Thus vertex count, edge density, and maximum path length all scale by the same factor \(4\), up to bounded additive terms. Repeating a fixed number of times cannot increase the limiting ratio. ∎

## Proposition 10

Let \(S\) be an edge-transitive Steiner triple system on \(v=2\ell+1\) vertices. If \(S\) has a spanning \(\ell\)-edge path, then every set of blocks meeting every spanning \(\ell\)-edge path has size at least
\[
v/3. \tag{10}
\]

#### Proof
Fix one spanning path \(P\), and choose a uniformly random automorphism from an edge-transitive automorphism group. For any fixed block \(e\),
\[
\Pr(e\in \gamma(P))
=
\frac{\ell}{|E(S)|}
=
\frac{3}{v}.
\]
If \(D\) meets every spanning path, then
\[
1
\le
\mathbb E|D\cap E(\gamma(P))|
=
\frac{3|D|}{v}.
\]
Hence \(|D|\ge v/3\). ∎

Deleting enough blocks to destroy all spanning paths therefore already loses the amount of density needed to return to the general \((\ell-1)/3\) benchmark.

Large full Steiner triple systems also contain linear paths on \((1-o(1))v\) vertices. Consequently, if such systems themselves are used as components, their normalized density at the first forbidden path length is at most
\[
\frac13+o(1). \tag{11}
\]

Ordinary Steiner-system doubling has the same limitation. Its mixed triples are obtained from a proper edge-coloring of a complete graph, and long rainbow graph paths lift to long linear hypergraph paths. Hence the doubled system already contains paths of length comparable with half its order, preventing a coefficient above one third.

Binary-projective diagonal tensor squares also fail. For \(d\ge3\), put
\[
M=2^d-1,\qquad N=2^{d-1}-1.
\]
Choose multiplicative generators \(\alpha,\beta\) of orders \(M,N\). Since \(\gcd(M,N)=1\), the sequence
\[
q_i=(\alpha^i x,(1,\beta^i z)),
\qquad 0\le i<MN,
\]
has period \(MN\). Put
\[
d_i=q_{i-1}+q_i.
\]
The \(q_i\) are distinct, the \(d_i\) are distinct, and the two sets are disjoint because their distinguished second-coordinate bits differ. Hence
\[
\{q_{i-1},q_i,d_i\},\qquad 1\le i<MN,
\]
form a linear path of length \(MN-1\). The tensor square has normalized density strictly below \(1/3\) at its first forbidden length.

These observations rule out the direct higher-dimensional projective, affine, single-weight-code, repeated fibre-extension, symmetric-deletion, ordinary-doubling, and diagonal-tensor enlargements of the preceding small examples.

## Metadata

- ID: algebraic_and_steiner_constructions_general_obstructions_to_amplification
- Kind: section
- Version: 1
- Math version: 1
- Audit: unaudited
- Refutation: unrefuted
- Composition version: 1
- Composition stale: False

## Development tree

- [Subsection 1 — (untitled)](../SUBSECTIONS/algebraic_and_steiner_constructions_general_obstructions_to_amplification_subsection_a.md) (\`algebraic_and_steiner_constructions_general_obstructions_to_amplification_subsection_a\`; development v1; composition v1; stale=False)
- [Subsection 2 — Proposition 9](../SUBSECTIONS/algebraic_and_steiner_constructions_general_obstructions_to_amplification_subsection_b.md) (\`algebraic_and_steiner_constructions_general_obstructions_to_amplification_subsection_b\`; development v1; composition v1; stale=False)
- [Subsection 3 — Proposition 10](../SUBSECTIONS/algebraic_and_steiner_constructions_general_obstructions_to_amplification_subsection_c.md) (\`algebraic_and_steiner_constructions_general_obstructions_to_amplification_subsection_c\`; development v1; composition vNone; stale=True)
