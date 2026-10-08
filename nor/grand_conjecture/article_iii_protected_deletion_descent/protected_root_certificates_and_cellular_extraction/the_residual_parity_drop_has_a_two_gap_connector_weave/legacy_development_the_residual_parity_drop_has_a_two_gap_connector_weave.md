# The residual parity drop has a two-gap connector weave — preserved pre-item development

## Development

## The residual parity drop has a two-gap connector weave

Let
[
P=(b_1,ldots,b_r)
]
be a NOR-good order of the large shore (B), normalized by
[
c(P)=0^p1^q.
]
Let (e_i) be the universal connector scan of §350.

Assume the residual switch state of §346:
[
e_p=1,qquad e_{p+2}=0.
]

Choose any two connector-side coordinates
[
y_L,y_Rin Acup{x,z},
qquad y_L
e y_R.
]

Insert (y_L) between (b_p,b_{p+1}) and (y_R) between (b_{p+2},b_{p+3}). Around the switch the new order is
[
ldots,b_p,y_L,b_{p+1},b_{p+2},y_R,b_{p+3},ldots
]

Put
[
r=e_{p+1}.
]

Using the universal insertion formula of §350:

[
alpha(b_p,y_L,b_{p+1})=1-e_p=0,
]

[
alpha(y_L,b_{p+1},b_{p+2})=e_{p+1}=r,
]

[
alpha(b_{p+1},b_{p+2},y_R)=e_{p+1}=r,
]

and

[
alpha(b_{p+2},y_R,b_{p+3})=1-e_{p+2}=1.
]

Hence the four central new statuses are exactly
[
oxed{0,r,r,1}.
]

For either value of (r), this packet has at most one change.

The immediately exterior new windows are
[
e_{p-1}
]
on the left and
[
e_{p+3}
]
on the right, with endpoint clipping.

Therefore the entire local replacement packet is
[
oxed{e_{p-1},,0,r,r,1,,e_{p+3}}.
]

All untouched windows farther left are zero and all untouched windows farther right are one.

### Consequence

If
[
e_{p-1}=0,qquad e_{p+3}=1,
]
then the two-gap insertion absorbs the shore switch completely into one global (0	o1) transition.

If closure fails, at least one of
[
e_{p-1}=1,qquad e_{p+3}=0
]
must hold. Thus the residual parity obstruction cannot remain confined to the two edges adjacent to the shore switch: it propagates at least one step outward.

This is the first explicit transport rule for the universal connector scan. Iterating analogous separated insertions should be viewed as moving the two ends of the parity wall away from the switch.
