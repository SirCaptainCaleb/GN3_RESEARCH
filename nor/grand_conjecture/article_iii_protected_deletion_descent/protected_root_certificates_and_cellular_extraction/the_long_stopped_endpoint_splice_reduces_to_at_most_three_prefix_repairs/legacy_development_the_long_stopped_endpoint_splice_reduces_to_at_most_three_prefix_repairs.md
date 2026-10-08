# The long stopped endpoint splice reduces to at most three prefix repairs — preserved pre-item development

Work in the long stopped endpoint branch of root §128. Thus
O_x=(a,b,c,d,e,...)
is a good deletion witness omitting x with word 0^p1^q, p>=4, the first splice bit
lambda=alpha(a,c,d)=1,
and the second splice bit
mu=alpha(a,d,e)=1.

Use the full order
F=(x,b,a,c,d,e,...)
from §128 and delete c. The resulting deletion order
O_c=(x,b,a,d,e,...)
omits c and has exact word
0,0,1,0^(p-3),1^q.

Compare this word with the ORIGINAL threshold target 0^p1^q. Every rank agrees except rank 3:
- ranks 1,2 are 0 as required;
- rank 3 is 1 instead of 0;
- ranks 4,...,p are the untouched old zero phase;
- ranks p+1 onward are the untouched old one phase.

Hence O_c is a fixed-omission deletion state with threshold defect count exactly one.

Let B be the maximal target-compatible interval containing the true switch between ranks p and p+1. Initially B contains every rank from 4 through the final window. Its only mismatch is immediately to the left at rank 3.

Apply the audited threshold-band boundary theorem. Whenever the left boundary mismatch is supported by a flat transition tetrahedron, the outward endpoint repair preserves every rank already in B and strictly extends B one rank to the left. All changed windows lie farther left.

Therefore there can be at most three such strict extensions before the band reaches the global left endpoint. The process has only two terminal outcomes:

1. B reaches rank 1. Then every window agrees with 0^p1^q, so O_c itself has been transformed into a genuine one-change deletion witness, still omitting c and retaining the entire untouched suffix beyond the repaired prefix.

2. Before reaching rank 1, the current left boundary transition is fully curved. Then it emits a protected physical root. Because the initial mismatch was rank 3 and every repair moves the boundary left, this terminal root is supported entirely in the bounded initial packet of O_c; in the original coordinates it uses at most the first six displayed coordinates x,b,a,d,e,f. The entire suffix beyond that packet and the omitted coordinate c remain fixed provenance.

Thus the unresolved long splice branch lambda=mu=1 is NOT an unbounded transport problem. It reduces in at most three certified band moves to either a new good deletion witness or a bounded-prefix fully-curved root with fixed omission and fixed outside suffix.

For p=3 the same construction is already a good deletion witness with a shorter first phase, as in §128. Hence every stopped endpoint pivot has a finite witness-preserving local handoff.

The remaining task is extraction of the bounded-prefix full barrier into the endpoint/corner-lift class or a strict deletion-witness improvement. This is now a six-coordinate local problem with all outer provenance frozen, rather than an arbitrary long-phase scan.
