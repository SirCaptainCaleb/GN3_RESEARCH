# An ascending last edge gives a three-halves incident rank bound and an eleven-twelfths Turan bound

## Statement

Let H be a finite linear 3-graph. If h is ascending of rank q and v is terminal at h, then #{f containing v: phi(f)<=q}<=floor((3q-1)/2), with the stronger bounds 1 for q=2 and 2 for q=3. Writing n_+ for the number of nonisolated vertices, S=sum_v phi(v), A for the number of ascending edges, and m=|E(H)|, one has A<=(3S-n_+)/4 and m<=(11S-5n_+)/12. Hence for ell>=2, ex_L(n,P_ell^(3))<=((11ell-16)/12)n.

## Body

Let H be a finite linear 3-graph. A linear path is an ordered sequence of distinct edges in which consecutive edges meet in one vertex and nonconsecutive edges are disjoint; its length is its number of edges. A last vertex belongs to the last edge but not the preceding edge. Write phi(e) for the maximum length of a path with last edge e, phi(v) for the maximum length with last vertex v, and phi(e,v) for the maximum with both prescribed. A vertex v is terminal at e when phi(e,v)=phi(e). A nonspecial edge has exactly two terminal vertices, and every longest path ending in it enters through its remaining vertex x. Such an edge is ascending when phi(x)=phi(e)-1.

LOCAL LEMMA.
Suppose h is an ascending edge of rank q, and v is terminal at h. Put J_q(v)={f: v in f and phi(f)<=q}. Then
 |J_q(v)| <= floor((3q-1)/2).
In fact |J_2(v)|=1 and |J_3(v)|<=2.

Proof. Choose a q-edge path P=(g_1,...,g_q) with last edge h=g_q and last vertex v. Write x=g_{q-1} cap h for the unique entrance of h. Then phi(x)=q-1. Let W=V(P) minus h, so |W|=2q-2. For every f in J_q(v) other than h, let C_f=(f minus {v}) cap W. This set is nonempty: if empty, linearity and f cap h={v} imply that appending f to P gives a (q+1)-edge path ending in f, contradicting phi(f)<=q. The sets C_f are pairwise disjoint by linearity, and each has one or two vertices.

For q=2, any f!=h through v makes (f,h) a longest two-edge path entering h through v, contrary to its unique entrance x. Hence J_2(v)={h}. For q=3, if C_f were contained in g_1, it would have exactly one vertex by linearity, and (g_1,f,h) would enter h through v in three edges. Thus every f!=h has a contact in W minus g_1, which has only one vertex. Hence |J_3(v)|<=2.

Assume q>=4. Put z_i=g_i cap g_{i+1}. For 2<=i<=q-1 let b_i be the unique vertex of g_i other than z_{i-1},z_i. Choose b_1 in g_1 minus {z_1}. In W consider the following pairwise disjoint sets:
 {b_i,z_{i+1}} for 1<=i<=q-4;
 {b_{q-3},b_{q-1}};
 {b_{q-2}};
 {z_{q-2}}.
There are q-1 sets: q-3 pairs and two singletons. The first family is empty when q=4.

No pair in this family can have both its vertices as one-vertex contact sets C_f,C_k. For the pair {b_i,z_{i+1}}, such edges f,k would give the sequence
 g_1,...,g_i,f,k,g_{i+2},...,g_{q-1}.
This is a q-edge linear path with last vertex x. The prefix and suffix are separated by the omitted edge g_{i+1}; f and k meet at v, which is absent from the retained path edges; their only other contacts with those edges are b_i in g_i and z_{i+1} in g_{i+2}. Also x belongs only to the final retained edge and cannot lie in f or k, since each already meets h at v. Thus every consecutive intersection is the specified singleton and every nonconsecutive intersection is empty. Its length q contradicts phi(x)=q-1.

For the pair {b_{q-3},b_{q-1}}, the same argument uses
 g_1,...,g_{q-3},f,k,g_{q-1},
again a q-edge linear path ending at x.

Neither singleton can itself be a one-vertex contact set. If C_f={b_{q-2}} or C_f={z_{q-2}}, then
 g_1,...,g_{q-2},f,h
is a q-edge linear path entering h through v rather than x. The possible second occurrence of z_{q-2} is in the omitted g_{q-1}, and h is disjoint from the entire retained prefix. This contradicts nonspeciality of h.

Let s be the number of one-vertex contact sets, d the number of two-vertex contact sets, and u the number of unused vertices of W. Disjointness gives
 s+2d+u=2q-2,
 |J_q(v)|=1+s+d=2q-1-d-u.
Each of the q-1 disjoint sets displayed above must contain an unused vertex or a vertex belonging to a two-vertex contact set. There are only u+2d such vertices. Consequently
 u+2d>=q-1,
 d+u>=ceil((q-1)/2),
and hence
 |J_q(v)|<=2q-1-ceil((q-1)/2)=floor((3q-1)/2).
This proves the lemma. Crucially, the singly contacting edges need not meet P at their own entrances. Their contacts may be terminals. The low-potential vertex contradicted by the two-edge splice is x, the entrance of the fixed last edge h.

ASCENDING-EDGE COUNT.
Let V_+ be the nonisolated vertices, n_+=|V_+|, S=sum_{v in V_+}phi(v), and A the number of ascending edges. Let t(v) count ascending edges at which v is terminal. If t(v)>0, select such an edge h of greatest edge rank q. Every edge counted by t(v) belongs to J_q(v), and q<=phi(v). The local lemma yields
 t(v)<=floor((3phi(v)-1)/2).
If t(v)=0, this bound still holds because phi(v)>=1 for v in V_+. Each ascending edge has two terminals. Therefore
 2A=sum_v t(v)<= (3S-n_+)/2,
 A<=(3S-n_+)/4.

GLOBAL ACCOUNTING.
For completeness, fix v in V_+ and a maximum p=phi(v) path P ending at v. Every incident edge f of rank at most p, except possibly the last edge of P, has a contact in V(P) outside that last edge; otherwise it could be appended to P. Distinct incident edges have disjoint contacts. Thus at most 2p-1 incident edges have rank at most p.

A special edge contributes three incidences (e,v) with phi(e)<=phi(v). A nonspecial edge e of rank q contributes its two terminal incidences; at its unique entrance x, deleting e from a longest e-ending path shows phi(x)>=q-1. The entrance incidence also contributes unless phi(x)=q-1, exactly the ascending case. Summing gives
 3m-A<=2S-n_+.
Together with the preceding ascending-edge count,
 3m<=2S-n_+ +(3S-n_+)/4=(11S-5n_+)/4.
Consequently
 m<=(11S-5n_+)/12.

In a P_ell-free linear 3-graph, phi(v)<=ell-1. For every integer ell>=2,
 m<=((11ell-16)/12)n_+<=((11ell-16)/12)n.
The matching construction, the treatment of double contacts, and all endpoint corrections are explicit. No consecutive-rank block conjecture, minimum-terminal-potential charging, or assumption that single contacts are entrance contacts is used.