# Gap: the proof does not obtain a concrete five/six-window disagreement from 44a0c8ced13c

## Statement

The proof of 7ba450ffcfe5 is not currently valid. The theorem 44a0c8ced13c proves existence of some relative-order disagreement by contradiction from global order-neutrality; it does not assert that the actual witness in an arbitrary minimum counterexample is the five-window/six-window witness constructed inside that contradiction argument. Thus one cannot cite “the proof of 44a0c8ced13c” to obtain two disagreeing paths of order at least three. Without such a substantial witness, the reversed-common-edge outcome of pathcalc01 may degenerate to two-vertex path data and does not automatically yield a reversing tight triple.

## Body

To repair 7ba450ffcfe5, one needs either a valid strengthening of 44a0c8ced13c to substantial disagreement, or a direct theorem that every arbitrary order-disagreement witness in a minimum counterexample yields nonvacuous local reversal data. The pending theorem 50137573941d was intended to supply the former but currently has the separate hypothesis gap recorded beneath it.
