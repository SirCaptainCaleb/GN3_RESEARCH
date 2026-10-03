# Quadratic-minimal three-covers have no components of order one or two

**Summary:** In a minimum counterexample, every Phi-minimal spanning three-cover has all three component orders at least three. A singleton beside an s-path with s>=3 repartitions as 2|(s-1), and a two-vertex component beside an s-path with s>=4 repartitions as 3|(s-1), strictly decreasing Phi.

## Statement

Let H be a minimum counterexample and let P_1|P_2|P_3 be a spanning three-cover that minimizes Phi=sum |P_i|^2 in its pairwise-repartition component. Then |P_i|>=3 for each i.

## Body

Suppose first that one component is a singleton (x). Since |V(H)|>10, among the other two components one has order s>=5, say C=(c_1,...,c_s). The pair (x,c_1) is a tight path of order two by definition, while (c_2,...,c_s) is the inherited suffix of C. Thus the pairwise repartition

(x)|C  ->  (x,c_1)|(c_2,...,c_s)

changes the affected component orders from (1,s) to (2,s-1). Its potential change is

2^2+(s-1)^2-1^2-s^2 = 4-2s < 0,

contradicting Phi-minimality.

Suppose instead that one component has order two. The other two component orders sum to more than eight, so one has order at least five. The general two-vertex balancing lemma repartitions (2,s) to (3,s-1), with potential change 6-2s<0. Again this contradicts Phi-minimality.

Therefore every component of a Phi-minimal spanning three-cover has order at least three.

## Metadata

- ID: toolkit_minimal_three_covers_have_no_components_of_order_one_or_two
- Kind: toolkit
- Version: 1
- Math version: 1
- Audit: unaudited
- Refutation: unrefuted
