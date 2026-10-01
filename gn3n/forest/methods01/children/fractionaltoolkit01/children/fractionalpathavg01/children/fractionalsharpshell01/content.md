# Fractional path-cover number is exact in the sharp half-order shell

## Statement

Let H be a minimum-order counterexample on n vertices and let lambda be its maximum tight-path order. Then n/lambda <= tau*(H) <= 2+1/lambda. Hence if n=2lambda+1, then tau*(H)=2+1/lambda. In particular, in the sharp half-order shell the fractional relaxation remains strictly above two, so fractional rounding alone cannot close the grand theorem there.

## Body

# Fractional sandwich and equality shell

Let H be a minimum-order counterexample on n vertices, and let lambda be the maximum order of a tight path.

For the lower bound, give every vertex weight 1/lambda in the dual fractional-cover linear program. Every tight path has at most lambda vertices, so every path has total dual weight at most one. Thus the uniform weighting is dual-feasible and has total weight n/lambda. By weak duality,

    tau*(H) >= n/lambda.

For the upper bound, take a tight path A of order lambda. For each v in A choose an exact two-path cover of H-v. Give each of the resulting 2lambda path occurrences weight 1/lambda, and give A itself weight 1/lambda. As in the concentrated deletion-averaging construction, every vertex receives total coverage exactly one. Hence

    tau*(H) <= 2+1/lambda = (2lambda+1)/lambda.

Therefore

    n/lambda <= tau*(H) <= (2lambda+1)/lambda.

The width of this interval is exactly (2lambda+1-n)/lambda, the normalized half-order slack.

In the sharp half-order shell n=2lambda+1 the two bounds coincide, giving

    tau*(H)=2+1/lambda.

Thus the fractional relaxation is completely determined in that shell and is strictly larger than two. Equivalently, the uniform dual weighting w(v)=1/lambda witnesses the obstruction to the weighted-half statement there: every tight path has weight at most one, while half the total vertex weight is 1+1/(2lambda).

Consequently Astra's weighted longest-path principle, if proved universally, would itself exclude the sharp half-order counterexample shell; but the fractional-cover rounding conjecture by itself does not close that shell, since ceil(tau*(H))=3 there. This identifies positive half-order slack, rather than the equality shell, as the only regime in which the fractional sandwich has room to improve without additional integral structure.
