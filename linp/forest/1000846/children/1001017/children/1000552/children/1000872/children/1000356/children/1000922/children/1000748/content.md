# A three-per-two-ranks bound for 0-1-1 edges alone gives the 11/12 coefficient

## Statement

Assign every 0-1-1 ascending edge to a minimum-potential terminal v. If for every v and q at most three assigned 0-1-1 edges have ranks in {q,q+1}, then U<=3/4 sum_v phi(v). Combined with the certified defect inequality 3m<=2 sum_v phi(v)-n+U, this gives m<=11/12 sum_v phi(v)-n/3 and therefore m<=((11ell-15)/12)n for every P_ell-free linear triple system.

## Body

Fix chosen maximum endpoint paths P_v at every nonisolated vertex and let U be the number of certified 0-1-1 edges from ceef20074f6f. Thus for every such edge
  e={x,y,z}
the entrance x is clean:
  mu_x(e)=0,
while both terminal incidences are single:
  mu_y(e)=mu_z(e)=1.

Assign each 0-1-1 edge to one of its two terminals of minimum endpoint potential, breaking ties arbitrarily. Let
  u(v)
be the number assigned to v. Then
  U=sum_v u(v).

Every edge assigned to v is potential-charged at v, so if p=phi(v) and r=phi(e), its rank lies in the certified charged window
  ceil((p+2)/2) <= r <= p.

For each rank r let u_r(v) be the number of assigned 0-1-1 edges of rank r. Assume the local consecutive-rank block:
  u_q(v)+u_{q+1}(v) <=3                           (1)
for every v and every q.

Pair the admissible rank levels exactly as in 2665d2c81d39/a9d95378e855. The certified bottom-level central-window bounds give
  u(v)<=floor(3p/4)<=3p/4.
Therefore
  U <= (3/4) sum_v phi(v)= (3/4)S.               (2)

By the certified 0-1-1 defect reduction ceef20074f6f,
  3m <= 2S-n+U.
Using (2),
  3m <= (11/4)S-n,
hence
  m <= (11/12)S-n/3.
If H is P_ell-free, S<=(ell-1)n, yielding
  m <= ((11ell-15)/12)n.

Thus the entire interrupted 11/12 route reduces to a single local theorem about 0-1-1 edges: at a lower-potential terminal, no four assigned 0-1-1 edges may have ranks contained in two consecutive levels.

This is strictly weaker than controlling all ascending edges and also weaker than the defect-corrected A-D block: paid clean edges and every edge with a double terminal are completely irrelevant.
