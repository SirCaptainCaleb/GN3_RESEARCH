# Positive protection does not guarantee fixed-root corridor absorption

## Metadata

- ID: positive_protection_does_not_guarantee_fixed_root_corridor_absorption
- Parent Section: terminalization_reachability_and_the_exact_frontier
- Position: 45
- Row version: 2
- Development version: 2
- Composition version: None
- Composition stale: False

## Composition

(none yet)

## Development

This is a local obstruction to one prescribed-interface repair, not a counterexample to the global two-cover theorem.

Fix k>=2 and d>=6. Put a=k-1, b=a+d, n=a+b+3=2k+d+1, and m=n-2. Take the displayed order (t_1,...,t_k,x,y,z,...), with A={t_1,...,t_k}. Prescribe its status word to be
1^{k-2} 0 1^4 0^{d-3} 1 0^{k-2}.
Its only positive forbidden occurrences are 011 at start a and 001 at start b. In particular a+b=m-1, so they are the two reflected span-two occurrences of one unsigned witness edge. There is no strictly inward positive occurrence of 001,011, or 0101. The span between the two determining windows is unbounded as d increases.

In addition prescribe h(u,v,x)=0 for every distinct u,v in A, and h(t,x,y)=1 for every t in A. Set h(x,y,z)=1. These prescriptions are compatible with boundary antisymmetry h(p,q,r)=1-h(r,q,p): the first family has middle vertex in A and final x; its reversals have initial x. The second family has middle x and final y; its reversals have initial y. None of the families identifies a prescribed triple with its boundary reversal. The displayed status assignments agree with them: the last two A vertices followed by x have status 0, the last A vertex followed by x,y has status 1, and x,y,z has status 1. Assign all other displayed triples according to the word and complete the remaining boundary-reversal pairs arbitrarily.

Now freeze the corridor beginning (x,y,z,...), and allow an arbitrary reorder of all k vertices of A. If the reordered prefix ends (u,v), the three consecutive statuses at the interface are always
h(u,v,x), h(v,x,y), h(x,y,z) = 0,1,1.
Thus the selected positive 011 witness survives at exactly the same start a in every prefix reorder. No fixed-root repair confined to A can remove it. Also no tight path of at least three vertices contained in A union {x} can end at x, because its last triple would have status 0.

This obstruction already satisfies the positive protected-word conditions used by the corridor proposal; it is stronger than merely observing that an unoriented endpoint theorem does not supply a terminal endpoint. However it does not exclude a repair which moves x, changes the corridor boundary, repartitions across that boundary, or uses additional relations not implied by positive protection. Accordingly a rooted endpoint-surgery theorem must state its mutable vertex set and fixed interface explicitly. The implication 'positive protection plus a positive-word-free corridor implies absorption with its first root fixed' is false.

For scope, the corridor's displayed order is positive-word-free after the left occurrence, up to the far right occurrence, but its boundary root cannot automatically be used as a terminal vertex of a new tight path. Separately, [[positive_only_witness_filtration_is_antipodal_and_surgery_compatible]] correctly identifies the positive language as antipodal, but its assertion that every terminal support has order at most ten excludes this reflected-double branch without justification. The valid bounded claims concern the exclusive branches and the alternating double branch; see [[positive_reflected_double_carriers_have_unbounded_local_spans]] and [[positive_alternating_double_occurrences_have_support_at_most_eight]].

The same example is protected on an entire ordered-partition face: make A one freely permutable block and every subsequent vertex a singleton. Under every A-permutation, all statuses from a onward remain fixed. New span-two positive words wholly in the variable prefix start at most a-2 (start a-1 ends in the fixed zero at a), and are strictly farther outward. Any new alternating occurrence starts at most a-2: starts a-1 and a end respectively in the fixed 011 and begin with 011, so neither can be 0101. These alternating windows are also strictly farther outward than the span-two occurrence at a. Thus there is no inward positive witness in any chamber, and both reflected occurrences persist throughout this whole face. This strengthens the obstruction from a single protected chamber to a protected reflected-double face.

## Frontier

- Development version when composed: None
- Development version now: 2
