# A coherent cycle-dimer growth fan forces a universal one-extension four-set

**Workspace:** D17
**State:** established
**Key:** `compatible-forest-coherent-cycle-dimer-fan-extinction`

**Summary:** Assume a tight cycle Q, a dimer D={x,y}, and a third rail V lie in the movable-break maximum-three-forest setting, and suppose the SV28505 coherent branch holds, say every rim vertex grows as (q_i,x,y)|(Q-q_i)|V, with no singleton-producing SLIDE. Then at each rim edge the opposite paired seed x->q_{i-1} using the reversed dimer (y,x) cannot be a non-singleton SLIDE because coherence gives (q_{i-1},x,y) tight, and by hypothesis it is not a singleton SLIDE; hence it is DOUBLE. The original growth seed has bad rim-side seam, so R3 gives (x,q_i,q_{i-1}); the opposite DOUBLE gives (q_i,q_{i-1},x). If the third cyclic turn (q_{i-1},x,q_i) is tight for some i, those three turns form an ordinary comparison triangle, so R902 makes a four-set containing it universally one-extendable. If every such third turn is bad, R3 gives (q_i,x,q_{i-1}) for all i, so the spokes xq_i form a directed comparison cycle in the tournament of edges incident with x; every cyclic tournament contains a directed triangle, yielding a star comparison triangle and again a universal one-extension four-set by R902. Thus the coherent fan cannot survive without exporting to the universal-core holonomy branch. The reverse coherent orientation is dual. Consequently the full cycle+dimer analysis now reduces to universal one-extension core or singleton-producing SLIDE.

### 1. Coherent fan setup
Let H be a Strong Level-(1) boundary tournament with pc(H)=3. Retain a literal maximum spanning three-forest

  Q | D | V,

where Q is the support of a literal tight cycle with cyclic vertices q_i, D={x,y} is a dimer rail, and V is a nonempty third rail. Assume every cyclic break of Q is available through the movable-break/CYCLE-ROTATE family.

Assume the coherent branch of SV28505 occurs in the orientation

  F_i=(Q-q_i) | (q_i,x,y) | V,             i in Z/rZ.   (CF.1)

Thus

  (q_i,x,y) tight for every i.                         (CF.2)

Also retain the defining hypothesis of that coherent branch that no singleton-producing SLIDE occurs at any paired rim edge. The reverse coherent orientation (y,x,q_i) is exactly dual.

### 2. The unused paired gate is DOUBLE everywhere
Fix a rim edge q_{i-1}q_i. The growth representative F_i came from the ordered seed q_i->x with D oriented (x,y). Since its non-singleton SLIDE branch occurs, its source-side turn is tight and rim-side turn bad:

  (q_i,x,y) tight,
  (q_{i-1},q_i,x) bad.                                (CF.3)

Hence R3 gives

  (x,q_i,q_{i-1}) tight.                              (CF.4)

Now inspect the opposite paired seed from SV28505: orient the same physical dimer as (y,x), use the cyclic break beginning q_{i-1}, and test

  x -> q_{i-1}.

Its two merge holes are

  alpha'_i=(y,x,q_{i-1}),
  beta'_i =(x,q_{i-1},q_i).                           (CF.5)

The non-singleton growth SLIDE on this opposite gate would require alpha'_i tight. But by coherence at index i-1, (q_{i-1},x,y) is tight, so exact reversal R3 makes

  alpha'_i=(y,x,q_{i-1}) bad.                         (CF.6)

Thus the opposite gate cannot be the non-singleton SLIDE. By the standing coherent-branch hypothesis it is not the singleton-producing SLIDE either. The exact SLIDE/DOUBLE dichotomy therefore forces this opposite gate to be DOUBLE. In particular beta'_i is bad, and R3 gives

  (q_i,q_{i-1},x) tight.                              (CF.7)

So for EVERY rim edge we have the two cyclic triangle turns (CF.4) and (CF.7).

### 3. One good third turn immediately gives the universal core
For a fixed i test the remaining cyclic turn on the physical triangle

  T_i={x,q_{i-1},q_i}:

  gamma_i=(q_{i-1},x,q_i).                            (CF.8)

If gamma_i is tight for some i, then

  (x,q_i,q_{i-1}),
  (q_i,q_{i-1},x),
  (q_{i-1},x,q_i)

are all tight. Equivalently the three ordinary edges of T_i form a directed comparison triangle.

Choose any fourth physical vertex d outside T_i; such a vertex exists in the present three-forest setting, for example y. Put

  S=T_i union {d}.

For every exterior vertex z outside S, the induced five-set S+z retains the directed comparison triangle on T_i, hence is nonintegrable. Accepted R902 therefore gives

  S+z Hamiltonian for every z outside S.              (CF.9)

Thus S is a universally one-extendable four-set, exactly the G10 small-core holonomy generator.

### 4. If every third turn is bad, the spoke tournament creates a star triangle
Assume instead that gamma_i is bad for every i. Boundary antisymmetry gives

  (q_i,x,q_{i-1}) tight for every i.                   (CF.10)

Let

  s_i={x,q_i}

be the ordinary spoke edge at x. The turn (CF.10) says precisely

  s_i -> s_{i-1}                                      (CF.11)

in the comparison orientation. Hence

  s_0,s_{r-1},s_{r-2},...,s_1,s_0

is a directed comparison cycle entirely inside the local tournament on ordinary edges incident with the common physical vertex x.

Every finite tournament containing a directed cycle contains a directed triangle: take a shortest directed cycle; if its length exceeds three, the chord between its first and third vertices shortens it in one of the two orientations. Therefore the spoke tournament contains a directed triangle

  s_a -> s_b -> s_c -> s_a.                           (CF.12)

This is a local star comparison triangle on the four physical vertices

  S={x,q_a,q_b,q_c}.

For every exterior z outside S, the five-set S+z retains the same directed comparison triangle and is therefore nonintegrable. R902 again yields

  S+z Hamiltonian for every z outside S.              (CF.13)

So S is universally one-extendable.

### 5. Coherent fan extinction
Both possibilities for the third turns produce a universally one-extendable four-set. Therefore the coherent family (CF.1) cannot remain a terminal cycle+dimer obstruction distinct from the universal-core branch.

Combining with SV28505 gives the sharpened global cycle+dimer trichotomy:

1. a paired DOUBLE already yields a universal Hamilton four-core by SV27921;
2. a singleton-producing SLIDE yields an explicit maximum three-forest with a singleton rail; or
3. the remaining coherent fan necessarily yields a universally one-extendable four-set by the present theorem.

Hence after identifying universal one-extension cores with their SV26947 holonomy destination, the only cycle+dimer output not yet exported to that destination is the singleton-producing SLIDE branch.

No claim is made here that the universal one-extension four-set itself closes H; under G10 it is exported to the pair-core cycle extinction problem. No static LOW/HIGH wall is used.
