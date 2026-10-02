# Type-A saturation forces rank-preserving propagation to a second terminal edge

## Statement

Continue in the saturated Type-A fan of 4c0a0105c825. Put q=p-1 and
  P=(g1,...,g_q=h),
and write
  C=g_{q-2}\g_{q-3}.

Let
  alpha=g_{q-3}∩g_{q-2},
and let beta be the private vertex of g_{q-1}, i.e. the vertex of g_{q-1} outside g_{q-2}∪h.
Let f_alpha,f_beta be the unique terminal edges whose W\C partition contacts are alpha,beta.

Then:
1. f_alpha has no additional C-contact; its only P-contact outside v is the joint alpha.
2. f_beta has no additional C-contact either.
3. Consequently phi(f_beta)=q and beta is the unique entrance of f_beta.

Thus every Type-A saturated fan around a rank-q=p-1 terminal edge h canonically produces a second rank-q nonspecial terminal edge through v, whose unique entrance is the private vertex beta of the penultimate edge of the chosen h-witness path.

## Body

By 4c0a0105c825, every terminal edge f!=h has exactly one partition contact in W\C and at most one additional contact in C.

For f_alpha, alpha lies in g_{q-2}, and every vertex of C also lies in g_{q-2}. Hence any additional C-contact would make f_alpha and g_{q-2} share two vertices, violating linearity. So f_alpha is a pure joint blocker at alpha.

Now consider f_beta.

If f_beta has no C-contact, replacing h by f_beta gives
  (g1,...,g_{q-1},f_beta),
a q-edge linear path. Hence phi(f_beta)=q, and because the predecessor meets f_beta at beta, nonspeciality makes beta its unique entrance.

It remains to rule out an additional C-contact.

Write
  b=g_{q-2}∩g_{q-1}
and let gamma be the private vertex of g_{q-2}; thus C={b,gamma}. Since f_beta already meets g_{q-1} at beta, it cannot also contain b, or it would share two vertices with g_{q-1}. Therefore any extra C-contact must be gamma, and then
  f_beta={v,beta,gamma}.

But now omit g_{q-1} and consider
  g1,...,g_{q-2},f_beta,h.
This is a q-edge linear path:
- f_beta meets the retained precursor only at gamma in g_{q-2};
- h meets f_beta at v;
- h is disjoint from g1,...,g_{q-2};
- the other f_beta contact beta lay in the omitted edge g_{q-1}.

Thus the nonspecial rank-q edge h has a longest q-edge path entering it through v. Since v is a terminal of h, this contradicts its unique entrance.

Therefore f_beta cannot have a C-contact. It is necessarily a second rank-q nonspecial terminal edge with unique entrance beta.