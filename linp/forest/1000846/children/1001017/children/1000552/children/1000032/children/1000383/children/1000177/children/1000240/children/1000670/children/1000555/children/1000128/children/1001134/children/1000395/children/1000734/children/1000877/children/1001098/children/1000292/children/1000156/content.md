# RETRACTED: low-rank residue from the lens-free whole-pair braid

## Statement

Retracted. The claimed positive-density lower-rank subfamily does not follow from the cumulative fixed-entrance bound. That bound says the number of common-terminal ascending edges of rank at most s is at most gamma(s); therefore it gives a lower bound, not an upper bound, on the number of edges with rank greater than s. The proof of the previous version reversed this inequality. No low-rank residue follows from 3ef8a7c2d941 by this counting argument.

## Body

The previous proof wrote that the number of early distinguished edges of rank greater than cq is at most h-gamma(floor(cq)). This is the wrong direction. If N_le(s) denotes the number of edges of rank at most s, the exact cumulative theorem gives N_le(s)<=gamma(s). Hence N_gt(s)=h-N_le(s)>=h-gamma(s), a lower bound on the high-rank tail. It does not prevent all of the 25q/88 retained whole pairs from lying in the high-rank tail. Therefore the 1/110 claim at c=4/5, and the displayed general c-bound, are unsupported and are withdrawn.
