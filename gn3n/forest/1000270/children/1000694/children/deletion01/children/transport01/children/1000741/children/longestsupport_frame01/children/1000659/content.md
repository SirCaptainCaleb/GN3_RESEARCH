# Two-crossing endpoint covers in the sharp half-order shell

## Statement

Let H be a minimum counterexample of order n=2lambda+1, where lambda is the maximum tight-path order, and let A=(a_0,...,a_{lambda-1}) be a globally longest path with U=V(H)-V(A). Let T be an exact two-cover of H-a_0 having exactly two ordinary edges across the cut (A-{a_0}) | U. Cutting the two crossings yields exactly two blocks on A-{a_0} and two blocks on U. Either the two crossings lie in different cover components, so each component consists of one A-block and one U-block; or one component has block pattern B_1-u-B_2, where {u} is a singleton U-block and B_1,B_2 partition A-{a_0}, while the other component is a Hamilton path on U-{u}. The opposite three-block pattern U_1-B-U_2 is impossible. Thus the only non-crosswise equality shape is a one-vertex exchange through the interior of the longest-path remainder.

## Body

# Two-crossing endpoint covers in the sharp half-order shell

Let H be a minimum counterexample with
|V(H)|=2 lambda+1,
where lambda is the maximum order of a tight path. Let
A=(a_0,...,a_{lambda-1})
be a globally longest tight path and put
U=V(H)-V(A).
Then |U|=lambda+1, and U is non-Hamiltonian with path-cover number two.

Let T be an exact two-path cover of H-a_0 having exactly two ordinary edges crossing the cut
B | U,
where
B=A-{a_0}
has order lambda-1.

Because H-a_0 has 2 lambda vertices and every tight path has order at most lambda, both components of T have order exactly lambda.

Cut the two B-U crossing edges. Let b_B and b_U be the numbers of resulting nonempty blocks contained in B and U. Cutting two edges from a two-component path forest gives exactly four blocks, so
b_B+b_U=4.
Since B is Hamiltonian, b_B>=1. Since U is non-Hamiltonian with pc(U)=2, its U-blocks cover U and hence b_U>=2. Thus b_B<=2.

We first exclude b_B=1. Then the unique B-block contains all lambda-1 vertices of B. Every crossing edge of T is incident with this unique B-block, so in the contracted block forest it has degree two and lies between two nonempty U-blocks. Its cover component therefore has block pattern
U_1-B-U_2
and order at least
1+(lambda-1)+1=lambda+1,
contradicting maximality of lambda.

Hence b_B=2, and therefore b_U=2.

Contract the four monochromatic blocks. There are two path components and exactly two cross edges.

If the two cross edges lie in different components, each component consists of one B-block joined to one U-block. This is the crosswise four-block shape.

Suppose instead that both crossings lie in one component. That component has three alternating blocks and the other component is the remaining block.

The pattern
U_1-B_1-U_2
is impossible, because it contains both U-blocks and hence all lambda+1 vertices of U, already exceeding the maximum path order lambda before B_1 is added.

Thus the only same-component possibility is
B_1-U_1-B_2
with the other component U_2.
Since B_1 and B_2 partition B, their total order is lambda-1. The three-block component is tight and has order
(lambda-1)+|U_1|.
Maximality gives
(lambda-1)+|U_1| <= lambda,
so |U_1|<=1. Since U_1 is nonempty, |U_1|=1.

Writing U_1={u}, the cover has the form
(B_1,u,B_2) | U_2,
where U_2 is a Hamilton path on U-{u}. In particular the non-crosswise two-crossing state is exactly a one-vertex support exchange: the singleton u replaces the deleted endpoint a_0 inside a Hamilton order on (A-{a_0}) union {u}, while U-{u} is Hamiltonian.

The statement at the other endpoint of A is symmetric. ∎
