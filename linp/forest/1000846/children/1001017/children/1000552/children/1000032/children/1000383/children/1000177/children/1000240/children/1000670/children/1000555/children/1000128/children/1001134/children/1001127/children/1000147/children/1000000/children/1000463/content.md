# An internal edge above the endpoint-path rank propagates forward with loss at most one or creates a cycle

## Statement

Let
  A=(g_1,...,g_L)
be a maximum endpoint path with last vertex a, so phi(a)=L. Let h=g_j be an internal edge, j<L, with edge rank
  r=phi(h)>L.

Then at least one of the following holds:

(C) the union of A with a suitable maximum endpoint path contains a linear cycle;

(P) there is an index t>j such that
  phi(g_t)>=r-1.

Consequently, if no linear cycle occurs in the successive applications of this alternative starting from h, then
  j <= 2L+1-r.

Equivalently, every internal path edge with
  j>2L+1-phi(g_j)
forces a linear cycle through the propagation process.

## Body

Put z=g_j intersect g_{j+1}.

If z is terminal at h, then 0000bd602854 forces every maximum phi(h)-edge path ending in h with last vertex z to meet the suffix g_{j+1},...,g_L at another vertex. By 41100a9882dd, since h itself is not an edge of this suffix, the resulting repeated intersection contains a linear cycle. Thus (C) holds.

Assume therefore that z is not terminal at h. Then h is nonspecial and z is its unique entrance. A longest path ending in h enters through z; deleting h leaves an (r-1)-edge path ending at z. Hence
  phi(z)>=r-1.

Choose a maximum endpoint path P_z ending at z. If P_z met the suffix g_{j+1},...,g_L only at z, concatenating P_z with that suffix would give a path ending at a of length
  phi(z)+(L-j)
  >= r-1+L-j
  > L,
because r>L and j<L. This contradicts phi(a)=L. Thus P_z has another common vertex with the suffix.

Apply 41100a9882dd to P_z and the suffix. Either their union contains a linear cycle, giving (C), or the last edge k of P_z is an edge of the suffix. In the latter case
  phi(k)>=|P_z|=phi(z)>=r-1.
Writing k=g_t gives t>j and (P).

For the iterative statement, suppose no cycle is produced. Start with j_0=j and r_0=r. Whenever g_{j_s} is internal and r_s=phi(g_{j_s})>L, apply the preceding alternative and choose
  j_{s+1}>j_s,
  r_{s+1}=phi(g_{j_{s+1}})>=r_s-1.
After s propagation steps,
  r_s>=r-s
and
  s<=L-j.

The process can stop without a cycle only in one of two ways. If it stops at an internal edge because r_s<=L, then r-s<=L, so s>=r-L. If it reaches the last edge g_L, then the incident-edge bound at the last vertex a gives
  phi(g_L)<=phi(a)+1=L+1,
so r-s<=L+1 and s>=r-L-1.
In either case
  L-j >= s >= r-L-1,
and therefore
  j<=2L+1-r.
