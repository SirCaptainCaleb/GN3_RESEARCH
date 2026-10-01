# Consecutive-rank source-clean common-terminal edges cross each other

## Statement

Let
  e={x,v,u},  f={y,v,z}
be distinct ascending nonspecial edges sharing the terminal vertex v. Assume
  phi(e)=q,
  phi(f) in {q,q+1}.
Let R_e,R_f be chosen maximum paths with last vertices x,y respectively, of lengths phi(e)-1 and phi(f)-1, such that R_e avoids v,u and R_f avoids v,z.

Then
  f intersects V(R_e)
and
  e intersects V(R_f).

Thus each source-clean edge meets the chosen maximum source path of the other; no assignment or terminal contact-multiplicity hypothesis is required.

## Body

Because e is ascending, R_e has q-1 edges and R_e,e is a q-edge linear path ending in e through its unique entrance x.

Suppose f were disjoint from R_e. Since e and f meet exactly at v and R_e avoids the two terminals v,u of e, the sequence
  R_e,e,f
would be a linear path of length q+1 ending in f through the terminal v.

If phi(f)=q, this exceeds the edge rank of f. If phi(f)=q+1, it is a longest path ending in the nonspecial edge f but enters f through the terminal v rather than its unique entrance y. Both are impossible. Hence f meets R_e.

For the reverse direction, let s=phi(f), so s is q or q+1. If e were disjoint from R_f, then
  R_f,f,e
would be a linear path of length s+1 ending in e. Since s+1>q=phi(e), this is impossible. Therefore e meets R_f as well.
