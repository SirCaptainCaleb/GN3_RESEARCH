# Proof rehearsal 20 — 2026-09-26 01:06 UTC

## Statement

Starting from a certified local witness—support-partition crossing, reversed common edge, reversing tight triple, vertex-simple tight cycle, or bounded insertion obstruction—derive a spanning two-cover directly, transport it by fully checked tight-path replacements to an absorbable endpoint reversal, or construct a spanning ordering of defect span at most two. Current results guarantee such witnesses broadly (in particular 9a7e3c1f5b20 for arbitrary opposite endpoint deletion covers), but no certified theorem supplies this consumption/termination step.

## Body

Shortest proof remains: minimum counterexample -> exact deletion two-cover -> omitted vertex is noninsertable in both components -> certified bounded local obstruction(s); independently, longest-path endpoint comparisons now universally produce explicit disagreement. Defect span <=2 would close by d43a7c9e2f61. The first unsupported inference is exactly e34dc91e238d, unchanged in substance though the producer side is now stronger.