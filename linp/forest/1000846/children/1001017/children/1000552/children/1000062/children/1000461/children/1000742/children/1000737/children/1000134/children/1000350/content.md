# A Type-A branching layer is either upper-half or exposes an exceptional entrance

## Statement

Let v be Type A with p=phi(v)>=5. Suppose for some rank r with 3<=r<=p-1 there are at least three nonspecial rank-r edges terminal at v.

If
  p>=2r-3,
then at least one of those rank-r edges has a non-Type-A unique entrance.

Equivalently, if all entrances of a three-edge rank-r terminal subfamily are Type A, then
  p<=2r-4,
so
  r>=ceil((p+4)/2).

## Body

Take three distinct rank-r nonspecial terminal edges e_i through v, with unique entrances x_i.

Suppose all x_i are Type A. By a57057ab0001, every nonspecial edge sourced at a Type-A vertex is ascending. Therefore each e_i is ascending, and because phi(e_i)=r its entrance has
  phi(x_i)=r-1.

Now apply a570b0ad0001 with q=r. Its odd-central-window conclusion says that whenever
  phi(v)=p>=2r-3,
at most two ascending nonspecial edges terminal at v can have rank at most r.

But e_1,e_2,e_3 are three such edges of rank exactly r, a contradiction.

Hence under p>=2r-3 at least one entrance must be non-Type-A.

The contrapositive is
  p<2r-3,
i.e.
  p<=2r-4
in integers, which is equivalent to
  r>=ceil((p+4)/2).