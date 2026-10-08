# The last flat corner has a forced noncolliding transport pattern — preserved pre-item development

## Composition

(none yet)

## Development

## The last flat corner has only one surviving transport pattern in each direction

Continue in the coboundary-flat pure-orientation sector. Let C be a Phi-maximal minimum four-change cyclic order with canonical run profile
1,p,q,2, with p,q>=2.
By the preceding extremal results, the transitions
1|p, p|q, q|2
are fully curved. Only the remaining transition D=2|1 can possibly be flat.

Assume D is flat. Then both endpoint repairs are available.

Represent the four transition positions cyclically by A,B,C,D with gap lengths
A->B=p, B->C=q, C->D=2, D->A=1.

### Left repair
A left repair of D transports the switch by distance 2 or 3 unless it annihilates with an occupied transition.
- Distance 2 lands exactly on C, because C->D=2. This would delete D and C and lower cyclic variation from four to two, closing NOR. Hence a counterexample forces the left transport distance to be 3.
- Distance 3 lands one transition slot before C. Replacing D by that new position changes the cyclic run lengths, up to rotation, from
  (1,p,q,2)
  to
  (1,3,p,q-1).
The Phi change is
  [1^2+3^2+p^2+(q-1)^2] - [1+p^2+q^2+2^2]
  = 6-2q.
Since C is Phi-maximal among four-change orders, this repair cannot increase Phi. Therefore q>=3.

### Right repair
A right repair of D transports by distance 2 or 3.
- Distance 2 crosses the singleton run and lands one slot inside the p-run. The new run lengths are, up to rotation,
  (3,1,p-1,q),
with
  Delta Phi = 6-2p.
Thus if the right selector chooses distance 2, extremality forces p>=3.
- Distance 3 lands two slots inside the p-run. If p=2, this target is exactly B, so variation drops to two and NOR closes. For p>=3 the new run lengths are
  (3,2,p-2,q),
with
  Delta Phi = 12-4p.
Thus this branch also cannot survive with p=2; for p=3 it is Phi-neutral and for p>3 it lowers Phi.

Consequently any Phi-maximal counterexample with the residual corner D flat must satisfy
p,q>=3,
the left repair selector is forced to distance 3, and the right repair avoids every collision with the already-pinned barriers.

This is not yet a contradiction, because for long p,q the surviving repairs may decrease Phi and move out of the extremal representative. But it sharply determines the local dynamics of any closed component: its Phi-maximal state has three fully-curved barriers and one flat corner whose left move is uniquely selected and whose two incident long runs satisfy p,q>=3. A no-closed-component theorem can now focus on the return path after this forced left move rather than on arbitrary four-switch configurations.
