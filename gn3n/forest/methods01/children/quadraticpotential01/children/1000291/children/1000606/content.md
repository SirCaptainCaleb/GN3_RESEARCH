# A largest-second size gap of three synchronizes adjacent windows without equality of the lower sides

## Statement

Let H be a minimum counterexample and let A|B|C be a globally Phi-minimal three-cover with a=|A|>=b=|B|>=c=|C|. Assume A=(a_0,...,a_{b+2}) is globally longest and a=b+3. Put S_L=(a_1,...,a_b) and S_R=(a_2,...,a_{b+1}). Then either a flanking label is internal in a complementary a|c two-cover, in which case after deleting that label every two-cover of the lower state contains an ordinary edge whose endpoints lie in two different inherited path blocks, or there are two two-covers of the common lower graph K=H-{a_1,...,a_{b+1}}, each with component orders a and c-1, whose small paths have respectively a_0 and a_{b+2} as endpoints. For these two covers, either their support partitions differ, or their common large support is contained in V(B) union V(C), is vertex-disjoint from A, and is globally longest; in the latter case it and A contain a two-sided maximum-path extension witness.

## Body

Apply 5ec26ec830d3 to each b-window S_L,S_R. Every two-cover of either complement has component orders {a,c}. Choose T_L=P_L|Q_L and T_R=P_R|Q_R with |P_L|=|P_R|=a and |Q_L|=|Q_R|=c. Apply 203187bcc627 to each window. If any flanking label is internal in the corresponding chosen cover, then after deleting that label every two-cover of the lower state contains an ordinary edge whose endpoints lie in two different inherited path blocks.

Assume no flank is internal. Then a_0 and a_{b+1} are the endpoints of Q_L, while a_1 and a_{b+2} are the endpoints of Q_R. Delete a_{b+1} from Q_L and a_1 from Q_R. This gives two two-covers of the same induced graph K=H-{a_1,...,a_{b+1}}, each with component orders a and c-1; the first small path has endpoint a_0 and the second has endpoint a_{b+2}.

If their support partitions differ, the first conclusion holds. If the partitions agree, the unequal component orders identify a common small support. It contains both a_0 and a_{b+2}, so the common large support contains no vertex of A. Since V(K)=V(B) union V(C) union {a_0,a_{b+2}}, that large support lies in V(B) union V(C). Its order is a, so it is globally longest. Apply the maximum-path splicing lemma in pathcalc01 to it and A. Again, b=c is never used.
