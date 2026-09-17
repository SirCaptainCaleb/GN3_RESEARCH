# Global edge extremes do not automatically form a universal extension core

**Workspace:** D17
**State:** established
**Key:** `acyclic-global-extreme-core-shortcut-fences`

**Summary:** Two exact finite edge orders fence tempting acyclic shortcuts. A K5 with disjoint global minimum 01 and maximum 23 has Hamiltonian extreme endpoint four-set {0,1,2,3} but no Hamilton P5, so the extreme four-set need not be universally one-extendable. A K4 with global minimum 01 and maximum 02 sharing vertex 0 has the increasing extreme trimer (1,0,2) but no Hamilton P4, so shared extremes do not automatically yield a universally extendable trimer. These are route fences only, not R888 counterexamples.

### 1. Disjoint global extremes do not automatically form a universal one-extension four-set
Consider the edge-ordered K5 on vertices 0,1,2,3,4 with strict edge order

  01 < 02 < 34 < 13 < 03 < 24 < 04 < 12 < 14 < 23.

The globally minimum edge is 01 and the globally maximum edge is 23, so the two extreme edges are disjoint. Their endpoint four-set S={0,1,2,3} is Hamiltonian, for example

  (1,0,2,3)

is increasing because 01<02<23. Nevertheless exhaustive inspection of all 5!=120 vertex orders shows that the full five-set has no increasing Hamilton path. Hence S is not universally one-vertex Hamilton-extendable: adjoining vertex 4 fails.

Therefore the acyclic extreme-edge program may not shortcut directly from “disjoint global minimum and maximum edges” to the G10 universal one-extension four-core. Additional complement-cover or exchange-class structure is essential.

### 2. Shared global extremes do not automatically give a universally extendable extreme trimer
Consider the edge-ordered K4 on vertices 0,1,2,3 with

  01 < 23 < 03 < 12 < 13 < 02.

The globally minimum edge 01 and globally maximum edge 02 share vertex 0. Thus

  (1,0,2)

is an increasing trimer because 01<02. Exhaustive inspection of all 4!=24 vertex orders shows that the full K4 is non-Hamiltonian. Hence the natural extreme trimer need not Hamilton-extend through the fourth vertex.

This fences the analogous shared-extreme shortcut. Any treatment of the shared-extreme case must use additional smallest-counterexample representative structure rather than assuming automatic extension of the extreme trimer.

### 3. Status
These are exact finite edge-order witnesses and route fences, not counterexamples to R888 and not positive structure theorems. They justify the current G10 strategy of consuming polarity changes and closed representative holonomy rather than declaring the global extreme endpoints themselves to be a small universal core.
