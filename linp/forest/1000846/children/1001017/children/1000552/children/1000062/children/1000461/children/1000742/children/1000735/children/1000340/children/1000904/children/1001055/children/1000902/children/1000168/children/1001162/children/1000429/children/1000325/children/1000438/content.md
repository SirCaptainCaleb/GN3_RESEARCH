# Every single-blocker rotation output pays by rank rise, specialness, flat orientation, or a high-potential joint

## Statement

Let P=(g_1,...,g_p) be a maximum p-edge path ending at v. Suppose a single blocker f through v has its unique precursor contact in an interior cell C_i={b_i,z_i}, and form the standard rotation
  Q=(g_1,...,g_i,f,g_p,g_{p-1},...,g_{i+2}),
with i<=p-3.
Put h=g_{i+2} and let
  z=g_{i+2} intersect g_{i+3}
be the forward joint of h on the original host path.

Then phi(h)>=p. Moreover exactly one of the following holds:
(1) phi(h)>p;
(2) phi(h)=p and h is special;
(3) phi(h)=p, h is nonspecial ascending, z is its unique entrance, and phi(z)=p-1;
(4) phi(h)=p, h is nonspecial nonascending, z is its unique entrance, and phi(z)>=p.

For distinct occupied cells the output edges h are distinct and their forward joints z are distinct.

Thus every occupied switching cell makes monotone progress unless it lands in the flat ascending rank-p branch (3).

## Body

The displayed rotation Q has p edges and ends in h=g_{i+2}. Hence, by definition of edge rank,
  phi(h)>=p.

If phi(h)>p we are in (1). Assume henceforth phi(h)=p. If h is special, (2) holds. Suppose h is nonspecial.

In Q the edge immediately preceding h is g_{i+3}, so Q enters h through
  z=h intersect g_{i+3}.
Since Q is a p-edge path ending in h and phi(h)=p, Q is a longest h-ending path. By the unique-longest-entrance characterization 7235fdc47d1a, every longest path ending in a nonspecial edge uses its unique entrance. Therefore z is the unique entrance of h.

Deleting h from Q leaves a (p-1)-edge path ending at z. Hence
  phi(z)>=p-1.
If phi(z)=p-1, then phi(h)=phi(z)+1 and h is ascending, giving (3).
If phi(z)>=p, then h is not ascending through its unique entrance and we are in (4). These cases are exhaustive.

Finally distinct cells C_i have distinct indices i, hence distinct output edges g_{i+2}. Their forward joints g_{i+2} intersect g_{i+3} are distinct joints of the original linear path P.
