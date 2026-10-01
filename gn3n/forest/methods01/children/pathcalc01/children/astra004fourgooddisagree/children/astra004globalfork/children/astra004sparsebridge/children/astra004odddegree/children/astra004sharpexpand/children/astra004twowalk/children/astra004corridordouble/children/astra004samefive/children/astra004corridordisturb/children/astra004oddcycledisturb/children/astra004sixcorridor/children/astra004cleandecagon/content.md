# A clean degree-two cycle without three-step label repetition forces odd degree at least three

## Statement

Let H be a minimum counterexample in the sharp half-order shell |V(H)|=2lambda+1, and let G be the Hamiltonian-support odd graph. Let S_0S_1...S_{m-1}S_0 be a simple 2-regular support cycle, with edge S_iS_{i+1} labelled x_i, and choose one Hamilton order on each support. Assume every length-two subwalk is in the clean branch of astra004twowalk and x_{i+3}!=x_i for every i (indices modulo m). Then G has a vertex of degree at least three. More precisely, the clean endpoint replacements force x_{i+5}=x_i, the cycle has length ten, and there are two disjoint ordered cores C,C_prime of order lambda-2 and five distinct active labels a_0,...,a_4 such that the five even supports are C plus the five edges of a 5-cycle on the active labels and the five odd supports are C_prime plus the same five endpoint pairs. Applying commonmiddle01 to two disjoint even endpoint-pairs creates a Hamiltonian support on a chord of that 5-cycle; the existing odd support carried by the unique 5-cycle edge disjoint from that chord thereby acquires a third odd neighbor. Consequently, under Delta(G)<=2, every all-clean 2-regular component must contain a three-step repeated label x_{i+3}=x_i.

## Body

# Proof

For a clean length-two walk S_i-S_{i+1}-S_{i+2}, let epsilon_i be the endpoint side on which the chosen Hamilton order on S_i replaces x_{i+1} by x_i to obtain the chosen order on S_{i+2}. Thus x_i is the endpoint of S_{i+2} on side epsilon_i. Compare the clean steps i and i+2. If epsilon_{i+2}=epsilon_i, then the next removed label is precisely that endpoint, so x_{i+3}=x_i. By hypothesis this never occurs. Hence epsilon_{i+2} is the opposite side from epsilon_i for every i.

Now compare steps i,i+2,i+4. After step i, x_i occupies side epsilon_i of S_{i+2}. Step i+2 uses the opposite side, so it removes the other endpoint and leaves x_i untouched; hence x_i is still the endpoint on side epsilon_i of S_{i+4}. Since epsilon_{i+4} is opposite epsilon_{i+2}, it equals epsilon_i. Step i+4 therefore removes x_i. Its removed label is x_{i+5}, so x_{i+5}=x_i for every i.

The clean support exchange formula gives S_{i+2}=(S_i-{x_{i+1}}) union {x_i}. Five successive jump-two exchanges therefore remove the labels x_{i+1},x_{i+3},x_{i+5},x_{i+7},x_{i+9} and insert x_i,x_{i+2},x_{i+4},x_{i+6},x_{i+8}. By x_{j+5}=x_j these two multisets agree, so S_{i+10}=S_i. Since the support cycle is simple, its length divides ten. It cannot have length one or two. It cannot have length five: bf783b4eef1e says every label on an odd closed walk occurs with odd parity and in fact every ambient label occurs; but a five-edge cycle has only five edge occurrences while |V(H)|>10. Hence m=10.

Put a_j=x_j for 0<=j<=4. These five labels are distinct. Adjacent labels are distinct because an edge label uniquely determines the opposite support from either endpoint. Labels at distance two are distinct because x_i belongs to S_{i+2} after the clean exchange, whereas x_{i+2} is omitted from S_{i+2}. Distance three equality is excluded by hypothesis. If x_{i+4}=x_i, then after the side flip at step i+2 the endpoint x_i survives in S_{i+4}, contradicting that x_{i+4} is omitted from S_{i+4}. Thus a_0,...,a_4 are pairwise distinct.

Consider the even supports. Cleanliness of step 0 says x_1 is one endpoint of S_0 and x_0 replaces it in S_2. Since step 2 uses the opposite endpoint and removes x_3, the other endpoint of S_0 is x_3. Therefore C=S_0-{a_1,a_3} is the common ordered middle block, of order lambda-2. Successive clean endpoint replacements preserve C and give the five even support sets
C+{a_1,a_3}, C+{a_0,a_3}, C+{a_0,a_2}, C+{a_2,a_4}, C+{a_1,a_4}.
Their chosen Hamilton orders all have the same ordered middle C and the displayed active labels at the two ends. The five displayed pairs form a 5-cycle E on {a_0,...,a_4}.

Because n=2lambda+1, the remaining vertices outside C and the five active labels form a set C_prime of order lambda-2. Taking complements along the odd edges shows that the five odd supports are C_prime plus exactly the same five pairs E (in cyclicly shifted order). Their clean chosen orders similarly share C_prime as common ordered middle.

Choose two disjoint edges e,e_prime of the 5-cycle E. The corresponding two even Hamilton paths have four distinct active endpoints and common ordered middle C. By commonmiddle01 the two mixed endpoint paths are also tight. Their endpoint pairs are the two cross-pairs between e and e_prime. At least one cross-pair g is not an edge of E, since E is a 5-cycle and contains no 4-cycle on those four endpoints. Hence C+g is a new Hamiltonian lambda-support.

Every chord g of a 5-cycle is disjoint from a unique cycle edge f in E. The odd support C_prime+f is one of the ten original cycle vertices. The supports C+g and C_prime+f are disjoint lambda-sets; their union omits the fifth active label, so they form an odd edge of G. Since g is not in E, C+g is distinct from the two original cycle neighbors of C_prime+f. Therefore deg_G(C_prime+f)>=3. ∎
