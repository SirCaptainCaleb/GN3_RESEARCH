# Research charter and first exact dictionary — preserved pre-item development

## Research charter: reduction first, unification second

The goal of this article is to investigate a structural bridge between directed NOR and Frankl's union-closed sets conjecture.

Primary target:
\[
\text{directed NOR}\longrightarrow\text{Frankl-type statement}
\]
or the reverse, by an explicit transformation preserving the relevant obstruction.

Secondary target:
formulate one stronger conjecture with two natural specializations:
1. a specialization yielding directed NOR;
2. a specialization yielding Frankl.

The article should not count a merely aesthetic analogy as progress. A useful bridge must preserve at least one of the following pieces of structure:
- antipodality;
- accessibility or union closure;
- cube-geodesic support;
- monotone/one-change behavior;
- mass transport or occupancy;
- first-level coordinate imbalance.

### Current dictionary

Directed NOR works with an antipodal coloring of local ordered windows along cube geodesics. Frankl works with a join-closed family of cube vertices and asks for a coordinate of nonnegative frequency bias.

The first exact bridge is the doubled-cube lift. Given
\[
\mathcal F\subseteq2^V,
\]
let
\[
g(A)=1_{\mathcal F}(A)-1_{2^V\setminus\mathcal F}(A).
\]
On
\[
Q_{V\cup\{\star\}}\cong Q_V\times\{0,1\},
\]
define
\[
G(A,0)=g(A),\qquad
G(A,1)=-g(V\setminus A).
\]
Then
\[
G(V\setminus A,1)=-G(A,0).
\]
Thus every set family determines an antipodal cube coloring one dimension higher.

If \(\mathcal F\) is union-closed, the positive lower-layer vertices form a join-closed family, while the antipodal negative upper-layer vertices form the corresponding meet-closed complement family.

For an old coordinate \(i\in V\), if
\[
m=|\mathcal F|,
\qquad
f_i=|\{A\in\mathcal F:i\in A\}|,
\]
then the first-level Fourier coefficient of the lift has sign
\[
\operatorname{sgn}\widehat G(i)=\operatorname{sgn}(2f_i-m).
\]
Hence Frankl is exactly the assertion that the antipodal lift of every nontrivial union-closed family has at least one old-coordinate first harmonic of nonnegative sign.

This is currently the sharpest exact common language between the two problems.
