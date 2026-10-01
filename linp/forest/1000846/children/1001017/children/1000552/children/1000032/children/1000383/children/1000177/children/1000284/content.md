# REFUTED route: top-boundary mutual-blocking rails

## Statement

Refuted as a general-q lemma. The construction incorrectly assumed that a rank-(q+1) edge f_j can terminate a maximum phi(v)=2q-2 edge path at v. For q>3, q+1<2q-2, so such a path cannot exist. The argument is valid only in the base case q=3 and must not be used in the general two-rank block.

## Body

The error is the sentence choosing a maximum (2q-2)-edge path ending in f_j. Since phi(f_j)=q+1, any path ending in f_j has length at most q+1. Thus for q>3 there is no such path of length 2q-2. The correct general top-boundary framework is 28445330afcc: fix one maximum phi(v)-path ending at v, not in a prescribed high competitor, and use path-relative witness localization to place the high competitors in the four slots L,A,B,R.
