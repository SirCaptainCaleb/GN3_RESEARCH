# Weighted longest-path principle and fractional two-cover

## Statement

For every finite boundary tournament H and every nonnegative vertex weight function w, some tight path P satisfies w(V(P)) >= w(V(H))/2.

## Body

Unproved conjecture. This is a weighted relaxation of the grand conjecture: a spanning two-cover immediately implies it, but the converse is not asserted. Attack the weighted statement directly using a maximum-weight path and exchange inequalities, rather than cardinality or endpoint cases. By finite linear-programming duality, the assertion for all nonnegative weights is equivalent to the existence of a fractional cover by tight-path supports of total weight at most two. A proof would give a global dual certificate to attack; an integral rounding theorem would still be needed. Main risk: the fractional relaxation may discard precisely the obstruction responsible for the difficult integral step. No literature or computational test has been performed.