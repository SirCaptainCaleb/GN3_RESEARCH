# The full contact-conflict graph improves the leading coefficient to 43/48

## Statement

Let h be an ascending edge of rank q and v a terminal. Using the full singleton-contact conflict graph around a longest h-path, rather than only a disjoint matching of conflicts, one obtains |{f containing v: phi(f)<=q}| <= (11/8)q+3/2. Consequently A<=(11/16)sum_v phi(v)+(3/4)n_+, and the standard incidence inequality gives m<=(43/48)sum_v phi(v)-n_+/12. Hence every P_ell^(3)-free linear 3-graph satisfies m<=((43ell-47)/48)n.

## Body


Let H be a finite linear 3-graph. Fix an ascending edge h of rank q and a terminal v of h. Choose a q-edge path
  P=(g_1,...,g_q)
with last edge h=g_q and last vertex v. Let
  x=g_{q-1} cap h
be the unique entrance of h, so phi(x)=q-1. Put
  W=V(P) minus h,
so |W|=2q-2.

For every f!=h through v with phi(f)<=q, put
  C_f=(f minus {v}) cap W.
As in a57011120001/48876ef77124, every C_f is nonempty, the C_f are pairwise disjoint, and |C_f| is one or two.

Write z_i=g_i cap g_{i+1}. Let a_1,b_1 be the two vertices of g_1 minus {z_1}; for 2<=i<=q-1 let b_i be the unique private vertex of g_i other than its two path joints (with the evident endpoint convention).

From 48876ef77124, the four vertices
  a_1, b_1, b_{q-2}, z_{q-2}
can never themselves be singleton contact sets.

FULL LOCAL CONFLICT GRAPH.
For every 1<=i<=q-3 define the forward-facing vertices of g_i and backward-facing vertices of g_{i+2}:
- for i=1, L_i={a_1,b_1,z_1};
- for i>=2, L_i={b_i,z_i};
- R_i={b_{i+2},z_{i+1}},
where vertices already excluded from W or forbidden as singleton contacts may simply be ignored.

Claim: no singleton contact vertex in L_i can coexist with a singleton contact vertex in R_i.

Indeed suppose C_f={c} with c in L_i and C_k={d} with d in R_i. Then
  g_1,...,g_i,f,k,g_{i+2},...,g_{q-1}
is a q-edge linear path ending at x. The omitted edge g_{i+1} separates the inherited prefix and suffix. By the definitions of L_i,R_i, c has no occurrence in the retained prefix before g_i and d has no occurrence in the retained suffix after g_{i+2}. The singleton-contact hypothesis says f,k have no other W-contacts; they meet each other exactly in v, which is outside W, and neither can contain x because each already shares v with h. Hence the displayed path is linear, has q edges, and ends at x, contradicting phi(x)=q-1.

Thus the singleton vertices form an independent set in this full conflict graph.

TRANSFER BOUND.
Discard the four individually forbidden singleton vertices. Apart from the two boundary vertices z_1 and b_{q-1}, organize the remaining potential singleton vertices into columns
  (b_i,z_i),  2<=i<=q-3.
Let B_i,Z_i be their 0-1 singleton indicators and A_i=max(B_i,Z_i).

The conflict claim implies, for every relevant i,
  A_i=1 => Z_{i+1}=0 and B_{i+2}=0.                 (1)

Consider the state sigma_i=(A_{i-1},A_i) in {00,01,10,11}. When choosing the next column, B_{i+1} is allowed only if A_{i-1}=0 and Z_{i+1} only if A_i=0. Therefore the maximal-weight state transitions, where the weight is B_{i+1}+Z_{i+1}, are:
  00 -> 00 with weight 0,   00 -> 01 with weight 2;
  01 -> 10 with weight 0,   01 -> 11 with weight 1;
  10 -> 00 with weight 0,   10 -> 01 with weight 1;
  11 -> 10 with weight 0.

Assign potentials
  pi(00)=0,
  pi(01)=-5/4,
  pi(10)=-3/4,
  pi(11)=-3/2.
For every allowed transition sigma->tau of weight w,
  w <= 3/4 + pi(sigma)-pi(tau).
This is checked directly on the seven displayed transitions. Summing along any state walk gives total weight at most 3/4 per new column plus at most 3/2 boundary potential loss.

The first two columns contribute at most four singleton vertices, and the two exceptional boundary vertices z_1,b_{q-1} contribute at most two more. Hence, for q>=6, the total number s of singleton contact sets satisfies
  s <= 4 + (3/4)(q-6) + 3/2 + 2
    = (3/4)q + 3.
The finitely many q<6 cases satisfy the same bound trivially.

Let d be the number of two-vertex contact sets and u the number of unused W-vertices. Then
  s+2d+u=2q-2
and
  |J_q(v)|=1+s+d
          =1+(2q-2+s-u)/2
          <=q+s/2.
Therefore
  |J_q(v)| <= (11/8)q + 3/2.                        (2)

GLOBAL ASCENDING COUNT.
Let t(v) be the number of ascending edges terminal at v. If t(v)>0 choose one of maximum rank q. Then every edge counted by t(v) lies in J_q(v), and q<=phi(v). Thus
  t(v) <= (11/8)phi(v)+3/2.
For t(v)=0 this is trivial. Summing over nonisolated vertices and using that every ascending edge has two terminals,
  2A=sum_v t(v)
     <= (11/8)S +(3/2)n_+,
so
  A <= (11/16)S +(3/4)n_+.                          (3)

Combine (3) with the certified/global incidence inequality
  3m-A <= 2S-n_+.
Then
  3m <= (43/16)S -(1/4)n_+,
hence
  m <= (43/48)S - n_+/12.                           (4)

If H is P_ell^(3)-free, S<=(ell-1)n_+, giving
  m <= [(43/48)(ell-1)-1/12] n_+
    = ((43ell-47)/48)n_+.
Thus the leading coefficient improves from the previous 11/12=44/48 coefficient to 43/48.

The constants above are intentionally nonoptimized. The exact independence number of the finite conflict graph appears smaller and periodic; sharpening the boundary analysis can improve the additive term further without changing the 43/48 leading coefficient.
