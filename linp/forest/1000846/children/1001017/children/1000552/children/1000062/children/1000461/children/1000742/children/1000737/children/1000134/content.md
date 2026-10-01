# Type-A terminal ranks either branch or form an exact ladder down to an exceptional entrance

## Statement

Let v be Type A with p=phi(v)>=5. For 2<=r<=p-1 let n_r(v) be the number of nonspecial edges of rank exactly r for which v is a terminal, and put
  N_r(v)=sum_{j=2}^r n_j(v).

Then:
  N_r(v)<=2r-3
for every r, and
  N_{p-1}(v)=2p-5=2(p-1)-3.

Consequently exactly one of the following holds.

(BRANCH) For some r with 3<=r<=p-1,
  n_r(v)>=3.

(LADDER) One has
  n_2(v)=1
and
  n_r(v)=2
for every 3<=r<=p-1.

Moreover, in the LADDER case the unique rank-two nonspecial terminal edge through v has a non-Type-A unique entrance whenever all Type-A vertices in the ambient argument have potential at least three.

## Body

The cumulative bound is exactly 0e550ff0eadd:
  N_r(v)<=2r-3.
Type A gives total nonspecial terminal degree
  N_{p-1}(v)=2p-5,
and a57057ab0001 says all such terminal edges have rank at most p-1, so equality holds at the top threshold.

Assume the BRANCH alternative fails, i.e.
  n_r(v)<=2
for all r>=3.

Since
  N_{p-1}=2p-5,
we have
  N_{p-2}=N_{p-1}-n_{p-1}
          >=2p-7.
But the cumulative bound at p-2 gives
  N_{p-2}<=2p-7.
Hence equality holds and n_{p-1}=2.

Repeat downward. If for some r>=3 we know
  N_r=2r-3,
then n_r<=2 gives
  N_{r-1}=N_r-n_r>=2r-5,
while the cumulative bound gives
  N_{r-1}<=2(r-1)-3=2r-5.
Thus
  N_{r-1}=2r-5
and
  n_r=2.

Inducting down to r=3 yields
  N_2=1,
  n_r=2 for every 3<=r<=p-1.
Since rank-one nonspecial edges do not exist, N_2=n_2=1. This is the LADDER distribution.

Conversely the LADDER distribution clearly has no layer of size at least three, proving the dichotomy.

Finally consider the unique rank-two nonspecial terminal edge e in the LADDER case and let x be its unique entrance. If x were Type A and all Type-A vertices under consideration had potential at least three, then a57057ab0001 would force every nonspecial edge sourced at x to be ascending. For a rank-two ascending edge,
  phi(x)=phi(e)-1=1,
contradicting the assumed Type-A potential floor. Therefore x is non-Type-A.