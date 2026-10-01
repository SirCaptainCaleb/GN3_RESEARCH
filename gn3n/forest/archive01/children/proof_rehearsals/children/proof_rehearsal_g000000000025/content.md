# Proof rehearsal 25 — 2026-09-27 13:28 UTC

## Statement

Given a minimum counterexample H, choose a deletion cover H-x=P|Q. Since x is noninsertable into both P and Q, transport01 supplies one bounded insertion-obstruction window on each component. The first unsupported inference is that every resulting pair of bounded windows can be consumed—by cross-swap, endpoint replacement, kernel extension, or another certified move—to produce either a spanning two-cover directly or a spanning ordering of defect span at most two. Certified results handle first-type cyclic kernels, boundary second-type pivots, interior pivot cross-swap clauses, and several support/order-disagreement configurations, but no trusted theorem currently exhausts all bounded-window pair configurations.

## Body

Assume a counterexample and choose one of minimum order. By the certified minimum-counterexample calculus, deleting any vertex x yields a two-cover P|Q. Restoring x into either displayed component would give a spanning two-cover, so x is noninsertable into both component orders. The certified insertion-obstruction theorem in transport01 therefore produces bounded local obstruction windows on P and Q. If a certified consumption theorem converted every such pair to a direct two-cover or defect span at most two, d43a7c9e2f61 would finish the contradiction. The argument stops precisely because that universal consumption theorem is not yet proved.
