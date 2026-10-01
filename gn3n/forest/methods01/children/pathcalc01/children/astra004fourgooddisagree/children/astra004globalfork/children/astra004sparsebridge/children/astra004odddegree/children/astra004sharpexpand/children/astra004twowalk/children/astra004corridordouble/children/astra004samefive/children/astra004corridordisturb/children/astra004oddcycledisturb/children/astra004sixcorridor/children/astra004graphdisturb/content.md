# The sharp-shell support graph always exposes degree, frozen, or corridor disturbance

## Statement

Let H be a minimum counterexample in the sharp half-order shell |V(H)|=2lambda+1, and let G be the Hamiltonian-support odd graph. Then at least one of the following occurs. (A) Some Hamiltonian support S has deg_G(S)>=3; for its complement R, at least three vertices are Hamiltonian deletions of R, and astra004threegoodmixed forces a direct mixed-support edge in an endpoint deletion cover or explicit relative-order disagreement. (B) Some nonisolated support S has deg_G(S)=1. If ST is its unique incident edge with omitted label x, then T union {x}=V(H)-S is frozen at x; for every t in T every exact cover of H-t lies in a support-crossing or relative-order-disagreement branch relative to H-x=S|T. (C) G has a 2-regular connected component. That component contains explicit crossing/order disturbance: if its cycle has at least seven vertices, astra004sixcorridor applies to six consecutive edges; if it has at most six vertices, the closed-walk label-parity theorem forces either impossibility (odd cycle, since n>10 labels would all have to occur) or a repeated edge label (even cycle), and the repeated label yields two distinct exact covers of one deletion with at least two mutual support crossings by d9ef8e3fe739. Hence the sharp shell has no nonisolated support component that is simultaneously low-degree and featureless.

## Body

# Proof

The odd graph G is nonempty; indeed in the sharp shell every one-vertex deletion has an exact lambda|lambda cover, giving an odd edge.

If some vertex has degree at least three, astra004odddegree identifies its degree with the number of Hamiltonian deletions of its (lambda+1)-vertex complement, and astra004threegoodmixed gives (A).

Assume now Delta(G)<=2. If some nonisolated vertex S has degree one, let ST be its unique incident edge, labelled x. By the degree dictionary, the Hamiltonian deletions of R=V(H)-S=T union {x} are in bijection with neighbors of S. Thus x is the unique Hamiltonian deletion of R. So R is frozen at x. Apply c4cd6c0f9141 to the exact deletion cover H-x=T|S, with frozen enlarged side T union {x}. For every t in T, every exact cover of H-t exposes support crossing or relative-order disagreement. This is (B).

It remains to suppose every nonisolated vertex has degree two. Every nontrivial connected component is then a finite cycle. Let C be one such cycle of length m. If m>=7, six consecutive edges form a simple six-edge path and astra004sixcorridor gives local crossing/order disturbance.

Suppose m<=6. By bf783b4eef1e, on an even closed walk every edge label occurs an even number of times. Hence an even simple cycle of length at most six has a repeated label. The two edges carrying that label are distinct exact covers of the same deletion with different support partitions, so d9ef8e3fe739 gives at least two crossings. If m is odd, the same parity theorem says every one of the n ambient labels occurs an odd number of times on the cycle, so m>=n. Minimum-counterexample calculus gives n>10, contradicting m<=6. Thus (C) holds in all cases. ∎
