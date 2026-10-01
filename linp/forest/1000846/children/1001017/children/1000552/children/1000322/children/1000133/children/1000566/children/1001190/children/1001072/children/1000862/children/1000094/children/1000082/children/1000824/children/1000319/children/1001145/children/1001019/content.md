# Rigid zero-slack half-neighborhoods obey a per-color cut-parity law

## Statement

In the zero-slack no-switch normal form fb4fc1ee4179, let
  S=N_G(y)=N_G(z),
so |S|=k, and let R=X\S, also of size k. For every threshold color d∈D, let M_d be its perfect matching on X and let c_d be the number of M_d-edges crossing the cut (S,R). Then
  c_d ≡ k (mod 2)
and c_d>=2.

Consequently:
- if k is odd, c_d>=3 for every color d;
- if k is even, c_d is even and at least 2.

Moreover, the two guaranteed crossing edges are exactly the d-matching edges incident with y and z. Thus for odd k every color has at least one further S-R connector disjoint from y,z.

## Body

A perfect matching M_d on X has k edges and saturates the k vertices of S. If a_d edges of M_d lie entirely inside S and c_d edges cross from S to R, then
  2a_d+c_d=k.
Hence c_d≡k mod2.

By fb4fc1ee4179, y,z belong to R and both have their d-matching partners in S, for every d. Since M_d is a matching, these are two distinct crossing edges, so c_d>=2.

The parity consequences are immediate. When k is odd, c_d cannot equal 2 and hence is at least 3. Any crossing edge beyond the y- and z-edges is disjoint from y,z because M_d is a matching.