# Each all-equal support blocks insertion of four complementary endpoints

## Statement

In the setting of 324625f1ec69, fix i and the displayed Hamilton path P_i=(t_i,M_i,t_{i+1}) on S_i. Let E_i be the set of displayed endpoints of the two complementary paths M_{i+1} and A_{i+2} in H-S_i=M_{i+1}|A_{i+2}, omitting duplicates only when a complementary path is a singleton. Every x in E_i is noninsertable into the displayed order P_i. Hence the three-support triangle carries, cyclically, four endpoint noninsertion constraints at each S_i.

## Body

Fix x to be an endpoint of one complementary path, say Q, and let R be the other complementary path. If x were insertable into the displayed Hamilton path P_i, then inserting x would give a Hamilton path on S_i union {x}. Since x is an endpoint of Q, deleting x from the displayed path Q leaves a tight path Q-x (possibly empty). Thus the enlarged Hamilton path together with Q-x and R is a spanning two-cover of H, contradicting pc(H)>2. The same argument applies to either endpoint of either complementary path. Applying it for i=1,2,3 gives the synchronized family of endpoint blockades.