# Endpoint-state Minty walk for potential-charged edges

## Statement

Use maximum paths with a distinguished last vertex as states. At state (P,v), every potential-charged ascending edge at v either places its low-potential entrance on P or, by the endpoint-rotation lemma, gives a move to a new state (P',w) with φ(w)>=φ(v). Analyze a walk that repeatedly takes such moves whenever too many charged edges are witnessed by their high terminals.

## Body

This state space separates the obstruction into the two currencies suggested by the Minty analogy. A low-entrance witness is static but must lie in the central window controlled by its edge rank. A high-terminal witness is dynamic and produces a length-preserving rotation whose endpoint potential does not decrease. Hence along a sequence of dynamic moves the scalar potential φ is monotone. Strict increases can occur only finitely many times; recurrent behavior is confined to a fixed potential level, where one can seek a secondary Minty potential on blocker positions or a no-positive-closed-walk statement. The target is to show that four charged edges cannot persist around every recurrent state, or at least that persistence forces geometric rank spacing and therefore logarithmic charged degree.
