# Quadratic minimization and maximin balance satisfy a universal one-sixth inequality

## Statement

Let F be any nonempty family of triples of positive integers with common sum n. Let (a,b,c) in F minimize a^2+b^2+c^2 over F, with c=min{a,b,c}, and let rho=max_{(x,y,z) in F} min{x,y,z}. Then 6rho<=n+3c. Applied to spanning three-path covers, if c is the minimum component order of a globally quadratic-minimal cover and rho is the maximin minimum-component parameter, then rho<=(n+3c)/6.

## Body

Let Phi_0 be the minimum of x^2+y^2+z^2 over F. For the minimizing triple with smallest entry c, the other two entries sum to n-c, so
Phi_0 >= c^2+(n-c)^2/2.                                      (1)

Choose a triple in F whose minimum entry is rho. All three entries are at least rho and sum to n. Since rho<=n/3, the largest possible sum of squares under those constraints is attained at the extreme triple
(n-2rho,rho,rho).
Therefore
Phi_0 <= (n-2rho)^2+2rho^2.                                  (2)

Subtract the right side of (1) from the right side of (2). A direct factorization gives
2[(n-2rho)^2+2rho^2-c^2-(n-c)^2/2]
=(n-c-2rho)(n+3c-6rho).

Because rho is the maximum minimum entry over F while c is the minimum entry of one member of F, rho>=c. Also n>=3rho. Hence
n-c-2rho=(n-3rho)+(rho-c)>=0.
The left side is nonnegative by (1)-(2). If n-c-2rho>0, the factorization therefore gives n+3c-6rho>=0. If n-c-2rho=0, then both nonnegative summands n-3rho and rho-c vanish, so n=3rho and c=rho; hence n+3c-6rho=0 as well. Thus in all cases
6rho<=n+3c.

If equality holds, then the second factor vanishes, so the two bounds (1) and (2) coincide. Consequently every inequality in the sandwich is equality: the two larger entries of the quadratic-minimizing triple are equal, and a maximin triple achieving the upper extremal value has profile (n-2rho,rho,rho). Thus equality simultaneously rigidifies the quadratic-minimizing and maximin profiles. ∎