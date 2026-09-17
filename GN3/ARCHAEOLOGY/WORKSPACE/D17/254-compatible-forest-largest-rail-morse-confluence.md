# Portal-free largest-rail Morse descent is confluent and has a unique literal terminal forest

**Workspace:** D17
**State:** established
**Key:** `compatible-forest-largest-rail-morse-confluence`

**Summary:** Mark a largest rail A in a literal maximum three-forest and use only the inward endpoint SLIDEs of SV40879, each of which transfers one endpoint vertex of another rail into A and strictly decreases d=n-|A|. The rewrite system is terminating. For two distinct available A-growth slides from the same state, apply the complete one-edge relation SV38940. If they target the same end of A, their added edges share the corresponding A endpoint copy, so the interaction is a current trimer portal rather than a square. If they target opposite ends, a SQUARE outcome is a genuine commuting A-growth diamond: when the donors are different, the untouched opposite gate survives literally after either move; when both slides use opposite ends of one donor of order at least three, deleting one donor endpoint leaves the other endpoint gate unchanged. If that donor has order two, the two slides share the unique donor edge deletion, so SV38940's common-deletion branch gives augmentation/trimer/cycle and cannot be a square. Therefore every portal-free critical pair of greedy A-growth rewrites is an exact square in the same rewrite relation. Since d decreases by one on every move, a direct induction on d gives a unique literal terminal normal form for every marked state: any two first moves square to a common lower state, whose normal form is unique by induction. Moreover any two greedy descent paths to the normal form are tiled by verified squares, so every square-coherent ancestry mark has path-independent transport to the terminal state. Thus SV40879 is not merely a terminating Morse descent: outside explicit trimer/cycle/augmentation portals it defines a canonical square-flat retraction of the marked maximum-three-forest space onto its terminal signed forests. The terminal opposite-end sign certificate is independent of all greedy slide choices.

### 1. Marked largest-rail rewrite system
Retain a literal maximum spanning three-forest

  F=A|B|C

and mark one rail A of maximum order, exactly as in SV40879. The marked physical descendant of A is retained through every move.

An A-GROWTH rewrite is one of the inward endpoint SLIDEs of SV40879: it transfers exactly one source or terminal vertex of B or C onto one end of A by the reversible one-edge SLIDE of SV22098. Thus every rewrite is a reversible support-changing one-edge transfer and

  |A| -> |A|+1,
  d(F,A)=|V(H)|-|A| -> d(F,A)-1.                         (MC.1)

The marked descendant remains a largest rail after every rewrite. Hence the oriented A-growth rewrite system is terminating.

The question is whether different choices of available greedy slides can lead to genuinely different terminal signed forests.

### 2. Critical pairs at one end of A are portals, not diamonds
Suppose two distinct available A-growth slides both enter the TAIL of A. Their added directed edges have the form

  a_r -> x,
  a_r -> y,                                               (MC.2)

with x!=y the two donor sources (or two distinct candidate physical endpoints). They share the same out-copy a_r,out. Thus their simultaneous replacement is not a bipartite matching. Section 4 of SV38940 applies: R3 on x,a_r,y gives a proper graph-intrinsic tight trimer, current by R4.

Dually, two distinct slides entering the HEAD of A add

  x -> a_0,
  y -> a_0,                                               (MC.3)

and compete for a_0,in, giving the same current-trimer portal.

Therefore a portal-free critical pair can only consist of one HEAD-growth and one TAIL-growth move.

### 3. Opposite-end slides in the SQUARE branch remain genuine A-growth slides after swapping
Take two available opposite-end rewrites s,t from the same marked state. Apply the complete pairwise one-edge theorem SV38940. Outside augmentation/current trimer/shared-cycle outputs, there is a verified fourth literal forest completing the exchange square. It remains to check that the two opposite sides of this square are still A-GROWTH rewrites, rather than merely abstract one-edge transfers.

First suppose s and t use different donor rails. A head-growth move changes only the head of A and one endpoint of its donor; a tail-growth move changes only the tail of A and one endpoint of the other donor. After either move, the physical endpoint and unique bad-root deletion used by the other SLIDE are literally untouched. Hence the other move remains the same inward endpoint SLIDE into the grown descendant of A. The verified SV38940 square is therefore an exact diamond in the oriented A-growth rewrite system.

Now suppose both moves use opposite endpoints of the SAME donor

  X=(x_0,...,x_m).                                       (MC.4)

A tail-growth uses x_0 and, when nontrivial, deletes x_0x_1. A head-growth uses x_m and deletes x_{m-1}x_m.

If |X|>=3, these boundary deletions are distinct. Performing the tail move leaves x_m and its head gate unchanged; performing the head move leaves x_0 and its tail gate unchanged. Thus a SQUARE outcome again consists of the same two literal A-growth slides in either order.

If |X|=2, both moves delete the unique donor edge x_0x_1. They are therefore in the COMMON-DELETION branch of SV38940. That branch has only augmentation, current trimer, or shared current cycle; it never has a square. If X is a singleton, SV40879 already shows neither inward gate is a legal slide in a counterexample: a successful merge would give a spanning two-cover.

Consequently:

  EVERY PORTAL-FREE CRITICAL PAIR OF A-GROWTH REWRITES
  COMPLETES TO A VERIFIED SQUARE OF A-GROWTH REWRITES.    (MC.5)

This is genuine local confluence with the distinguished physical rail preserved.

### 4. Termination plus the exact diamonds gives a unique terminal normal form
We prove uniqueness directly, without treating confluence as a black box.

For a marked state S=(F,A), let d(S)=n-|A|. If S has no A-growth rewrite, it is terminal. Suppose inductively that every state of deficit less than d has a unique terminal descendant whenever no portal is encountered in its reachable A-growth system.

Let S have two possible first rewrites

  S -> S_1,
  S -> S_2.                                              (MC.6)

If their critical pair emits augmentation/trimer/cycle, we have the advertised portal exit. Otherwise (MC.5) supplies a common square endpoint U with

  S_1 -> U,
  S_2 -> U,                                               (MC.7)

and d(U)=d(S)-2.

By induction, U has one terminal normal form N. Since S_1 and U lie in the same portal-free reachable system and d(S_1)<d(S), the unique terminal descendant of S_1 is N; likewise for S_2. Hence every possible first rewrite from S has the same terminal normal form. Induction proves:

  PORTAL-FREE A-GROWTH DESCENT HAS ONE UNIQUE LITERAL
  TERMINAL MARKED FOREST N_A(F).                          (MC.8)

In particular its final path words, support partition, physical descendant A*, and the two opposite-end sign certificates of SV40879 are independent of every greedy slide choice.

### 5. Any two descent histories are square-homotopic
The same induction records more than endpoint uniqueness. Given two A-growth descent paths from S to N_A(F), compare their first moves. If they agree, strip the common first edge. If they differ, use the verified square (MC.7) and then apply the induction below U. Repeating tiles the region between the two histories by actual SV38940 square cells.

Therefore every two portal-free greedy histories are related by a finite sequence of elementary square swaps and inverse cancellations. No triangle relation is needed because every A-growth move lowers d by exactly one, so serial compression would skip a Morse level.

This yields a canonical square-flat transport theorem. Let mu be ANY history-bearing datum carried along A-growth SLIDEs. If transport around each verified A-growth square is identity, then its value transported from (F,A) to N_A(F) is independent of the chosen greedy descent path.                                                        (MC.9)

Thus the marked A-growth complex is not merely terminating: its portal-free directed part retracts coherently onto one normal form.

### 6. Synthesis with the global Morse theorem
SV40879 says every terminal A-growth state either has already closed H or carries the exact two-ended signed geometry which is then paid, through the order-three rooted component-drop branch or the order-at-least-four mass-four branch, to a genuine ancestry-bearing both-singleton floor.

The present theorem makes the TERMINAL BIRTH STATE canonical before payment. Outside explicit augmentation/trimer/cycle critical-pair portals, the terminal forest F*=A*|B*|C*, both reverse boundary dimers of A*, all four source/terminal sign witnesses, and the branch |A*|=3 versus |A*|>=4 are independent of all choices made during greedy largest-rail growth.

So the remaining ambiguity in the global Morse program is pushed strictly downstream: it can live in the payment/floor continuation or in an explicit portal encountered by a critical pair, but not in wandering among greedy maximum-forest descents.

Equivalently, SV40879 plus SV38940 supplies a genuine abstract rewrite structure:

  strict integer Morse function + exact local diamonds
  => canonical terminal representative + square-flat ancestry transport. (MC.10)

This is the confluence form of the G15 exchange-structure moonshot. It does not yet consume the terminal paid singleton floor, nor the trimer/cycle portals which can appear when local confluence fails.