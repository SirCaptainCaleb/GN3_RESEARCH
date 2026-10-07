# The t=tau double-full singleton packet has an exact finite transport law

## Metadata

- ID: the_ttau_double_full_singleton_packet_has_an_exact_finite_transport_law
- Parent Section: directed_nor_union_closed_bridge
- Position: 126
- Row version: 1
- Development version: 1
- Composition version: None
- Composition stale: False

## Composition

(none yet)

## Development

## In the t=tau branch, double-full cancellation transports the singleton packet by a finite run transformation

Continue with a Phi-extremal flat-sector four-change cyclic order of profile
1,p,q,2
and focus on the singleton run together with its two adjacent fully-curved switches. Write the local status sequence, starting at the last status of the q-run, as
tau, sigma, sigma, tau, sigma, sigma, ...
corresponding to coordinates
...,x,u,a,b,c,d,e,v,...
with
alpha(x,u,a)=tau,
alpha(u,a,b)=sigma,
alpha(a,b,c)=sigma,
alpha(b,c,d)=tau,
alpha(c,d,e)=sigma,
alpha(d,e,v)=sigma.

Assume the residual five-set bit of the double-full gadget is t=tau. Replace the five coordinates
(a,b,c,d,e)
by
(b,a,c,e,d).
The five statuses from alpha(u,b,a) through alpha(e,d,v) are all tau.

Because the preceding transition q|2 is also fully curved in the extremal carrier, the tetrahedron {x,u,a,b} is fully curved. Its face pattern forces
alpha(x,u,b)=sigma.
Thus after the replacement the local word begins
tau, sigma, tau,tau,tau,tau,tau,...
so the q|2 barrier and the singleton packet have been converted into a new singleton sigma-run followed by a long tau-run.

Let
r=alpha(d,v,w)
denote the first new status after the displayed tau block, where w is the next exterior coordinate; equivalently, in the original indexing this is the status occupying the third position of the p-run after the local replacement. There are two equality cases when p is long enough.

If r=sigma, then the new four run lengths, up to cyclic rotation, are
1, p-2, q-1, 5.

If r=tau, then the tau block absorbs one further position and the new run lengths are
1, p-3, q-1, 6.

These formulas follow simply by tracking the transition positions: the old q-run loses its last status, the old two-run and singleton are replaced by a one-status sigma run plus the five-status tau block, and the old p-run loses respectively two or three statuses. The untouched transition p|q remains in place.

If one of the displayed lengths becomes zero, two adjacent same-color runs merge and cyclic variation drops from four to two, which closes NOR. Thus, in a counterexample, the second branch in particular requires p>=4; for p=3 it closes immediately.

The corresponding Phi changes are:
- r=sigma: Delta Phi = 26 - 4p - 2q;
- r=tau: Delta Phi = 42 - 6p - 2q.

This is not yet a global descent theorem: for long p,q these moves can decrease Phi and leave the chosen extremal representative. But it is a concrete finite transport law. The double-full singleton packet cannot remain stationary in the t=tau branch; it either closes NOR or consumes a definite amount of the two neighboring long runs and reappears as another four-run configuration with a newly created short/long packet.

A closed repair component must therefore support repeated packet transport with changing local residual bits. This gives a more precise holonomy target: show that repeated t=tau transport, interspersed with the t=sigma one-sided resolutions, cannot return to the original four-run state without a switch collision or a two-change intermediate.

## Frontier

- Development version when composed: None
- Development version now: 1
