# Square lifting closes the injective Hamiltonian endpoint-cycle branch

## Metadata

- ID: square_lifting_closes_the_injective_hamiltonian_endpoint_cycle_branch
- Parent Section: protected_root_certificates_and_cellular_extraction
- Position: 111
- Row version: 1
- Development version: 1
- Composition version: None
- Composition stale: False

## Composition

(none yet)

## Development

## Square lifting closes the injective Hamiltonian endpoint-cycle branch

Continue with the endpoint cycle
rho_i=e_{x_i}-e_{x_{i+1}},
C_i={x_i,a_i},
where the physical cycle x_0,...,x_{k-1} uses all coordinates in the ambient instance, the partner assignment is injective, and hence the partner set is the same coordinate set.

Assume the endpoint square-lift theorem in the witness-preserving form isolated in Subsection 93: every nondegenerate missing Johnson corner either is realized by a legal endpoint/deletion witness for the same physical root or yields a full-support one-change order / strict protected improvement.

Subsection 108 shows that after finitely many Q-decreasing square commutations, an unresolved witness-realized assignment has synchronized form
a_i=x_{i+r}
for one fixed displacement r in {2,...,k-1}.

### Uniform offset transport

For a synchronized assignment of displacement r<=k-2, the missing corner at step i is
M_i={x_i,a_{i+1}}
={x_i,x_{i+r+1}}.

The two coordinates are distinct and x_{i+r+1} is neither x_i nor x_{i+1}, because r+1 lies in {3,...,k-1}. Thus this is a nondegenerate Johnson square.

If square lifting does not already solve/improve the instance, M_i is realized by an endpoint witness for the SAME physical root
rho_i=e_{x_i}-e_{x_{i+1}}
with new partner
a_i'=a_{i+1}=x_{i+r+1}.

Endpoint witnesses for different omitted coordinates are independent choices. Hence after realizing all k missing corners we may choose, for each x_i, the new witness supplied at step i. The physical cycle is unchanged and the new partner assignment is synchronized with displacement r+1.

Therefore an unresolved synchronized cycle of offset r can be transported uniformly to offset r+1.

Iterating gives an unresolved synchronized assignment with
r=k-1,
namely
a_i=x_{i-1}
for every i.

### The predecessor-core endpoint pattern is impossible on a Hamiltonian physical cycle

For the witness omitting x_i, write its normalized beginning as
O_i=(a_i,b_i,c_i,...)
=(x_{i-1},b_i,x_{i+1},...),
because c_i=x_{i+1} is exactly the endpoint-root successor.

Prepending x_i gives the established fully-curved endpoint 10 barrier on
(x_i,x_{i-1},b_i,x_{i+1}).

For a 10 transition on an ordered quadruple (u,v,w,z), full curvature means in particular that the last-pair endpoint repair fails. The flat last-pair repair would require
alpha(u,v,z)=alpha(u,v,w)=1.
Since here alpha(x_i,x_{i-1},b_i)=1, failure forces
alpha(x_i,x_{i-1},x_{i+1})=0.

By alternation, swapping the first two coordinates complements the color:
alpha(x_{i-1},x_i,x_{i+1})=1.

This holds for every i.

Now use the Hamiltonian physical-cycle order
(x_0,x_1,...,x_{k-1}).
Every ternary window of this full order is one of
(x_i,x_{i+1},x_{i+2}),
and the preceding identity with index i+1 gives
alpha(x_i,x_{i+1},x_{i+2})=1.

Hence the full-support order has monochromatic word
1,1,...,1,
which is stronger than the required one-change order and contradicts counterexamplehood.

### Theorem

Assuming witness-preserving endpoint square lifting (with strict improvement as the failure alternative), no minimum counterexample can contain an injective Hamiltonian endpoint-root cycle.

The proof is finite and constructive:
1. bubble-sort partner displacements by the Q potential to one synchronized offset;
2. uniformly lift the Johnson squares to advance that offset to the predecessor shift;
3. read the endpoint full-curvature equations, which turn the physical Hamiltonian cycle order into a monochromatic full-support order.

Thus the square-lift lemma, if proved, closes the entire injective Hamiltonian branch rather than merely producing partner alignment.

The remaining endpoint branches are genuinely different:
- physical root cycles whose support is proper in the ambient coordinate set;
- noninjective partner assignments / repeated partners;
- failure of a required square lift, which by the desired lemma must itself yield the strict witness improvement.

## Frontier

- Development version when composed: None
- Development version now: 1
