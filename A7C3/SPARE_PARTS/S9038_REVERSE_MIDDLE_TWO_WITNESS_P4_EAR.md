# S9038 — Reverse-Middle Two-Witness P4 Ear

## Theorem

Let A,C,x,y be four distinct vertices in a Strong Level-(1) boundary tournament. If (A,x,C) and (A,y,C) are tight, then at least one of (A,x,C,y) and (A,y,C,x) is a tight Hamilton P4. More precisely, if (x,C,y) is tight the first path is tight; if it is bad, boundary antisymmetry makes `(y,C,x)` tight and the second path is tight.

## Proof

Assume (A,x,C) and (A,y,C) are tight. Test the turn (x,C,y). If it is tight, then (A,x,C,y) is a tight P4 because its consecutive turns are (A,x,C) and (x,C,y). If (x,C,y) is bad, boundary antisymmetry gives (y,C,x) tight; together with the given (A,y,C), this makes (A,y,C,x) a tight P4. Thus one of the two displayed labelled Hamilton `P4`s always exists.

## Why this is reusable

Two witnesses through the same ordered endpoints automatically assemble into one of two literal P4s. This is the smallest useful consumer of a reverse-middle collision and is independent of any surrounding cover frame.

## Scope and nonclaims

The theorem is purely local on four vertices. It does not assert where such a two-witness packet comes from.

## Provenance

Rescued from accepted archived result `R584`.
