# S9034 — Complementary Absorbers Force Dual Non-Hamiltonicity

## Theorem

Let H be a finite boundary tournament with pc(H)>2. Let T be a vertex set, let c,d be distinct vertices outside T, and suppose there are tight paths L_c and L_d such that V(L_c)=V(H)\(T union {d}) and V(L_d)=V(H)\(T union {c}). Then neither H[T union {c}] nor H[T union {d}] has a Hamilton tight path.

## Proof

Assume H[T union {c}] has a Hamilton tight path K_c. By hypothesis L_d is a tight path with vertex set V(H)\(T union {c}). Thus K_c and L_d are vertex-disjoint tight paths whose supports partition V(H), contradicting pc(H)>2. Therefore H[T union {c}] is non-Hamiltonian. The argument for H[T union {d}] using L_c is identical.

## Why this is reusable

Two complementary absorber paths immediately forbid Hamiltonicity on the two complementary witness sides whenever the whole system needs more than two paths. This is a tiny but broadly reusable replacement argument.

## Scope and nonclaims

The theorem asserts only induced-subsystem non-Hamiltonicity. It does not control insertion positions or Hamilton orders on larger supports.

## Provenance

Rescued from accepted archived result `R538`.
