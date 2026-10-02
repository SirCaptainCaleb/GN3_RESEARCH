# A longest component in a global quadratic minimum propagates its complementary size profile to every equal-order path

## Statement

Let H be a counterexample minimal by order and let A|B|C be a globally Phi-minimal spanning three-cover with a=|A|>=b=|B|>=c=|C|. Assume A is globally longest. Then every tight path F of order b has the property that every exact two-cover of H-F has component-order multiset {a,c}. Likewise every tight path F of order c has the property that every exact two-cover of H-F has component-order multiset {a,b}.

## Body

Fix a tight path F of order b. Since F is a proper path in a minimum counterexample, H-F has path-cover number exactly two. Let U|V be any exact two-cover of H-F and put u=|U|, v=|V|.

Because F|U|V is a spanning three-cover and A|B|C is globally Phi-minimal,
a^2+b^2+c^2 <= b^2+u^2+v^2,
so
a^2+c^2 <= u^2+v^2.                       (1)

Also
u+v=|V(H)|-b=a+c.
Since A is globally longest, both U and V have order at most a.

Among nonnegative integers u,v with sum a+c and each at most a, the quantity u^2+v^2 is maximized at the most imbalanced allowable pair {a,c}; equivalently,
u^2+v^2 <= a^2+c^2.                        (2)

Combining (1) and (2) forces equality throughout. Hence {u,v}={a,c}.

The argument for a tight path F of order c is identical. Now u+v=a+b, both u,v<=a, and global Phi-minimality gives
a^2+b^2 <= u^2+v^2 <= a^2+b^2.
Therefore every exact complementary two-cover has orders {a,b}.

Thus once a global quadratic minimum contains a globally longest component, the displayed three-cover size profile is not local to its chosen supports: it propagates to every path of either smaller displayed order.