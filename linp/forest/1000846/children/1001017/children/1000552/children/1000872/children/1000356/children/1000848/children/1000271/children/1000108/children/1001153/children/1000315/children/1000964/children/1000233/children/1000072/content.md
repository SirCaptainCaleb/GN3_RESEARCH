# The rising four-slot gadget orders the two far terminals on its fully occupied side

## Statement

In the rising low-terminal four-slot gadget 33522a8389e9, suppose the two left slots
  L=r_{q-2}∩r_{q-1},
  A=private(r_{q-1})
are both occupied as entrances of high edges
  h_L={L,v,z_L}, h_A={A,v,z_A}.
Let k_L,k_A be the first right-half path-edge indices containing z_L,z_A. Then
  k_L<=k_A.
Moreover z_L does not lie on r_q, so k_L>=q+1.

Dually, if both right slots
  B=private(r_q),
  R'=r_q∩r_{q+1}
are occupied, and i_B,i_R are the last left-half occurrence indices of their opposite terminals, then
  i_R>=i_B,
with the terminal of the joint-side entrance R' strictly left of r_{q-1}.

## Body

Assume L,A are occupied. By 33522a8389e9, z_L,z_A lie on the right half.

First z_L cannot lie on r_q. If it did, then
  r_1,...,r_{q-2},h_L,r_q
would be a q-edge linear path. The prefix meets h_L at L; h_L meets r_q at z_L; the omitted edge r_{q-1} separates the inherited path pieces; and h_L is a hyperedge with only the displayed two R-contacts. The final edge r_q has x=r_{q-1}∩r_q as a last vertex. Thus phi(x)>=q, contradicting phi(x)=q-1. Hence k_L>=q+1.

Suppose for contradiction that k_L>k_A. Consider
  r_1,...,r_{q-2}, h_L,h_A,
  r_{k_A},r_{k_A-1},...,r_q.

The prefix meets h_L at L. The two high edges meet exactly at v. The edge h_A meets the reversed suffix at z_A, using its first right-half occurrence, so any possible second path-edge occurrence is r_{k_A+1}, which is omitted. The entrance A lies on omitted r_{q-1}. Since k_L>k_A, the other contact z_L of h_L is absent from the retained suffix. All remaining intersections are inherited consecutive intersections of R. Hence the sequence is linear.

Its length is
  (q-2)+2+(k_A-q+1)=k_A+1.
Since k_A>=q, this is at least q+1. Its final edge is r_q, and x is a last vertex because r_{q-1} is omitted. Thus phi(x)>=q+1, contradicting phi(x)=q-1. Therefore k_L<=k_A.

The right-base statement follows by reversing R. Under reversal the joint-side entrance is R' and the private-side entrance is B, giving i_R>=i_B; the analogue of the first splice shows the joint-side far terminal cannot lie on r_{q-1}.
