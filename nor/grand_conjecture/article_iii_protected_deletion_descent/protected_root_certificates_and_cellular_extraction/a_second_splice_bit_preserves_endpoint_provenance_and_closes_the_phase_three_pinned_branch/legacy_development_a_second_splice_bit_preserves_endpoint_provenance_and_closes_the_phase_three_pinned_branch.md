# A second splice bit preserves endpoint provenance and closes the phase-three pinned branch — preserved pre-item development

## A second splice bit retains endpoint provenance at a pinned junction

Work in a minimum counterexample in the coboundary-flat alternating ternary sector. Fix the common global status convention. Let a good deletion witness omitting x be
O_x=(a,b,c,d,e,...), with word 0^p1^q, p>=2, q>=1.
Its fully-curved endpoint packet gives
alpha(x,a,b)=1, alpha(a,b,c)=0,
alpha(x,a,c)=0, alpha(x,b,c)=1.
Assume the first pivot stops:
lambda=alpha(a,c,d)=1.
Since alpha(a,b,c)=alpha(b,c,d)=0, tetrahedral parity gives alpha(a,b,d)=1.

There are two explicit full-support/deletion surgeries.

### 1. The first surgery closes when p=2

The full order
F=(x,b,a,c,d,e,...)
has exact word
0,1,1,0^(p-2),1^q.
Indeed its first three labels are alpha(x,b,a)=0, alpha(b,a,c)=1, alpha(a,c,d)=1; every later window is an unchanged window of O_x beginning at c.

Thus p=2 gives the spanning NOR-good word 0,1^(q+2). A stopped first pivot with p=2 cannot occur in a counterexample. This proof uses neither a scan assumption nor transport.

### 2. The next splice bit can produce a genuine endpoint chord

Suppose p>=3 and put mu=alpha(a,d,e).
Delete c from F. The resulting order on V minus {c} is
O_c=(x,b,a,d,e,...).
Its exact word is
0,0,mu,0^(p-3),1^q.
The second zero follows from alpha(b,a,d)=1-alpha(a,b,d)=0. Again all windows beginning at d are unchanged.

If mu=0, O_c is a good deletion witness with exactly the original profile 0^p1^q. Prepending c gives first label alpha(c,x,b)=alpha(x,b,c)=1, and the first transition has ordered packet (c,x,b,a). Its endpoint root is
e_c-e_a,
with central cut {c,x}.
The endpoint faces are explicitly
alpha(c,x,b)=1, alpha(x,b,a)=0,
alpha(c,x,a)=0, alpha(c,b,a)=1.
Hence this is a fully-curved endpoint root of the SAME admissible witness class, not merely a raw transition or a mixed transport root.

At a pinned physical junction a->x->c, this new root c->a completes an actual three-edge endpoint cycle. If the original simple endpoint cycle has length greater than three, this gives a strictly shorter endpoint cycle, retaining the same phase profile and global status convention.

If mu=1, O_c instead has word 0,0,1,0^(p-3),1^q. For p=3 this is the good word 0^2 1^(q+1), so it strictly decreases the first phase.

### Precise consequence

If p is globally minimum among admissible good deletion witnesses, a pinned stopped pivot with p=3 has mu=0 and produces a genuine endpoint three-cycle. Therefore a minimum-length endpoint cycle of length greater than three cannot contain a pinned stopped pivot whose witness has p<=3: p=2 closes outright; p=3 either decreases p or supplies a shorter cycle.

For p>=4, the genuinely unresolved local branch is lambda=mu=1. The new deletion order then has the explicit bad word 0,0,1,0^(p-3),1^q. This is the packet that must be repaired with retained deletion provenance. No terminating repair is claimed here.

### Relation to the current endpoint-cycle claims

This refines the first-stop branch of roots §§119/123/124. Their raw root x->d lies on a deletion order with word 0,1,0^(p-2),1^q and need not be an endpoint root from a good deletion witness. The surgery above supplies an actual endpoint replacement in the mu=0 branch, avoiding that class change.

The conclusion is local and assumes a realized pinned junction when using cycle shortening. Endpoint corner lifting itself remains unproved, and this does not establish unrestricted r=3 NOR.
