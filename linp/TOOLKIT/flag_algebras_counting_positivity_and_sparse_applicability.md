# Flag algebras: counting, positivity, and sparse applicability

**Summary:** Use rooted extension counts and nonnegative squares to derive density inequalities. Keep finite overlap errors and labeling factors explicit. For linear 3-graphs, fixed-size vertex samples converge to the empty hypergraph, so LINP requires an exact finite or justified sparse/derived-graph formulation.

## Statement

Flag algebras organize induced-pattern density inequalities using partially labeled structures, exact expansion identities, and averaged nonnegative squares. This toolkit supplies the product and label-averaging conventions, a certificate workflow, an explicit finite overlap-error bound, a worked finite example, and a proof that ordinary dense vertex-sampled 3-graph flags cannot detect LINP's linear edge coefficient.

## Body

# Flag algebras: a practical counting and positivity toolkit

## Scope and sources

Flag algebras, introduced by Alexander A. Razborov, organize asymptotic inequalities among densities of fixed induced patterns in finite relational structures. The standard setting includes graphs, directed graphs, and hypergraphs. Their principal application is extremal density bounds. They are not fixed-point theorems, and “flag” here means a partially labeled structure, rather than a chain of subsets.

Sources consulted:
- Razborov, *Flag algebras*, Journal of Symbolic Logic 72 (2007), 1239–1282. Publisher abstract and bibliographic record: https://doi.org/10.2178/jsl/1203350785. The author's full PDF could not be fetched.
- de Carli Silva, de Oliveira Filho, Sato, *Flag Algebras: A First Glance* (2016), especially §§2–7: https://arxiv.org/abs/1607.04741. Full text was read.
- Jeong, Park, Yang, *An Introduction to Razborov's Flag Algebra as a Proof System for Extremal Graph Theory* (2026), density expressions and labeled transfer: https://arxiv.org/abs/2601.12741. Relevant full-text sections were read.
- Austin, *Razborov flag algebras as algebras of measurable functions* (2008), conditional expectation interpretation: https://arxiv.org/abs/0801.1538. Relevant full-text sections were read.

The finite estimates and LINP assessment below are independently derived here. No optimization or enumeration program was run.

## 1. Dictionary and algebra

Choose a class closed under induced substructures. A type σ is a fixed structure on labeled vertices [s]. A σ-flag F extends that labeled copy; isomorphisms preserve its labels. For an embedding θ of σ in G, pσ(F;G,θ) samples |F|-s additional vertices uniformly.

The exact chain rule is
pσ(F;G,θ)=Σ_(H of size L) pσ(F;H)pσ(H;G,θ).

Take formal linear combinations of flags, modulo these expansion identities. Define
F₁F₂=Σ_H pσ(F₁,F₂;H)H,
where the two sampled extensions are disjoint outside the type and L≥|F₁|+|F₂|-s. Cross-relations between them are unrestricted. The chain rule makes the product independent of L in the quotient; σ is its unit.

Forgetting labels requires a factor:
[[F]]σ=qσ(F)·(unlabeled F),
where qσ(F) is the probability that a uniform injection [s] into the underlying F realizes its specified labeled flag. Plain erasure omits this normalization.

This is the finite combinatorial description used in *A First Glance*. Induced density differs from non-induced or homomorphism density; fix the convention before counting.

## 2. Why squares prove inequalities

At a fixed labeled copy, let X_F be its extension density. For any coefficients c_F,
(Σ_F c_F X_F)²≥0.
The asymptotic flag product expresses this square by disjoint extension counts; label averaging transfers it to an unlabeled inequality. Austin's conditional-expectation interpretation explains why averaging retains positivity.

Thus an upper-bound certificate has the form
λ·1-f=Σ_H r_H H+Σ_σ [[vσᵀQσvσ]]σ,
with r_H≥0 and Qσ positive semidefinite. Here f is the target density expression and vσ is a column of flags. Expansion to a common size permits exact coefficient checking. The labeled-transfer proof-system formulation supplies the positivity principle; a certificate must be checked in the chosen class, rather than assumed from suggestive coefficients.

A matrix Q=Σ_j d_j c_jc_jᵀ, d_j≥0, explicitly represents a weighted sum of squares. Hand-chosen squares therefore suffice; semidefinite programming is a discovery technique, not part of the logical requirement. Numerical output alone is not a proof: verify the exact identity and positive semidefiniteness. A selected finite collection of squares is a sufficient proof system, not a guarantee that every true inequality has a certificate at that size.

## 3. An explicit finite replacement for the asymptotic product

Lemma. Fix a type embedding in an n-vertex structure, put N=n-s, and let flags F_i have extension sizes a_i=|F_i|-s. If a_i+a_j≤N, then
|pσ(F_i,F_j;G,θ)-pσ(F_i;G,θ)pσ(F_j;G,θ)|≤a_i a_j/N.

Proof. Choose independent uniform subsets U_i,U_j of the remaining N vertices. Their two flag events have product probability. Conditional on disjointness, they have the disjoint-sampling distribution. Moreover
Pr(U_i∩U_j≠∅)≤E|U_i∩U_j|=a_i a_j/N.
For any event A, the difference between Pr(A) and Pr(A|disjointness) is at most the probability of overlap. This proves the bound.

Corollary. For x_i=pσ(F_i;G,θ), Q positive semidefinite, and K_ij=pσ(F_i,F_j;G,θ),
Σ_ij Q_ij K_ij ≥ -(1/N)Σ_ij |Q_ij|a_i a_j,
because xᵀQx≥0. The matrix K need not itself be positive semidefinite at finite n.

Averaging over uniform injections realizes the downward operator EXACTLY:
p([[F]]σ;G)=Pr(random injection induces σ)·E[pσ(F;G,θ)|θ induces σ].
When the type is absent, the left side is zero. Since the prefactor is at most one, a certificate as above yields, for n large enough to fit all patterns,
p(f;G)≤λ+Σ_σ (Σ_ij |(Qσ)_ij|a_i a_j)/(n-sσ).

This is a usable explicit error bound, not an exact finite inequality λ. Alternatively expand independent sampling into ALL intersection patterns and retain their contributions. That gives exact finite moment calculations but requires a separate counting convention; ordinary disjoint flag products do not already include those overlaps.

## 4. A small worked example: triangle-free graphs

Here is an exact finite calculation illustrating the rooted-square principle without limit objects.

Let G have n vertices, e edges, and degrees d(v). For every edge uv, triangle-freeness gives d(u)+d(v)≤n: the two neighbor sets are disjoint. Summing over edges gives
Σ_v d(v)²≤ne.
The rooted nonnegative square, or Cauchy–Schwarz, gives
Σ_v d(v)²≥(Σ_v d(v))²/n=4e²/n.
Hence e≤n²/4 and therefore e≤floor(n²/4).

In flag language the labeled vertex is the type, a neighbor is an extension, and its second moment counts pairs of extensions. The useful move is to connect a square to a forbidden local configuration. Introducing flags without such a relation adds notation but no bound.

## 5. How to build a certificate by hand

1. Specify the structure, induced-sampling convention, and hypotheses stable under restriction.
2. Identify the quantity to bound or a local configuration whose positive count would give the desired move.
3. Choose a small type retaining the essential incidences; use labeled endpoints, an edge, or an ordered pair when appropriate.
4. Derive exact expansion identities. For each proposed square, explain what its cross-terms count.
5. Seek a combination of nonnegative squares and admissible-pattern densities giving the target difference. Use symmetries that preserve the hypotheses.
6. Expand to one common size; check every coefficient and every labeling factor exactly.
7. For a finite conclusion, retain intersection terms or prove that an explicit error is dominated by the required strict difference.

Equality can be informative: if a nonnegative average of squares is exactly zero, the corresponding linear relation holds at every sampled root of positive probability. Equality only in a limit gives an almost-sure limit relation, not an exact assertion at every vertex of a finite structure.

## 6. The sparse LINP obstruction

The ordinary dense 3-graph algebra does not directly detect the linear leading term sought in LINP.

Proposition. For every sequence of linear 3-graphs G_n and every fixed k, a uniform k-vertex induced subhypergraph is empty with probability tending to one.

Proof. Each hyperedge contains three unordered pairs, and linearity makes these pair sets disjoint. Thus
3|E(G_n)|≤binom(n,2),
and
p(single 3-edge;G_n)=|E(G_n)|/binom(n,3)≤1/(n-2).
If Y counts edges in a uniform k-set, then
E Y=binom(k,3)|E(G_n)|/binom(n,3)≤binom(k,3)/(n-2).
Therefore Pr(Y≥1)≤E Y→0.

If |E(G_n)|=c n, the triple-edge density is exactly
6c/((n-1)(n-2)).
The coefficient c disappears from every fixed-size ordinary vertex-sampled limit. Rescaling that density changes the problem; dense flag multiplication and its error terms cannot be imported unchanged.

Potential LINP uses, to be developed rather than presumed:
- exact rooted degree/incidence moments, sampling a present edge or a vertex neighborhood;
- counting an actual path-extension configuration whose positive count directly yields a longer linear path;
- applying graph flags to a derived intersection or shadow graph while retaining the hyperedge and vertex information needed to reconstruct a linear path.

The derived-graph option needs a transfer theorem. An induced path in a graph, a rainbow path, and a linear path in the original hypergraph are not interchangeable. Conditioning on a rare edge type needs its own normalization and estimates. Sparse sampling also invalidates the simple independent-uniform-vertex product approximation if its distribution has been changed.

Longest-path ranks and chosen entrances are not automatically inherited by induced subhypergraphs. They may be recorded as relations, but one must prove which axioms of the expanded structure hold on restriction; global witness existence cannot be replaced by a finite local condition without proof.

## 7. When to use the method

Use flag-algebra reasoning when rooted extensions have countable compatibility relations, and their first/second moments can force a useful local pattern or a density bound. The most promising LINP starting point is a hand-derived finite moment inequality tied to a legal path extension.

A density inequality alone does not produce a spanning structure, preserve witness provenance, or establish termination of an iterative surgery. First supply the bridge from positive pattern count to the desired combinatorial output. A fixed small type can also forget a growing ordered boundary or a global witness; increasing flag size indefinitely is not a substitute for that bridge.

The reusable lesson is to organize conditional counting identities and positivity certificates, with finite errors explicit. For LINP, the sparse sampling model is part of the theorem, not a cosmetic choice.


## Metadata

- ID: flag_algebras_counting_positivity_and_sparse_applicability
- Kind: toolkit
- Version: 1
- Math version: 1
- Audit: unaudited
- Refutation: unrefuted
