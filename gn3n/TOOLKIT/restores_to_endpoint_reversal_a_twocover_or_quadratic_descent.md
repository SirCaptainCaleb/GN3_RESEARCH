# A one-block endpoint attachment restores to endpoint reversal, a two-cover, or quadratic descent

**Summary:** A one-block endpoint attachment restores to endpoint reversal, a two-cover, or quadratic descent.

## Statement

Let H be a minimum counterexample, let y=r_0 be the initial endpoint of a displayed tight path R=(r_0,r_1,...,r_m), m>=2, and let T=C|D be a two-cover of H-y. Suppose B=(r_1,...,r_m) occurs as one contiguous block of C in inherited order and C has an ordinary mixed-support edge incident with B. Write C=L,B,K, where L,K contain no R-vertices (either may be empty).

If K is nonempty, then S=(r_0,B,K) is tight. Hence L|S|D is a spanning cover; if L is empty it is a two-cover, while if l=|L|>=1 its quadratic-potential change from C|D|{r_0} is -2(l-1)(|C|-l). Thus l=1 is Phi-neutral and l>=2 is a strict Phi decrease.

If instead the mixed attachment is on the initial side of B, write L=A,a with a exterior and A possibly empty. Then either (a,r_0,r_1) is non-tight, in which case (r_1,r_0,a) is tight and explicitly reverses the displayed endpoint edge r_0r_1, or (a,r_0,r_1) is tight. In the latter case S=(a,r_0,B,K) is tight and A|S|D is spanning; if A is empty it is a two-cover, while for t=|A|>=1 the Phi change from C|D|{r_0} is -2(t-1)(|C|-t), so t=1 is neutral and t>=2 is a strict decrease.

The terminal-end version is symmetric. Therefore an order-neutral one-block direct mixed cut interaction cannot remain diffuse: it produces an endpoint-edge reversal, a spanning two-cover, a neutral singleton transfer, or strict quadratic descent.

## Body

Because B is a contiguous inherited block, every consecutive triple wholly inside B is tight. For a terminal-side attachment, K is the suffix of the tight path C beginning immediately after B. The sequence (r_0,B,K) is tight: its first triple is inherited from R, all triples through B are inherited from R, and all triples from the end of B through K are inherited from C. Splitting C immediately before B therefore gives L|(r_0,B,K)|D. If c=|C| and l=|L|, the changed path orders are c,1 -> l,c-l+1, and l^2+(c-l+1)^2-c^2-1=-2(l-1)(c-l). This gives the stated alternatives.

For an initial-side attachment, let a be the final exterior vertex immediately preceding r_1 and write L=A,a. The only triple needed to splice y=r_0 between a and B that is not already inherited from C or R is (a,r_0,r_1). If it is non-tight, boundary antisymmetry gives the tight reverse (r_1,r_0,a), which reverses the displayed endpoint edge r_0r_1. If it is tight, (a,r_0,B,K) is tight, and splitting off A gives the same algebra with t=|A|. The terminal-end statement follows symmetrically.

## Metadata

- ID: restores_to_endpoint_reversal_a_twocover_or_quadratic_descent
- Kind: toolkit
- Version: 1
- Math version: 1
- Audit: unaudited
- Refutation: unrefuted
