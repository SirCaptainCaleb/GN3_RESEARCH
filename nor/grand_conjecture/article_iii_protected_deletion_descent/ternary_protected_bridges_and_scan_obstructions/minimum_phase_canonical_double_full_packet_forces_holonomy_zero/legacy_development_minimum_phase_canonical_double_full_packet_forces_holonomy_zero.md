# Minimum-phase canonical double-full packet forces holonomy zero — preserved pre-item development

## Composition

(none yet)

## Development


Work in a minimum coboundary-flat ternary counterexample. Let
O=(v_1,...,v_m)
be a one-change deletion carrier with word 0^p1^q, where p is globally minimum over all one-change deletion carriers after reversal and global color complement. In the current flat-sector normal form p,q>=4. Let x be the omitted perfect blocker, so its scan is 1^(p+1)0^q.

Use the canonical middle insertion state from the fixed deletion fiber (Article III's imported §189 geometry):
(a,b,c,x,d)=(v_{p-1},v_p,v_{p+1},x,v_{p+2}).
Its internal word is 0,1,0, both bounding transition tetrahedra are fully curved, and its residual double-full holonomy bit is
t = alpha(a,b,d)=alpha(a,c,d)=alpha(a,x,d).

Proposition. One must have t=0.

Proof. Suppose t=1. Return to the deletion carrier O and swap the adjacent old coordinates a,b, leaving x omitted:
O'=(...,v_{p-2},b,a,c,d,v_{p+3},...).

Only the four deletion windows starting at ranks p-3,p-2,p-1,p change. Write
epsilon=alpha(v_{p-3},v_{p-2},b)
when p>3. The changed packet is
epsilon,
alpha(v_{p-2},b,a)=1,
alpha(b,a,c)=1,
alpha(a,c,d)=t=1.
The middle two equalities are just alternation from the old zero windows
alpha(v_{p-2},a,b)=0 and alpha(a,b,c)=0.
The last equality is the residual holonomy identity. Every window from rank p+1 onward is untouched and already lies in the old 1-phase.

Hence O' is itself a one-change deletion order, regardless of epsilon: before epsilon all unchanged windows are 0, and from rank p-2 onward every window is 1. If epsilon=0 its first phase has length p-3; if epsilon=1 its first phase has length p-4 (with p=4 giving a monochromatic deletion witness). In every case this either closes immediately or contradicts the global minimality of p.

Therefore t cannot equal 1, so t=0. QED.

Consequences.
1. The canonical same-deleted-order double-full singleton does not carry a free holonomy bit. Minimum-phase provenance forces the one-sided branch t=0.
2. This is exactly the kind of extra provenance absent from the unconstrained four-bit independence theorem: flatness alone leaves the bit free, but deletion extremality removes one value.
3. Any boundary-band analysis starting from this canonical insertion fiber may therefore assume the t=0 double-full normal form. The remaining task is to use its one-sided protected resolutions together with the known perfect-blocker scan, rather than classifying arbitrary flat reconnection bits.
