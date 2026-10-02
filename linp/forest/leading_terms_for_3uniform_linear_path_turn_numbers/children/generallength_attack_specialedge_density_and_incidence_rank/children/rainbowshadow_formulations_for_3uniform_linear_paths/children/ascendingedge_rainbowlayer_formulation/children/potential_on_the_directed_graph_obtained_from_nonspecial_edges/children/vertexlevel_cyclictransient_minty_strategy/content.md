# Vertex-level cyclic-transient Minty strategy

## Statement

Use the directed graph R formed by orienting each nonspecial edge from its unique entrance toward its two snake vertices as the primary Minty object. Treat arcs in recurrent strongly connected structure by the closed-walk potential inequality, and control the remaining ascending arcs by repeated-blocker and path-rotation arguments. This retains the transient sharp examples while putting the cyclic argument directly on the physical vertex set of H.

## Body

The vertex-level formulation is preferable to the transfer digraph on hyperedges for the current counting problem. It records every nonspecial edge by exactly two arcs and therefore every ascending edge by exactly two positive-score arcs. Moreover d_R^+(x)=2b(x), where b(x) is the number of nonspecial edges with entrance x, while d_R^-(v) is the number of nonspecial snake incidences at v and is bounded by the snake-indegree argument. The three-center examples remain acyclic from their entrance vertices to their snake vertices, explaining why a closed-walk argument alone cannot bound them. The proposed proof therefore uses Minty on recurrent components and the repeated-blocker/Pósa-rotation mechanism on the acyclic remainder. A successful implementation should control the same defect A-H_2 appearing in the refined ascending-edge accounting.