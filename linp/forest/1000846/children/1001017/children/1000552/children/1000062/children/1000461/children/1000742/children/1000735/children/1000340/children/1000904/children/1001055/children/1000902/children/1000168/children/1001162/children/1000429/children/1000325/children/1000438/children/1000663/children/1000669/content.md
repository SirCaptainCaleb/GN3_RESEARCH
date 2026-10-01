# Cell dispersion forces a source-mass / switcher-triangle tradeoff

## Statement

Let P=(g_1,...,g_p) be a maximum p-edge path ending at v with last vertex v. Let F be a family of distinct ascending nonspecial edges terminal at v, each having exactly one off-v contact with P, and suppose all these contacts lie in the interior cells
  C_i={b_i,z_i},  1<=i<=p-3,
where b_i is private to g_i and z_i=g_i∩g_{i+1}.
Let s=|F|, let D be the number of cells containing two F-contacts, and hence let C=s-D be the number of occupied cells. For f∈F write x_f for its unique entrance.

Then
  sum_{f∈F} phi(x_f)
  >= (p/2)s + floor(C^2/4)
  =  (p/2)s + floor((s-D)^2/4).

Consequently, for any theta∈[0,1], either D>=theta s, or
  sum_{f∈F} phi(x_f)
  >= (p/2)s + ((1-theta)^2/4)s^2 - O(1).

In particular, if F is the interior part of a low-defect switching family at a p-center, so s=(5/8-o(1))p, then either D>=theta(5/8-o(1))p or
  sum_{f∈F}phi(x_f)
  >= [5/16 + 25(1-theta)^2/256 - o(1)]p^2.

## Body

For a singleton ascending terminal edge f of rank r with unique P-contact c, the central-window localization 49080cbf1371 gives:
- the first occurrence index a(c) satisfies a(c)<=r-1 (and in the terminal-only case even a(c)<=r-2);
- the last occurrence index b(c) satisfies b(c)>=p-r+2.

Hence if c=b_i is private to g_i, then
  r>=max{i+1,p-i+2},
so
  phi(x_f)=r-1>=max{i,p-i+1}>=max{i,p-i}.             (1)

If c=z_i=g_i∩g_{i+1}, then a=i and b=i+1, so
  r>=max{i+1,p-i+1},
and therefore
  phi(x_f)>=max{i,p-i}.                               (2)

Thus every switcher whose contact lies in cell C_i has source potential at least
  w_i=max{i,p-i}.                                     (3)

Choose one representative edge from each of the C occupied cells. The cell indices are distinct. Among the integers 1,...,p-3, the C smallest values of w_i=max{i,p-i} occur as close as possible to p/2. Their sum satisfies the exact elementary bound
  sum_{occupied representatives} phi(x_f)
  >= (p/2)C + floor(C^2/4).                           (4)
Indeed, after subtracting p/2, the multiset of deviations is 0,1,1,2,2,... when p is even, and 1/2,1/2,3/2,3/2,... when p is odd, up to boundary truncation; the sum of the C smallest deviations is at least floor(C^2/4).

There remain exactly D nonrepresentative edges, one extra edge in each doubly occupied cell. Every singleton ascending terminal edge on a maximum p-path satisfies rank at least ceil((p+2)/2), again by 49080cbf1371, and hence
  phi(x_f)=r-1>=ceil(p/2)>=p/2.                       (5)

Adding (4) and the D copies of (5), and using C+D=s, gives
  sum_{f∈F}phi(x_f)
   >=(p/2)C+floor(C^2/4)+(p/2)D
   =(p/2)s+floor((s-D)^2/4).

If D<theta s, then s-D>(1-theta)s, and the second assertion follows (the floor contributes only O(1)). For a low-defect switching family, b032348c1a8a and the boundary loss give s=(5/8-o(1))p; substitution yields the final coefficient.
