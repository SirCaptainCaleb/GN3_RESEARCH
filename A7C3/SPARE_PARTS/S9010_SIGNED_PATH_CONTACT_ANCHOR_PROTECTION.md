# S9010 — Signed-Path Contact and Historical Anchor Protection

## Theorem

Let `(w;P)` be a graph-intrinsic head-signed tight path in a Strong Level-(1) boundary tournament, with

`P=(v_0,...,v_k)`

and signed anchor `v_0`. Let `Q` be any proper tight path meeting `P`.

If `Q` avoids `v_0`, let

`i = min{j : v_j in V(Q)}`.

Then `i>=1`, and the prefix

`P^-=(v_0,...,v_{i-1})`

is a nonempty, strictly shorter head-signed support disjoint from `Q`, with the same anchor `v_0`.

If `Q` contains `v_0`, then, apart from the vacuous exact replay of the same singleton support with no new certificate data, at least one of the following occurs:

1. strict tight-path growth of the old support `P`;
2. strict tight-path growth of `Q`;
3. a vertex-simple proper tight cycle;
4. explicit reverse-contact geometry of the Reverse-Ear type.

The tail-signed dual is exact.

Consequently, outside these explicit events, a genuinely later signed support or marker cannot silently contain the signed anchor of an older historical support. Quiet contact away from the anchor can only shorten the old support on its signed side while preserving that anchor.

## Proof

We prove the head-signed case. The tail case is obtained by reversing all displayed path orders.

Because `(w;P)` is head-signed, the extended path

`(w,v_0,...,v_k)`

is tight.

Suppose first that `Q` avoids `v_0`. Let `i` be the first index for which `v_i` lies on `Q`. Then `i>=1`. The prefix

`P^-=(v_0,...,v_{i-1})`

is nonempty and disjoint from `Q` by minimality of `i`. Moreover

`(w,v_0,...,v_{i-1})`

is a prefix of the old tight signed extension, so `P^-` remains head-signed by the same witness `w`. It is strictly shorter than `P` and retains the same signed anchor.

Now suppose `Q` contains `v_0`.

If `k=0`, then `P` is the singleton `(v_0)`. Any nontrivial `Q` strictly grows `P`. If `Q=(v_0)` and carries no genuinely new certificate, this is only stationary replay and is explicitly excluded from being counted as progress.

Assume therefore that `k>=1`. Apply the Reverse-Ear Lemma to `P` and `Q`. Unless it already produces a reverse-contact cell or a proper tight cycle, the vertices of `P` occur along `Q` in increasing `P`-order. In particular `v_0` is the first `P`-vertex encountered on `Q`.

If `Q` has a predecessor `a` immediately before `v_0`, test the turn

`(a,v_0,v_1)`.

If it is tight, the prefix of `Q` ending at `v_0` concatenates with all of `P`, strictly extending `P`. If it is bad, boundary antisymmetry makes

`(v_1,v_0,a)`

tight, which is explicit reverse-contact geometry.

It remains to consider the case in which `v_0` is the head of `Q`. If `Q` is the singleton `(v_0)`, then the old dimer `(w,v_0)` strictly extends `Q`, except in the stationary-replay case already fenced.

Otherwise write

`Q=(v_0,q_1,...)`.

If `w` is outside `Q`, test

`(w,v_0,q_1)`.

If it is tight, `(w,Q)` is a strict extension of `Q`. If it is bad, boundary antisymmetry makes

`(q_1,v_0,w)`

tight, again giving explicit reverse-contact geometry.

Finally, if `w` lies on `Q` after `v_0`, compare the two tight paths `(w,P)` and `Q`. They contain `w` and `v_0` in opposite orders, so the Reverse-Ear Lemma yields reverse-contact geometry or a proper tight cycle.

These cases exhaust every contact with the signed anchor and prove the theorem. ∎

## Historical-anchor corollary

Suppose a signed support is retained as historical information and a genuinely later support or marker meets it. If the later object contains the old signed anchor, the theorem forces one of the explicit growth/cycle/reversal events. Otherwise the old support may be shortened only to its signed-side prefix or suffix, which preserves the anchor.

Thus historical signed anchors are protected against silent reuse. This is not a claim that old supports remain current in later covers; it is a graph-intrinsic contact statement.

## Scope and nonclaims

The theorem does not declare a proper tight cycle contradictory. It does not convert historical capture into current representative information. Exact stationary replay of an identical singleton certificate is not fresh progress.

The only external mathematical primitive used is the Reverse-Ear Lemma, published here as `S9001`, together with boundary antisymmetry.

## Provenance

Rescued from the accepted theorem historically recorded as `R436`. Citation-graph mining found `R436` referenced from **136 distinct corpus files**, making it one of the most reused non-foundational results in the entire archaeology. Its proof structure is genuinely portable rather than branch-specific.