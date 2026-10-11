# Superincreasing compression preserves zero chambers

**Summary:** A bounded odd defect vector can be compressed to one odd scalar with the same zero chambers using superincreasing weights.

## Statement

A superincreasing weighted scalar of a discrete {-1,0,1}^D defect vector is odd and vanishes exactly at the discrete vector zeros. This pointwise equivalence does not preserve zero sets under continuous or affine interpolation.

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


## Discrete-only scope; continuous interpolation can create spurious scalar zeros

The equivalence E(x)=0 if and only if F(x)=0 applies ONLY at points where all coordinates of F(x) lie in {-1,0,1}. It does not generally hold after affine interpolation of vertex labels, nor does scalar compression preserve the zero set of a continuous vector-valued map.

Indeed, assign F(v_0)=(1,1), F(v_1)=(-1,1), and weights W_1>W_2>0. Along their connecting edge the affine vector interpolation has second coordinate identically 1 and thus never vanishes. Its scalar interpolation has endpoint values W_1+W_2>0 and -W_1+W_2<0, hence an interior scalar zero. Therefore replacing a continuous multi-coordinate odd map by this scalar before Borsuk–Ulam/Tucker extraction does not preserve vector-zero certificates; a separate extraction theorem would be necessary.


## Metadata

- ID: superincreasing_compression_preserves_zero_chambers
- Kind: toolkit
- Version: 3
- Math version: 2
- Audit: unaudited
- Refutation: unrefuted
