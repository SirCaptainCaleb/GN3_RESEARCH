# Near-saturated gap-one vertices force a large anchor-to-maximum-path switching matching

## Statement

In the gap-one shell p=phi(v)=q+1, let delta=gamma(q)-(t(v)-X_v^T), where X_v^T is maximum-path excess multiplicity from the ascending terminal family. For any rank-q anchor path Q and any maximum p-path P ending at v, at least gamma(q)-ceil((3q-4)/4)-delta = (5/8)q-O(1)-delta ascending terminal edges are double on Q but single on P. Their disjoint non-v pairs form a matching in the anchor precursor R=V(Q)\h crossing from R∩V(P) to R\V(P). Hence both sides of this cut have size at least that quantity.

## Body

Let v have p=phi(v)=q+1 with q>=4, and let T be the full family of ascending nonspecial edges terminal at v. Assume q(v)=q, so some h in T has rank q.

Choose:
- a q-edge longest h-path Q ending at v, and put R=V(Q)\h;
- an arbitrary maximum p-edge path P ending at v.

Let t=|T|. Let X_v be the excess contact multiplicity of T on P:
  X_v^T=sum_{e in T} max(mu_P(e)-1,0),
so X_v^T<=X_v for the full incident excess.

Put
  a(q)=ceil((3q-4)/4),
  gamma(q)=floor((11q-5)/8),
and define the gap-one local slack
  delta=gamma(q)-(t-X_v^T)>=0.

Then
  delta=(gamma(q)-t)+X_v^T.                          (1)

SHORT-ANCHOR DOUBLES.
By cac6635878e5 / 243723939a85, if d_Q(T) is the number of e in T\{h} whose two non-v vertices both lie in R, then
  d_Q(T)>=t-a(q).                                    (2)

MAXIMUM-PATH DOUBLES.
Every edge e in T has rank <=q<p, so e cannot be clean on P; hence mu_P(e)>=1. The number of e in T with mu_P(e)>=2 is at most X_v^T, because each such edge contributes at least one to X_v^T.

Therefore at least
  d_Q(T)-X_v^T
of the anchor-double edges are single on P. Using (1),(2),
  d_Q(T)-X_v^T
  >=t-a(q)-X_v^T
   =gamma(q)-a(q)-delta.                            (3)

The floor-ceiling identity in the Astra stability calculation gives
  gamma(q)-a(q)=floor(5q/8)-epsilon_q,
with at most an O(1) residue correction (equivalently retain the exact expression gamma(q)-a(q)).
Thus the number s_switch of edges which are double on Q but single on P satisfies exactly
  s_switch >= gamma(q)-a(q)-delta
           = (5/8)q-O(1)-delta.                    (4)

CROSSING MATCHING INTERPRETATION.
For every switching edge e={v,a_e,b_e}, both a_e,b_e lie in R because e is Q-double. Since e is P-single and e already meets the last P-edge at v, exactly one of {a_e,b_e} lies in V(P)\last(P); the other is absent from V(P).

Distinct switching edges have disjoint non-v pairs by linearity. Hence the pairs
  {a_e,b_e}
form a matching in R crossing the cut
  I = R intersect (V(P)\last(P)),
  O = R minus V(P).

Consequently
  |I|>=s_switch,
  |O|>=s_switch.                                    (5)

Thus every gap-one vertex whose local master contribution is within delta of the dangerous bound manufactures a crossing matching of size
  (5/8)q-O(1)-delta
between anchor vertices retained by a maximum terminal path and anchor vertices omitted by it.

This is stronger than mere overlap: it records the paired Q-geometry of each transferred double.
