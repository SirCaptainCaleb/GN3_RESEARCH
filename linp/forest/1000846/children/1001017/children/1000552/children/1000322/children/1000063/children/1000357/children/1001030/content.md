# Minimum degree forces ascending edges to have large φ

## Statement

Let H be a finite linear 3-graph with minimum degree δ. If e is an ascending nonspecial edge, then φ(e)>=ceil((δ+3)/2).

## Body

This statement is valid. The earlier proof attempt was invalid because it applied the terminal-degree bound directly at the entrance of a locally longest path, and the object was temporarily marked refuted using c3e95f4ce77d. That family is not a counterexample: its global minimum degree is 3, even though its shared entrance vertices have large degree. The corrected proof is b3f79b5fc50d, based on the endpoint-specific path-length lemma 1956950d4285. If x is the unique entrance of an ascending edge e, then φ(x)=φ(e)-1. The endpoint-specific lemma gives φ(x)>=ceil((δ+1)/2), hence φ(e)>=ceil((δ+3)/2).
