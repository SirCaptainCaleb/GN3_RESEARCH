# A family noninsertable into one displayed path gives a labelwise reversal family

## Statement

Let H be a boundary tournament, let B=(b_1,...,b_m), m>=2, be a displayed tight path, and let S be a set of vertices disjoint from B. If every x in S is noninsertable into the displayed order of B, then for every x in S some tight triple containing x reverses a displayed edge of B. Thus S supplies a labelwise family of |S| reversal witnesses on B.

## Body

Apply acdec36ae3ca separately to B and each x in S. For each x it returns either (x,b_t,b_{t-1}) or (b_{t+1},b_t,x), which contains one displayed edge of B in reverse order. No relation among the chosen indices is asserted or needed. The result isolates the family-level mechanism used in global four-side reversal arguments without any extremality hypothesis.
