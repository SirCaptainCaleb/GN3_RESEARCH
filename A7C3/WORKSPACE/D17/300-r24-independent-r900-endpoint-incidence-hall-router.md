# R900 is R24-independent: endpoint-incidence Hall routing uses only actual Hamilton supports

**Workspace:** D17
**State:** established
**Key:** `r24-independent-r900-endpoint-incidence-hall-router`

**Summary:** R900, `Endpoint Incidence Hall Router`, is independent of R24. Build the bipartite graph whose left vertices are Hamilton supports and whose right vertices are endpoint-deletion cores, joining a support to every core obtained by deleting an actual exposed endpoint of one of its Hamilton paths. Hall deficiency, minimal deficient families, degree counting, and endpoint-core routing depend only on these actual incidences and accepted Hall structure R934. No singleton-deletion rail-order floor is needed.

### 1. Incidence graph
For every Hamilton support X in the R900 family, retain every actual Hamilton path and each physical endpoint p. Join X to

  X-{p}.                                                  (R900.1)

This defines the complete endpoint-incidence graph used by R900.

### 2. Hall structure
Choose any inclusion-minimal Hall-deficient left family F. Accepted R934 gives

  |N(F)|=|F|-1

and the standard connected/factor-critical incidence properties. Every left support has at least two endpoint-core neighbors because every Hamilton path has two distinct physical endpoints.

Degree counting and the ensuing endpoint-core router are therefore consequences of the incidence graph itself.

### 3. Independence from R24
At no point is a singleton-deletion two-cover decomposed by rail order, nor is any short complement classified. R900 requires only actual Hamilton paths, their endpoints, and R934.

Thus R900 has an R24-independent proof.