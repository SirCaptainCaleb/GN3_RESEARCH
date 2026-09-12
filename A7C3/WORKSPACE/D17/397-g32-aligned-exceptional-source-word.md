# The sole aligned G32 exceptional residue has one three-vertex X block and only three or four B blocks

**Workspace:** D17
**State:** established
**Key:** `g32-aligned-exceptional-source-word`

**Summary:** After SV101535 eliminates the crossed exception, the only no-B-active-omission branch is aligned. Let the two B-active source spokes form the M_S edge complementary to the common endpoint gate, and let the complementary gate edge be {v,s}, where s is the unique B-inactive source spoke. Since s is internal in the retained source cover and has no B incidence, both selected neighbors of s lie in X. P4-freeness forces the source restriction to X to be exactly one three-vertex path with s as its middle plus one singleton X-block, so b_X=2. The exact source degree law then gives tau=b_B=2+d_F(v), hence exactly three or four source X|B transitions and B-blocks. The crossing degrees and contracted source words are completely determined by which of v or the two active spokes is the singleton X-block.

### 1. Sole surviving exceptional input
Retain SV100744 and SV101535. The crossed rigid residue is impossible, so the only branch in which no endpoint-favorable R582 path omits a B-active source spoke is ALIGNED. Write X={v,s,t,u}, where t,u are exactly the two B-active source spokes and form the M_S edge complementary to the common L/R gate edge, while {v,s} is the common gate M_S edge and s is the unique B-inactive source spoke. The retained exact source cover is F=U|V, and all three source spokes s,t,u are internal in F.

### 2. The inactive spoke determines the X-block structure
Because s is B-inactive and internal in F, both selected F-neighbors of s lie in X. Hence deg_{F[X]}(s)=2. The selected graph F[X] is a subgraph of the two-path forest F. If all four X vertices lay in one selected X-component, that component would be a spanning selected P4 on X, contradicting the retained P4-freeness of X. Therefore the component containing s has exactly three vertices, with s as its middle, and the fourth X vertex is a singleton X-block. Thus b_X=2. Write the actual three-vertex source block as (x,s,y), with {x,y} a two-element subset of {v,t,u}, and write z for the remaining singleton X vertex.

### 3. Exact crossing and B-block counts
Apply SV101138. Put d=d_F(v). Then d is 1 or 2 and

  tau = 2 b_X + d - 2 = 2+d,
  b_B = b_X + d = 2+d.

Hence d=1 gives exactly three X|B transitions and three B-blocks, while d=2 gives exactly four of each. No larger source-fragmentation family survives in the exceptional aligned branch.

### 4. Physical crossing degrees
Because s has no B incidence, every source crossing is incident with v,t,u. If the singleton X-block is v, the three-vertex block is the actual source trimer on t,s,u; t and u each have exactly one B incidence, while v has exactly d. If the singleton X-block is t, then t has exactly two B incidences, the three-block has support {v,s,u}, u has exactly one B incidence, and v has exactly d-1. The case with singleton u is dual. These account for all 2+d crossings.

### 5. Contracted source words
When d=1 the contracted X/B forest has five vertices and three edges. Therefore the two source rails have block types B-X3-B and B-v in the v-singleton case, or B-z-B and B-X3 in the active-singleton cases, up to rail reversal and exchange.

When d=2 the contracted forest has six vertices and four edges and both X-blocks have contracted degree two. Hence either the two source rails are separate B-X-B paths, or one source rail is the alternating path B-X-B-X-B and the other is the remaining pure B block. No other contracted source word is possible.

### 6. Scope
This is a finite source-word reduction, not absorption. It does not choose the physical B vertices at the three or four source crossings and does not yet consume the bad R582 endpoint-cut seam. Its purpose is to reduce the sole exceptional G32 branch to a bounded source word before the full-H splice. R24 and R5 are unused.
