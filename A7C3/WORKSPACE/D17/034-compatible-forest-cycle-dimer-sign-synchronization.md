# Absent a core or singleton SLIDE, a dimer synchronizes to one coherent growth orientation around the whole cycle

**Workspace:** D17
**State:** established
**Key:** `compatible-forest-cycle-dimer-sign-synchronization`

**Summary:** Let Q be a tight cycle rail and D={x,y} a dimer rail in a maximum three-forest, with every cyclic break available. Pair, at each rim edge q_{i-1}q_i, the seed q_i->x using D=(x,y) with the seed x->q_{i-1} using the freely reversed dimer (y,x). If both are DOUBLE, SV27921 gives a universally one-extendable four-set. If a non-DOUBLE gate takes the singleton-producing SLIDE branch, retain that actual singleton three-forest. Excluding both outcomes, define epsilon_i=1 iff (q_i,x,y) is tight. The remaining non-singleton SLIDE alternatives force epsilon_i=1 or epsilon_{i-1}=0 for every i. A cyclic binary word with no 1->0 transition is constant. Hence either every q_i grows onto the dimer as (q_i,x,y), or every q_i grows onto the reversed dimer as (y,x,q_i), yielding a full coherent cyclic fan of actual maximum three-forest representatives.

### 1. Paired gates along one rim edge
Let H have pc(H)=3 and retain a maximum spanning three-forest

  Q | D | V,

where Q is the support of a literal tight cycle with cyclic vertices q_i and D={x,y} is a dimer component. Because a dimer has no triple constraint, both orientations

  (x,y), (y,x)

are legitimate literal path components. Assume every cyclic break of Q is available, for example inside the augmented closed exchange class supplied by CYCLE-ROTATE.

Fix a rim edge q_{i-1}q_i. Use the break

  Q_i=(q_{i+1},...,q_i)

ending at q_i and orient D as (x,y). The ordered merge seed q_i->x has holes

  alpha_i=(q_{i-1},q_i,x),
  beta_i =(q_i,x,y).                                  (DS.1)

Use also the break

  Q^{i-1}=(q_{i-1},q_i,...,q_{i-2})

beginning at q_{i-1}, orient the same dimer as (y,x), and test the ordered seed x->q_{i-1}. Its holes are

  alpha'_i=(y,x,q_{i-1}),
  beta'_i =(x,q_{i-1},q_i).                           (DS.2)

If both paired seeds are DOUBLE, the paired-DOUBLE core section gives the universally one-extendable four-set {x,y,q_{i-1},q_i}. Thus, in the no-core branch, at least one of the two paired seeds is not DOUBLE.

### 2. Distinguish productive singleton SLIDEs from dimer-growth SLIDEs
For q_i->x, the SLIDE/DOUBLE calculus has two one-hole outcomes.

If alpha_i is tight and beta_i bad, the SLIDE is

  (Q_i,x) | (y) | V,                                  (DS.3)

which has singleton component y. Call this a singleton-producing SLIDE.

If beta_i is tight and alpha_i bad, the SLIDE is

  (Q_i-q_i) | (q_i,x,y) | V.                          (DS.4)

This grows q_i onto the dimer and keeps all three components nonempty without creating a singleton.

For the reversed-dimer seed x->q_{i-1}, the two outcomes are dual. If beta'_i is tight and alpha'_i bad, one gets the singleton-producing SLIDE

  (y) | (x,Q^{i-1}) | V.                              (DS.5)

If alpha'_i is tight and beta'_i bad, one gets the non-singleton dimer-growth SLIDE

  (y,x,q_{i-1}) | (Q^{i-1}-q_{i-1}) | V.              (DS.6)

No claim is made here that singleton-producing SLIDEs already close H. They are retained as an explicit alternative.

### 3. Binary sign around the cycle
Assume from now on that neither a universal four-core nor a singleton-producing SLIDE occurs at any paired rim edge. Define

  epsilon_i=1  iff  (q_i,x,y) is tight.                (DS.7)

By exact reversal R3,

  epsilon_{i-1}=0  iff  (y,x,q_{i-1}) is tight.        (DS.8)

At rim edge q_{i-1}q_i, at least one paired seed is non-DOUBLE. Under the no-singleton assumption, every non-DOUBLE seed must take its dimer-growth branch. Therefore either (DS.4) occurs, forcing epsilon_i=1, or (DS.6) occurs, forcing epsilon_{i-1}=0. Hence for every i,

  epsilon_i=1  OR  epsilon_{i-1}=0.                   (DS.9)

Equivalently, the cyclic word epsilon contains no directed transition 1->0.

A nonconstant cyclic binary word necessarily contains both a 0->1 and a 1->0 transition. Therefore (DS.9) forces epsilon to be constant.

### 4. Coherent cyclic growth fan
If epsilon_i=1 for every i, then beta_i is tight for every i. Since both merge holes cannot be tight in a graph with pc(H)>2, alpha_i is bad, so the non-singleton SLIDE (DS.4) is available for every i. Thus H carries the full family

  (Q-q_i) | (q_i,x,y) | V,        i in Z/rZ.           (DS.10)

Here Q-q_i denotes the inherited tight path obtained by deleting q_i from the cyclic order.

If epsilon_i=0 for every i, then by R3 every alpha'_{i+1}=(y,x,q_i) is tight. Again its partner beta'_{i+1} must be bad, so (DS.6) is available at every index. Hence H carries the reverse coherent family

  (y,x,q_i) | (Q-q_i) | V,        i in Z/rZ.           (DS.11)

Therefore a dimer rail interacting with a movable tight cycle has only three global outcomes in this paired-gate analysis:

1. a paired DOUBLE produces a universally one-extendable four-set;
2. a singleton-producing SLIDE gives an explicit maximum three-forest with singleton component; or
3. all rim vertices coherently grow onto the same oriented dimer, producing one of the cyclic fans (DS.10)-(DS.11).

This is a global synchronization statement, not a claim that the coherent fan already augments to two paths.
