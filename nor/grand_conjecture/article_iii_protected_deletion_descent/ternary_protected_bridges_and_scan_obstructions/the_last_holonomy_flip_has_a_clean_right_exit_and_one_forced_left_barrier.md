# The last holonomy flip has a clean right exit and one forced left barrier

## Composition

Choose the last special-scan holonomy drop h_j=1,h_{j+1}=0. Then h_k=0 for every later k. For the color-0 toggle order (x,a,d,b,c,e), this makes the right continuation threshold-compatible: for j<=p-3 the first right crossing has color h_{j+2}=0 and the untouched carrier then remains in the old zero phase until its unique cut; at j=p-2 the first crossing may be either color, but the following untouched suffix is already all 1, so there is still at most one right-side phase change.

Thus the last holonomy flip gives a full-support color-0 realization whose six-set interior and entire right suffix are compatible with a one-change 0-to-1 target. If j>=3, the audited common-left-reconnection theorem further shows that the sole excess oscillation on the left is 010 and its 10 edge is a fully-curved barrier carrying e_{v_{j-2}}-e_{v_j}. For j=1,2 the clean-right conclusion remains valid but the left endpoint must be analyzed separately.

This is the sharp special-branch normal form: clean right exit, and—away from the extreme left endpoint—one canonical full-barrier root as the only remaining defect.

## Development

## The last holonomy flip has a clean right exit and one forced left barrier

Continue in the special perfect-blocker branch with holonomy sequence

h_1,...,h_{p-1},

where h_1=1 and h_{p-1}=0. Choose j to be the last index with

h_j=1, h_{j+1}=0.

Then necessarily
h_k=0
for every k>=j+1; otherwise a later 0->1 would have to be followed by another 1->0 before the terminal value h_{p-1}=0.

Use the color-0 phase-toggle order

Pi_0=(x,a,d,b,c,e),

where
a=v_j, b=v_{j+1}, c=v_{j+2}, d=v_{j+3}, e=v_{j+4}.

Its four internal statuses are 0000.

### Right reconnection for j <= p-3

Let f=v_{j+5}. The first right crossing status is

alpha(c,e,f).

By the holonomy identity for packet j+2,

alpha(c,e,f)=h_{j+2}=0

whenever j+2<=p-1. Thus for j<=p-3 the first right reconnection window is color 0.

If j<=p-4, the next untouched old window begins at e=v_{j+4} with j+4<=p, hence is still color 0. All subsequent old windows remain 0 until the original phase cut and then remain 1. Therefore the entire suffix is threshold-compatible.

If j=p-3, the next untouched old window begins at v_{p+1} and is the first color-1 old window. Hence the right side is exactly

...,0,0,1,1,...

and is again threshold-compatible.

### Endpoint j=p-2

Now the next untouched old window after the first right crossing already lies in the 1-phase. Write r=alpha(c,e,f). If r=0, the unique 0->1 transition occurs one window later; if r=1, it occurs at the first crossing itself. Either way the right continuation has at most one phase change and then stays in the old 1-phase.

Thus the right side is also clean in the endpoint case without determining r.

### The only extra oscillation is on the left

By subsection 53, the common left reconnection has the fixed pattern

0,1,0

inside the old zero phase, and the central 10 transition is fully curved with protected root

rho_j=e_{v_{j-2}}-e_{v_j}.

Therefore the last holonomy flip admits a full-support color-0 order whose entire interior and right suffix agree with a one-change 0-to-1 target. The sole excess variation is the single left 010 defect, and its right-hand 10 edge is a forced full-curvature barrier.

This gives a canonical one-sided normal form for the special perfect-blocker branch:

one isolated left barrier root + otherwise threshold-compatible full order.

The remaining closure problem is now to eliminate or exploit that single root; no right reconnection obstruction survives after choosing the last holonomy flip.
