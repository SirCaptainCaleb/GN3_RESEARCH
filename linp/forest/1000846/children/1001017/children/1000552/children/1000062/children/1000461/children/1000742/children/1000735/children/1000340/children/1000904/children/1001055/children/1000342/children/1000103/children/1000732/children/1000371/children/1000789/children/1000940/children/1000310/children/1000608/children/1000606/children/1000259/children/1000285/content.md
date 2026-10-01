# A saturated terminal star nearly realizes the period-four singleton extremizer on the opposite source rail

## Statement

Let e={x,u,v} be an ascending nonspecial edge of rank q>=4 and let R be a canonical (q-1)-edge source rail of e. Fix one terminal w in {u,v}, and assume q is the maximum rank of an ascending nonspecial edge terminal at w.

Let t(w) be the number of ascending nonspecial edges terminal at w and put delta_w=gamma(q)-t(w)>=0, where gamma(q)=floor((11q-5)/8).

Relative to R, classify the t(w)-1 ascending terminal competitors f!=e as single-contact or double-contact edges, with counts S_w,B_w, and let U_w count vertices of W=V(R) minus {x} unused by all these competitors. Put alpha(q)=ceil((3q-8)/4) and kappa_q=alpha(q)-2gamma(q)+2q. Then kappa_q belongs to {0,1}, and
alpha(q)-kappa_q-2delta_w <= S_w <= alpha(q),
0 <= U_w <= kappa_q+2delta_w <= 2delta_w+1.

Thus if delta_w=o(q), the terminal star has S_w=(3/4+o(1))q single blockers on R and leaves only o(q) rail vertices unused. If e is maximum-rank at both terminals u,v and both deficits are o(q), the same source rail simultaneously supports two near-extremal period-four singleton patterns, one from each terminal star.

## Body

Take T_w in 38e2ce9f9772 to be all ascending terminal edges through w other than e. The maximum-rank assumption ensures every such edge has rank at most q, so the source-rail coupling lemma applies. Its exact identity gives 2t(w)=2q+S_w-U_w, because d_w^*=t(w). Hence S_w-U_w=2gamma(q)-2q-2delta_w. (1)

The exact fixed-entrance transfer theorem eb40ddcc33ca, applied to the q-edge path R,e ending at w, bounds the number of singleton contacts among all incident edges of rank at most q by alpha(q)=ceil((3q-8)/4). Our ascending-terminal competitors form a subfamily, so S_w<=alpha(q). (2)

Combining (1) and (2), U_w=S_w-[2gamma(q)-2q-2delta_w]<=alpha(q)-2gamma(q)+2q+2delta_w=kappa_q+2delta_w. Since U_w>=0, equation (1) also gives S_w>=2gamma(q)-2q-2delta_w=alpha(q)-kappa_q-2delta_w.

Finally, substituting gamma(q)=floor((11q-5)/8) and alpha(q)=ceil((3q-8)/4) in the eight residue classes modulo 8 gives kappa_q in {0,1}. This proves the inequalities and the asymptotic conclusion.
