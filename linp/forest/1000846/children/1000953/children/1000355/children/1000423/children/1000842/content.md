# The crossed-chord order-six normal form forces a forbidden rainbow cycle

## Statement

The crossed-chord normal form of 8d4230198b1b is impossible. Therefore every proper 6-edge-coloring of K_{6,6} contains a rainbow P_6.

## Body

Normalize the crossed-chord case as in b3cf269da794:
        A B C
a       1 6 3
b       2 3 6
c       t 4 5,
where properness leaves t in {3,6}.

We show that either value of t forces a rainbow C_6, contradicting f644f80c598e.

Case 1: t=3.
Color 6 is absent from column A on the used rows a,b,c, so let d be the unused left vertex with dA=6. Likewise row c has used colors 3,4,5, so let D be the unused right vertex with cD=6.

Consider
d-A-b-B-c-C.
Its colors are 6,2,3,4,5, so it is a rainbow P_5 missing color 1. At endpoint C, the used left vertices on this path are d,b,c. The edges bC and cC have colors 6 and 5, while a is outside the path. Since aC=3, the color-1 edge at C cannot use a either. To avoid extending the displayed path to a rainbow P_6, the color-1 mate of C must therefore be d. Hence dC=1.

But then
C-d-A-b-B-c-C
is a rainbow C_6 with successive colors 1,6,2,3,4,5, contradicting f644f80c598e.

Case 2: t=6.
Now color 3 is absent from column A on the used rows, so let d be the unused left vertex with dA=3.

The path
d-A-a-B-c-C
has colors 3,1,6,4,5, hence is a rainbow P_5 missing color 2. At endpoint C, the used left vertices are d,a,c. We have aC=3 and cC=5, while b is outside the path but bC=6. Thus the unique color-2 edge at C cannot go to a,b, or c. To avoid extending the path, it must go to d. Therefore dC=2.

Consequently
d-A-a-B-c-C-d
is a rainbow C_6 with colors 3,1,6,4,5,2, again contradicting f644f80c598e.

Both possibilities are impossible. Hence the crossed-chord normal form cannot occur. Together with 3618afd5f90f, 8d4230198b1b, and f644f80c598e, this proves that every proper six-coloring of K_{6,6} has a rainbow P_6.
