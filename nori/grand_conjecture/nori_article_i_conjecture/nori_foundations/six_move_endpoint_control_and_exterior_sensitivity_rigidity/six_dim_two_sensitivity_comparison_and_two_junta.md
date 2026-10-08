# Two sensitivities force a comparison coloring; three are impossible

## Development

Statement:
Under the hypotheses of the preceding lemma, let T=(a,b,c) and U={d,e,f}. If C_T is sensitive to both exterior bits d and e, then every ordered triple σ on U is face-independent, and there exists h∈{0,1} such that C_σ=h when d occurs before e in σ, and C_σ=1-h when e occurs before d. Consequently, for every ordered triple T in any hypothetical six-dimensional NORI counterexample, C_T depends on at most two of its three exterior bits (a two-junta).

Proof:
Apply the preceding lemma to sensitivity in d, obtaining constants h_d on the two orderings of U beginning with d and 1-h_d on the two ending with d. Apply it likewise to sensitivity in e, obtaining h_e on orders beginning with e and 1-h_e on orders ending with e. The ordering (d,f,e) begins with d and ends with e, so h_d=1-h_e. These relations determine all six orders of U: (d,e,f),(d,f,e),(f,d,e) have value h_d, whereas (e,d,f),(e,f,d),(f,e,d) have value 1-h_d. They are exactly the orders distinguished by d preceding e. If C_T were also sensitive to f, applying the preceding lemma in direction f would force C_{fde}=C_{fed}, since both orders begin with f. The established comparison rule instead gives C_{fde}=h_d and C_{fed}=1-h_d, contradiction. Since there are precisely three exterior coordinates in Q_6, each C_T is sensitive to at most two. A Boolean function independent of its remaining inessential coordinate depends only on at most two exterior bits.
