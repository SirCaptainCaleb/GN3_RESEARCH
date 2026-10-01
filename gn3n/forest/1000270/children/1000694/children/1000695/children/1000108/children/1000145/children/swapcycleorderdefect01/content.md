# Every singleton-swap cycle in a counterexample carries a genuine order defect

## Statement

Let H be a boundary tournament with pc(H)>2. Choose deletion covers F_{a_1},...,F_{a_k} for distinct labels, k>=4, with nonempty common surviving core, and suppose their singleton lifts form a cycle in the singleton-swap graph. Then all covers on the cycle are pairwise support-compatible, but they cannot be pairwise fully compatible. Consequently some pair of covers on the cycle is support-compatible and order-incompatible on a common support.

## Body

Every singleton-swap edge is support-compatible by singletonsupsandwich01, so the cycle is support-compatible. The certified cycle-closure theorem compatsupportc5close24 makes the whole cycle a support-compatibility clique. If every pair were also fully compatible, then any four covers from the cycle would have globally consistent full pair-state data; by the certified compatibility-gluing threshold summarized in cocyclescope01, those four deletion covers would glue to a spanning two-cover of H, contrary to pc(H)>2. Therefore at least one pair is support-compatible but not fully compatible. Since support already agrees, its incompatibility is purely relative-order disagreement. Thus singleton-swap cycles are automatic producers of order defects rather than support defects.