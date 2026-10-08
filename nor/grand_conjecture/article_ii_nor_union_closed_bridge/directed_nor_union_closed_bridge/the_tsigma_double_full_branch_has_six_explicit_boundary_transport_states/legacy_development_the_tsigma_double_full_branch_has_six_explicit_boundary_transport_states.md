# The t=sigma double-full branch has six explicit boundary transport states — preserved pre-item development

## The t=sigma double-full branch reduces to six four-run boundary states

Continue in the coboundary-flat pure-orientation sector with a four-change carrier of canonical profile
1,p,q,2,
and suppose the singleton run is bounded by two fully-curved switches. Use the local notation of the previous subsections, and assume the residual five-set bit is t=sigma.

Choose the right-compatible tau-monochromatic five-vertex resolution
(c,b,a,e,d).
Assume p>=4 and q>=2 so there is at least one unchanged q-status immediately to the left and one unchanged p-status immediately to the right of the affected packet.

Write
r=alpha(x,u,c),
s=alpha(u,c,b),
z=alpha(d,v,y).
Then the affected status packet, including one unchanged status on each side, has the form
tau, r, s, tau,tau,tau,tau, z, sigma.

The right tail
tau,z,sigma
always has exactly one change, regardless of z. The left packet
tau,r,s,tau
has either zero or two changes. Therefore the new full-support order has cyclic variation at most four. Since a two-change cyclic order would cut to a spanning one-change order, counterexamplehood forces the left packet to have exactly two changes:
(r,s) != (tau,tau).

Thus there are exactly six equality states, according to
(r,s) in {(tau,sigma),(sigma,tau),(sigma,sigma)}
and z in {tau,sigma}.

Tracking the four transition positions gives the following new run profiles, up to cyclic rotation:

1. (r,s,z)=(tau,sigma,tau):
   (p-3, q, 1, 5),
   Delta Phi = 30-6p.

2. (tau,sigma,sigma):
   (p-2, q, 1, 4),
   Delta Phi = 16-4p.

3. (sigma,tau,tau):
   (p-3, q-1, 1, 6),
   Delta Phi = 42-6p-2q.

4. (sigma,tau,sigma):
   (p-2, q-1, 1, 5),
   Delta Phi = 26-4p-2q.

5. (sigma,sigma,tau):
   (p-3, q-1, 2, 5),
   Delta Phi = 34-6p-2q.

6. (sigma,sigma,sigma):
   (p-2, q-1, 2, 4),
   Delta Phi = 20-4p-2q.

At a Phi-maximal state every surviving branch must have Delta Phi<=0. Hence the six states satisfy respectively:
p>=5;
p>=4;
3p+q>=21;
2p+q>=13;
3p+q>=17;
2p+q>=10.

For p=2 or 3 the same right-compatible resolution still has variation at most four, but the right endpoint of the packet crosses the p|q transition and the run table degenerates; those bounded cases should be handled separately rather than forced into the displayed formulas.

### Significance
The t=sigma all-curved singleton trap is no longer an arbitrary reconnection problem. At minimum variation it enters one of six explicit transport states. Together with the two t=tau transport states, the all-curved terminal branch becomes a finite local automaton whose state records:
- the residual five-set bit;
- two left reconnection bits;
- one right reconnection bit;
- the adjacent run lengths.

A closed repair component would induce a cycle in this transport automaton. The next exact target is to derive the transition rule for the residual bit and reconnection triple after one packet move; a parity or monotonicity obstruction on that finite-state evolution would close the flat sector.
