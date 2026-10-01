# An oversized longest component forces a one-step moving longest-path family

## Statement

Let H be a counterexample minimal by order and let A|B|C be a globally Phi-minimal spanning three-cover with a=|A|>=b=|B|>=c=|C|. Assume A is globally longest and a>=b+2. Then c>=2, and for every tight path F of order b+1, every exact two-cover of H-F has component-order multiset {a,c-1}. In particular every contiguous (b+1)-vertex window of A has a complementary globally longest a-vertex path.

## Body

Fix any tight path F of order b+1. It is proper, so the minimum-counterexample calculus gives an exact two-cover U|V of H-F. Write u=|U|, v=|V|.

Because F|U|V is a spanning three-cover and A|B|C globally minimizes Phi,
a^2+b^2+c^2
<=
(b+1)^2+u^2+v^2.
Hence
u^2+v^2 >= a^2+c^2-2b-1.                 (1)

Also
u+v=a+c-1,
and global longestness of A gives u,v<=a.

First c cannot equal 1. If c=1, then u+v=a and u,v are both positive. Thus
u^2+v^2 <= (a-1)^2+1.
But (1) would give
u^2+v^2 >= a^2-2b.
These inequalities imply
a^2-2b <= a^2-2a+2,
hence a<=b+1, contradicting a>=b+2.
Therefore c>=2.

Now c>=2. Among positive integer pairs with sum a+c-1 and both entries at most a, the unique most imbalanced pair is {a,c-1}. The next-most-imbalanced possibility has square sum at most
(a-1)^2+c^2.
But the lower bound (1) exceeds this by
[a^2+c^2-2b-1]-[(a-1)^2+c^2]
=
2(a-b-1)
>=2.
Therefore no non-extremal pair can satisfy (1). Hence necessarily
{u,v}={a,c-1}.

Since F was arbitrary, this holds for every tight (b+1)-path. In particular A contains a contiguous tight subpath of order b+1 because a>=b+2. The complement of every such window therefore has an exact two-cover with one component of order a, which is globally longest, and the other of order c-1.

Thus a genuine size gap above the second component does not merely create local endpoint barriers: it creates an arbitrary-scale moving-window family of new globally longest paths.
