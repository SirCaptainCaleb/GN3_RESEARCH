# First-edge contacts sharpen the eleven-twelfths bound

## Statement

Let H be a finite linear 3-graph. If h is an ascending edge of rank q and v is terminal at h, then #{f containing v: phi(f)<=q}<=floor((3q-2)/2) for q>=4; for q=2,3 the sharper bounds are 1 and 2. Consequently, if n_+ is the number of nonisolated vertices, S=sum_v phi(v), A is the number of ascending edges, and m=|E(H)|, then A<=(3S-2n_+)/4 and m<=(11S-6n_+)/12. Hence every P_ell^(3)-free linear 3-graph satisfies m<=((11ell-17)/12)n for ell>=2.

## Body

Fix an ascending edge h of rank q and a terminal v of h. Choose a q-edge path P=(g_1,...,g_q) with last edge h=g_q and last vertex v. Let x=g_{q-1}∩h. Since h is ascending, x is its unique entrance and phi(x)=q-1. Put W=V(P) minus h, so |W|=2q-2. For every incident edge f!=h with phi(f)<=q define C_f=(f minus {v})∩W. Then C_f is nonempty, since otherwise f could be appended to P through v, and the sets C_f are pairwise disjoint by linearity. Each has size one or two. The cases q=2,3 give the sharper bounds 1 and 2 exactly as follows: for q=2 any second edge through v would give a longest h-path through the wrong entrance v; for q=3 every f!=h must meet the unique vertex of W outside g_1, so at most one such f exists.

Assume q>=4. Write z_i=g_i∩g_{i+1}. Let a_1,b_1 be the two vertices of g_1 minus {z_1}; for 2<=i<=q-1 let b_i be the vertex of g_i minus {z_{i-1},z_i}. Four vertices can never be singleton contact sets: a_1,b_1,b_{q-2},z_{q-2}. Indeed, if C_f={a_1} or {b_1}, then f,g_1,...,g_{q-1} is a q-edge linear path with last vertex x, contradicting phi(x)=q-1. If C_f={b_{q-2}} or {z_{q-2}}, then g_1,...,g_{q-2},f,h is a q-edge path ending in h through terminal v rather than its unique entrance x, again impossible.

For q>=5 consider additionally the pair {b_{q-3},b_{q-1}}, and for 2<=i<=q-4 the pairs {b_i,z_{i+1}}. (The latter family is empty when q<=5.) No such pair can consist of two singleton contact vertices. For {b_i,z_{i+1}}, singleton edges f,k would make g_1,...,g_i,f,k,g_{i+2},...,g_{q-1} a q-edge linear path with last vertex x. For {b_{q-3},b_{q-1}}, use g_1,...,g_{q-3},f,k,g_{q-1}. In each case linearity follows because the omitted path edge separates the retained prefix and suffix, while f and k meet exactly at v and have no other contacts with P.

Thus for q=4 there are four pairwise disjoint one-vertex forbidden sets {a_1},{b_1},{b_2},{z_2}. For q>=5 there are four such singleton sets together with q-4 pair sets, all pairwise disjoint. In either case there are q disjoint constraint sets, each of which contains either an unused vertex of W or a vertex belonging to some two-vertex contact set C_f.

Let s be the number of one-vertex contact sets, d the number of two-vertex contact sets, and u the number of unused vertices of W. Then s+2d+u=2q-2 and |J_q(v)|=1+s+d=2q-1-d-u, where J_q(v)={f:v∈f, phi(f)<=q}. The q disjoint constraints give u+2d>=q, hence d+u>=ceil(q/2). Therefore |J_q(v)|<=2q-1-ceil(q/2)=floor((3q-2)/2).

Now let t(v) count ascending edges at which v is terminal. If t(v)>0, choose one of greatest rank q. Every edge counted by t(v) lies in J_q(v), and q<=phi(v). The preceding bound, together with the q=2,3 cases, gives t(v)<=(3phi(v)-2)/2 for every nonisolated v; when t(v)=0 the same inequality is trivial. Since every ascending edge has exactly two terminals, 2A=sum_v t(v)<=(3S-2n_+)/2, so A<=(3S-2n_+)/4.

Finally, the standard ascending-incidence count gives 3m-A<=2S-n_+: at a vertex v, at most 2phi(v)-1 incident edges have rank at most phi(v), while every special or nonascending edge contributes three such incidences and every ascending edge contributes two. Hence 3m<=2S-n_++(3S-2n_+)/4=(11S-6n_+)/4, proving m<=(11S-6n_+)/12. If H is P_ell^(3)-free, then phi(v)<=ell-1, so S<=(ell-1)n_+ and m<=((11ell-17)/12)n_+<=((11ell-17)/12)n.
