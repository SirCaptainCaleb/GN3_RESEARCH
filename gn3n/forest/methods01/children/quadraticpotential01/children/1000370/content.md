# A longest component in a global quadratic minimum forbids every intermediate path order

## Statement

Let H be a counterexample minimal by order and let A|B|C be a globally Phi-minimal spanning three-cover with a=|A|>=b=|B|>=c=|C|. Assume A is globally longest. Then H has no tight path of order f with c<f<b. Consequently b-c<=1.

## Body

Let F be any tight path of order f with c<=f<=b. By the minimum-counterexample calculus F is proper and H-F has path-cover number exactly two. Choose any exact two-cover U|V and write u=|U|, v=|V|.

Global Phi-minimality gives
a^2+b^2+c^2 <= f^2+u^2+v^2.              (1)

Also
u+v=a+b+c-f.
Because A is globally longest,
u,v<=a.
For c<=f<=b, the complementary sum satisfies
u+v-a=b+c-f,
which lies between c and b and hence is at most a. Therefore, among pairs u,v with this sum and with u,v<=a, the maximum possible value of u^2+v^2 is obtained at the most imbalanced allowable pair
{a,b+c-f}.
Thus
u^2+v^2 <= a^2+(b+c-f)^2.                 (2)

Combining (1) and (2) and cancelling a^2 yields
b^2+c^2 <= f^2+(b+c-f)^2.
The difference between the right and left sides is
f^2+(b+c-f)^2-b^2-c^2
=2(f-b)(f-c).
Hence
0<=2(f-b)(f-c).

If c<f<b, the two factors have opposite signs, a contradiction. Therefore no tight path has order strictly between c and b.

Finally, if b>=c+2, the displayed tight path B contains a contiguous tight subpath of order c+1, which lies strictly between c and b. Contradiction. Hence b-c<=1.

This uses only the certified minimum-counterexample complement principle and global quadratic minimality, plus the hypothesis that A is globally longest. It strengthens the size conclusion by excluding intermediate path orders throughout H, not merely constraining the displayed cover.
