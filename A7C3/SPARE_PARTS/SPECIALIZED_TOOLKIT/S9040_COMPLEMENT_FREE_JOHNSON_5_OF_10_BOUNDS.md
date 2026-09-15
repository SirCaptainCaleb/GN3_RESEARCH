# S9039 — Complement-Free Johnson 5-of-10 Bounds

This Spare Part preserves two genuinely different finite-set arguments on the 5-subsets of a 10-set. Both were useful in the historical order-ten analysis, but neither depends on boundary-tournament structure.

## Theorem A — four-core Johnson cut ceiling

Let `Omega` be a 10-element set and let `F` be a family of 5-subsets of `Omega` containing no complementary pair. Put

`barF = {Omega \ A : A in F}`.

In the Johnson graph `J(10,5)`, where two 5-sets are adjacent when they meet in four vertices,

`e_J(F,barF) <= 15|F|`.

Equivalently, the average number of four-overlap neighbors in `barF` seen from a member of `F` is at most `15`.

### Proof

For each 4-set `C subset Omega`, let

`K_C = {C union {v} : v in Omega\C}`.

The six members of `K_C` form a clique `K_6` in `J(10,5)`, and every Johnson edge lies in exactly one such clique, namely the clique indexed by the four-set intersection of its endpoints.

Write

`r_C = |F intersect K_C|`,

`s_C = |barF intersect K_C|`.

Because `F` contains no complementary pair, `F` and `barF` are disjoint, so

`r_C+s_C <= 6`.

The number of `F`-to-`barF` Johnson edges inside `K_C` is `r_C s_C`. For nonnegative `r,s` with `r+s<=6`,

`rs <= (r+s)^2/4 <= (3/2)(r+s)`.

Therefore

`e_J(F,barF) = sum_C r_C s_C <= (3/2) sum_C (r_C+s_C)`.

Each 5-set contains exactly five 4-subsets, hence

`sum_C r_C = 5|F|`,

`sum_C s_C = 5|barF| = 5|F|`.

Thus

`e_J(F,barF) <= (3/2)(10|F|) = 15|F|`.

This proves the cut ceiling.

## Theorem B — spectral intersection-one ceiling

Let `G` be the graph on the 252 five-subsets of a 10-element set `Omega`, joining distinct `S,T` exactly when

`|S intersect T| = 1`.

If `H` is a complement-free family of `m` five-subsets, then the average degree of the induced graph `G[H]` is at most

`7 + 18m/252`.

In particular, since complement-freeness implies `m<=126`, the average degree of `G[H]` is at most `16`.

### Proof

Let `J=A_1` denote ordinary Johnson adjacency on the 5-subsets of `Omega`, so two vertices are adjacent when they meet in four elements. For a `j`-subset `T` of `Omega`, let

`f_T(S)=1_{T subset S}`,

let `W_j` be the span of the functions `f_T`, and let

`U_j = W_j intersect W_{j-1}^perp`.

A one-swap count gives

`J f_T = ((5-j)^2-j) f_T + (6-j) sum_{T' subset T, |T'|=j-1} f_{T'}`.

Hence `J` acts on `U_j` with eigenvalue

`theta_j=(5-j)^2-j`,

namely

`25,15,7,1,-3,-5`

for `j=0,1,2,3,4,5`.

Let `A_i` be the Johnson distance-`i` matrix. The standard one-swap recurrence expresses `A_i` as a polynomial in `J`. Iterating to distance four gives

`A_4 = p_4(J)`,

where

`p_4(t)=(t^4-32t^3+166t^2+864t-1575)/576`.

Evaluating `p_4` on the six Johnson eigenvalues gives

`25,-15,7,-1,-3,5`.

But `A_4` is exactly the adjacency matrix of `G`, because Johnson distance four between two 5-subsets of a 10-set means intersection size one. Thus `G` is 25-regular and every nonconstant eigenvalue is at most `7`.

Let `chi` be the characteristic vector of `H`, and decompose

`chi=(m/252)1+v`, with `v perpendicular to 1`.

Then

`||v||^2 = m-m^2/252`.

By the Rayleigh bound on the orthogonal complement of the constants,

`2e(G[H]) = chi^T A_4 chi`

`<= 25m^2/252 + 7(m-m^2/252)`.

Dividing by `m` gives average degree at most

`7+18m/252`.

Finally, the 252 five-subsets split into 126 complementary pairs, so a complement-free family has `m<=126`. Substitution gives average degree at most `16`.

## Why this is reusable

The two arguments expose different pieces of Johnson geometry.

- Theorem A is a local-clique cut inequality: four-set intersections partition the Johnson edges into `K_6` blocks, and complement-freeness alone controls every block.
- Theorem B is a spectral inequality in the distance-four Johnson graph: it controls intersection-one structure through the Johnson eigenspaces rather than local occupancy.

They can therefore generalize in different directions. Theorem A is especially useful when a local replacement mechanism produces many four-overlap complement neighbors. Theorem B remains useful when intersection-one incidence, rather than replacement adjacency, is the natural statistic.

## Scope and nonclaims

Both theorems are pure finite set-system statements. They require no boundary-tournament, path-cover, minimality, carrier, or Hamiltonicity hypothesis. They do not themselves supply any lower bound on Johnson cut degree or any reason a particular support family is complement-free; those facts must come from the application.

The spectral theorem is parameter-specific to 5-subsets of a 10-set. The structural density principles in `S9030` are more general and are usually the preferred tool when only a local `(k+1)`-set occupancy cap is available. This Spare Part is retained because the complement cut and the spectral intersection-one mechanism are mathematically distinct.

## Provenance

Rescued from the accepted historical order-ten Johnson arguments `R185/P185` and `R186/P186`. The corpus explicitly records these as two genuinely different proof routes: spectral intersection-one versus four-core `K_6` cut.