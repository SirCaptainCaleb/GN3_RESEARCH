# A global quadratic minimum containing a longest path has its other two sides nearly equal

## Statement

Let H be a counterexample minimal by order. Let A|B|C be a spanning three-cover minimizing Phi among all spanning three-covers, with |A|=a>=b=|B|>=c=|C|. Assume A is globally longest among all paths of H. Then b-c<=1.

## Body

Set
x=a-b,
y=a-c,
so 0<=x<=y and
b-c=y-x.

Assume for contradiction that b-c>=2. Then there is an integer h with
x<h<y.
Because y=a-c<=a-1, we may choose such h with 1<=h<a.

Delete h vertices from one displayed end of A, leaving a nonempty contiguous path F of order a-h. Since H is minimal by order and F is a proper path, H-F has a two-cover U|V. Write
s=b+c,
d=b-c=y-x,
delta=||U|-|V||.

By the dual quadratic shrink penalty 348a6129cf13,
delta^2 >= d^2+h(4a-2s-3h).              (1)

Because A is globally longest, each of U,V has order at most a. Their total order is
|U|+|V|=s+h.
Therefore
delta <= 2a-(s+h).                         (2)
Put
M=2a-s=(a-b)+(a-c)=x+y.
Then (2) is
delta <= M-h.

Compare the square of this upper bound with the lower bound in (1):
[d^2+h(4a-2s-3h)]-(M-h)^2
=
d^2+h(2M-3h)-(M-h)^2
=
4[h(M-h)-xy]
=
-4(h-x)(h-y).

Since x<h<y, one has (h-x)(h-y)<0, so the final quantity is strictly positive. Thus (1) forces
delta^2>(M-h)^2,
contradicting (2).

Hence no integer lies strictly between x and y. Since x,y are integers, y-x<=1. Therefore
b-c<=1.

The proof is entirely symbolic. It uses no fixed order or size case: a gap of at least two between the two smaller sides would let one truncate the globally longest side at an intermediate gap depth, where global quadratic minimality forces a complementary imbalance larger than the longest-path cap permits.
