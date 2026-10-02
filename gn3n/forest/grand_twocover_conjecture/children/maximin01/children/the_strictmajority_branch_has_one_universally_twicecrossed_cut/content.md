# The strict-majority branch has one universally twice-crossed cut

## Statement

Let H be a minimum counterexample, and let A|B|C be a spanning three-path cover whose decreasing component-order triple is lexicographically maximal. Write a=|A|>=b=|B|>=c=|C| and assume c>=2. Put U=V(B) union V(C). Then A is a globally longest tight path, H[U] and H[U-{u}] are non-Hamiltonian for every u in U, and every exact two-path cover of every one-vertex deletion H-v has at least two ordinary path edges crossing the natural cut induced by A|U: namely (A)|(U-{v}) when v in U, and (A-{v})|U when v in A.

## Body

The lexicographic deletion-cover theorem in maximin01 gives, under c>=2, that every exact two-cover of every H-v has both component orders in [b+c,a-1], and both components meet V(A). It also records that U=B union C is non-Hamiltonian.

First A is globally longest. If R were a tight path with |R|>a, then R is proper in the counterexample and the minimum-counterexample complement theorem gives an exact two-cover P|Q of H-V(R). Thus R|P|Q would be a spanning three-path cover whose largest component has order greater than a, contradicting lexicographic maximality of A|B|C. Hence the global maximum tight-path order is a.

Next fix u in U. We claim U-{u} is non-Hamiltonian. If it had a Hamilton path, then A|(U-{u}) would be a two-path cover of H-u with one component of order a. The deletion H-u is not Hamiltonian, since a Hamilton path on H-u together with the singleton u would two-cover H. Hence A|(U-{u}) would be an exact two-cover of H-u, contradicting the lexicographic theorem's upper bound a-1 on every deletion-cover component. Thus U-u is non-Hamiltonian for every u in U. Since these are proper induced subtournaments, their path-cover number is exactly two.

Now let u in U and let T be any exact two-cover of H-u. The path A is globally longest and U-u is non-Hamiltonian. By the longest-path cut crossing theorem 059cef4adeae, T has at least two ordinary edges crossing A | (U-u).

Finally let v in A and let T be any exact two-cover of H-v. Cut T at the partition (A-v)|U. The lexicographic theorem says both components of T meet A, hence the resulting A-v blocks number at least two. The set U is non-Hamiltonian and, being the complement of the proper Hamiltonian path A in a minimum counterexample, has path-cover number exactly two; therefore the U-blocks number at least two. The transition identity from coversurg01 gives

t = b_{A-v}+b_U-2 >= 2.

Thus every deletion cover, regardless of which side contains the omitted vertex, crosses the same global majority cut at least twice.