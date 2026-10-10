# Two-ended cap quadrants force support growth and majority-label the short maximal path

# Two-ended cap agreement forces used directions; short extremal paths determine local majority labels

Let n>=6 and c be an arbitrary binary coloring of actual ordered three-faces of Q_n. Let k<n be the global maximum length of a good direction-distinct path, where good means its ordered-three-face color word changes at most once. Fix such a P from x to y with direction word (alpha,beta,...,a,b), k>=5, initial color q and terminal color r=1−q. For each coordinate d outside the four distinct endpoint directions {alpha,beta,a,b}, define actual physical cap bits
 E(d)=c(F_y({a,b,d});(a,b,d)),
 I(d)=c(F_x({d,alpha,beta});(d,alpha,beta)).
These bits are defined for every such d, whether or not P traverses d. Let T be the unused-coordinate set of P, size m=n−k.

**Theorem 1 (two-ended cap-quadrant support forcing).** The unused set satisfies
 T ⊆ {d:E(d)=q AND I(d)=r}.
Consequently every d with E(d)=I(d) MUST belong to the direction support of P, and
 m <= |{d:E(d)=q,I(d)=1−q}|
   <= max_{t∈{0,1}} |{d:E(d)=t,I(d)=1−t}|.
In particular, if for EVERY pair of endpoints x,y, all ordered disjoint endpoint memories (alpha,beta),(a,b), and each t, the two-ended opposite cap quadrant has size at most B, then the coloring admits a good geodesic of length at least n−B. This is a dimension-independent deterministic sufficient lower bound based on genuine physical cap agreement.

**Proof.** The global maximal-good-path two-sided cap law gives, for each unused d, E(d)=q and I(d)=r. The two set inclusions and counting inequalities follow. If a maximum path has length n, the asserted n−B bound is immediate; otherwise its m is bounded by B as above. QED.

**Theorem 2 (strict-majority extraction below the half-dimension threshold).** If m>(n−2)/2, equivalently k<(n+2)/2, then the terminal cap star d↦c(F_y({a,b,d});(a,b,d)), indexed by ALL n−2 directions outside {a,b}, has a unique strict majority color q, equal to the INITIAL phase of P. The initial cap star d↦c(F_x({d,alpha,beta});(d,alpha,beta)), indexed by ALL n−2 directions outside {alpha,beta}, has a unique strict majority color r, equal to the TERMINAL phase. In particular these two locally computable strict-majority labels are OPPOSITE. For fixed y,(a,b), any globally longest good k-path terminating there has the same terminal phase 1−majority_end, regardless of its root, support or earlier order. A dual assertion holds at its initial ordered-pair hub.

**Proof.** Each cap star has n−2 possible directions, and all m missing directions contribute the same forced bit, q at the end and r at the beginning. Since m>(n−2)/2, that bit is the unique strict majority. Its relation to the two phases follows from r=1−q. The terminal majority depends only on the endpoint y and terminal ordered pair (a,b), so it gives an honest local endpoint-memory phase label. QED.

**Limit and next extraction condition.** This is a genuine support-growth estimate, but the hypotheses controlling opposed cap quadrants require independent verification in an arbitrary coloring. For unrestricted NORI the cap quadrant can be large, and the majority theorem applies only when the maximum support deficit exceeds half the available terminal cap directions. A topological closure route should force a real path whose initial and terminal majority labels violate their required opposition, or prove a uniform shrinking bound on the opposed cap quadrants via exchanged paths with verified root and end memories. Neither step is established by the local counting alone.
