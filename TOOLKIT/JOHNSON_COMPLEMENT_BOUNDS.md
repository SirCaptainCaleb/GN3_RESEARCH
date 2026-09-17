# Complement-free Johnson bounds on five-subsets of a ten-set

## Theorem. Spectral bound for intersection-one pairs

Let `Omega` be a ten-element set. Let `G` be the graph whose vertices are the `252` five-subsets of `Omega`, with two distinct five-sets adjacent exactly when they meet in one element.

Let `F` be a complement-free family of `m` five-subsets, meaning that `A in F` implies `Omega-A notin F`. Then the average degree of the induced graph `G[F]` is at most

`7 + 18m/252`.

In particular, `m<=126`, so the average degree is at most `16`.

**Proof.** Let `J` be the adjacency matrix of the ordinary Johnson graph `J(10,5)`, where two five-sets are adjacent when they meet in four elements. For `0<=j<=5`, let `U_j` denote the usual `j`th Johnson eigenspace. The eigenvalues of `J` on

`U_0,U_1,U_2,U_3,U_4,U_5`

are respectively

`25,15,7,1,-3,-5`.

The distance-four adjacency matrix of `J(10,5)` is exactly the adjacency matrix `A` of `G`, since Johnson distance four means intersection size one. The standard Johnson one-swap recurrence gives

`A = p_4(J)`

with

`p_4(t)=(t^4-32t^3+166t^2+864t-1575)/576`.

Evaluating this polynomial at the six Johnson eigenvalues gives the eigenvalues of `A`:

`25,-15,7,-1,-3,5`.

Thus `G` is `25`-regular, and every eigenvalue on the orthogonal complement of the constant vectors is at most `7`.

Let `chi` be the characteristic vector of `F` and write

`chi=(m/252)1+v`,

where `v` is orthogonal to `1`. Then

`||v||^2=m-m^2/252`.

By the Rayleigh bound,

`2e(G[F]) = chi^T A chi`

`<=25m^2/252 + 7(m-m^2/252)`.

Dividing by `m` gives average degree at most

`7+18m/252`.

Finally, the `252` five-subsets split into `126` complementary pairs, and a complement-free family contains at most one member of each pair. Hence `m<=126`, giving the bound `16`. ∎
