# The rainbow-six-cycle branch has one canonical chord matrix

## Statement

In the closing-chord normal form for a proper 6-coloring of K_{6,6} with no rainbow P_6, normalize the rainbow cycle
a-A-b-B-c-C-a
to have successive colors 1,2,3,4,5,6. Then, up to the half-turn symmetry of the cycle and relabeling colors by +3 modulo 6, the colors on the three remaining used-vertex chords are forced to be
aB=2, bC=4, cA=6.
Equivalently the used 3x3 color matrix is
[ [1,2,6], [2,3,4], [6,4,5] ].

## Body

Write
u=col(aB), v=col(bC), w=col(cA).
Properness gives
u in {2,5}, v in {1,4}, w in {3,6}.

We repeatedly use the following maximality fact: if a rainbow P_5 misses color t and an endpoint has its unique color-t edge going to a vertex outside that P_5, then that edge extends the path to a rainbow P_6, contradiction.

(1) If u=5 and w=3, consider
B-a-C-b-A-c.
Its colors are 5,6,v,2,3. If v=4 this is a rainbow P_5 missing color 1. At endpoint B the three used-left neighbors a,b,c have colors 5,3,4, so the color-1 edge at B goes outside the path and extends it. Hence v=1.

(2) If u=2 and w=6, consider
A-c-C-b-B-a.
Its colors are 6,5,v,3,2. If v=1 this is rainbow and misses color 4. At endpoint A the used-left neighbors a,b,c have colors 1,2,6, so its color-4 edge goes outside and extends. Hence v=4.

(3) If u=2 and v=4, consider
B-a-A-c-C-b.
Its colors are 2,1,w,5,4. If w=3 this is rainbow and misses color 6. At endpoint B the used-left neighbors a,b,c have colors 2,3,4, so its color-6 edge goes outside. Hence w=6.

(4) If u=5 and v=1, consider
A-b-C-a-B-c.
Its colors are 2,1,6,5,4, so it is rainbow and misses color 3. If w=6, then at endpoint A the used-left neighbors a,b,c have colors 1,2,6, so the color-3 edge goes outside and extends. Hence w=3.

These implications leave two exceptional triples not covered by their antecedents. The triple (u,v,w)=(2,1,3) is impossible because
A-c-B-a-C-b
has colors 3,4,2,6,1, hence is a rainbow P_5 missing color 5, while endpoint A sees colors 1,2,3 on a,b,c and therefore has its color-5 edge outside the path.

Similarly (u,v,w)=(5,4,6) is impossible because
c-A-a-B-b-C
has colors 6,1,5,3,4, hence is a rainbow P_5 missing color 2, while endpoint C sees colors 6,4,5 on a,b,c and therefore has its color-2 edge outside the path.

Thus only
(u,v,w)=(2,4,6)
or
(u,v,w)=(5,1,3)
can remain.

A half-turn of the six-cycle swaps the bipartition classes and, after relabeling each color i by i+3 modulo 6, fixes the normalized cycle while sending the first chord triple to the second. Hence the two survivors are equivalent. We may therefore assume
aB=2, bC=4, cA=6,
which gives the displayed symmetric 3x3 matrix.