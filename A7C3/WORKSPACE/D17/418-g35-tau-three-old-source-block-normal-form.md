# Every tau-three old source cover has one source-only internal X-block with two source gates

**Workspace:** D17
**State:** established
**Key:** `g35-tau-three-old-source-block-normal-form`

**Summary:** When tau(F)=3, SV101138 forces b_X=2,b_B=3,d_F(v)=1 and e_XX=2. Contracting maximal X/B blocks gives five block vertices in two alternating path components with three edges. The only block-shape possibilities are a four-block alternating rail plus an isolated B-block, or a B-X-B rail plus a two-block B-X rail (up to reversal). In either shape there is exactly one endpoint X-block and exactly one internal X-block bracketed by B blocks. Because p,q,r are physically internal in F, the physical outer endpoint of the endpoint X-block must be v; hence the internal X-block contains only source spokes. Its two block-boundary selected edges are therefore source-spoke-to-B transitions. Thus every tau-three hard packet has two distinguished source gates bounding one literal tight source-only X-block; the third transition is the sole boundary of the v-containing endpoint X-block and is source-bearing unless that block is the singleton {v}.

### 1. Exact tau-three counts
Retain the singleton-star old source cover

  F=U|V

on G=X union B, with X={v,p,q,r}, and suppose

  tau(F)=3.                                                (BN.1)

The exact degree law SV101138 gives

  tau=2b_X+d_F(v)-2,
  b_B=b_X+d_F(v),
  d_F(v) in {1,2}.

Hence (BN.1) has the unique solution

  b_X=2,  b_B=3,  d_F(v)=1.                               (BN.2)

Also e_XX=4-b_X=2, so the selected F-subgraph on X has exactly two edges and two path components.

### 2. The contracted two-rail word has only two shapes
Contract every maximal nonempty X-block and B-block of the two F-rails. The result is a two-component path forest with

  two X-block vertices, three B-block vertices,
  and exactly three X|B edges.                              (BN.3)

Because each contracted rail alternates block types, the five block vertices can be distributed between the two rails only as follows, up to reversing either rail and exchanging the two rails:

1. FOUR-PLUS-ONE: one rail is

     B-X-B-X

   (or its reversal X-B-X-B), while the other rail is one isolated B-block; or

2. THREE-PLUS-TWO: one rail is

     B-X-B,

   while the other is B-X (or X-B).

Indeed a 1+4 block-count distribution forces the isolated block to be B by the global counts 2X+3B; a 2+3 distribution then forces the three-block word to use two B-blocks and one X-block, hence B-X-B. There are no other alternating two-path words with these block counts.

Thus in every case there is exactly one X-block which is a contracted rail endpoint and exactly one X-block which is internal between two B-blocks. Call them

  E_X  and  I_X,                                           (BN.4)

respectively.

### 3. The endpoint X-block is the v-block
The physical outer endpoint of the F-rail containing E_X is also a physical endpoint of the tight X-subpath E_X. But all three source spokes p,q,r are retained as internal physical vertices of the old source cover. Therefore that outer endpoint cannot be p,q,or r. The only remaining X-vertex is v. Hence

  v belongs to E_X and is its physical outer rail endpoint. (BN.5)

In particular v does not belong to I_X. Therefore

  I_X is a nonempty tight path consisting entirely of
  source spokes from {p,q,r}.                               (BN.6)

### 4. The internal source block has two literal source gates
By definition I_X is bracketed by B-blocks on its F-rail. Therefore the two selected block-boundary edges incident with I_X are X|B transitions. Since every vertex of I_X is a source spoke, both transitions are source-spoke-to-B incidences.

If |I_X|=1, its unique source spoke uses both selected degrees on the two B gates. If |I_X|>=2, the two physical endpoints of the tight source path I_X are distinct source spokes and each is B-active through its adjacent boundary edge. Thus every tau-three old source cover contains two distinguished physical source gates

  B_left -- I_X -- B_right.                                (BN.7)

The third old transition is the unique B-boundary edge of E_X. It is incident with a source spoke when |E_X|>=2; only when E_X=(v) is it the unique v-B transition.

### 5. Hard-cell consequence
In the parity-hard G35 cell w(C_*)=2, the unique augmenter C_* contains at least two of the three old F transitions. Since at most one old transition can lie outside C_*, at least one of the two source gates in (BN.7) belongs to C_*. Combined with SV112110/SV112527, one of the low-transition corridor boundaries is source-bearing; the present normal form identifies what that source edge physically is: a gate of the single internal source-only X-block of F.

Thus the remaining source-bearing blocker is attached to a literal old block boundary, not to an arbitrary source incidence. The retained old source path order inside I_X and the historical trimers (A,t,C) for every t in I_X are available to the next consumer.

### 6. Scope
This is a static support-word normal form. It does not assert that I_X itself is the moving defect component, does not expose its endpoints in a new cover, and does not by itself splice A,C into the corridor. It records the exact old physical geometry forced in the sole tau-three hard regime. No R24, R5, payment, replay, computation, or seam taxonomy is used.
