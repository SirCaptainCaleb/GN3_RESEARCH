# Minimum degree gives an endpoint-potential floor and a stronger ascending-edge rank floor

## Statement

Let H be a finite linear 3-graph of minimum degree delta. Every vertex v satisfies
  phi(v)>=ceil((delta+1)/2).
Consequently every ascending nonspecial edge e with unique entrance x satisfies
  phi(e)>=ceil((delta+3)/2).

## Body

Fix a vertex v and choose a longest linear path P=(e_1,...,e_t) whose last vertex is v, so t=phi(v). Let z be a last vertex of e_1 at the opposite end. Every edge f distinct from e_1 through z must meet V(P) outside e_1, or else f,e_1,...,e_t would be a longer path still ending at v. By linearity, distinct such edges use distinct blocker vertices in V(P)\e_1. Since a t-edge linear 3-uniform path has 2t+1 vertices, |V(P)\e_1|=2t-2. Hence
  d_H(z)-1 <= 2t-2.
If H has minimum degree delta, then delta<=d_H(z), so
  phi(v)=t >= ceil((delta+1)/2).

Now let e be an ascending nonspecial edge with unique entrance x. By the definition of ascending,
  phi(x)=phi(e)-1.
Applying the endpoint bound to x gives
  phi(e) >= ceil((delta+1)/2)+1
         = ceil((delta+3)/2).
Thus the endpoint-specific minimum-degree obstruction immediately yields the sharper rank floor for ascending nonspecial edges.
