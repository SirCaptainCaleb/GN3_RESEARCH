# Minimum-hole rebasing collapses the unbounded reflected corridor to six vertices — preserved pre-item development

## Rebase at a minimum hole: the unbounded corridor collapses to six vertices

Let H have kappa_2(H)=2, let X={x,y} be a minimum deletion pair, and fix a two-cover
H-X=P|Q
with displayed orders P=(p_1,...,p_r) and Q=(q_1,...,q_s).

By the exact minimum-hole concatenation theorem, for either ordering (u,v) of (x,y), the spanning order
pi=(P,u,v,Q^rev)
has exact deficiency two and
p(pi)=r-1,
q(pi)=r+2,
c(pi)=s-1.

Hence every status before r-1 is 1 and every status after r+2 is 0. The only undetermined statuses lie in the four-position central window
r-1,r,r+1,r+2.
The first is necessarily 0 and the last necessarily 1. Therefore the status word has the form
1^(r-2) 0 a b 1 0^(s-2),
with a,b in {0,1}.

Every positive witness from W_+={001,011,0101} is consequently contained in those four central status positions. Equivalently, every determining witness support is contained in the six actual vertices
{p_{r-1},p_r,x,y,q_s,q_{s-1}}.
There are only four central word types:
0001, 0011, 0101, 0111.
Their positive witnesses are respectively a terminal 001, the overlapping pair 001 and 011, the single 0101, and an initial 011. Reverse-complement exchanges 0001 with 0111 and fixes the middle two types.

If the complementary two-cover is balanced, r=s, then p=c=r-1. Thus a symmetric genuine two-deletion state is simultaneously:
(1) a minimum-deficiency state;
(2) a zero exact-root state; and
(3) a positive-witness state whose complete witness geometry is supported on six central vertices.

Therefore the unbounded reflected-double corridor is not a persistent terminal obstruction after deletion distance two has been established. It is a presentation used to prove kappa_2<=2. Once a genuine kappa_2=2 minimum pair is identified, one may and should rebase on a minimum-hole concatenation, where the positive obstruction is six-vertex local.

The surviving combinatorial task is consequently an anchored six-vertex routing problem: use the forced central tournament relations, together with the inherited path edges immediately outside the window, to repartition the two hole labels and boundary vertices into two paths compatible with the two untouched path interiors. No unbounded corridor analysis is required at this stage.
