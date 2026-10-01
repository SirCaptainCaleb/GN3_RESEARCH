# Every six central deletions force three crossings or explicit order disagreement

## Statement

Under the hypotheses and notation of 10cf5889ee4a, every six consecutive indices in the central interval contain an index i such that every exact two-cover T of H-a_i satisfies at least one of the following: (1) T has at least three ordinary edges joining different members of the four-part partition V(L_i)|V(R_i)|V(B)|V(C); or (2) on one inherited support X in {L_i,R_i,B,C}, the T-block on V(X) is a Hamilton order different from the displayed inherited order, and therefore the displayed path and that T-block yield a reversed common edge, a tight triple reversing an ordered edge, or a vertex-simple tight cycle.

## Body

Choose i from 10cf5889ee4a so that H-a_i has no block-faithful exact two-cover. Let T be any exact two-cover of H-a_i. Cut every ordinary T-edge whose endpoints lie in different classes of the partition Pi={V(L_i),V(R_i),V(B),V(C)}. Let b_X be the number of resulting nonempty blocks in class X and let t be the number of cut cross-class edges. By the transition identity in coversurg01,

t = sum_X b_X - 2.

Each of the four classes is nonempty and Hamiltonian in its displayed inherited order, so b_X>=1 for every X. If some b_X>=2, then sum_X b_X>=5 and therefore t>=3. This is outcome (1).

It remains that b_X=1 for all four classes, so t=2. Thus for every inherited support X, all vertices of X occur contiguously in one T-component and form a tight Hamilton path Q_X on exactly V(X). If every Q_X had the same relative vertex order as the displayed inherited path X, then T would be block-faithful, contrary to the choice of i. Hence for some X the Hamilton orders X and Q_X disagree.

Apply the reversed-order lemma of pathcalc01 to these two tight Hamilton paths on the same vertex set. It gives one of: an ordered edge of Q_X that reverses an ordered edge of X; a tight triple on V(X) reversing an ordered edge of one of the two paths at an intersection; or a vertex-simple tight cycle on V(X). This is outcome (2).

Since 10cf5889ee4a supplies such an i in every six consecutive central positions, the asserted density follows.
