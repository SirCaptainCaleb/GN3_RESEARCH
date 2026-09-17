# The retained source frame crosses the singleton-star spectator cut at least three times

**Workspace:** D17
**State:** established
**Key:** `singleton-star-source-frame-three-crossing-floor`

**Summary:** In the G32 singleton-star spectator frame, contract the retained exact source cover H-{a,c}=U|V into maximal X-blocks and B-blocks, where X={v,p,q,r} is the non-Hamiltonian four-cell and p,q,r are all source-internal. If b_X,b_B are the block counts and tau is the number of selected X|B transitions, contraction gives tau=b_X+b_B-2 and non-Hamiltonicity gives b_X>=2. Tau=1 forces an isolated X-only source rail; tau=2 leaves only (3,1) or (2,2) block counts, whose path-forest shapes either isolate an X-only rail or place X at source-rail endpoints. An isolated X-rail is either the forbidden singleton v by R429 or has a source spoke endpoint; two mixed X-B rails would require the sole non-source vertex v to be the X-endpoint of both. Hence every live source representative has at least three literal X|B transitions. This is the source-frame information absent from boundary-only spectator models and is retained for the G32 full-H splice.

### 1. Setup
Retain the G32 transitive singleton-star spectator frame. Thus

  G=H-{a,c}=X union V(B),
  X={v,p,q,r},

where X is non-Hamiltonian, B is a Hamilton spectator path, and the retained exact source cover

  G=U|V

has the three source spokes p,q,r internal on their displayed source rails. By R429 both source rails are nontrivial.

Split U and V into maximal nonempty X-blocks and B-blocks. Let b_X and b_B denote the total numbers of these blocks over the two rails, and let tau be the total number of selected source-cover states with one endpoint in X and one in B. Contract every maximal block to one vertex. The result is still a two-component path forest, every contracted edge is an X|B transition, and therefore

  tau=b_X+b_B-2.                                      (SF.1)

Since X is non-Hamiltonian, b_X>=2.

### 2. One transition is impossible
Assume tau=1. Then (SF.1) forces (b_X,b_B)=(2,1). The contracted forest has three block-vertices and one edge, hence one X-block is an isolated whole source rail.

If that isolated X-rail contains only v, it is a singleton source rail, contradicting R429. If it contains any source spoke, then because v is the only non-source vertex of X, at least one physical endpoint of that X-only rail is one of p,q,r. This contradicts the retained fact that all three source spokes are internal. Hence tau!=1.

### 3. Two transitions are impossible
Assume tau=2. Then b_X+b_B=4.

#### 3a. The case (b_X,b_B)=(3,1)
The unique B-block can meet at most two X-blocks in the two-edge contracted forest. To have exactly two path components, two X-blocks lie with that B-block on one rail as X-B-X and the third X-block is an isolated whole rail. The isolated X-rail is impossible by the argument of Section 2.

#### 3b. The case (b_X,b_B)=(2,2)
There are only three two-edge bipartite path-forest shapes.

1. Two disjoint X-B edges. Then each physical source rail has an X-block at one end. Since p,q,r are all internal, the X-side endpoint of each rail would have to be the sole non-source vertex v, impossible on two disjoint rails.
2. X-B-X together with one isolated B-block. The mixed rail has both physical endpoints in X. With only one non-source vertex v, at least one of those two endpoints is a source spoke, contradicting internality.
3. B-X-B together with one isolated X-block. The isolated X-rail is impossible by Section 2.

Thus tau!=2.

### 4. Source-frame crossing floor
Consequently every retained source representative in the G32 singleton-star residue satisfies

  tau_{X|B}(U|V) >= 3.                                  (SF.2)

This is literal selected-state information from the actual old source frame, not an anonymous component-drop certificate. In particular, a finite endpoint-splice model that retains only X, the spectator endpoint gates, and the source trimers but forgets the source-cover X|B transitions is genuinely weaker than the live G32 packet.

### 5. Scope
The three-crossing floor is a reduction, not absorption. It does not claim any one crossing has a prescribed orientation or position, and it does not convert a crossing into R159/payment currency. Its purpose is to expose the extra physical source-frame layer that must be spent in the trimerized full-H endpoint cut. R24 and R5 are unused.

## References

```json
[
    {
        "relation": "dependency",
        "revision_id": "R429"
    }
]
```
