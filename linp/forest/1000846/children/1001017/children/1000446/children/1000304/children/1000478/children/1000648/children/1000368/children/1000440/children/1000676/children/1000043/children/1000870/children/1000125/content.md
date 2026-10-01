# High-terminal five-paths in the 4445 triangle satisfy a three-way late-contact alternative

## Statement

In the 4445 triangle setting, write
  g_3={a,b,c},
  f_b={b,v,u_b},
with phi(b)=phi(c)=3.

For every five-edge path
  R=(r_1,...,r_5)
ending physically at u_b, at least one of the following holds:
(A) v∈r_4;
(B) b=r_3∩r_4;
(C) a∈r_4∪r_5.

Moreover b,c are absent from r_5, and any occurrence of b or c in r_4 is necessarily the joint r_3∩r_4.

Symmetrically, every five-edge path ending at u_c satisfies
  v∈r_4, or c=r_3∩r_4, or a∈r_4∪r_5.

## Body

Let R be a five-edge path ending at u_b.

First use the position-sensitive endpoint-potential bound 8b1790d79d74. Since phi(b)=phi(c)=3:

- neither b nor c can lie privately in r_5, since a private vertex of the fifth edge has endpoint potential at least 5;
- neither can be the joint r_4∩r_5, since such a joint has endpoint potential at least 4.

Hence b,c are absent from r_5.

Likewise, if b or c lies in r_4, it cannot be private to r_4 (which would give potential at least 4) and cannot be the joint r_4∩r_5. Therefore its only possible occurrence in r_4 is as the joint r_3∩r_4.

Now apply c2e8b77d6c. At least one of:
(i) r_4 meets f_b={b,v,u_b};
(ii) r_4 meets g_3={a,b,c};
(iii) r_5 meets g_3.

Because R ends physically at u_b, u_b is private to r_5 and cannot lie in r_4. Thus in case (i), r_4 contains b or v. If it contains v we are in (A); if it contains b, the positional classification above gives (B).

In case (ii), r_4 contains a,b,or c. If it contains a we are in (C). If it contains b then (B). If it contains c, then c=r_3∩r_4. But r_3∩r_4 is a single vertex, so c cannot coexist there with the terminal-tail requirement unless the f_b blocker is v in r_3; in any event c at this joint is a symmetric low-joint alternative. [For the stated three-way form, this residual c-joint case needs elimination or absorption; keep statement provisional until that final check.]

In case (iii), b,c are absent from r_5, so necessarily a∈r_5, giving (C).
