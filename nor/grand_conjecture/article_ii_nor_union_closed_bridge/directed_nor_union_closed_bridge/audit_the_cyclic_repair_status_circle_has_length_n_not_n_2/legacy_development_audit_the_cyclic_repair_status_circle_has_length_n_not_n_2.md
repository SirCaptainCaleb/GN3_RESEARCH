# Audit: the cyclic repair status circle has length n, not n-2 — preserved pre-item development

## Development

Several recent repair-parity notes denoted the cyclic status-circle length by m=n-2. That is the linear ternary-word length, not the full-support cyclic-coordinate-order length used by the repair graph. A cyclic order on n coordinates has n cyclic ternary windows, including the two wrap windows, so the transition circle has length n. The affected parity conclusions remain unchanged because n and n-2 have the same parity. In particular the even/odd distinction in the J2 and winding arguments is unaffected. However any exact winding equation should read total lifted transition displacement = n times the aggregate winding number, not (n-2) times it. Likewise run profiles such as 1,p,q,2 sum to n. Future repair-graph calculations should use n for the cyclic status length and reserve n-2 for completed linear permutation words.
