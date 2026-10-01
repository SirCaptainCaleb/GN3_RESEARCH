# The forced middle-private low entrance raises the outer right joint to full terminal potential

## Statement

Let v have p=phi(v)=2q-3 with q>=4, and let
  P=(g_1,...,g_p)
be a maximum path ending physically at v.

Suppose f={B,v,u} is an ascending nonspecial rank-q edge which is non-double on P and whose unique entrance
  B=private(g_{q-1})
lies on P. Then u is absent from P and, putting
  D=g_q∩g_{q+1},
one has
  phi(D)>=p=2q-3.

Consequently D cannot be the entrance of any rank-(q+1) ascending edge. In particular, in the two-rank-q saturation patterns of 35ee7b35de05, the outer right joint D is unavailable as a non-double charged witness of any rank in {q,q+1}.

## Body

Because f is non-double and B is its entrance on P, its opposite terminal u is absent from P.

Consider
  g_1,...,g_{q-1}, f, g_p,g_{p-1},...,g_{q+1}.
The omitted central edge g_q separates the retained prefix and reversed suffix. The edge f meets the prefix only at B in g_{q-1}, meets the final path edge g_p at v, and has no other P-contact because u is absent. Thus the displayed sequence is linear.

Its length is
  (q-1)+1+[p-(q+1)+1]
  =q+[2q-3-q]
  =2q-3
  =p.

Its last edge is g_{q+1}. Since g_q is omitted, the joint
  D=g_q∩g_{q+1}
occurs only in that final edge and may be chosen as the physical last vertex. Hence
  phi(D)>=p.

If D were the unique entrance of a rank-(q+1) ascending edge, then
  phi(D)=q,
contradicting p=2q-3>q for q>=4.

Finally, in either two-low witness pattern of 35ee7b35de05, B is exactly such a rank-q entrance, so the conclusion applies.