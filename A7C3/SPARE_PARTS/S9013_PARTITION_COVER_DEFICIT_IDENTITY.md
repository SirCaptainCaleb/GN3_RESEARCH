# S9013 — Partition-Cover Deficit Identity

## Theorem

Fix a partition

`Pi={X_1,...,X_m}`

of a finite vertex set into nonempty physical classes. Let `T` be a literal exact path cover of the whole vertex set with `q` path components.

Let `t_Pi(T)` be the number of selected adjacent states of `T` whose endpoints lie in different partition classes. For each class `X_i`, let

`pc(X_i)`

be the intrinsic minimum number of tight paths needed to cover the induced subsystem on `X_i`.

Then there is a nonnegative integer `sigma_Pi(T)` such that

`t_Pi(T) = sum_i pc(X_i) - q + sigma_Pi(T)`.

More concretely, if `b_i(T)` is the number of monochromatic path blocks obtained by restricting the displayed cover `T` to class `X_i`, then

`sigma_Pi(T)=sum_i (b_i(T)-pc(X_i)) >= 0`.

Hence

`t_Pi(T) >= sum_i pc(X_i)-q`,

with equality if and only if every class restriction of `T` realizes the intrinsic path-cover minimum of that class.

## Proof

Start with the `q` path components of `T`. Cut every selected adjacent state whose endpoints belong to different partition classes. There are exactly `t_Pi(T)` such transitions.

Each cut increases the number of path pieces by one. Therefore after all cross-class transitions are cut, the displayed cover has exactly

`q + t_Pi(T)`

monochromatic path blocks.

For each partition class `X_i`, let `b_i(T)` be the number of those blocks lying in `X_i`. The blocks partition the vertices class by class, so

`sum_i b_i(T) = q + t_Pi(T)`.

The `b_i(T)` blocks form a literal path cover of the induced subsystem on `X_i`. By definition of intrinsic path-cover number,

`b_i(T) >= pc(X_i)`.

Define

`sigma_Pi(T)=sum_i (b_i(T)-pc(X_i))`.

Every summand is nonnegative, so `sigma_Pi(T)>=0`. Rearranging the block-count identity gives

`t_Pi(T)
 = sum_i b_i(T)-q
 = sum_i pc(X_i)-q+sigma_Pi(T)`.

Finally, `sigma_Pi(T)=0` if and only if every nonnegative summand vanishes, equivalently

`b_i(T)=pc(X_i)`

for every class `X_i`. ∎

## Why this is reusable

The identity separates **intrinsic class complexity** from **representative-relative cross-class transitions**. It is useful whenever a path cover is analyzed relative to a fixed physical partition: a low transition count forces the restrictions inside the classes to be close to intrinsically optimal, while equality means every class restriction is already minimum.

The excess `sigma_Pi(T)` is bookkeeping attached to the displayed representative, not a global resource.

## Scope and nonclaims

No Strong Level-(1) property, smallest-counterexample hypothesis, antisymmetry, deletion structure, or extremality is used. The statement is a general path-cover counting identity once the notions of tight path and intrinsic path-cover number are fixed.

The excess `sigma_Pi(T)` is not asserted to be monotone under exchanges and must not be treated as literal exchange credit.

## Provenance

Rescued from the accepted identity historically recorded as `R7`. Citation-graph mining found it reused across the corpus despite its terse original presentation; its proof is completely self-contained and independent of the later project machinery.