# Johnson-graph density bounds

Let `J(r,k)` be the Johnson graph whose vertices are the `k`-subsets of an `r`-element set, with two vertices adjacent exactly when their intersection has order `k-1`.

## 1. A quadratic density bound from local `(k+1)`-set occupancy

Let `B` be a family of `k`-subsets of an `r`-element set, where `r>=k+1`. Write

`b=|B|`, `M=binom(r,k)`, `p=b/M`.

Suppose every `(k+1)`-subset contains at most `t` members of `B`. Then

`(r-k+1)p^2-p <= t(t-1)(r-k)/(k(k+1))`,

and therefore

`p <= [1+sqrt(1+4t(t-1)(r-k)(r-k+1)/(k(k+1)))]/[2(r-k+1)]`.

If `t>=2` and equality holds throughout, then every `(k+1)`-subset contains exactly `t` members of `B`, and every `(k-1)`-subset is contained in the same number of members of `B`.

**Proof.** For each `(k+1)`-set `U`, put

`y_U=|B intersect binom(U,k)|`.

Every edge of `J(r,k)[B]` has a unique union of order `k+1`, so

`e(B)=sum_U binom(y_U,2) <= binom(r,k+1) binom(t,2)`.

For each `(k-1)`-set `S`, put

`x_S=|{F in B:S subset F}|`.

Every Johnson edge has a unique intersection of order `k-1`, hence

`e(B)=sum_S binom(x_S,2)=(sum_S x_S^2-kb)/2`,

because `sum_S x_S=kb`. By Cauchy-Schwarz,

`sum_S x_S^2 >= k^2b^2/binom(r,k-1)`.

Combining the lower and upper bounds for `e(B)` and using

`binom(r,k-1)=binom(r,k)k/(r-k+1)`,

`binom(r,k+1)=binom(r,k)(r-k)/(k+1)`,

and `b=p binom(r,k)` gives the displayed quadratic inequality. Solving it for the positive root gives the density bound.

If equality holds and `t>=2`, then equality is required both in the pointwise estimate `binom(y_U,2)<=binom(t,2)` and in Cauchy-Schwarz. Thus every `y_U=t` and all `x_S` are equal. ∎

## 2. A degree bound from the same local occupancy hypothesis

Under the same hypotheses,

`p <= [k+(t-1)(r-k)]/[k(r-k+1)]`.

More precisely, every vertex of `J(r,k)[B]` has degree at most

`(t-1)(r-k)`,

while the average degree of `J(r,k)[B]` is at least

`k(r-k+1)p-k`.

If equality holds, then every member `F of B` has exactly `t-1` neighbors of `B` inside each `(k+1)`-set containing `F`, and every `(k-1)`-subset lies in the same number of members of `B`.

**Proof.** Fix `F in B`. Every Johnson neighbor `G of F` has a unique union `U=F union G` of order `k+1`. There are `r-k` such supersets `U` of `F`, and each contains at most `t-1` further members of `B`. Hence

`deg_B(F)<= (t-1)(r-k)`.

Thus

`2e(B)<=b(t-1)(r-k)`.

Using the intersection counts `x_S` from the previous proof,

`2e(B)=sum_S x_S(x_S-1)=sum_S x_S^2-kb`.

Cauchy-Schwarz gives

`2e(B)>=k^2b^2/binom(r,k-1)-kb`.

Comparing the two inequalities and substituting

`binom(r,k-1)=binom(r,k)k/(r-k+1)`, `b=p binom(r,k)`

yields

`k(r-k+1)p-k <= (t-1)(r-k)`,

which is equivalent to the claimed bound. Equality forces equality in every pointwise degree bound and in Cauchy-Schwarz, giving the stated regularity conditions. ∎

For `k=2,t=2` the second bound gives `p<=r/[2(r-1)]`. For `k=5,t=2` it gives `p<=r/[5(r-4)]`.

## 3. Complement-pair cut bound in `J(10,5)`

Let `Omega` be a ten-element set and let `F⊆binom(Omega,5)` contain no complementary pair. Put

`bar(F)={Omega-A : A in F}`.

In the Johnson graph `J(10,5)`, whose vertices are the five-subsets of `Omega` and whose adjacent vertices meet in four elements, let `e(F,bar(F))` denote the number of Johnson edges with one endpoint in `F` and one endpoint in `bar(F)`. Then

`e(F,bar(F)) <= 15|F|`.

**Proof.** For every four-set `C⊆Omega`, let

`K_C={C∪{v} : v in Omega-C}`.

This is a clique of order six in `J(10,5)`, and every Johnson edge belongs to exactly one such clique, namely the clique indexed by the intersection of its endpoints. Put

`r_C=|F∩K_C|`, `s_C=|bar(F)∩K_C|`.

Since `F` contains no complementary pair, `F` and `bar(F)` are disjoint. Hence `r_C+s_C<=6`, and therefore

`r_C s_C <= (r_C+s_C)^2/4 <= (3/2)(r_C+s_C)`.

Summing over all four-sets counts every edge from `F` to `bar(F)` exactly once. Each five-set contains exactly five four-subsets, so

`sum_C r_C=5|F|`, `sum_C s_C=5|bar(F)|=5|F|`.

Consequently

`e(F,bar(F)) <= (3/2)(10|F|)=15|F|`. ∎

## 4. Hamilton-five density hierarchy in boundary tournaments

Let `H` be a boundary tournament, let `W⊆V(H)` have order `r>=6`, and fix `S⊆W` of order `s∈{0,1,2,3}`. Let `h_5(W;S)` be the number of five-subsets `F` such that

`S⊆F⊆W`

and `H[F]` is Hamiltonian. Then the fraction of five-subsets containing `S` that are non-Hamiltonian is at most

`(r-s)/[(5-s)(r-4)]`.

Equivalently,

`h_5(W;S) >= [1-(r-s)/((5-s)(r-4))] binom(r-s,5-s)`.

For `s=0`, this gives Hamilton-five density at least

`4(r-5)/[5(r-4)]`.

For fixed vertex, pair, and triple, the corresponding asymptotic guaranteed densities tend respectively to `3/4`, `2/3`, and `1/2`. For every `r>10`, these bounds strictly improve the elementary fixed-subset density bounds obtained by direct double counting from the four-of-six theorem.

**Proof.** Let `B_S` be the family of sets

`F-S`

where `S⊆F⊆W`, `|F|=5`, and `H[F]` is non-Hamiltonian. Then `B_S` is `k=(5-s)`-uniform on the `N=r-s` vertices of `W-S`.

Every `(k+1)=(6-s)`-subset `U⊆W-S` corresponds to the six-set `S∪U`. By `SMALL_ORDER_HAMILTONICITY.md` Section 6, at least four of the six five-subsets of `S∪U` are Hamiltonian. Hence at most two members of `B_S` lie inside `U`.

Apply Section 2 with `t=2`. The bad-set density satisfies

`p_bad <= [k+(N-k)]/[k(N-k+1)] = N/[k(N-k+1)]`.

Substituting `N=r-s`, `k=5-s`, and `N-k+1=r-4` gives

`p_bad <= (r-s)/[(5-s)(r-4)]`.

Complementing inside the family of all five-subsets containing `S` gives the displayed Hamiltonian density. ∎

