# The c+3,c,c longest-path residue synchronizes two adjacent windows on one lower state

## Statement

Let H be a minimum counterexample and let A|B|C be a globally Phi-minimal spanning three-cover with |A|=c+3 and |B|=|C|=c. Assume A=(a_0,...,a_{c+2}) is globally longest. Put S_L=(a_1,...,a_c) and S_R=(a_2,...,a_{c+1}). Then either an adjacent-window endpoint is internal in a complementary a|c cover and, after its deletion, every two-cover has an ordinary edge joining two distinct inherited blocks, or there are two two-covers of the common lower graph K=H-{a_1,...,a_{c+1}}, each of component orders c+3 and c-1, such that the small path of one has a_0 as an endpoint and the small path of the other has a_{c+2} as an endpoint. For these two covers, either their support partitions differ, or their support partitions agree, in which case their common large support is contained in B union C and is a globally longest path vertex-disjoint from A; hence A and that path carry the two-sided maximum-path extension witness from pathcalc01.

## Body

# Proof

Set a=c+3. Apply the certified profile-propagation theorem 5ec26ec830d3 to each c-window S_L,S_R. Thus every two-cover of J_L=H-V(S_L) and J_R=H-V(S_R) has component-order multiset {a,c}. Choose covers
T_L=P_L|Q_L,  T_R=P_R|Q_R
with |P_L|=|P_R|=a and |Q_L|=|Q_R|=c.

For S_L the flanking displayed vertices are a_0 and a_{c+1}; for S_R they are a_1 and a_{c+2}. Apply 203187bcc627 to each window. If any one of its two flanking labels is internal in the corresponding chosen cover, then after deleting that label every two-cover of the resulting lower graph contains an ordinary edge joining two distinct blocks of the three-part partition inherited from that cover. This is the first alternative.

Assume no flank is internal. Then 203187bcc627 forces a_0 and a_{c+1} to be the two displayed endpoints of Q_L, and a_1 and a_{c+2} to be the two displayed endpoints of Q_R. Delete the endpoint a_{c+1} from Q_L and the endpoint a_1 from Q_R. This yields two-covers
F_L=P_L | (Q_L-a_{c+1}),
F_R=P_R | (Q_R-a_1)
of the same induced lower graph
K=H-{a_1,...,a_{c+1}}.
Both have component orders a=c+3 and c-1. Moreover the small component of F_L has a_0 as a displayed endpoint, while the small component of F_R has a_{c+2} as a displayed endpoint.

If the two unordered support partitions differ, we obtain two different support partitions on K. Suppose instead that the support partitions agree. Since the two component orders c+3 and c-1 are unequal, the small support is canonically identified and is the same in both covers. It therefore contains both a_0 and a_{c+2}. The large common support contains neither. But
V(K)=V(B) union V(C) union {a_0,a_{c+2}},
so the common large support is contained in V(B) union V(C). Any Hamilton path on this support is vertex-disjoint from A and has order c+3=|A|. Since A is globally longest, this large path is globally longest as well.

Apply the certified maximum-path splicing lemma in pathcalc01 to A and this vertex-disjoint globally maximum path. It supplies distinct r,p,q in their union for which both (r,p,q) and (p,q,r) are tight. ∎