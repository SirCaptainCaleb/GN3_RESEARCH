# Every three-side beside a path of order at least five has immediate strict quadratic descent

## Statement

Let H be any boundary tournament and let C=X|P|Q be a spanning three-cover with |X|=3 and |P|=m>=5. Then one legal pairwise repartition of X|P produces a spanning three-cover C' with strictly smaller quadratic potential. If m=5, the pair X|P can be replaced by a Hamiltonian 4|4 partition and Phi decreases by exactly two. If m>=6, the certified three-side descent theorem gives an immediate strict descent.

## Body

If m=5, the induced boundary tournament on the eight-vertex set V(X) union V(P) has, by balanced8_conceptual_repair01, a partition into two Hamiltonian four-vertex induced subtournaments. Replacing X|P by these two Hamiltonian paths is one legal pairwise repartition, leaves Q unchanged, and changes the pairwise quadratic contribution from 3^2+5^2=34 to 4^2+4^2=32. Hence Phi decreases by two.

If m>=6, apply threesidedescent6 directly to X|P. It gives one legal pairwise repartition with strictly smaller quadratic potential. Thus the threshold is five for arbitrary boundary tournaments.
