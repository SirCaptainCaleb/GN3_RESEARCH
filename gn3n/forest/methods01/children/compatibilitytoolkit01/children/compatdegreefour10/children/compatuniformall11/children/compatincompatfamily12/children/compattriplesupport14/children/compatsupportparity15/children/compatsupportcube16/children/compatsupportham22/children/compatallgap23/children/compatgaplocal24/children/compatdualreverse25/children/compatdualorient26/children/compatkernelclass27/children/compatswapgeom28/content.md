# Opposite reverse-cross orientation is exactly a two-core label transposition

## Statement

Continue the opposite-orientation branch of compatdualorient26 inside the two-gap/two-gap setting. After orienting the local common orders, one may write the occupied gaps on R as L_R | r | R_R and on S as L_S | s | R_S so that x uses the left gap and y the right gap at r, whereas y uses the left gap and x the right gap at s. Thus the synchronized reverse-cross pattern is exactly a transposition of x and y across the two cores. The third special label z uses one of the two occupied gaps at each core, so relative to the pair {x,y} it has exactly four alignment types: it follows x on both cores, follows y on both, follows x on R and y on S, or follows y on R and x on S.

## Body

# Proof

In the two-gap/two-gap branch, compatgaplocal24 arises from two adjacent occupied insertion gaps around a unique shared core vertex.

On R, choose the local orientation so x is inserted in the left occupied gap and y in the right occupied gap. The simultaneous candidate then contains the local word

..., x, r, y, ...

and its coupling triple is (x,r,y). Since simultaneous insertion would give a spanning two-cover, this triple is non-tight. Boundary antisymmetry gives the reverse-cross triple

(y,r,x)

tight.

The opposite-orientation residue from compatdualorient26 says that on S the synchronized reverse-cross triple has the opposite orientation,

(x,s,y)

tight.

If x were again in the left occupied gap and y in the right occupied gap on S, the forbidden simultaneous-insertion cross triple would be (x,s,y), whose reverse would have to be tight. But (x,s,y) itself is tight. Therefore this placement is impossible. Hence on S the gap roles are reversed: y occupies the left gap and x the right gap.

Thus x,y exchange their left/right positions between the two cores.

The remaining label z occupies one of the same two adjacent gaps at each core by compatallgap23. At R it therefore follows either x's gap or y's gap; independently at S it follows either x's gap or y's gap. These two binary choices give exactly the four listed alignment types.

No Hamiltonicity assertion beyond the already established insertion paths is used.