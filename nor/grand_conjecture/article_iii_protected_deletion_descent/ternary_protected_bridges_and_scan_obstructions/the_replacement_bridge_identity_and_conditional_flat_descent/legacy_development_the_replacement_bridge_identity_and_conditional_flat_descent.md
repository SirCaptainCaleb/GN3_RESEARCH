# The replacement bridge identity and conditional flat descent — preserved pre-item development

## Composition

(none yet)

## Development

Sources: Article II §§187,188,191,194,199, with the scan premise corrected.

Use a ternary deletion order O of word 0^p1^q, p>=3, and omitted x. Put s_i=alpha(x,v_i,v_{i+1}). Let
kappa=delta alpha({x,v_{p-1},v_p,v_{p+1}}).
The four-face identity, with w_{p-1}=0, gives
alpha(x,v_{p-1},v_{p+1})=s_{p-1} xor s_p xor kappa.
Thus replacing v_p by x changes precisely the three-window packet to
B=(s_{p-2}, 1 xor s_{p-1} xor s_p xor kappa, s_{p+1}).

For a minimum-first-phase deletion witness, every B in {001,011,111} gives strict descent and contradicts extremality; all these packets are monotone with a nonempty second phase. The word 000 is inert, and every remaining binary packet contains 10.

In the flat sector kappa=0. If the SPECIAL scan s=1^(p+1)0^q is additionally known, then B=111 and
O' has word 0^(p-3)1^(q+3).
Moving v_p to the beginning of O' gives a full order whose word adds one initial bit. That bit equal to zero closes the full instance; equal to one makes O' the explicit improved deletion witness. At a globally minimum first phase, either alternative is impossible. This is the valid local core of the protected-descent proof.

The theorem is conditional on applicability of the scan or an equivalent bridge hypothesis. Flatness alone does not make B=111. For example the alternative blocking scan 11,0,...,0 gives B=010 when p>=5 even with kappa=0. Therefore neither flat-sector closure nor the forced nonzero-curvature corridor of §199 follows from the currently proved insertion facts.

A useful sufficient condition uses only four scan bits: s_{p-2}=s_{p+1}=1 and s_{p-1} xor s_p=kappa. Under these hypotheses B=111. This isolates precisely what a selection or synchronization lemma would have to supply.
