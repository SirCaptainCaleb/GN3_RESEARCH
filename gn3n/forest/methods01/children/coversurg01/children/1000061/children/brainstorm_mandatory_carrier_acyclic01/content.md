# A support carrying a mandatory triple has acyclic edge comparisons

## Statement

Let H be a finite boundary tournament admitting a two-cover, and let T=(a,b,c) be a tight triple that occurs consecutively in this order in one path of every two-cover of H. For every two-cover A|B with T occurring on A, the comparison digraph of H[V(A)] is acyclic. Here the comparison digraph has the ordinary pairs of V(A) as vertices, with uv directed to vw exactly when (u,v,w) is tight.

## Body

Conjecture; no proof is asserted. Existing mandatory-triple rigidity says that every Hamilton order on a carrying support must contain the same consecutive triple. The proposed strengthening turns this order rigidity into acyclicity of the comparison digraph on that support, without assuming the entire tournament is edge-orderable.

First approach: choose a shortest directed comparison cycle inside the carrying support. Such a cycle is supported by a star, a triangle, or an ordinary cycle. Try to use its directed comparisons to reorder a Hamilton path on the same support while avoiding the consecutive word a,b,c. Keeping B unchanged would contradict mandatory occurrence. A comparison cycle alone need not yield a spanning reordered path; that extension is the main obstacle. If true, the result would allow edge-order methods on the carrying support of arbitrary mandatory-triple examples.
