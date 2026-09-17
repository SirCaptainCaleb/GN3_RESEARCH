# Source-cover degree conservation forces crossings on at least two distinct source spokes

**Workspace:** D17
**State:** established
**Key:** `singleton-star-source-crossing-degree-law`

**Summary:** In the retained G32 source cover F=U|V, let b_X,b_B count maximal X- and B-blocks, tau count selected X|B transitions, and d=d_F(v). Since p,q,r are internal and e_XX=4-b_X, selected-degree counting gives tau=2b_X+d-2. Combining with the contracted-forest identity tau=b_X+b_B-2 yields b_B=b_X+d. R429 excludes d=0, so d is 1 or 2 and tau is respectively 2b_X-1 or 2b_X. At least tau-d=2b_X-2 crossings are incident with source spokes. They cannot all hit one spoke: that would make it a singleton X-block, force b_X=2, and then the remaining three-vertex X-block containing v cannot supply the remaining required crossings without exceeding d(v). Hence at least two distinct source spokes physically meet B in the old source frame. This narrows the G32 full-H splice obstruction to the possibility that the R582-omitted spoke is the unique noncrossing spoke.

### 1. Setup
Retain the G32 singleton-star spectator frame and the source-cover notation of SV100350. Thus

  G=H-{a,c}=X union V(B),
  X={v,p,q,r},

and the retained exact source cover F=U|V has p,q,r internal. Let b_X and b_B be the total numbers of maximal nonempty X- and B-blocks in F, let tau be the number of selected X|B transitions, and let d=d_F(v) be the selected degree of the singleton center v in the two-path forest F. By SV100350, X is non-Hamiltonian and hence b_X>=2.

### 2. Exact degree law
Let e_XX be the number of selected F-states with both endpoints in X. Since the b_X maximal X-blocks partition the four vertices of X,

  e_XX=4-b_X.                                      (SD.1)

The three source spokes are internal on their F-rails, so each has selected degree two. Summing selected degrees over X therefore gives

  6+d = 2 e_XX + tau.                              (SD.2)

Using (SD.1),

  tau = 2 b_X + d - 2.                             (SD.3)

On the other hand the contracted two-component path forest from SV100350 gives

  tau=b_X+b_B-2.                                   (SD.4)

Comparing (SD.3)-(SD.4),

  b_B=b_X+d.                                       (SD.5)

These are exact identities for the actual retained source representative, not inequalities and not statements about another cover.

### 3. The center is never isolated
The only possible selected degrees of v are 0,1,2. If d=0, then v is an isolated component of the two-path forest F, hence a singleton source rail. Accepted R429 says both rails in every exact two-cover of H-{a,c} are nontrivial. Therefore

  d in {1,2}.                                      (SD.6)

Consequently the crossing number is completely parity-coded:

- if v is a source-cover endpoint, d=1 and tau=2b_X-1 is odd;
- if v is internal, d=2 and tau=2b_X is even.

### 4. At least two distinct source spokes meet the spectator rail
Let c_v be the number of X|B transitions incident with v. Since c_v<=d, (SD.3) gives at least

  tau-c_v >= tau-d = 2b_X-2                         (SD.7)

selected X|B transitions incident with the source spokes p,q,r. In particular there are at least two such transitions.

We now show they cannot all be incident with one source spoke s. If they were, then s would use both of its selected degrees on B-neighbors, so s would have no selected X-neighbor and {s} would be a singleton X-block. If b_X>=3, (SD.7) gives at least four source-spoke crossings, impossible at one degree-two vertex. Hence b_X=2. The other X-block then contains the remaining three vertices, including v, and has size three.

If d=1, then tau=3. The singleton block {s} contributes exactly two crossings. The third crossing would have to be incident with v. But v lies in the three-vertex X-block, so it already has at least one selected X-neighbor; d=1 leaves no degree for an X|B transition, contradiction.

If d=2, then tau=4. Again {s} contributes two crossings. The remaining three-vertex X-block must therefore contribute two crossings. At most one can be incident with v: if v is an endpoint of that X-block it already spends one selected degree on its X-neighbor, while if v is its middle vertex it spends both degrees inside X. Hence at least one of the two remaining crossings is incident with another source spoke, contradiction.

Therefore at least two distinct vertices of {p,q,r} are physically incident with selected source-cover X|B transitions.             (SD.8)

### 5. Scope
This is a source-frame refinement of SV100350. It does not choose which two spokes cross, does not assert that the R582-omitted spoke is one of them, and does not itself splice the anchors a,c into the endpoint-favorable K_s. Its use for G32 is to reduce the difficult mismatch to the case where an endpoint-favorable K_s omits the unique noncrossing source spoke, if such a spoke exists. R24 and R5 are unused.

## References

```json
[
    {
        "relation": "dependency",
        "revision_id": "R429"
    }
]
```
