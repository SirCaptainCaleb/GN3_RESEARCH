# Shared edges above the host-path rank are confined to an initial prefix unless a cycle occurs

## Statement

Let
  A=(a_1,...,a_{q-1})
be a maximum endpoint path with last vertex x, where q<p. Let H be a set of T distinct hyperedges belonging to A, each of edge rank at least p.

Then at least one of the following holds:

(1) in the propagation process of 678901b48360 for some h in H, the union of A with a suitable maximum endpoint path contains a linear cycle;

(2) every h in H occurs among
  a_1,...,a_{2q-p-1},
and consequently
  T <= max{0,2q-p-1}.

In particular, if no such cycle occurs and T>0, then
  q >= ceil((p+T+1)/2).

Applied to the type-U common-edge outcome of 20cdd04e92ca, if one of the two higher-rank source paths has edge rank q, then either a cycle is produced or the number T of distinct common hyperedges of edge rank at least p satisfies
  T<=2q-p-1.

## Body

Fix h in H and let h=a_j. Since A has q-1 edges, put L=q-1. By assumption
  r=phi(h)>=p>q-1=L.
Thus 678901b48360 applies.

If its cycle alternative occurs for any h, we are in (1). Otherwise its positional conclusion gives
  j <= 2L+1-r
    <= 2(q-1)+1-p
    = 2q-p-1.

Hence every member of H is one of the first 2q-p-1 edges of A. The members of H are distinct, so
  T<=max{0,2q-p-1}.
Rearranging T<=2q-p-1 gives
  2q>=p+T+1,
and therefore
  q>=ceil((p+T+1)/2).

For the stated application, 20cdd04e92ca supplies T distinct hyperedges common to the two higher-rank source paths, each with edge rank at least p. Apply the preceding argument to either host path separately.
