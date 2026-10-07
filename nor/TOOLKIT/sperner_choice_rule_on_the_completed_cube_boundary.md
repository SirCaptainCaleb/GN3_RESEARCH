# Sperner choice-rule theorem on the completed-cube simplex boundary

**Summary:** Any rule choosing one element from each nonempty subset has an ordering pi for which every prefix chooses its newest element. This is exactly Sperner lemma on the barycentric simplex boundary produced by the cube-to-simplex completion.

## Statement

On the macroface B_0=sd(Delta^{n-1}) of the completed Freudenthal cube, every choice rule l(S) in S on nonempty coordinate subsets is a legal Sperner labeling. Hence there exists a permutation pi such that l({pi_1,...,pi_k})=pi_k for every k.

## Body


## Sperner-ready adjustment

The completed Freudenthal cube already triangulates an n-simplex. For direct use of Sperner, focus on the macroface opposite the distinguished vertex e_0.

This face is exactly

B_0 = sd(Delta^{n-1}),

the barycentric subdivision of the simplex on coordinate vertices 1,...,n.

Its vertices are naturally indexed by nonempty subsets S of [n]:
- singleton S={i} is the added coordinate vertex a_i;
- |S|>=2 is the old cube vertex S, realized as the barycenter of the simplex face S.

Therefore any labeling

l(S) in S

is automatically a valid Sperner labeling: the vertex corresponding to S lies in the simplex face spanned by S, and its label is one of the vertices of that face.

### Theorem: prefix-newest permutation

For every choice rule l on nonempty subsets, there exists a permutation

pi=(pi_1,...,pi_n)

such that, writing

S_k={pi_1,...,pi_k},

one has

l(S_k)=pi_k

for every k=1,...,n.

### Proof

Apply Sperner lemma to B_0 with the labeling l.

A fully labeled top simplex of B_0 is a maximal chain

S_1 subset S_2 subset ... subset S_n=[n],

with |S_k|=k, whose n labels are all distinct.

Write pi_k for the unique element of S_k minus S_{k-1}. Since l(S_1) belongs to S_1, l(S_1)=pi_1.

Inductively, l(S_k) belongs to S_k and must differ from the labels on S_1,...,S_{k-1}, which by induction are pi_1,...,pi_{k-1}. The only remaining element of S_k is pi_k. Hence l(S_k)=pi_k.

### Why this is the right Sperner interface for NOR

The cube-to-simplex construction should not be forced to equal the barycentric subdivision of the whole simplex. That is unnecessary.

The macroface B_0 already has exactly the barycentric structure Sperner needs, and it parametrizes coordinate prefixes directly.

Thus the NOR closure problem can be attacked by designing a choice rule

l_h(S) in S

from the reversal-odd ordered-window coloring h with the following property:

if a permutation pi satisfies l_h(S_k)=pi_k for every prefix S_k, then the h-word of pi has at most one change.

Sperner would then produce the required permutation automatically.

This isolates a concrete target: construct a prefix choice function from the NOR data whose "newest-element fixed point" condition enforces one-change behavior.

### Variants

If h naturally labels higher-dimensional faces rather than subset vertices, take one barycentric subdivision of the completed simplex. A face then becomes a vertex, and any selected coordinate lying in that face is again a legal Sperner label. This permits ordered-window selectors, defect vertices, or other face-valued NOR data to be promoted to ordinary vertex labels before applying Sperner.


## Metadata

- ID: sperner_choice_rule_on_the_completed_cube_boundary
- Kind: toolkit
- Version: 1
- Math version: 1
- Audit: unaudited
- Refutation: unrefuted
