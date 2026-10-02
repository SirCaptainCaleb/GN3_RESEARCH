# Top-layer switching packets force one-eighth paid structure

## Statement

Along a global longest path, forward-flat ascending top-rank output edges form an independent set. For a dense family of interior single blockers at a top-layer switching center, this implies at least a one-eighth-scale payment into doubly occupied switcher cells or nonflat outputs. Refining by contact type, the same family satisfies s_int<=ceil((L-3)/2)+U+2Y, so U+2Y>=L/8-eta_v-O(1): linearly many switchers are terminal-retained or lie in cells whose output is special or all-top nonspecial nonascending.

## Body

Consecutive host edges cannot both be flat ascending outputs because the shared joint would simultaneously need potential L-1 and at least L. Hence flat occupied cells are independent. Counting occupancy gives the basic paid-cell dichotomy. A flat cell carrying two entrance-retained switchers forces the preceding three cells empty by the joint exclusion and quantitative separation lemmas, yielding the one-dimensional recurrence W(n)<=max(W(n-1),W(n-2)+1,W(n-4)+2) and W(n)<=ceil(n/2). The remaining interior switchers are U-type or live in nonflat cells, each of capacity two, giving the refined one-eighth X/U-or-nonflat inequality.