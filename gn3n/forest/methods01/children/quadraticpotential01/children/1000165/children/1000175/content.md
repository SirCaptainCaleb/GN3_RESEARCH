# Distance from the longest path controls the residual size gap at a global quadratic minimum

## Statement

Let H be a counterexample minimal by order, let lambda be the maximum path order, and let A|B|C minimize Phi among all spanning three-covers, with a=|A|>=b=|B|>=c=|C|. Put t=lambda-a, M=2a-b-c, and d=b-c. Then d^2 <= 2tM+3t^2+1. In particular, if a=lambda then d<=1.

## Body

Let
s=b+c,
M=2a-s,
d=b-c,
t=lambda-a.
Thus M,t,d are nonnegative integers.

Fix an integer h with 1<=h<a. Delete h vertices from one displayed end of A and let F be the surviving contiguous path, so |F|=a-h. By minimality of H, the complement H-F has a two-cover U|V. Put
delta=||U|-|V||.

The dual shrink penalty 348a6129cf13 gives
delta^2 >= d^2+h(4a-2s-3h)
         = d^2+h(2M-3h).                    (1)

Every path has order at most lambda=a+t. Since
|U|+|V|=s+h,
the larger of U,V has order at most a+t, and hence
delta <= 2(a+t)-(s+h)
       = M+2t-h.                             (2)

Combining (1) and (2), for every integer h in [1,a-1],
0 <= (M+2t-h)^2-d^2-h(2M-3h).              (3)

Write
x=a-b,
y=a-c.
Then M=x+y and d=y-x, so M^2-d^2=4xy. Dividing the right side of (3) by four gives the quadratic
Q(h)=h^2-(M+t)h+t^2+tM+xy.
Its discriminant is
D=(M+t)^2-4(t^2+tM+xy)
 =d^2-2tM-3t^2.                              (4)

We claim D<=1. Suppose instead D>1. First, (M+t)/2>=1: if M+t<=1, then the only nonnegative integer possibilities have d<=M<=1, and (4) gives D<=1. Second,
lambda<=|V(H)|-4
by the minimum-counterexample path-complement bound. Since |V(H)|=a+s, this gives
t=lambda-a<=s-4,
and therefore
(M+t)/2=(2a-s+t)/2<=a-2.

Set
mu=(M+t)/2.
Thus 1<=mu<=a-2. Choose an integer h with |h-mu|<=1/2; then 1<=h<=a-1. Completing the square,
Q(h)=(h-mu)^2-D/4.
Because D>1,
Q(h)<1/4-D/4<0,
contradicting (3).

Hence D<=1. Substituting (4) yields
d^2<=2tM+3t^2+1,
that is,
(b-c)^2 <= 2(lambda-a)(2a-b-c)+3(lambda-a)^2+1.

When t=0 this reduces to d^2<=1, hence b-c<=1. The result is a scale-free quantitative version of c9d6942af4ff: any residual imbalance between the two smaller sides is paid for by a definite shortfall of the largest displayed side from the global longest-path order.
