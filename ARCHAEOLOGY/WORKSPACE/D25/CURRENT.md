# D25 — Four-core replacement occupancy and substitute geometry

Focused four-core development: dense-hole replacement laws and their sharp countermodels, global-longest insertion blockers, common-substitute fibers, pair/triple replacement occupancy, aligned-swap reverse blockers, opposite-polarity swap geometry, and substitute-coordinate payment interfaces.

## Small-complement recycling, dense-hole columns, and sharp growth fences

R229 is the small-complement balanced-pair recycler. If a literal pair frame leaves a third rail of order at most three, R171 either decreases pair mass or swallows a support. The swallow corners are only `(2,3),(3,2),(3,3)`, so the untouched support sees a five- or six-vertex exterior and returns to the R192/R196 replacement gateways. This is a valid bridge between payment and exterior geometry.

R232 applies the `4/5` replacement law row-by-row. If a five-exterior replacement grid has m carrier rows, there are at least `4m` successful row-hole incidences; some fixed hole is therefore successful for at least `ceil(4m/5)` carrier vertices. R237 sharpens the elementary density: for m≥6, a column with at most `floor(m/5)` failures must contain three consecutive successful rows.

The local countermodels R233,R234,R238 are essential fences. R233 is an explicit eleven-vertex system attaining the `4/5` density sharply while all thirty obvious carrier swaps fail to make P6; it even contains a repeated signed dimer and a restoration/contact branch. R234 shows one hole can fail universally in every row while the other four always succeed, again without carrier P6. R238 gives a seven-vertex cell where a four-core and three successful core-plus-exterior P5s coexist with no P6. Hence row density, a dense fixed column, or even repeated collision data cannot be upgraded to carrier growth without a separate bridge.

R235 is the corresponding orientation fence: a reverse terminal dimer produced by endpoint shielding cannot simply be spliced into the forward orientation of the old carrier. R236 records the correct global-longest insertion clauses: every forbidden insertion position yields a finite reverse-turn disjunction, with two-way clauses at endpoints and three-way clauses internally.



## Four-core common substitutes and exact replacement occupancy

R240 is the key cross-replacement theorem. If two longest-five supports share a four-core S and have different completion vertices a,b, then for every `s∈S` the support `(S-s)+{a,b}` is a P5. Equivalently, once two completions of one four-core exist, the pair of completion vertices substitutes for any one core vertex. This gives `4*binom(r,2)` localized P5 supports when a four-core has r completion vertices.

R242 recasts the geometry as a common-substitute carrier fiber: fix the union U of the core and its completion set A. For each completion a, `K_a=U-a` is a global-longest carrier, U itself is non-Hamiltonian, and switching from K_a to K_b is exactly a one-vertex substitute operation.

R244 uses the repeated replacement rows to extract capture candidates. For a fixed frame/hole, successful completions are classified by one of six physical dimer classes; pigeonhole produces a repeated class, and an exact deletion frame can capture all but the two completion vertices adjacent to the selected crossing. The robust output is a **large indexed set of carrier vertices sharing one physical support class**, not simultaneous captures in one cover.

R245 adds a support cascade: pairs of completions generate the four cross P5s above, while triples of completions force at least two further core-pair-plus-three-completion P5s. The exact counts `4*binom(r,2)` and at least `2*binom(r,3)` are durable occupancy information.

R246 is the aligned-swap obstruction. Replacing a carrier vertex b by a substitute a inherits every old carrier turn except the at-most-three turns touching the insertion site; if the swap path is not tight, one of those new turns is bad and its exact reverse is a named blocker.

R247 treats the opposite case. If the aligned swap *is* tight, global longestness forbids inserting a and b consecutively in either order, so the physical swap dimer `{a,b}` acquires two opposite signed certificates. Pair it with the opposite terminal sign of an exterior trimer and use the balanced-pair/floor machinery. This is valid signed geometry, but its historical payment conclusion must respect the endpoint-selective floor theorem rather than pretend the swap path stays current.

R248 shows every exterior vertex can be chosen as a paid-floor coordinate by the same terminal-sign mechanism. It is a coordinate-selection theorem, not a simultaneous family of floors.



## Where the former capture and four-cell branches now live

The former capture-density and puncture sections are not discarded. R239/R241/R250 and the R251/R254/R256/R259/R261 failure genealogy, their capture-free repairs, and the original-frame puncture repairs are expanded in D15 with exact physical ancestry boundaries. The tested-order parity failures and corrected four-cell compiler R516/R517/R518/R519/R520/R521 are expanded in D27. R247/R248 remain here because their hypotheses are the specialized common-substitute/swap geometry; whenever they enter generic balanced-pair or floor descent, that generic descent is supplied by D16 rather than re-derived here.