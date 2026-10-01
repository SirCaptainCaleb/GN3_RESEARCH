# Exact rank-sensitive master inequality for the three-uniform Astra-multiplicity synthesis

## Statement

Let H be a finite linear 3-graph. For each nonisolated vertex v put p(v)=phi(v), let t(v) count ascending nonspecial edges terminal at v, and if t(v)>0 let q(v) be their maximum rank. Choose P_v to end in a rank-p(v) ascending terminal edge whenever q(v)=p(v), and arbitrarily otherwise. Define
B(v)=0 if t(v)=0;
B(v)=ceil((3p(v)-4)/4) if q(v)=p(v);
B(v)=gamma(q(v)) if 0<q(v)<p(v),
where gamma(1)=0,gamma(2)=1,gamma(3)=2 and gamma(q)=floor((11q-5)/8) for q>=4.
Then
3m <= 2S-n_+ + (1/2)sum_v B(v),
where S=sum_v phi(v). Equivalently
m <= (2S-n_+)/3 + (1/6)sum_v B(v).
This retains the exact local rank q(v), exact low-rank corrections, and exact aligned multiplicity cancellation.

## Body

Let X_v be excess chosen-path contact multiplicity and X=sum_v X_v. For an aligned active vertex q(v)=p(v), choose P_v to end in a top-rank ascending edge. The exact singleton/double-contact inequality cac6635878e5 gives t(v)-X_v <= ceil((3p(v)-4)/4)=B(v), because every nonsingleton contact contributes at least its first unit to X_v. For a misaligned active vertex, discard X_v>=0 and apply the exact fixed-entrance terminal bound at a maximum-rank ascending terminal edge: t(v)-X_v<=t(v)<=gamma(q(v))=B(v). For t(v)=0 one has t(v)-X_v<=0=B(v). Summing over vertices and using sum_v t(v)=2A gives
2A-X <= sum_v B(v).
Since X>=0, 2(A-X)<=2A-X, hence A-X <= (1/2)sum_v B(v). The three-uniform contact-multiplicity inequality gives
3m <= 2S-n_+ +(C-X),
and every clean incidence belongs to an ascending nonspecial edge, so C<=A. Therefore C-X<=A-X <= (1/2)sum_v B(v), proving the claim.