# Genuine two-deletion doubles reverse all four corridor ends — preserved pre-item development

## Development

## In the genuine two-deletion case both exterior vertices reverse every exposed corridor end

Let J=C union {x,y} be a reflected-double span with corridor two-cover
[
C=Pmid Q,
]
where
[
P=(p_1,ldots,p_s),qquad Q=(q_1,ldots,q_t),
]
and suppose
[
kappa_2(H[J])=2.
]

Then neither one-vertex deletion has a two-cover:
[
operatorname{pc}(H[J-x])>2,qquad operatorname{pc}(H[J-y])>2,
]
while deleting the remaining exterior vertex from either leaves C, which has path-cover number at most two. Thus both H[J-x] and H[J-y] are deletion-distance-one instances.

In particular every immediate extension of the displayed corridor cover by x or y must fail.

For each e in {x,y}, if
[
h(e,p_1,p_2)=1,
]
then
[
(e,P)mid Q
]
would be a two-cover of C union {e}, contradicting the preceding statement. Hence
[
h(e,p_1,p_2)=0,
]
and boundary antisymmetry gives
[
h(p_2,p_1,e)=1.
]
Likewise
[
h(q_2,q_1,e)=1.
]

At the terminal ends, if
[
h(p_{s-1},p_s,e)=1,
]
then
[
(P,e)mid Q
]
would two-cover C union {e}. Therefore
[
h(p_{s-1},p_s,e)=0
]
and hence
[
h(e,p_s,p_{s-1})=1.
]
Symmetrically
[
h(e,q_t,q_{t-1})=1.
]

Consequently, in the genuine kappa_2=2 reflected-corridor residue, **both** exterior vertices reverse **all four** exposed endpoint edges:
[
egin{aligned}
&h(p_2,p_1,x)=h(p_2,p_1,y)=1,\
&h(q_2,q_1,x)=h(q_2,q_1,y)=1,\
&h(x,p_s,p_{s-1})=h(y,p_s,p_{s-1})=1,\
&h(x,q_t,q_{t-1})=h(y,q_t,q_{t-1})=1.
end{aligned}
]

This is substantially stronger than generic failure of the terminal attachment matching. In particular:

- the attachment graph has no edges at all;
- each one-vertex deletion C+e is a kappa_2=1 instance;
- the endpoint data contain two same-edge twins at each of four exposed edges and common-reverser configurations across the two initial edges and across the two terminal edges.

The same-edge twin condition alone is insufficient, but the simultaneous four-end condition is the correct strengthened residue for the next local analysis. Any two-deletion closure theorem need only handle this configuration, not arbitrary Hall failure.
