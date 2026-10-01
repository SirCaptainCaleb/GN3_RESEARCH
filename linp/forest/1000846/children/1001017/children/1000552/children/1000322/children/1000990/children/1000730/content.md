# Two two-contact chords through one outside owner give an exact bridge splice

## Statement

Let P=(p_1,...,p_s) be a linear path and o outside P. Suppose f={o,r,r_prime} and g={o,t,t_prime} are distinct edges through o, with four distinct P-contacts. If r is last seen in p_i, t is first seen in p_k, i<k, and all occurrences of r_prime,t_prime lie strictly between i and k, then p_1,...,p_i,f,g,p_k,...,p_s is a linear path of length s+3-(k-i). Thus gap two extends the path and gap three gives a length-preserving rotation.

## Body

Let P=(p_1,...,p_s) be a linear 3-uniform path ending at a prescribed last vertex x. Let o notin V(P), and let
  f={o,r,r'},  g={o,t,t'}
be distinct hyperedges through o such that r,r',t,t' are four distinct vertices of V(P).

Let
  i=max{j:r∈p_j},
  k=min{j:t∈p_j},
and assume i<k. Suppose every path edge containing r' or t' has index strictly between i and k.

Then
  (p_1,...,p_i,f,g,p_k,...,p_s)
is a linear path.

Indeed, f meets the retained prefix only at r: its other path contact r' occurs only in the omitted interval, and o lies outside P. Similarly g meets the retained suffix only at t. The two new edges f,g meet exactly at o by linearity. The retained prefix and suffix were mutually nonintersecting except through omitted path material, and the hypotheses place the unused contacts r',t' entirely inside that omitted material. Thus the only new consecutive intersections are
  p_i∩f={r},  f∩g={o},  g∩p_k={t}.

Its length is
  i+2+(s-k+1)=s+3-(k-i).

Consequently:
- if k-i=2, this gives an (s+1)-edge extension;
- if k-i=3, this gives an s-edge length-preserving rotation;
- more generally the loss is k-i-3.

In particular, if P is a longest witness ending in a fixed nonspecial target and the suffix from p_k onward contains that target, then a gap-two pair is impossible and a gap-three pair gives another longest witness ending in the same target. If the new path changes the target entrance label, nonspeciality is contradicted immediately; otherwise it supplies a canonical rotation state.
