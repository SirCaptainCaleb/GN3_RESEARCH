# Route 5 — Inductive longest-path pair capacity with outside defect

## Statement

Comprehensive synthesis of the one-third induction route that removes a longest path and pays all incident edges from internal pair capacity, path slack, and the outside extremal defect.

## Body

# Route 5. Longest-path induction with pair capacity and outside defect

## Goal and status

This route targets the one-third upper bound directly by induction on the number of vertices.

Let H be an n-vertex P_ℓ-free linear 3-uniform hypergraph. The desired theorem is

3|E(H)| ≤ ℓ|V(H)|.      (1)

Choose a longest linear path P with k edges and put

X=V(P),   Y=V(H)\X.

Since P is 3-uniform and linear,

|X|=2k+1.      (2)

Let m_Y be the number of hyperedges lying entirely in Y, and let

e_X=|E(H)|−m_Y

be the number of edges meeting X.

Assume inductively that the target inequality already holds for H[Y], and define its unused extremal capacity by

D_Y = ℓ|Y|−3m_Y ≥0.      (3)

The route reduces the entire theorem to one local charging inequality around the single longest path P.

The reduction itself is proved, but it is still pending independent audit. The charging theorem that would finish the argument is not known.

## 1. Exact inductive reduction

Starting from

3|E(H)|=3m_Y+3e_X,

the desired inequality (1) is equivalent, using (3), to

3e_X ≤ ℓ|X|+D_Y.      (4)

Because |X|=2k+1,

binom(|X|,2)=k(2k+1)=k|X|.

Hence

ℓ|X| = binom(|X|,2)+(ℓ−k)|X|,

and (4) becomes

3e_X ≤ binom(|X|,2)+(ℓ−k)|X|+D_Y.      (5)

This is the exact pair-capacity form of the induction.

In the saturated case k=ℓ−1, which is the hardest case because the explicit slack is smallest,

3e_X ≤ binom(|X|,2)+|X|+D_Y.      (6)

There is no loss in this derivation. Thus a proof of (5) for every longest path would prove the one-third theorem by induction.

## 2. Interpretation of the three currencies

Equation (5) exposes three distinct resources.

### Internal pair capacity

A linear hyperedge meeting X uses pairs of vertices in a highly constrained way. Since H is linear, no unordered pair of vertices can belong to two different hyperedges. The quantity

binom(|X|,2)

is therefore the natural total local capacity available inside the longest-path vertex set.

### Path-length slack

If k<ℓ−1, the path is shorter than the forbidden length, and the term

(ℓ−k)|X|

records the resulting extra allowance. Thus shorter longest paths are automatically easier; the saturated case k=ℓ−1 is the critical one.

### Outside extremal defect

The term

D_Y=ℓ|Y|−3m_Y

is not an error term. It is the precise amount by which the induced outside hypergraph falls short of the inductive extremal bound. If the local configuration around P consumes more than its internal pair capacity, the intended proof must show that this overdraw forces H[Y] to be correspondingly nonextremal, thereby paying through D_Y.

This is the genuinely new feature of the route. A purely local proof that discards D_Y throws away the main resource introduced by induction.

## 3. What longest-path maximality contributes

A longest path prevents arbitrary interactions between crossing edges and X.

The maximum-path contact theory developed elsewhere in LINP implies that an edge meeting P in a way that would permit a clean splice cannot exist; otherwise P could be extended or rerouted into a longer path. Consequently edges meeting X can be divided according to the internal pairs or path contacts that block their extension.

The desired charging philosophy is therefore:

1. ordinary incident edges are assigned to distinct or bounded-multiplicity internal pairs of X;
2. exceptional edge classes consume the explicit slack (ℓ−k)|X|;
3. any family that still exceeds these two resources must force a quantitative deficit D_Y outside P.

The proof has not yet constructed this assignment globally. Nevertheless, several certified deletion and threshold lemmas show how the third step might arise.

## 4. Threshold deletion and the outside structure

There is a useful critical-set lemma of the following form. In the relevant threshold setting, after deleting a critical vertex set D, the remaining hyperedges lie inside every corresponding path witness. Hence H−D is a linear path forest: its maximum degree is at most two and its edge count is at most half the number of surviving vertices.

At the same time, every vertex outside D sends many of its incident edges back into D. Thus a dense configuration cannot hide entirely outside the longest-path core; high degree forces a large number of structured crossings.

This provides a possible charging mechanism. If too many edges meeting X cannot be paid by internal pairs, then the same density constraints force many vertices in Y to send edges through a small critical set, creating rigid bridges or reducing the edge count available inside Y.

## 5. Exact deletion defect and the lift-back correction

A previously tempting induction shortcut is false in its naive form.

Suppose one deletes a small set S and observes that the remaining graph still has nearly the same density. It is not enough to say that this contradicts vertex-minimality. The correct identity is an exact density-defect formula: the change in the extremal deficit is determined by the number of edges meeting S and the amount of vertex mass removed.

For a singleton deletion in a vertex-minimal equality obstruction, a cheap deletion does not immediately contradict minimality. Instead it forces an exact bridge configuration when the deleted vertex is lifted back: a surviving low-degree vertex must have exactly one compensating edge through the deleted vertex.

This matters for (5). The outside defect D_Y can only be claimed when a local overdraw is converted into an actual loss of edges in H[Y]. A deletion argument that does not trace the lift-back bridge is insufficient.

## 6. Reservoir outside a fixed path

Dense equality configurations also have a useful reservoir property.

If H has exact density d and minimum degree at least d+1, then many vertices have degree at least d+2. Quantitatively, there are at least 4d−1 such vertices. Therefore any fixed q-edge path omits at least

4d−2q−2

high-degree vertices.

These omitted high-degree vertices are potential sources of outside defect or lift-back structure. In a saturated longest-path configuration, they cannot simply attach freely to P without creating an extension. Their incident edges must instead be absorbed by constrained crossing patterns, which is exactly the setting in which a defect-transfer argument might prove D_Y>0.

This result does not by itself establish the charge, but it prevents the induction from degenerating into a completely local problem on X.

## 7. The payment theorem that would finish the proof

The route closes if one proves the following statement.

**Longest-path payment theorem.** For every longest k-edge path P in every P_ℓ-free linear 3-graph H, with X=V(P), Y=V(H)\X, and D_Y defined by (3),

3e_X ≤ binom(|X|,2)+(ℓ−k)|X|+D_Y.      (7)

A proof should be structural rather than an ℓ-dependent enumeration. One possible formulation is a bounded-overlap map from the three units carried by each edge meeting X into:

- internal unordered pairs of X;
- explicit path-slack tokens;
- certified units of outside extremal deficit.

An equivalent formulation would show that whenever the first two resources are overdrawn by r units, then D_Y≥r.

No such theorem is currently proved.

## 8. Known dead ends

Three mistakes are already understood.

First, the algebraic reduction (5) is not itself the charging theorem. It merely identifies what must be paid.

Second, one cannot discard D_Y and attempt to pay every incident edge from pairs of X alone. The outside defect is the only genuinely new inductive currency and is expected to be necessary in extremal local configurations.

Third, “cheap deletion preserves density, therefore minimality is contradicted” is not valid. The correct conclusion is the exact lift-back bridge described above.

The route should also avoid an unbounded ladder of ℓ-specific contact cases. Such an enumeration would not explain why the pair-capacity inequality is uniform.

## 9. First unsupported implication

Everything reduces to (7), and this is the first unsupported implication.

The reduction to (7) is exact. The maximum-path contact lemmas, threshold path-forest lemma, deletion-defect identity, lift-back bridge, and outside high-degree reservoir are certified tools. What is missing is a theorem composing them into a bounded-overlap payment.

In particular, there is not yet a proof that every local overdraw of internal pair capacity produces a quantitatively equal loss in H[Y].

The attempted induction must stop there.

## Research handoff

The saturated case k=ℓ−1 is the cleanest place to work because the slack term is only |X|. Classify edge families by which internal pair of X they can naturally pay to, and treat only the genuine collisions as candidates for transfer into D_Y.

The most valuable next theorem is an overdraw-to-defect statement: if r more charge units are demanded than can be placed on internal pairs plus path slack, prove D_Y≥r.

Do not retry the invalid cheap-deletion contradiction, discard the outside defect, or replace the structural problem by an ℓ-dependent finite case ladder.

Status note: the pair-capacity reduction is proved but pending audit; the deletion, lift-back, threshold, and reservoir results used as supporting tools are certified.