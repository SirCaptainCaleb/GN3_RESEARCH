# High 0-1-1 terminal paths have a four-level reciprocal central normal form

## Statement

Let h={y,v,D} be a 0-1-1 ascending nonspecial edge of rank q+1 with q>=5, unique entrance y, and terminals v,D. Suppose
  s=phi(D)>=2q-3.
Then s<=2q and, on the globally chosen maximum D-ending path
  R=(r_1,...,r_s),
the unique h-contact has the following central localization.

If the contact is the terminal v:
- s=2q: impossible;
- s=2q-1: v is necessarily the joint r_{q-1}∩r_q;
- s=2q-2: v is private in r_{q-1}, or a joint r_i∩r_{i+1} with i in {q-2,q-1};
- s=2q-3: v is private in r_i with i in {q-2,q-1}, or a joint with i in {q-3,q-2,q-1}.

If the contact is the entrance y:
- s=2q: y is necessarily the central joint r_q∩r_{q+1};
- s=2q-1: y is private in r_q, or a joint with i in {q-1,q};
- s=2q-2: y is private in r_i with i in {q-1,q}, or a joint with i in {q-2,q-1,q};
- s=2q-3: y is private in r_i with i in {q-2,q-1,q}, or a joint with i in {q-3,q-2,q-1,q}.

In particular every reciprocal D-path state is confined to O(1) central slots, and the maximal-potential case s=2q forces the entrance y at the exact central joint.

## Body

The terminal-potential bound a7b7670e955a applied to the rank-(q+1) edge gives
  s=phi(D)<=2(q+1)-2=2q.
Together with s>=2q-3, only the four displayed values occur.

Because q>=5, s>=2q-3>q+1=phi(h), so h cannot itself be the last edge of the s-edge D-ending path R. Since mu_D(h)=1, exactly one of y,v occurs on R.

Suppose first that the sole contact is terminal v, so y is absent. If v is private in r_i, terminal-tail localization for a rank-(q+1) edge gives
  i>=s-(q+1)+2=s-q+1.
But
  r_1,...,r_i,h
is a path ending in h through wrong terminal v. Since h has rank q+1 and unique longest entrance y, its length i+1 is at most q. Thus i<=q-1.
Hence
  s-q+1<=i<=q-1.

If v=r_i∩r_{i+1}, the tail lower bound is
  i>=s-(q+1)+1=s-q,
while the same wrong-entrance prefix r_1,...,r_i,h gives i+1<=q, so i<=q-1.
Hence
  s-q<=i<=q-1.
Substituting s=2q,2q-1,2q-2,2q-3 gives exactly the terminal-contact list.

Now suppose the sole contact is entrance y, so v is absent. Since phi(y)=q, the position-sensitive endpoint-potential bound on the s-edge path R gives:
- if y is private in r_i,
    max{i,s-i+1}<=q,
  equivalently s-q+1<=i<=q;
- if y=r_i∩r_{i+1},
    max{i,s-i}<=q,
  equivalently s-q<=i<=q.
These agree with the terminal-tail lower bounds and yield the displayed entrance-contact lists after substituting the four possible values of s.