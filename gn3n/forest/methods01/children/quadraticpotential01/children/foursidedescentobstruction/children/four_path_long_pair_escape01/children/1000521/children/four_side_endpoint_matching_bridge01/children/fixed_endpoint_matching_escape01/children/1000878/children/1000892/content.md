# A locally minimal four-side forces a positioned square with only five terminal outcomes

## Statement

Let H be a minimum counterexample and let X|P|Q be a spanning three-cover minimizing quadratic potential in its pairwise-repartition component, with |X|=4, P=(p_1,...,p_m), m>=7, and |V(H)|>=12. Put E={p_1,p_m}. Then there exist distinct a,b,c,d in X and C=E union {d} such that C+b and C+c are Hamiltonian and, writing K=H-(C union {b,c}), all four states K, K+b, K+c, and K+b+c=H-C are non-Hamiltonian with path-cover number two. Moreover at least one of the following holds: (1) a derived spanning three-cover C|A|B lies in a pairwise-repartition component containing a strictly smaller-Phi cover; (2) b and c are the two displayed endpoints of one component of some top-state two-cover of H-C, and that component has order at most five; (3) one of b,c is internal in every two-cover of H-C; (4) two two-covers of H-C induce different unordered support partitions; or (5) Hamilton paths on a common component support exhibit order disagreement.

## Body

The locally minimal four-side first saturates its endpoint six-shell by 1000878. Thus U=X union E is non-Hamiltonian, the two endpoint deletions are non-Hamiltonian, and every X-label deletion is Hamiltonian.

The endpoint-deletion graph on X cannot be a perfect matching: by the certified adjacent-edge elimination underlying 1000880 it has two adjacent edges. Relabel X={a,b,c,d} so the corresponding Hamiltonian four-windows are C+b and C+c with C=E union {d}. Their union C+b+c=U-a is Hamiltonian. The adjacent-window theorem therefore gives the full square
K, K+b, K+c, K+b+c,
where K=H-(C union {b,c}); all four states are non-Hamiltonian with path-cover number two.

Apply the certified two-label-square top-cover normal form. Either b and c are simultaneously exposed as displayed endpoints in a top two-cover A|B of H-C, one label is internal in every top two-cover, two top covers have different support partitions, or common-support Hamilton orders disagree.

Only the simultaneous-endpoint branch needs further work. If b and c lie on different components, transferring either exposed label into the Hamiltonian three-core C changes pair sizes (3,s) to (4,s-1), with Phi change 8-2s. In order at least twelve, failure of strict descent on both components would force both component orders at most four and hence |V(H)|<=11, impossible. Thus this case gives (1).

If b,c are the two endpoints of one component A of order s, then C+b+c is Hamiltonian and the two successive endpoint transfers replace C|A by (C+b+c)|(A-{b,c}). The Phi change is 20-4s, strictly negative for s>=6. Hence either the derived pairwise-repartition component contains a smaller-Phi cover, or s<=5, giving (2).

The remaining square-normal-form cases are exactly (3)-(5).
