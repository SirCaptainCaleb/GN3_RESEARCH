# Full endpoint conflict matching sharpens the fixed-entrance incident-rank bound

## Statement

If h is an ascending edge of rank q in a finite linear 3-graph and v is terminal at h, then for q>=4
|J_q(v)| <= floor((3q-3)/2),
where J_q(v)={f: v in f and phi(f)<=q}. For q=2,3 the sharper bounds are 1 and 2. Consequently, with S=sum_v phi(v), n_+ the number of nonisolated vertices, E_even the number of nonisolated vertices of even rank, N_3 the number of vertices of rank 3, A the number of ascending edges, and m=|E(H)|,
A <= (3S-3n_+-E_even-2N_3)/4
and
m <= (11S-7n_+-E_even-2N_3)/12.
Hence every P_ell^(3)-free linear 3-graph satisfies m<=((11ell-18)/12)n.

## Body

Choose a q-edge path P=(g_1,...,g_q) ending in h=g_q at v, and let x=g_{q-1} intersect h. Since h is ascending, phi(x)=q-1. Put W=V(P) minus h. For f in J_q(v) minus {h}, let C_f=(f minus {v}) intersect W. These nonempty sets are pairwise disjoint and have size one or two.

Write z_i=g_i intersect g_{i+1}; write g_1={a_1,b_1,z_1}; and for 2<=i<=q-1 let b_i be the private vertex of g_i. Singleton contacts at a_1 or b_1 are impossible, because f,g_1,...,g_{q-1} would be a q-edge path ending at x. Singleton contacts at b_{q-2} or z_{q-2} are impossible, because g_1,...,g_{q-2},f,h would be a q-edge longest path entering h through v rather than its unique entrance x.

For q>=5, add the q-3 pair constraints
{z_1,z_2}, {b_i,z_{i+1}} for 2<=i<=q-4, and {b_{q-3},b_{q-1}}.
Together with the four forbidden singleton positions, these sets are pairwise disjoint and partition W. No pair can consist of two singleton contact vertices. For {z_1,z_2}, the forbidden splice is
g_1,f,k,g_3,...,g_{q-1};
for {b_i,z_{i+1}} it is
g_1,...,g_i,f,k,g_{i+2},...,g_{q-1};
and for {b_{q-3},b_{q-1}} it is
g_1,...,g_{q-3},f,k,g_{q-1}.
Each is a q-edge linear path ending at x, contradicting phi(x)=q-1. For q=4, the four singleton constraints are a_1,b_1,b_2,z_2 and the remaining pair {z_1,b_3} has the same splice g_1,f,k,g_3.

Let s,d,u be the numbers of singleton contacts, double contacts, and unused vertices of W. Then
s+2d+u=2q-2
and
|J_q(v)|=1+s+d=2q-1-d-u.
Every one of the q+1 disjoint constraints contains an unused vertex or a vertex of a double contact. Hence u+2d>=q+1, so d+u>=ceil((q+1)/2), proving
|J_q(v)|<=floor((3q-3)/2).

If t(v) counts ascending edges at which v is terminal, choose a maximum-rank one when t(v)>0. The local bound gives t(v)<=beta(phi(v)), where beta(1)=0,beta(2)=1,beta(3)=2 and beta(p)=floor((3p-3)/2) for p>=4. Since each ascending edge has two terminals,
2A=sum_v t(v)<=sum_v beta(phi(v))
<= (3S-3n_+-E_even)/2-N_3.
Thus A<=(3S-3n_+-E_even-2N_3)/4. Combining with the certified inequality 3m-A<=2S-n_+ gives the stated global bound. For P_ell-free H, S<=(ell-1)n_+, yielding m<=((11ell-18)/12)n.