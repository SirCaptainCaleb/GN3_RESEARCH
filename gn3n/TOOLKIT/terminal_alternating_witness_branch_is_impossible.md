# The terminal alternating-witness branch is impossible

**Summary:** A terminal disjoint-window configuration cannot have nearest witness type 0101 or 1010. Hence every surviving terminal local-witness obstruction is of span-two type and has support at most ten vertices.

## Statement

Assume a terminal single-sided disjoint-window configuration for the nearest dual-polarity witness and suppose its type is 0101 or 1010. Then the bridging block has alpha=beta=2 and order four. Protection from the closer span-two witness makes the left occurrence depend only on the first block vertex and the right occurrence only on the last. The identity that exactly one side occurs for every block permutation forces both state functions to be constant, contradicting occurrence of both orientations.

## Body

By [[terminal_local_block_sharpens_to_four]], alpha,beta<=2 and |B|=alpha+beta. Consider type 0101; the complemented case 1010 is identical. In the left six-position determining window write the four statuses s1,s2,s3,s4. The witness is 0101. The span-two witness one step closer to the center tests s2 against s4. Since the selected alternating witness is nearest, every chamber has s2=s4. The first two statuses lie outside B when alpha<=2, so a chamber realizing 0101 forces s1=0 and s2=1 globally on the face, hence s4=1 globally. If alpha=1 then s3 also lies outside B and is fixed; the left witness would therefore be either present in every chamber or absent in every chamber, incompatible with a terminal carrier having both reflected orientations. Thus alpha=2. The left witness is now equivalent to s3=0, and s3 depends only on the first of the two B-vertices in the left suffix. Symmetrically beta=2 and the right witness depends only on the last B-vertex in the right prefix. Therefore B has four vertices. For a chamber whose B-order is (x,y,z,w), write L(x) and R(w) for the two witness indicators. Terminality gives L(x)+R(w)=1 for every distinct x,w. Given any w1,w2, choose x distinct from both; then R(w1)=R(w2). Hence R is constant, and then L is constant. This contradicts that the balanced carrier supplies chambers of both witness orientations. Therefore no terminal alternating-witness configuration exists.

## Metadata

- ID: terminal_alternating_witness_branch_is_impossible
- Kind: toolkit
- Version: 1
- Math version: 1
- Audit: passed
- Refutation: unrefuted
- Toolkit status: Limbo
