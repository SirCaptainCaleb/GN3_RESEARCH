# Two alternative-2 failed-insertion obstructions on one path have a complete spacing trichotomy

## Statement

Let B=(b_1,...,b_m) be a tight path in a boundary tournament, and let x,y be distinct exterior vertices. Suppose alternative 2 of the failed-insertion normal form in insert01 holds for x at gap b_i|b_{i+1} and for y at gap b_j|b_{j+1}. After interchanging x,y assume i<=j. Then: (1) if i=j, H[{x,y,b_i,b_{i+1}}] is Hamiltonian; (2) if j>=i+2, (x,b_{i+1},...,b_j,y) is a tight path; (3) if j=i+1, then either H[{x,y,b_i,b_{i+1},b_{i+2}}] is Hamiltonian or the explicit cross triple (x,b_{i+1},y) is tight. Thus every pair of alternative-2 failed-insertion obstructions on one displayed path yields a bounded Hamiltonian or cross-triple witness, or a direct tight connector joining the two exterior vertices through the interval between their obstruction gaps.

## Body

For alternative 2 of insert01 at gap b_i|b_{i+1}, the displayed arcs imply that the prefix capped by x and the suffix begun by x are tight:
(b_1,...,b_i,x)
and
(x,b_{i+1},...,b_m).
In particular the reverse-through-gap triple
(b_{i+1},x,b_i)
is tight. The same statements hold for y at its gap.

Assume first i=j. Then both
(b_{i+1},x,b_i)
and
(b_{i+1},y,b_i)
are tight. Apply the parallel-middle four-path lemma from localextend01 with a=b_{i+1} and c=b_i. At least one of
(b_{i+1},x,b_i,y)
and
(b_{i+1},y,b_i,x)
is a tight Hamilton path on {x,y,b_i,b_{i+1}}. Hence that four-set is Hamiltonian.

Now assume j>=i+2. The sequence
(x,b_{i+1},...,b_j,y)
has at least four vertices. Its initial and internal consecutive triples are inherited from the tight suffix
(x,b_{i+1},...,b_m)
supplied by the obstruction for x. Its final consecutive triple
(b_{j-1},b_j,y)
is inherited from the tight prefix
(b_1,...,b_j,y)
supplied by the obstruction for y. Therefore the whole displayed sequence is tight.

Finally assume j=i+1. Put
a=b_i, b=b_{i+1}, c=b_{i+2}.
The two reverse-through-gap triples give
(b,x,a)
and
(c,y,b)
tight. Exactly one of
(y,b,x)
and
(x,b,y)
is tight by boundary antisymmetry. If (y,b,x) is tight, then
(c,y,b,x,a)
is a Hamilton tight path on {x,y,a,b,c}. Otherwise (x,b,y) is the asserted explicit cross triple.

These cases exhaust all possible relative gap positions. ∎
