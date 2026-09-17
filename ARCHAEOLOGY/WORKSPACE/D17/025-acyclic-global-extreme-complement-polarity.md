# Disjoint global extremes polarize every nontrivial complement two-cover

**Workspace:** D17
**State:** established
**Key:** `acyclic-global-extreme-complement-polarity`

**Summary:** In a minimum R888 counterexample with disjoint global minimum edge m0m1 and global maximum edge M0M1, let S be their four endpoints and U|V any exact two-cover of G-S. For a nontrivial rail R, define MIN-source activity when some minimum-edge endpoint can precede R, and MAX-terminal activity when R can precede some maximum-edge endpoint. One rail cannot have both activities, since m-pair | R | M-pair would become one increasing path and the other rail would close G. Combining this same-rail exclusion with accepted R1001's two crossed exclusions yields a whole-cover dichotomy: if U,V are nontrivial, either both sources are shielded from the minimum pair or both terminals are shielded from the maximum pair. If one rail is a singleton z, then S+z must be non-Hamiltonian, forcing the exact 2x2 spoke inversion zM_k < zm_h for every h,k. Thus the extreme four-set reduces arbitrary complement covers to a global SOURCE-shield / TERMINAL-shield polarity or a rigid singleton inversion cell.

### 1. Extreme four-set and endpoint activities
Let G be a minimum-order counterexample to R888. Let

  m={m_0,m_1}

be the globally minimum ordinary edge and

  M={M_0,M_1}

the globally maximum ordinary edge, and assume m and M are vertex-disjoint. Put

  S={m_0,m_1,M_0,M_1},   W=V(G)-S.

Fix any exact two-cover U|V of W. For a nontrivial increasing rail R with source s_R, first edge e_R^-, terminal t_R, and last edge e_R^+, define

  SRC(R) : lambda(m_h s_R) < lambda(e_R^-) for some h in {0,1},
  TERM(R): lambda(e_R^+) < lambda(t_R M_k) for some k in {0,1}.

These are exactly the source and terminal activities used in accepted R1001.

### 2. One nontrivial rail cannot be active at both ends
Suppose SRC(R) and TERM(R) both hold, witnessed by h,k. Because m is globally minimum and M globally maximum,

  lambda(m_{1-h}m_h)
    < lambda(m_h s_R)
    < lambda(e_R^-) < ... < lambda(e_R^+)
    < lambda(t_R M_k)
    < lambda(M_kM_{1-k}).

Hence

  (m_{1-h},m_h,R,M_k,M_{1-k})

is one increasing path. Together with the other rail of U|V it is a spanning two-cover of G, contradiction. Therefore

  not(SRC(U) and TERM(U)),
  not(SRC(V) and TERM(V))                           (EP.1)

whenever the displayed rail is nontrivial.

### 3. Accepted crossed shields collapse to one whole-cover polarity
Assume now that both U and V are nontrivial. Accepted R1001 gives the crossed exclusions

  not(TERM(U) and SRC(V)),
  not(TERM(V) and SRC(U)).                           (EP.2)

Combine (EP.1)-(EP.2). If SRC(U) holds, then EP.1 forces not TERM(U) and the second crossed clause forces not TERM(V). Thus neither terminal is active. The same conclusion holds if SRC(V) holds. If neither source is active, then both sources are shielded. Consequently every nontrivial exact complement cover satisfies at least one of the two global alternatives

  SOURCE-SHIELD:
    not SRC(U) and not SRC(V),

  TERMINAL-SHIELD:
    not TERM(U) and not TERM(V).                     (EP.3)

Both may hold simultaneously. Written as strict edge inequalities, SOURCE-SHIELD means that for R=U,V every edge from either minimum-edge endpoint to s_R lies above the first selected edge of R. TERMINAL-SHIELD means that for R=U,V every edge from t_R to either maximum-edge endpoint lies below the last selected edge of R. Thus the four independent endpoint tests of the extreme carrier collapse to one cover-level polarity.

### 4. Singleton complement rails force a rigid extreme-spoke inversion
Suppose instead one exact complement rail is the singleton {z}; write the other rail R. If S+z had an increasing Hamilton path, that path together with R would two-cover G. Hence S+z is non-Hamiltonian.

Fix h,k in {0,1}. If

  lambda(m_h z) < lambda(z M_k),

then global extremality of m and M makes

  (m_{1-h},m_h,z,M_k,M_{1-k})

an increasing Hamilton path on S+z, contradiction. Therefore for EVERY h,k,

  lambda(z M_k) < lambda(z m_h).                     (EP.4)

So a singleton exact complement rail is not an unstructured exception to EP.3: its four incident spokes form a strict 2x2 cut, with both spokes to the maximum-edge pair below both spokes to the minimum-edge pair.

### 5. Acyclic closed-class interface
Together with `acyclic-edge-rank-extremal-six-gate-wall`, the disjoint-extreme case now has two synchronized scales. Globally, maximum three-covers have ALL-TERMINAL and ALL-SOURCE rank-extremal wall representatives anchored respectively at the global maximum and minimum edges. On the fixed four-endpoint complement W, every exact two-cover is either SOURCE-SHIELD, TERMINAL-SHIELD, or carries a singleton satisfying the rigid inversion EP.4.

This is not R888 closure. In particular R1003 already fences the claim that one doubly shielded rail must itself absorb S. The next parent consumer should compare the polarity of several exact covers of W, or force a polarity change along the R982-connected maximum-cover exchange space. A polarity change cannot be treated as four unrelated endpoint events: EP.3 shows it is a whole-cover transition.
