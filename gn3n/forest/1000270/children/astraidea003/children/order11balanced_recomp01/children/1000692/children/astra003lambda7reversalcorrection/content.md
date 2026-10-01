# Correction: the current lambda-seven eliminations use invalid reversal steps

## Statement

The current proofs astra003lambda7case1, astra003noLambda7, and astra003nolambda7 do not establish elimination of maximum path order seven. definitions01 explicitly forbids arbitrary reversal of a tight path. The first two proofs reverse a displayed tight path without checking the reversed triples. The third proof takes a tight triple (s,R,v) and incorrectly infers its reversal (v,R,s) is tight; boundary antisymmetry implies the opposite. Thus the lambda=7 branch remains open pending a reversal-free repair.

## Body

The project convention in definitions01 is: for each three distinct x,y,z, exactly one of (x,y,z) and (z,y,x) is tight. Accordingly, arbitrary reversal of a tight path is not valid; reversing even one tight triple gives its non-tight mate.

This invalidates the currently pending lambda-seven arguments as written.

1. astra003lambda7case1 starts from the tight path A=(u,L,o_0,o_1) and asserts that (o_1,o_0,L,u) is tight because paths reverse. No theorem establishes the reversed consecutive triples, and definitions01 explicitly forbids this inference.

2. astra003noLambda7 repeats the same error with A=(u,L,o_0,o_1,R,v), asserting its complete reversal is tight.

3. astra003nolambda7 instead uses codim4_01 Proposition 1.2, which gives (i_0,R,v) tight, and then asserts “reversing gives” (v,R,i_0) tight. Boundary antisymmetry says exactly one of these is tight, so the latter is non-tight.

Therefore none of these three nodes currently eliminates lambda=7. The valid codim4_01 output remains: for Y=(L,u,x_2,x_3,x_4,v,R) with four-vertex complement S, Proposition 5.1 supplies either a 4|4 or a 6|2 exact cover on S union {L,u,v,R}. A correct closure needs a reversal-free splice or a different contradiction. Until then lambda remains in {5,6,7}.
