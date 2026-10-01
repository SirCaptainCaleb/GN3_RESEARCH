# A 4|4|m state with m at least six has a two-move quadratic descent of size at least 2m-10

## Statement

Let H be a boundary tournament and let C=X|Y|P be a spanning three-cover with |X|=|Y|=4 and |P|=m>=6. Then there is a spanning three-cover C' at distance at most two from C in the pairwise-repartition graph such that Phi(C')<=Phi(C)-(2m-10). In particular C is not componentwise Phi-minimal.

## Body

Use fourfour_long_escape01. Its first move changes the 4|4 pair to 3|5 and raises Phi by 2. The second move is threesidedescent6 on the three-side and P. In its endpoint-extension branch that move drops Phi by 2m-8, giving net drop 2m-10. In its two-endpoint branch it drops Phi by 4m-20, giving net drop 4m-22, which is at least 2m-10 for m>=6. Thus the descent occurs within two moves and has the stated quantitative size. Consequently any branch requiring a componentwise Phi-minimal 4|4|m state for m>=6 is vacuous.
