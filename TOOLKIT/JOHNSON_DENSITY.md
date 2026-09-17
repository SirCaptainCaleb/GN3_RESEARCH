# Johnson-graph density bounds

**Status: PENDING GN3 AUDIT.**

The results in this file are pure extremal set theory. They are migrated from A7C3 spare part `S9030`; legacy acceptance is provenance only and does not certify this exact GN3 text.

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