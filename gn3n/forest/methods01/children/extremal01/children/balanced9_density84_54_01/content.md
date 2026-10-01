# Nine vertices force at least 84 Hamiltonian five-sets and 54 Hamiltonian four-sets

## Statement

Every boundary tournament on nine vertices has at least 84 Hamiltonian five-vertex subsets and at least 54 Hamiltonian four-vertex subsets.

## Body

For the five-set count, count incidences (F,E) where E is a six-set and F is a Hamiltonian five-set contained in E. By the four-of-six theorem in smallset01, every six-set contains at least four Hamiltonian five-subsets. There are C(9,6)=84 six-sets, so there are at least 84*4=336 incidences. Every five-set lies in exactly four six-sets, hence the number h_5 of Hamiltonian five-sets satisfies 4h_5>=336 and therefore h_5>=84.

For the four-set count, fix an unordered pair T={u,v}. By 1000615, the other seven vertices split into two fixed-pair orientation classes, and any two vertices in the same class complete T to a Hamiltonian four-set. If the class sizes are c and 7-c, this yields C(c,2)+C(7-c,2)>=9 same-class exterior pairs. Summing over the C(9,2)=36 choices of T gives at least 324 witness incidences (T,F). A four-set has only six unordered pairs, so it contributes to at most six incidences. Hence h_4>=324/6=54.