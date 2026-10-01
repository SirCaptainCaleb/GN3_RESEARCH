# Two-edge odd walks are one-vertex omission swaps with a fixed Hamiltonian side

## Statement

Let H be a minimum counterexample in the sharp half-order shell |V(H)|=2lambda+1, and let G be the Hamiltonian-support odd graph. Suppose S_0-S_1-S_2 is a length-two walk with distinct consecutive edge labels x,y. Then y is in S_0, x is in S_2, and S_2=(S_0-{y}) union {x}. The two edges give exact deletion covers F_x=S_0|S_1 of H-x and F_y=S_1|S_2 of H-y with one identical Hamiltonian component S_1. For any exact two-cover T of H-{x,y}, at least one of the following holds: (i) y is internal in its F_x component and T crosses the three inherited pieces of F_x-y; (ii) x is internal in its F_y component and T crosses the three inherited pieces of F_y-x; (iii) both x,y are endpoints of their outer components, and after deleting them the induced covers of H-{x,y} either expose relative-order disagreement on their common support, or coincide as one exact cover K|S_1 where K=S_0-{y}=S_2-{x}, with x and y both restoring at the same end of the same Hamilton order on K. Thus every length-two odd walk yields explicit deletion disturbance or a rigid clean one-vertex omission swap around the fixed side S_1.

## Body

# Proof

Because S_0 and S_1 are disjoint lambda-sets in a (2lambda+1)-set, V(H)=S_0 disjoint-union S_1 disjoint-union {x}. Likewise V(H)=S_1 disjoint-union S_2 disjoint-union {y}. Since the two edges are distinct, x!=y. Hence y lies in S_0 and x lies in S_2, and complementing S_1 gives S_2=(S_0-{y}) union {x}. Put K=S_0-{y}=S_2-{x}.

Choose arbitrary Hamilton orders on S_0,S_1,S_2, using the same chosen Hamilton order on S_1 in both edge covers. Then F_x=S_0|S_1 and F_y=S_1|S_2 are exact covers of H-x and H-y. By minimum-counterexample calculus H-{x,y} has an exact two-cover T.

Apply the certified two-deletion endpoint trichotomy from deletion01 to F_x,F_y,T. If y is internal in its F_x component, its first alternative gives (i). If x is internal in its F_y component, its second alternative gives (ii). Otherwise both are endpoints and deleting them gives exact covers T_x=F_x-y and T_y=F_y-x of H-{x,y}. Both have the same unordered support partition {K,S_1}. If their ordered covers differ, the exact-cover disagreement theorem in deletion01 gives relative-order disagreement on K or S_1; the S_1 orders were chosen identical, so the disagreement is on K. If T_x=T_y, the common endpoint-extension lemma in deletion01 says the restorations by x and y use the same end of the same component. They cannot restore to S_1, because F_x places y in S_0=K union {y} and F_y places x in S_2=K union {x}. Hence both restore at the same end of the common K-component. This is (iii). ∎
