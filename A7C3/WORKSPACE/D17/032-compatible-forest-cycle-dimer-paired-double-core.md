# A paired DOUBLE trap between a tight cycle edge and a dimer rail is already a universal Hamilton four-core

**Workspace:** D17
**State:** established
**Key:** `compatible-forest-cycle-dimer-paired-double-core`

**Summary:** Let Q be a proper tight cycle occurring as one rail of a maximum three-cover together with a dimer D={x,y} and a third rail. Fix a rim edge q_{i-1}q_i. Orient D as (x,y) and use the Q break ending at q_i; if q_i->x is DOUBLE, its reverse P4 is (y,x,q_i,q_{i-1}). Reverse the dimer freely to (y,x) and use the Q break beginning (q_{i-1},q_i); if x->q_{i-1} is DOUBLE, its reverse P4 is (q_i,q_{i-1},x,y). These are Hamilton paths on the same four-set X={x,y,q_{i-1},q_i}; the first begins with (y,x) and the second ends with the reversed boundary dimer (x,y). Accepted R561 therefore makes X universally one-vertex Hamilton-extendable, and X itself is Hamiltonian. Consequently for each such paired cycle-edge/dimer gate, either at least one gate is a reversible SLIDE or the four-set is exactly a universal Hamilton four-core. This is an order-free short-rail realization of the G9 small-core/representative-switch parent.

### 1. Cycle-edge / dimer setup
Let H be a Strong Level-(1) boundary tournament with pc(H)>2. Suppose a literal maximum three-cover has a proper tight-cycle support Q, a dimer rail D={x,y}, and a third nonempty rail V. Fix a cyclic orientation

  Q=(...,q_{i-1},q_i,...)

and one physical rim edge {q_{i-1},q_i}. Because Q is a tight cycle, it has both a Hamilton break ending

  Q^-_i=(...,q_{i-1},q_i)

and a Hamilton break beginning

  Q^+_i=(q_{i-1},q_i,...).

The dimer D may be oriented freely as either (x,y) or (y,x), because a two-vertex path has no turn constraint.

### 2. First DOUBLE gives a P4 beginning with the reversed dimer
Orient D as

  D^+=(x,y).

In the three-cover Q^-_i | D^+ | V, test the ordered merge seed

  q_i -> x.

Its two merge turns are

  (q_{i-1},q_i,x),
  (q_i,x,y).                                             (CD.1)

If the seed is DOUBLE, both turns in (CD.1) are bad. Boundary antisymmetry R3 gives

  (x,q_i,q_{i-1}) tight,
  (y,x,q_i) tight,

so

  P_start=(y,x,q_i,q_{i-1})                              (CD.2)

is a literal Hamilton P4 on

  X={x,y,q_{i-1},q_i}.

In particular P_start begins with the ordered dimer (y,x).

### 3. Opposite-direction DOUBLE gives the reverse boundary ending on the same support
Now orient the same physical dimer in the opposite direction

  D^-=(y,x)

and use the cyclic break Q^+_i beginning (q_{i-1},q_i). Test the ordered merge seed

  x -> q_{i-1}.

Its merge turns are

  (y,x,q_{i-1}),
  (x,q_{i-1},q_i).                                      (CD.3)

If this seed is DOUBLE, R3 reverses both failures to

  (q_{i-1},x,y) tight,
  (q_i,q_{i-1},x) tight.

Hence

  P_end=(q_i,q_{i-1},x,y)                                (CD.4)

is a second Hamilton P4 on the SAME support X. It ends with the ordered dimer (x,y), which is the complete reverse of the initial dimer (y,x) of P_start.

### 4. R561 produces the Director small core
Apply accepted R561 to X with boundary dimer

  (u,v)=(y,x).

P_start begins with (y,x), while P_end ends with (x,y)=(v,u). Therefore every vertex d outside X Hamilton-extends X. Explicitly, exact reversal decides between prepending d to P_start and appending d to P_end.

Thus

  X is Hamiltonian,
  X+d is Hamiltonian for every d outside X.              (CD.5)

So X is not merely a universal one-extension four-set: it is a universal HAMILTON four-core.

### 5. Exact paired-gate dichotomy
Because H has no spanning two-cover, neither complete merge window can have both turns tight. Therefore each tested gate above is either SLIDE or DOUBLE by the exact SLIDE/DOUBLE classification SV22098.

Consequently for every rim edge {q_{i-1},q_i} and every choice of one dimer endpoint x as the common tested endpoint, exactly one of the following parent-scale outcomes occurs:

1. at least one of the two opposite-direction gates q_i->x or x->q_{i-1} is a reversible SLIDE, hence an actual maximum-three-forest representative switch; or
2. both gates are DOUBLE, and X={x,y,q_{i-1},q_i} is the universal Hamilton four-core (CD.5).

This uses no shortest-holonomy hypothesis. It needs only the movable-break family supplied by a proper tight cycle and the free reversal of the dimer rail. In a terminal exchange class closed under the relevant SLIDEs, a dimer rail therefore cannot be statically trapped against a cycle edge without producing the exact small-core object singled out by G9.

No claim is made that a SLIDE preserves the dimer as a separate rail, or that repeated SLIDEs terminate.
