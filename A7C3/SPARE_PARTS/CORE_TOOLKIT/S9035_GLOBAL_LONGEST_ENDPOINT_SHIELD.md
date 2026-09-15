# S9035 — Global-Longest Path Endpoint Shield

## Theorem

Let K=(k_1,...,k_m) be a globally longest tight path in a Strong Level-(1) boundary tournament. For every vertex w outside K, the direct endpoint attachment turns (w,k_1,k_2) and (k_{m-1},k_m,w) are bad. Hence by boundary antisymmetry the reverse endpoint turns (k_2,k_1,w) and (w,k_m,k_{m-1}) are tight. Thus every exterior vertex simultaneously witnesses both terminal reverse systems of K as graph-intrinsic facts.

## Proof

Fix w outside K=(k_1,...,k_m). If (w,k_1,k_2) were tight, then (w,k_1,...,k_m) would be a tight path of order m+1, contradicting global longestness of K. Therefore (w,k_1,k_2) is bad, and boundary antisymmetry makes its complete reversal (k_2,k_1,w) tight. Likewise, if (k_{m-1},k_m,w) were tight then (k_1,...,k_m,w) would extend K, so this direct turn is bad and boundary antisymmetry makes (w,k_m,k_{m-1}) tight. The argument is independent for every exterior w, so all asserted reverse turns hold simultaneously as graph-intrinsic facts.

## Why this is reusable

Every exterior vertex simultaneously certifies the two reverse terminal systems of a globally longest tight path. The fact is elementary, but preserving it as a named spare prevents repeated rederivation and keeps endpoint geometry explicit.

## Scope and nonclaims

This gives only terminal reverse turns. It does not assert internal attachment, pairwise interaction among exterior witnesses, or a longer path.

## Provenance

Rescued from accepted archived result `R199`.
