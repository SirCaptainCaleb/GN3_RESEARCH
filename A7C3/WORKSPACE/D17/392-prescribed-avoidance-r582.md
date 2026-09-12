# R582 can omit a nonprescribed vertex

**Workspace:** D17
**State:** established
**Key:** `prescribed-avoidance-r582`

**Summary:** In the pure six-vertex R582 gate setup, fix any prescribed vertex w of the transitive matching-height four-cell X. Then some endpoint-favorable Hamilton P5 on {L,R} union (X-{s}) omits a vertex s distinct from w. The proof is an explicit refinement of P660: after normalizing the L-outgoing middle gate to {b,z}, assume no endpoint-favorable P5 omits a nonprescribed vertex. In the aligned gate case, one four-step forcing chain using only paths omitting b gives a contradiction whenever w!=b; a symmetric four-step chain using only paths omitting z handles w=b. In the crossed case, four short chains handle w=a,b,c,z, each using only paths whose omitted label differs from w. Every step has two already-tight consecutive turns; forbidding that endpoint-favorable P5 forces the third turn bad and R3 supplies its reverse. Thus the finite-search evidence in G32 is converted into a reconstructible proof. In the singleton-star application with prescribed center v, the omitted vertex is necessarily one of the source spokes p,q,r.


### 1. Statement and normalization
Let

  X={a,b,c,z}

be a transitive matching-height P4-free four-cell with

  M_R={ab,cz} > M_S={ac,bz} > M_L={bc,az}.

Let L,R be exterior vertices satisfying the R582 middle-gate hypotheses. Normalize exactly as in P660 so that the L-outgoing M_S edge is {b,z}; hence

  Lbz, Lzb, acL, caL

are tight. The matching-height rule supplies every X-only turn used below, in particular

  abc, abz, acb, bac, baz, bza, caz, cza, czb, zbc, zca, zcb.

Fix a prescribed vertex w in X. Call a Hamilton P5 on {L,R} union (X-{s}) admissible when s!=w. The claim is that some admissible P5 is endpoint-favorable in the sense of R582.

Assume contrariwise that every endpoint-favorable admissible P5 fails. Every displayed candidate below is endpoint-favorable and omits a nonprescribed vertex. Whenever two of its three consecutive turns are already tight, its remaining turn must be bad; R3 therefore makes the complete reverse tight.

### 2. Aligned gate
Assume the R-incoming M_S edge is also {b,z}, so

  bzR, zbR, Rac, Rca

are tight.

#### 2a. Prescribed vertex w!=b
All five candidates below omit b, so all are admissible.

1. `L R c a z`: Rca and caz are tight, so LRc is bad and

   cRL

   is tight.

2. `z c a L R`: zca and caL are tight, so aLR is bad and

   RLa

   is tight.

3. `z c R L a`: cRL and RLa are tight, so zcR is bad and

   Rcz

   is tight.

4. `R c z a L`: Rcz and cza are tight, so zaL is bad and

   Laz

   is tight.

Now `c R L a z` has cRL, RLa, Laz all tight. It is endpoint-favorable because R is in position 1, and it omits b. Contradiction.

#### 2b. Prescribed vertex w=b
Use only candidates omitting z.

1. `L R a c b`: Rac and acb are tight, so LRa is bad and

   aRL

   is tight.

2. `b a c L R`: bac and acL are tight, so cLR is bad and

   RLc

   is tight.

3. `b a R L c`: aRL and RLc are tight, so baR is bad and

   Rab

   is tight.

4. `R a b c L`: Rab and abc are tight, so bcL is bad and

   Lcb

   is tight.

Then `a R L c b` is a tight Hamilton P5, endpoint-favorable because R is in position 1, and it omits z!=b. Contradiction.

Thus the prescribed-avoidance conclusion holds in the aligned gate.

### 3. Crossed gate
Assume instead that the R-incoming M_S edge is {a,c}, so

  acR, caR, Rbz, Rzb

are tight.

#### 3a. Prescribed vertex w=a
The first three candidates omit c and the final one omits b.

1. `L R b z a`: Rbz and bza are tight, so LRb is bad and bRL is tight.
2. `R b z a L`: Rbz and bza are tight, so zaL is bad and Laz is tight.
3. `b R L a z`: bRL and Laz are tight, so RLa is bad and aLR is tight.

But `z c a L R` has zca, caL, aLR tight; it is endpoint-favorable and omits b!=a. Contradiction.

#### 3b. Prescribed vertex w=b
Use omissions a,z,a and finish with omission a:

1. `L R z b c`: Rzb and zbc are tight, so LRz is bad and zRL is tight.
2. `b a c L R`: bac and acL are tight, so cLR is bad and RLc is tight.
3. `R z b c L`: Rzb and zbc are tight, so bcL is bad and Lcb is tight.

Then `z R L c b` is tight, endpoint-favorable because R is in position 1, and omits a!=b. Contradiction.

#### 3c. Prescribed vertex w=c
Exactly the same chain as in 3b is admissible: its omitted labels are only a and z. Hence `z R L c b` again gives the contradiction.

#### 3d. Prescribed vertex w=z
Use only candidates omitting b until the final contradiction, which omits a:

1. `R z c a L`: zca and caL are tight, so Rzc is bad and czR is tight.
2. `z c a L R`: zca and caL are tight, so aLR is bad and RLa is tight.
3. `c z R L a`: czR and RLa are tight, so zRL is bad and LRz is tight.

Now `L R z b c` has LRz, Rzb, zbc tight; it is endpoint-favorable and omits a!=z. Contradiction.

Thus the prescribed-avoidance conclusion also holds in the crossed gate.

### 4. Consequence for G32
For every prescribed w in X, some endpoint-favorable Hamilton P5

  K_s on {L,R} union (X-{s})

has s!=w. In the live singleton-star frame take w=v, the singleton center. Since X={v,p,q,r}, the omitted vertex s is one of the genuine source spokes p,q,r. Therefore the source trimer (a,s,c) survives as the exact omitted-spoke anchor required by the second G32 moonshot.

### 5. Scope
This is a pure six-vertex strengthening of R582. It uses only exact reversal R3 and the normalized transitive matching-height/gate data. It does not use the finite falsification search as proof, does not invoke R540, and does not itself build the full-H splice. R24 and R5 are unused.


## References

```json
[
    {
        "relation": "dependency",
        "revision_id": "R3"
    }
]
```
