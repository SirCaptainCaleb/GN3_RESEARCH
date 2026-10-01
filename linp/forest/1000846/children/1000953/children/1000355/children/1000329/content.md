# Characteristic-two additive blow-ups lift every fixed base cycle to an almost q-fold path

## Statement

Let T contain a linear cycle of length s>=3 and let q=2^k be sufficiently large. Its coordinatewise additive F_q blow-up contains a linear path of length at least s(q-2). Hence its normalized density at the first forbidden path length is at most m/(vs)+o(1). For AG(2,3), a base four-cycle gives a 4q-8 path and asymptotic coefficient at most 1/3.

## Body

Let E_1,...,E_s be the base cycle with successive joint clusters X_0,...,X_{s-1}. Let g generate F_q^*. Choose alpha!=1 with alpha^{s-1}!=g, possible for fixed s and sufficiently large q, and set a_t=g^t for 0<=t<=q-2. For each 0<=t<=q-3, choose one lifted lap whose joint coordinates are a_t,alpha a_t,...,alpha^{s-1}a_t,g a_t. In characteristic two the private coordinates are fixed nonzero scalar multiples of a_t, namely alpha^{i-1}(1+alpha)a_t for i<s and (alpha^{s-1}+g)a_t on the last edge. Hence coordinates are distinct within every cluster except at intended consecutive joints. The q-2 laps concatenate to a linear path of length s(q-2).

The blow-up has qv vertices and q^2m edges, so its normalized density at the first forbidden length is (mq/v)/(s(q-2)+1)=m/(vs)+o(1). For AG(2,3), v=9,m=12,s=4, giving path length 4q-8 and coefficient 1/3+O(1/q).
