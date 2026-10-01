# Every neutral endpoint-attachment swap cycle with surviving core forces order disagreement

## Statement

Let F_{a_1},...,F_{a_k}, k>=4, be distinct deletion covers arising around a cycle of Phi-neutral one-block endpoint-attachment restorations as in eaf8cbdad3f3, and assume their omitted labels leave a nonempty common surviving core. Then some pair of covers on the cycle has relative-order disagreement on a common support. Consequently such a neutral omission-swap cycle cannot recur without producing a standard endpoint-transport order defect.

## Body

By eaf8cbdad3f3, each neutral restoration edge is a fully compatible omission swap, and its two singleton lifts differ by the corresponding legal singleton-swap move. Thus the singleton lifts of the deletion covers form a cycle in the singleton-swap graph. Because the omitted labels are distinct and leave a nonempty common surviving core, the certified singleton-swap cycle theorem swapcycleorderdefect01 applies directly. It says the deletion covers on the cycle form a support-compatibility clique but cannot all be fully compatible; hence some pair is support-compatible and order-incompatible on a common support. This is the required relative-order disagreement. The previous stronger wording without the nonempty-core hypothesis was not justified by the available monodromy theorem.
