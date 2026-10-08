# Independent audit: existential versus protected filtration gap

## Composition

(none yet)

## Development

## Independent audit: the existential/protected filtration gap remains

The current composition does **not** yet justify the final genus iteration.

The terminal square/hexagon analysis, including the new endpoint-exclusion lemma for the maximal ten-support alternating braid, appears locally sound. In particular, the repaired argument does not use the invalid identity \(\ell(\pi)=g(\pi)e_r\).

The load-bearing problem is one level earlier: the current composition iterates through the existential next-depth face spaces \(Y_r\), where a proper face belongs to \(Y_r\) as soon as it contains **one** chamber of selected witness depth at least \(r\). Such a face may simultaneously contain chambers with selected witness depth less than \(r\).

That is exactly the issue already identified in [[protected_carrier_separator_and_the_acyclic_carrier_reduction]]. The mixed-cell/terminal classification is proved for a **protected** face, where every chamber avoids all witness edges closer than \(e_r\). It therefore cannot be applied to arbitrary vertices or cells of the existential \(Y_r\).

The new terminal surgery coherence results construct outward replacement chambers and, at best, common proper carriers that **contain** outward chambers. This is enough to land in existential \(Y_{r+1}\), but it does not imply that every chamber of those carrier faces is outward. Hence it does not produce the protected next-stage complex
\[
X_{r+1}=\{F:\text{every chamber of }F\text{ has selected witness depth at least }r+1\}.
\]
Consequently the next separator step cannot simply reapply the protected mixed-cell theorem.

Equivalently, the present chain
\[
S_r\longrightarrow Y_{r+1},\qquad
\gamma(Y_{r+1})\ge\gamma(Y_r)-1
\]
does not establish an iterable filtration, because protection is lost after the first outward surgery.

This is not repaired by rank-two endpoint coherence: square/hexagon compatibility controls how local replacement choices fit together, but it does not upgrade an existential carrier to a face whose entire chamber set is protected.

### Smallest repair obligation

One needs one of the following.

1. A protected filtration \(X_r\) with an equivariant separator map
   \[
   S_r\to X_{r+1}
   \]
   and the same one-unit genus loss; or
2. a stronger theorem showing that the particular coherent carriers produced by terminal surgery are wholly depth-\(>r\), not merely that they contain one outward chamber; or
3. a new mixed-face theorem valid on the existential \(Y_r\) without any protected-face hypothesis.

Until one of these is supplied, the iteration
\[
\gamma(Y_{d+1})\ge3
\]
and the claimed grand-conjecture closure do not follow.

### Additional extension issue

The current composition also invokes a “usual Coxeter-cell/acyclic-carrier extension” after checking commuting squares and braid hexagons. Rank-two Coxeter relations do give path-independence for chamber transport, but an acyclic-carrier extension over the whole separator additionally requires a compatible contractible/acyclic target carrier for every higher-dimensional source face. The existing rank-two notes construct such carriers residue-by-residue; they do not presently prove the required higher-face carrier condition. This is a second, potentially independent global obligation unless a precise Coxeter-carrier theorem is stated and its hypotheses verified here.

Thus the endpoint-exclusion repair closes the **local maximal braid**, but Article VII remains globally unclosed at the protected-filtration / higher-carrier step.
