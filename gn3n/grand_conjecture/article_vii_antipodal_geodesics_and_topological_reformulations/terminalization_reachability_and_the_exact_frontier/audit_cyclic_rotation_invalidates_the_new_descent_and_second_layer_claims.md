# Audit: cyclic rotation invalidates the new descent and second-layer claims

## Composition

(none yet)

## Development

## Audit: cyclic rotations do not preserve tightness in a boundary tournament

This audit concerns development version 1 of
[[order_two_complementary_paths_force_strict_descent_or_an_order_twelve_cap]]
and
[[same_tail_anchor_cores_force_valid_second_layer_reversal]].

Both use the implication
h(s_2,s_1,u)=1 implies h(s_1,u,s_2)=1,
explicitly attributed to cyclic invariance. This implication is false for the project's boundary 3-tournaments. The axiom is only
h(x,y,z)+h(z,y,x)=1.
The middle label is unchanged by this boundary flip. Triples having different middle labels belong to independently assignable reversal orbits. The Dictionary explicitly states that cyclic rotation has no implied status.

### Explicit local counterexample, including noninsertability

Take a tight path S=(s_1,s_2,s_3,s_4) and two distinct exterior labels u,v. For each w in {u,v}, prescribe
h(s_2,s_1,w)=1,
h(s_i,w,s_{i+1})=0 for i=1,2,3,
h(s_3,s_4,w)=0,
h(w,s_2,s_3)=1.

Set h(s_1,s_2,s_3)=h(s_2,s_3,s_4)=1. All displayed prescriptions lie in distinct boundary-reversal orbits, apart from identities obtained by their required flips, so they extend to a boundary tournament.

Each w is individually noninsertable into the displayed S:
- prepending w fails because h(w,s_1,s_2)=0, the flip of its prescribed hook;
- insertion into any internal gap s_i|s_{i+1} fails at h(s_i,w,s_{i+1})=0;
- appending w fails at h(s_3,s_4,w)=0.

Nevertheless
h(s_1,w,s_2)=0
and
h(s_3,s_2,w)=0
for both exterior labels. Thus both the asserted cyclic conversion and the claimed existence of an exterior label giving the initial second-layer reversal fail under the stated tight-path, hook, and individual-noninsertability hypotheses.

The same four-set can even be made Hamiltonian: additionally prescribe
h(s_1,s_2,u)=1 and h(s_2,u,v)=1.
These are fresh reversal orbits, so (s_1,s_2,u,v) is a tight four-path on {s_1,s_2,u,v}. Unspecified Hamiltonicity of the four-set therefore does not repair the missing canonical order.

This is a local counterexample to those implications, not a claimed maximal-support counterexample to the grand theorem.

### What remains valid

If h(s_1,u,s_2)=1 is independently established and u is noninsertable into S, then h(u,s_2,s_3)=0 follows: otherwise inserting u into the first gap would produce a tight path. Boundary antisymmetry then gives h(s_3,s_2,u)=1. This conditional second-layer argument is sound. Its required first tight triple cannot be obtained by cyclically rotating the hook.

Likewise, if the four-set {s_1,s_2,p_1,p_2} is independently known to be Hamiltonian, the displayed repartition with the untouched suffix of S and the quadratic-potential calculation 16-4k remain valid. The cited hook relations alone do not establish that Hamiltonian four-set by the proposed parallel-middle argument. Any simultaneous maximal-support and minimum-potential choice also needs its own justified quantifiers.

### Repair obligation

For the order-twelve claim, establish the Hamiltonian four-support through a valid boundary-tournament argument, then justify the extremal choice used for descent. For the second-layer claim, establish an appropriate rooted Hamilton order or the individual tight triple h(s_1,u,s_2)=1. Neither repair may assume cyclic invariance.

The exact five/six-label carrier results in the neighboring addenda use only the actual boundary flip and are independent of these two claims.
