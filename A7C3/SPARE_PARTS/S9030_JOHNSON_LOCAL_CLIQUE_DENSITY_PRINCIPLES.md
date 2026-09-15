# S9030 — Johnson Local-Clique Density Principles

## Theorem A — dual-clique density bound

Let r>=k+1, let B be a family of k-subsets of an r-element ground set, write b=|B|, M=binom(r,k), and p=b/M. Assume every (k+1)-subset contains at most t members of B. Then (r-k+1)p^2-p <= t(t-1)(r-k)/(k(k+1)), hence p <= [1+sqrt(1+4t(t-1)(r-k)(r-k+1)/(k(k+1)))]/[2(r-k+1)]. For t>=2, equality can occur only if every (k+1)-set contains exactly t members of B and every (k-1)-set lies in the same number kb/binom(r,k-1) of members of B. The case `k=5,t=2` is the structural form used in Hamilton-five density applications.

### Proof

For each (k+1)-set U let y_U=|B intersect binom(U,k)|. Every edge of J(r,k) has a unique union U, so e(B)=sum_U binom(y_U,2)<=binom(r,k+1)binom(t,2). For each (k-1)-set S let x_S=|{F in B:S subset F}|. Every Johnson edge has a unique intersection S, so e(B)=sum_S binom(x_S,2)=(sum_S x_S^2-kb)/2 because sum_S x_S=kb. Cauchy gives sum_S x_S^2>=k^2 b^2/binom(r,k-1), hence e(B)>=[k^2 b^2/binom(r,k-1)-kb]/2. Compare with the upper bound and use binom(r,k-1)=binom(r,k)k/(r-k+1), binom(r,k+1)=binom(r,k)(r-k)/(k+1), b=p binom(r,k), obtaining (r-k+1)p^2-p<=t(t-1)(r-k)/(k(k+1)). The positive quadratic root gives the stated ceiling. If t>=2 and equality holds, every y_U must equal t and Cauchy must be equality, so all x_S are equal.

## Theorem B — degree-local density bound

Let B be a family of k-subsets of an r-element ground set, r>=k+1, and suppose every (k+1)-set contains at most t members of B. Write p=|B|/binom(r,k). Then p <= [k+(t-1)(r-k)]/[k(r-k+1)].

More precisely, the induced subgraph J(r,k)[B] has maximum degree at most (t-1)(r-k), while the intersection-clique decomposition forces average degree at least k(r-k+1)p-k. Comparing them gives the stated ceiling. Equality requires both mechanisms to be tight: every member F of B must lie in exactly t members of B inside every (k+1)-superset U of F, and the (k-1)-core occupancies x_S=|{F in B:S subset F}| must all be equal. For k=2,t=2 the bound becomes p<=r/[2(r-1)], the usual Mantel density scale. For k=5,t=2 it gives p<=r/[5(r-4)].

### Proof

Let b=|B| and M=binom(r,k). Fix F in B. Every Johnson neighbor G of F has a unique union U=F union G of size k+1. There are r-k such supersets U of F, and each contains at most t members of B total, hence contributes at most t-1 neighbors G of F. Thus deg_B(F)<= (t-1)(r-k), so 2e(B)<=b(t-1)(r-k). For each (k-1)-set S let x_S count members of B containing S. The intersection-clique decomposition gives 2e(B)=sum_S x_S(x_S-1)=sum_S x_S^2-kb. Since sum_S x_S=kb, Cauchy gives sum_S x_S^2>=k^2b^2/binom(r,k-1). Hence 2e(B)>=k^2b^2/binom(r,k-1)-kb. Comparing and dividing by b>0 gives k^2b/binom(r,k-1)-k <= (t-1)(r-k). Using binom(r,k-1)=M*k/(r-k+1) and p=b/M yields k(r-k+1)p-k <= (t-1)(r-k), hence the claimed bound. Equality forces equality in the pointwise degree bound for every F and equality in Cauchy, giving the stated regularity.

## Why this is reusable

These are pure extremal set-system tools on the Johnson graph. A local cap inside `(k+1)`-sets converts into a global density ceiling, with equality forcing regular design-like structure. They are useful well beyond the original Hamilton-five application.

## Scope and nonclaims

The two inequalities are generic combinatorial bounds. They do not assert that a particular A7C3 support family satisfies the required local cap.

## Provenance

Rescued from accepted archived results `R322`, `R326`.
