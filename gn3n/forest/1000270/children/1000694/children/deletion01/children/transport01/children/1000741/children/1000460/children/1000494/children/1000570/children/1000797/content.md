# One-crossing sharp half-order comparisons have two endpoint forms and a third deletion cover

## Statement

Let H be a minimum counterexample with |V(H)|=2lambda+1 and maximum tight-path order lambda. Let G_x,G_y be exact two-covers of H-x,H-y, with y terminal in G_x and x initial in G_y. Put T_x=G_x-y and T_y=G_y-x. Suppose T_y has exactly one ordinary edge crossing the support partition of T_x, and every common component intersection has the same relative order in T_x and T_y. Then there are paths B,Q of order lambda-1 and a vertex m such that G_y=(x,B)|(Q,m), G_m=(x,B)|(Q,y) is an exact two-cover of H-m, and G_x is either (m,B)|(Q,y) or (b,m,R)|(Q,y), where B=(b,R). The reciprocal crossing count is respectively one or two. In the first case, with q=last(Q), the five triples (b,m,q),(b,x,m),(b,m,x),(y,m,q),(m,y,q) are tight. In the second case, with r=first(R), the five triples (b,x,m),(m,b,x),(r,m,x),(y,m,q),(m,y,q) are tight.

## Body

# One-crossing endpoint comparisons in the sharp half-order case

## Theorem

Let H be a minimum counterexample with |V(H)|=2lambda+1 and maximum tight-path order lambda. Let G_x,G_y be exact two-covers of H-x,H-y, with y terminal in G_x and x initial in G_y. Put T_x=G_x-y and T_y=G_y-x. Suppose T_y has exactly one ordinary edge crossing the support partition of T_x, and every common component intersection has the same relative order in T_x and T_y. Then there are paths B,Q of order lambda-1 and a vertex m such that G_y=(x,B)|(Q,m), G_m=(x,B)|(Q,y) is an exact two-cover of H-m, and G_x is either (m,B)|(Q,y) or (b,m,R)|(Q,y), where B=(b,R). The reciprocal crossing count is respectively one or two. In the first case, with q=last(Q), the five triples (b,m,q),(b,x,m),(b,m,x),(y,m,q),(m,y,q) are tight. In the second case, with r=first(R), the five triples (b,x,m),(m,b,x),(r,m,x),(y,m,q),(m,y,q) are tight.

Here x and y are distinct. The order-preservation assumption means that whenever a component of T_x and a component of T_y have common vertices, those vertices occur in the same relative order. No assumption is made about crossings of a separately chosen longest path.

## A unique crossing determines the support transfer

Every component of a one-vertex deletion cover has order lambda. Consequently each of T_x,T_y has one component of order lambda and one of order lambda-1. Write T_x=P|Q, with |P|=lambda and |Q|=lambda-1. Since y is terminal in G_x, it restores to Q, giving G_x=P|(Q,y).

Cut the unique crossing edge of T_y relative to P|Q. This leaves three nonempty monochromatic blocks. The whole P-support cannot be one block: its component would contain an additional Q-vertex and have order greater than lambda. Thus P is split into two blocks B,M and Q occurs as one whole block. The mixed component has support M union Q, whose order is at most lambda. Since |Q|=lambda-1, M={m} is a singleton. Hence |B|=lambda-1, the mixed component has order lambda, and x restores initially to B. Order preservation makes B exactly the order of P with m removed, and makes the mixed component either (m,Q) or (Q,m).

The former possibility is impossible: (m,Q,y) is tight, since its two endpoint joins are inherited from (m,Q) and (Q,y), and |Q|>=2. Together with (x,B), it would be a spanning two-cover. Therefore G_y=(x,B)|(Q,m).

Write P=(p_0,...,p_{lambda-1}) and m=p_j. If j>=2, the first two vertices of B are p_0,p_1. The tight path (x,B) supplies (x,p_0,p_1), so (x,P) is a tight path of order lambda+1, a contradiction. Thus j is zero or one.

For j=0, P=(m,B). For j=1, write B=(b,R), giving P=(b,m,R). The bounds n>10 and n=2lambda+1 imply lambda>=5, so B,Q have at least four vertices and R is nonempty.

The paths (x,B) and (Q,y) are disjoint and cover H-m. Thus they give the asserted third exact deletion cover G_m.

Relative to the support partition B | (Q union {m}) of T_y, all vertices of Q lie in the second class. In T_x, the only crossing edges are the edges of P incident with m. Their number is one when j=0 and two when j=1. This proves the exact reciprocal crossing counts.

## Forced triples in the endpoint case

Suppose P=(m,B), and put b=first(B), q=last(Q). The vertex-simple sequence (Q,m,B) has order 2lambda-1>lambda. All consecutive triples are inherited from (Q,m) or (m,B), except (q,m,b). This triple is therefore non-tight, giving (b,m,q) tight.

Each of the following vertex-simple sequences has order lambda+1, with its only unverified triple displayed alongside it:

- (m,x,B): (m,x,b);
- (x,m,B): (x,m,b);
- (Q,m,y): (q,m,y);
- (Q,y,m): (q,y,m).

All other triples are inherited respectively from (x,B), (m,B), (Q,m), and (Q,y). Maximality and reversal antisymmetry give the other four claimed tight triples.

## Forced triples in the second-position case

Suppose P=(b,m,R), B=(b,R), and put r=first(R), q=last(Q).

The sequence (m,x,b,R) has order lambda+1 and inherits all triples from (x,b,R) except (m,x,b). Hence (b,x,m) is tight.

The sequence (x,b,m,R) has order lambda+1 and inherits all triples from (b,m,R) except (x,b,m). Hence (m,b,x) is tight.

Now (b,x,m,R) has order lambda+1. Its first triple (b,x,m) was just proved tight, and all triples starting with m or later are inherited from (m,R). Its only unchecked triple is (x,m,r). Hence (r,m,x) is tight.

Finally, (Q,m,y) and (Q,y,m) each have order lambda+1. Their only unchecked triples are (q,m,y) and (q,y,m), respectively. This gives (y,m,q) and (m,y,q), as claimed.

## Consequence for support reconfiguration

In either case the four supports

V(B) union {m}, V(Q) union {y}, V(B) union {x}, V(Q) union {m}

form an induced path in the Hamiltonian-support disjointness graph, in the displayed order. Its edge labels are x,m,y. Consecutive supports are disjoint and omit precisely the indicated vertex; nonconsecutive pairs intersect in B, Q, or {m}.

Thus a one-crossing comparison yields a third exact deletion state and only two possible inherited path orders. In particular reciprocal crossing number one forces the first form. This does not yet imply absorption or termination.

The argument continues the reciprocal-crossing reduction and extends the endpoint localization used for crosswise endpoint covers to arbitrary one-crossing comparisons in the sharp half-order case. Its proof is independent of the pending general singleton-transfer theorem.
