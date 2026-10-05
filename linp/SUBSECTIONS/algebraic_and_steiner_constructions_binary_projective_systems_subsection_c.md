# Theorem 3

## Metadata

- ID: algebraic_and_steiner_constructions_binary_projective_systems_subsection_c
- Parent Section: algebraic_and_steiner_constructions_binary_projective_systems
- Position: 3
- Row version: 1
- Development version: 1
- Composition version: None
- Composition stale: True

## Cold composition

(none yet)

## Development

The projective system on \(\mathbb F_2^4\setminus\{0\}\) contains no \(7\)-edge linear path. Consequently
\[
\operatorname{ex}_L(n,P_7^{(3)})
\ge
\frac73 n-O(1). \tag{4}
\]

#### Proof
The system has \(15\) vertices and
\[
\binom{15}{2}/3=35
\]
edges. A \(7\)-edge linear \(3\)-uniform path has \(15\) vertices, so any such path would be spanning.

Let \(j_1,\ldots,j_6\) be the joints of a hypothetical spanning path. By Lemma 2,
\[
j_1+\cdots+j_6=0. \tag{5}
\]
The six vectors lie in a \(4\)-dimensional vector space, so their relation space has dimension at least two. Besides (5), choose a nonzero proper relation and replace its support by its complement if necessary. Its support has size at most three. A zero-sum set of distinct nonzero vectors cannot have size one or two, so it has size three. Hence the joints split as
\[
J=U^*\sqcup W^*,
\]
where \(U^*=U\setminus\{0\}\) and \(W^*=W\setminus\{0\}\) for complementary \(2\)-dimensional subspaces
\[
\mathbb F_2^4=U\oplus W.
\]

Two consecutive joints cannot both lie in \(U^*\). If \(u,u'\in U^*\) were consecutive, their path edge would also contain \(u+u'\), the third point of \(U^*\), which is another joint, contrary to the intersection pattern of a linear path. The same holds for \(W^*\). Thus
\[
j_1,\ldots,j_6
\]
alternates between \(U^*\) and \(W^*\).

Identify the nine vectors outside \(U^*\cup W^*\) with the edges of \(K_{3,3}\): the vector \(u+w\) corresponds to the edge \(uw\), where \(u\in U^*\) and \(w\in W^*\). The joint sequence is a Hamilton path \(T\) of \(K_{3,3}\), and the five internal nonjoint vertices of the hypergraph path correspond exactly to the five edges of \(T\).

The four remaining nonjoint vertices therefore correspond to
\[
E(K_{3,3})\setminus E(T).
\]
Assume \(j_1\in U^*\), so \(j_6\in W^*\). The first hyperedge contains \(j_1\) and two of these four remaining vertices. Writing them as
\[
u+w,\qquad u'+w',
\]
their sum is \(j_1\in U\), so \(w=w'\). Hence the two corresponding edges of \(K_{3,3}\setminus T\) share the vertex \(w\).

In the complement of a Hamilton path of the cubic graph \(K_{3,3}\), the only vertices of degree two are the endpoints \(j_1,j_6\). Since \(w\in W^*\), we must have \(w=j_6\). The two \(U\)-neighbors required by the first hyperedge include \(j_5\), so the complement would contain \(j_5j_6\). But \(j_5j_6\) is the last edge of the Hamilton path \(T\), a contradiction.

Thus the projective system is \(P_7^{(3)}\)-free. Taking disjoint copies gives (4). ∎

This exceptional obstruction does not persist in higher dimensions. For all sufficiently large projective dimensions, the projective system has a spanning linear path. Likewise, deleting two prescribed nonzero points from a sufficiently large projective system still leaves a spanning linear path. Thus the projective construction yields isolated exceptional lengths rather than an infinite improvement.
