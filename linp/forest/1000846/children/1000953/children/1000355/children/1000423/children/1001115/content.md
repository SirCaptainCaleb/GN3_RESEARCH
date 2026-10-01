# The rainbow-six-cycle normal form forces a color collision

## Statement

The closing-chord (rainbow C_6) normal form of 8d4230198b1b is impossible. Hence any hypothetical proper 6-coloring of K_{6,6} with no rainbow P_6 must lie in the crossed-chord normal form.

## Body

By 81565c9de9a6 we may normalize the used 3x3 color matrix to
        A B C
a       1 2 6
b       2 3 4
c       6 4 5.

Let D,E,F be the three unused right-side vertices. Row a already uses colors 1,2,6 on A,B,C, so its three edges to D,E,F have colors 3,4,5 in some order. Relabel the unused columns so that
aD=3 and aF=5.
(The color-4 column is irrelevant.)

Consider the five-edge path
D-a-A-b-C-c.
Its colors are
3,1,2,4,5,
so it is rainbow and misses color 6. Since there is no rainbow P_6, the color-6 edge at endpoint D must go to one of the three left-side vertices used by this path, namely a,b,c. It is not aD, whose color is 3. It also cannot be cD, because c already has its unique color-6 edge cA. Therefore
bD=6.

Now consider
F-a-A-b-B-c.
Its colors are
5,1,2,3,4,
so this is another rainbow P_5 missing color 6. Exactly the same endpoint argument at F shows that its color-6 mate must be one of a,b,c. It is not a because aF=5, and it is not c because cA=6. Hence
bF=6.

But a proper edge-coloring has at most one edge of a given color incident with b. The two distinct edges bD and bF cannot both have color 6. This contradiction eliminates the closing-chord normal form.
