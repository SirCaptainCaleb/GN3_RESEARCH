# Two consecutive charged rank levels suffice for the 11/12 leading coefficient

## Statement

Suppose that for every vertex v and every q, at most three potential-charged ascending terminal edges at v have ranks in {q,q+1}. Then the certified charged-rank window implies c_+(v)<=floor(3phi(v)/4) in three residue classes and <=floor(3phi(v)/4)+1 in the fourth; using the current odd-central-window bound gives the exact floor bound in all residues. The +1 fallback already implies A<=3/4 sum phi+n and hence m<=11/12 sum phi<=11/12(ell-1)n for P_ell-free systems. This two-rank block statement is distinct from full four-edge spacing: the pattern q,(q+1),(q+1),(q+1) satisfies the spacing inequality at equality but is forbidden here.

## Body

Fix a vertex v with p=phi(v), and let n_q(v) be the number of potential-charged ascending nonspecial edges e={x,v,u} such that v is terminal, phi(u)>=p, and phi(e)=q.

By the certified terminal-potential/rank lower bound a7b7670e955a, every such edge has
  L:=ceil((p+2)/2) <= q <= p.                         (1)

Assume the two-rank block property
  n_q(v)+n_{q+1}(v) <= 3                              (2)
for every q in [L,p-1].

Pair the admissible rank levels consecutively.

If p=4r, then L=2r+1 and there are exactly 2r admissible levels. Pairing them into r blocks and using (2) gives
  c_+(v)<=3r=3p/4.

If p=4r+1, then L=2r+2 and again there are exactly 2r levels, so
  c_+(v)<=3r=floor(3p/4).

If p=4r+2, then L=2r+2 and there are 2r+1 levels. The certified central-window bound 6959dc2c0376 at Q=L gives
  n_L(v)<=C_L(v)<=4L-2p-3=1.
Pair the remaining 2r levels to obtain
  c_+(v)<=1+3r=floor(3p/4).

If p=4r+3, then L=2r+3 and there are 2r+1 levels. Without any endpoint sharpening, leave the bottom level unpaired. The central-window bound gives n_L<=3, and pairing the remaining 2r levels gives
  c_+(v)<=3r+3 <= 3p/4+3/4,
hence c_+(v)<=floor(3p/4)+1.

If in addition the odd-central-window bound a570b0ad0001 is used at p=2L-3, then n_L(v)<=2, giving
  c_+(v)<=2+3r=floor(3p/4)
also in this residue.

Thus (2) plus certified rank-window structure gives the exact three-quarters local bound in three residues and within one unit in the fourth; with the current odd-central-window lemma it gives the exact bound in all residues.

For the global consequence, assign every ascending edge to the lower-potential member of its terminal pair (ties arbitrarily). Every edge assigned to v is counted by c_+(v). Hence even the certified-fallback estimate
  c_+(v)<=3phi(v)/4+1
implies
  A<= (3/4)sum_v phi(v)+n.
Combining with
  3m-A<=2sum_v phi(v)-n
yields
  3m <= (11/4)sum_v phi(v),
so
  m <= (11/12)sum_v phi(v)
    <= (11/12)(ell-1)n
for P_ell-free H.
Therefore the two-rank block lemma alone, even without the final residue correction, already proves leading coefficient 11/12.

Correction to the original comparison with a4ddc7455f1c: the two-rank block property is NOT a consequence of the charged four-edge spacing conjecture. The rank pattern (q,q+1,q+1,q+1) satisfies
  2q_2 = q_1+q_4+1
at equality, so full spacing allows this four-edge pattern while the two-rank block forbids it. The two-rank block is therefore a distinct local statement. Four of the five two-rank patterns violate spacing, but q(q+1)^3 is the genuinely new equality pattern and is the critical case for the 11/12 route.
