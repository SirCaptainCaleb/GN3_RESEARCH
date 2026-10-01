# Reciprocal singleton transfer strictly decreases quadratic cover potential

## Statement

In the reciprocal-one-crossing singleton-transfer configuration with component orders (lambda,lambda,1), lambda>=5, the Astra-003 move component contains a three-cover with strictly smaller quadratic potential Phi=sum |P|^2. In the three branches of astra003plateauescape the drop Phi_initial-Phi_new is respectively 6lambda-20, 6lambda-24, or 8lambda-32, hence at least 6. Consequently no Phi-minimal trapped three-cover can itself be a reciprocal singleton-transfer state.

## Body

# Strict quadratic descent from the reciprocal singleton-transfer state

Start from any of the reciprocal singleton-transfer covers C_x,C_m,C_y. Each has component orders

(lambda,lambda,1),

so

Phi_0=2lambda^2+1.

The certified plateau-escape theorem astra003plateauescape supplies one of three covers in the same Astra-003 connected component.

1. If the left endpoint window is Hamiltonian, the new component orders are

(lambda-1,lambda-2,4).

Hence

Phi_1=(lambda-1)^2+(lambda-2)^2+16=2lambda^2-6lambda+21,

and

Phi_0-Phi_1=6lambda-20.

2. If the left window is non-Hamiltonian and the right window is Hamiltonian, the new orders are

(lambda,lambda-3,4).

Thus

Phi_2=lambda^2+(lambda-3)^2+16=2lambda^2-6lambda+25,

and

Phi_0-Phi_2=6lambda-24.

3. If both endpoint windows are non-Hamiltonian, the five-bridge cover has orders

(lambda-2,lambda-2,5).

Therefore

Phi_3=2(lambda-2)^2+25=2lambda^2-8lambda+33,

and

Phi_0-Phi_3=8lambda-32.

The reciprocal-one-crossing shell has lambda>=5. The three drops are therefore at least 10, 6, and 8 respectively. In every branch Phi strictly decreases, by at least 6.

Consequently the reciprocal singleton-transfer state is not merely outside an equality plateau: it cannot be a quadratic-potential minimum of any trapped Astra-003 connected component. Any terminal obstruction to pairwise repartition must occur only after this descent and must satisfy the pairwise imbalance-minimality conditions of the quadratic-potential reduction.
