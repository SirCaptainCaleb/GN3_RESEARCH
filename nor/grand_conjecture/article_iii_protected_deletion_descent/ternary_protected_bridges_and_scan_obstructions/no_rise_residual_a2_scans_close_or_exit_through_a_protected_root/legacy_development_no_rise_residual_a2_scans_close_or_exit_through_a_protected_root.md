# No-rise residual A2 scans close or exit through a protected root — preserved pre-item development

## Composition

(none yet)

## Development

## A no-rise residual A2 scan closes or exits through a protected root

Continue in the recurrent flat A2 replacement configuration and fix one residual coordinate u.

Delete the final u from its companion seven-coordinate weave. By the recurrent A2 theorem, the resulting full deletion carrier has a protected front of word
0,1,1,1
and then the untouched common suffix
T=(t_1,ldots,t_L),
whose consecutive ternary windows all have color 1.

Write
s_j=alpha(u,t_j,t_{j+1}),qquad 1<=j<=L-1.
The scan starts with 1 and ends with 0.

Assume this scan has NO later 0->1 rise. Then it is necessarily
1^*0^*.
Let d be its last 1:
s_d=1,qquad s_{d+1}=cdots=s_{L-1}=0.
Put
r=(L-1)-d,
the length of the terminal zero-run.

We show that every r>=1 either closes NOR or leaves the recurrent flat A2 class through a certified protected root.

### Case r=1: the drop is at the final scan edge

Insert u in the final suffix gap, between t_{L-1} and t_L.

Only the last two ternary windows are new. Their colors are
alpha(t_{L-2},t_{L-1},u)=alpha(u,t_{L-2},t_{L-1})=s_{L-2}=1,
and
alpha(t_{L-1},u,t_L)=1-alpha(u,t_{L-1},t_L)=1-s_{L-1}=1.

Everything earlier in the suffix already has color 1, while the protected front is 0 followed by 1s. Hence the resulting full-support order has at most one color change. NOR closes.

### Case r=2: the terminal mixed full/flat packet

Now
s_{L-3}=1,qquad s_{L-2}=s_{L-1}=0.
Insert u in the final gap between t_{L-1} and t_L.

The last three statuses are
alpha(t_{L-3},t_{L-2},t_{L-1})=1,
alpha(t_{L-2},t_{L-1},u)=s_{L-2}=0,
alpha(t_{L-1},u,t_L)=1-s_{L-1}=1.
Thus the tail is the isolated singleton word 101.

This is exactly the shortest-valley mixed full/flat motif of the residual scan-rise theorem, with the left 1->0 transition flat and the right 0->1 transition fully curved.

Use the already-proved full-flat five-set resolution exactly as in §65. In the two-sided holonomy branch the singleton disappears outright. In the one-sided branch choose the resolution preserving the protected LEFT boundary and exporting risk to the right.

Here the five-set reaches the global suffix endpoint, so there are no right reconnection windows beyond the packet. Therefore the one-sided exit is already a spanning one-change order. NOR closes.

### Case r>=3: a double-full singleton appears one gap after the drop

Insert u between t_{d+1} and t_{d+2}.

The three new statuses are
s_d,quad 1-s_{d+1},quad s_{d+2},
hence
1,1,0.

Because r>=3, the next untouched suffix window exists and has color 1. Therefore the last new 1, the new 0, and the next old 1 form an isolated 101 singleton.

We verify that BOTH transitions are fully curved.

For the left 1->0 transition, put
a=t_{d+1},quad b=t_{d+2},quad c=t_{d+3}.
We have
alpha(u,a,b)=s_{d+1}=0,
alpha(u,b,c)=s_{d+2}=0,
alpha(a,b,c)=1.
Flat four-face parity forces
alpha(u,a,c)=1,
hence
alpha(a,u,c)=0.
Thus the two off-faces of the ordered transition (a,u,b,c) are 0 and 1 in the fully-curved pattern.

For the right 0->1 transition, use the next suffix coordinate e=t_{d+4}. Since r>=3,
alpha(u,b,c)=0,
alpha(u,c,e)=s_{d+3}=0,
alpha(b,c,e)=1
after the obvious relabeling along the suffix; the same parity calculation gives the opposite off-face pattern. Equivalently this is the right-hand calculation already used in the residual scan-rise theorem. Hence the right transition is fully curved as well.

So the isolated 101 is double-full.

Use the color-complemented one-sided resolution of §62 that preserves the ordered LEFT boundary pair. It changes the internal 101 packet to 110. Consequently every already-compatible window to the left is preserved, while the first possible mismatch moves strictly to the right of the old singleton defect.

Pass to the maximal target-compatible band containing the protected left side. Its right endpoint has strictly advanced. Apply the audited threshold-band dynamics:
- every flat nearest boundary is repaired outward and strictly enlarges the band;
- if the band reaches the end, the full order is one-change;
- otherwise the first terminal fully-curved boundary emits an actual protected physical root.

Thus r>=3 also closes NOR or exits through a protected root.

### Theorem

A residual scan in the recurrent flat A2 replacement configuration that has no later 0->1 rise cannot remain recurrently flat. Its unique 1->0 drop yields either:
1. a spanning one-change order; or
2. after a strict boundary-safe band enlargement and finite combing, a fully-curved protected root.

Combined with §65, which gives the same close-or-protected-root dichotomy whenever a later 0->1 rise occurs, EVERY residual scan yields that dichotomy.

Therefore a recurrent flat A2 replacement cycle is not a closed terminal obstruction: it either closes NOR or exits the flat A2 class through an actual protected root.
