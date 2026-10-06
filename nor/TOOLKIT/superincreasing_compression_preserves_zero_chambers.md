# Superincreasing compression preserves zero chambers

**Summary:** A bounded odd defect vector can be compressed to one odd scalar with the same zero chambers using superincreasing weights.

## Statement

Let F=(F_1,...,F_D) take values in {-1,0,1}^D and satisfy F(a x)=-F(x) under an involution a. Choose positive weights W_1,...,W_D with W_d>sum_{j>d}W_j and set E=sum_d W_d F_d. Then E is odd and E(x)=0 if and only if F(x)=0.

## Body


Let
\[
F=(F_1,\ldots,F_D):X\to\{-1,0,1\}^D
\]
satisfy
\[
F(a x)=-F(x)
\]
for an involution \(a\) on \(X\).

Choose positive weights
\[
W_d>\sum_{j>d}W_j
\]
for every \(d\), for example \(W_d=3^{D-d}\), and define
\[
E(x)=\sum_{d=1}^D W_dF_d(x).
\]

Then \(E(ax)=-E(x)\). Moreover,
\[
E(x)=0\iff F_1(x)=\cdots=F_D(x)=0.
\]

If \(d_0\) is the first index with \(F_{d_0}(x)\ne0\), the leading term
\[
W_{d_0}F_{d_0}(x)
\]
has larger absolute value than the sum of all later terms, so cancellation to zero is impossible.

This is useful when a high-dimensional discrete defect vector has the desired chamber zeros but one wants to spend the released target dimensions on additional antipodal gauges.


## Metadata

- ID: superincreasing_compression_preserves_zero_chambers
- Kind: toolkit
- Version: 1
- Math version: 1
- Audit: unaudited
- Refutation: unrefuted
