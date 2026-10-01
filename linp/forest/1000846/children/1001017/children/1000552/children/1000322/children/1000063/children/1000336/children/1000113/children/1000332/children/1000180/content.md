# Consecutive private single blockers can occur on a longest endpoint path

## Statement

The claim 47c17993cf60 is false. There is a linear 3-graph with a longest 3-edge path Q ending at x whose opposite endpoint a supports two single-blocking edges with blockers in consecutive private slots p_2,p_3.

## Body

Let g1={a,a1,c1}, g2={c1,p2,c2}, g3={c2,p3,x}, f2={a,p2,r2}, and f3={a,p3,r3}, with all displayed symbols distinct except the intentional repetitions. This is a linear 3-graph. Its intersection graph has adjacencies g1-g2, g2-g3, g1-f2, g2-f2, g1-f3, g3-f3, f2-f3. The induced paths ending at g3 have maximum length three; examples are g1,g2,g3; g1,f3,g3; f2,g2,g3; and f2,f3,g3. Since x is private in g3, φ(x)=3 and Q=(g1,g2,g3) is a longest path with last vertex x. Relative to the opposite last vertex a of g1, f2 is single-blocking with blocker p2, the private slot of C2, and f3 is single-blocking with blocker p3, the private terminal slot of C3. Thus consecutive private single blockers do occur. The splice displayed in 47c17993cf60 is not a linear path: f2 is not adjacent to g2 at the point where it is placed after the reversed prefix as written, and more invariantly the old consecutive intersection g2∩g3 becomes a nonconsecutive chord in the attempted four-edge route. Hence 47c17993cf60 is refuted, and the dependent 4/7 rank-floor lemma 673744910282 is unsupported.