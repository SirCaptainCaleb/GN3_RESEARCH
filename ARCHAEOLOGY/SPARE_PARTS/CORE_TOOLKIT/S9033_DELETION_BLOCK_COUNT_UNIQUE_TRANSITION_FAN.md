# S9033 — Deletion Block Count and Unique-Transition Witness Fan

## Theorem A — deletion block-count inequality

Let H be any finite directed tight-path system. Let V(H)=D disjoint-union S disjoint-union C, with S,C nonempty. Suppose A=A_1 sqcup ... sqcup A_a is a literal tight-path cover of H[D union S], and T=T_1 sqcup ... sqcup T_k is a literal tight-path cover of H-D=H[S union C]. Split every T-rail at each selected S|C transition and let b_C(T) be the total number of nonempty maximal contiguous C-blocks. Then pc(H) <= a+b_C(T). Equivalently b_C(T) >= pc(H)-a. In particular, if A is one tight path and pc(H)>k, then every k-rail cover T of H-D has b_C(T)>=k. If such a T has exactly one selected S|C transition, then it has the following canonical normal form: exactly one rail is mixed and consists of one S-block and one C-block, in either order; every other one of the k-1 rails lies wholly in C; hence all vertices of S occur in the unique S-block and there is no S-only rail. For `k=2` this gives the familiar two-rail crossing/block-count normal form, without Strong Level-(1) or any small-order hypothesis.

### Proof

Let T=T_1 sqcup ... sqcup T_k cover S union C. Split every T-rail at each selected S|C transition. The resulting maximal C-blocks are pairwise vertex-disjoint tight paths covering C, so there are b_C(T) of them. Together with the supplied a-path cover A of D union S, these C-blocks form a spanning path cover of H by a+b_C(T) paths. Hence pc(H)<=a+b_C(T), equivalently b_C(T)>=pc(H)-a. If a=1 and pc(H)>k, integrality gives pc(H)>=k+1, hence b_C(T)>=k.

Now assume T has exactly one selected S|C transition. Splitting all rails at that unique transition produces exactly k+1 monochromatic blocks in total. Since C is nonempty, b_C>=1; since S is nonempty, the number b_S of S-blocks is at least one. From b_C>=k and b_S+b_C=k+1 we obtain b_S<=1, hence b_S=1 and b_C=k. The unique transition lies on exactly one mixed rail, which therefore consists of the unique S-block adjacent to one C-block, in one of the two orders SC or CS. Every other rail is monochromatic. Because there is only one S-block total and it already lies on the mixed rail, every other rail lies wholly in C; in particular there is no S-only rail. This proves the stated block-count and one-transition normal form.

## Theorem B — unique transition inherits Hamilton boundary multiplicity

Let H be a finite exact-reversal tight-turn system with pc(H)>k. Partition V(H)=D disjoint-union S disjoint-union C with S,C nonempty, and suppose X=H[D union S] is Hamiltonian. Let T be a literal k-path cover of H-D having exactly one selected S|C transition. By Theorem A, T has one mixed rail and k-1 pure C-rails. (SC orientation.) Suppose the unique transition is the selected state x y with x in S and y in C. For every vertex p in (D union S)-{x} for which X has a Hamilton tight path ending with the ordered state (p,x), the turn (y,x,p) is tight. Hence the tested crossing dimer (y,x) is tail-signed by every such Hamilton predecessor p. In particular, two distinct Hamilton predecessors p_1,p_2 force a same-oriented two-tail witness collision on the actual selected crossing dimer (y,x). (CS orientation.) Dually, if the unique transition is y x with y in C and x in S, then for every p for which X has a Hamilton tight path starting with (x,p), the turn (p,x,y) is tight; thus the tested crossing dimer (x,y) is head-signed by every such Hamilton successor p, and two distinct successors force a same-oriented two-head witness collision. Therefore a unique recompletion transition converts Hamilton boundary multiplicity of the absorber into a role-sensitive witness fan on the literal selected crossing.

### Proof

Assume first that the unique selected transition is x y with x in S and y in C. By Theorem A, after relabelling T consists of one mixed rail A B, where A is the unique S-block ending at x and B is a nonempty C-block beginning at y, together with k-1 rails lying wholly in C. Let Q be any Hamilton tight path of H[D union S] ending with ordered state (p,x). Replace A in the mixed rail by Q, keep B in its literal T-order, and keep every other T-rail unchanged. The resulting k vertex-disjoint sequences cover all of H. Every turn is certified by Q, by T inside B and the other rails, and, if B has at least two vertices, by the original T turn beginning with the selected state xy, except possibly the single splice turn (p,x,y). If (p,x,y) were tight, these sequences would form a literal k-cover of H, contrary to pc(H)>k. Hence (p,x,y) is bad. Exact reversal antisymmetry gives (y,x,p) tight. Since p was arbitrary among Hamilton predecessors of x in H[D union S], every such p is a tail witness on the same tested crossing dimer (y,x); two distinct predecessors therefore give the `S9032` two-tail collision packet. For the dual orientation y x, Theorem A writes the mixed rail as B A with B ending at y and A beginning at x. Replace A by a Hamilton path Q starting (x,p). The only possible missing splice is (y,x,p), which must be bad, so boundary antisymmetry gives (p,x,y) tight. Thus every Hamilton successor p is a head witness on the same tested crossing dimer (x,y).

## Why this is reusable

The block-count theorem is a general deletion-cover accounting identity. In the unique-transition case, Hamilton boundary multiplicity on the absorbed side is forced onto the literal crossing dimer as a same-oriented witness fan. Together they form a compact recompletion interface.

## Scope and nonclaims

The first theorem applies to arbitrary directed tight-path systems. The witness-fan strengthening additionally needs exact reversal antisymmetry and `pc(H)>k`.

## Provenance

Rescued from accepted archived results `R560`, `R566`.
