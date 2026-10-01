# Local balance improvement drives quadratic descent to equitable three-covers

## Statement

Let C be a spanning three-cover of a boundary tournament H. Assume that whenever a reachable three-cover has two components A,B with ||A|-|B||>=2, the induced subtournament on V(A) union V(B) has a two-cover R|S with ||R|-|S||<||A|-|B||. Then finitely many legal pairwise repartitions transform C either into a two-cover or into a three-cover whose component orders differ pairwise by at most one.

## Body

# Proof

For a spanning three-cover C=P_1|P_2|P_3 define the quadratic potential

Phi(C)=|P_1|^2+|P_2|^2+|P_3|^2.

Suppose a reachable three-cover has components A,B,D with a=|A|, b=|B| and |a-b|>=2. By hypothesis, the induced subtournament on V(A) union V(B) has a two-cover R|S with r=|R|, s=|S|, r+s=a+b, and |r-s|<|a-b|. Replacing A|B by R|S is a legal repartition, leaving D unchanged.

For integers x,y with fixed sum t,

2(x^2+y^2)=t^2+(x-y)^2.

Hence |r-s|<|a-b| implies r^2+s^2<a^2+b^2, so the repartition strictly decreases Phi.

Repeat whenever two component orders differ by at least two. Since Phi is a nonnegative integer, only finitely many strict decreases are possible. If a repartition ever merges the selected pair into one path, the resulting cover has at most two components. Otherwise the process terminates with three components, and at termination no pair of component orders differs by two or more. Thus the three orders differ pairwise by at most one. ∎

## Consequences

Astra-002 implies the hypothesis, because a balanced two-cover of a pair-union minimizes the absolute difference of its two component orders. Therefore Astra-002 reduces Astra-003 to the equitable case.

More importantly, the full balanced two-cover conjecture is unnecessary for this reduction. It suffices that every imbalanced pair-union arising along the repartition process admit some two-cover whose component-order difference is strictly smaller than the displayed difference. Thus any surviving obstruction to Astra-003 after local size balancing must be carried by path order or orientation rather than by component-size imbalance.
