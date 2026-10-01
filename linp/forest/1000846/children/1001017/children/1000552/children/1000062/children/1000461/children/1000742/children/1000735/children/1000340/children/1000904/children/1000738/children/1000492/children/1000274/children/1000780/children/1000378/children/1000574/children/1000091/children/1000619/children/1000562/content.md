# Maximum-rank terminal transfer reaches a charged step or alignment within the rank gap

## Statement

Let v_0 be active, with p_0=phi(v_0), q_0=q(v_0), and Delta_0=p_0-q_0. Starting at v_i, choose an ascending nonspecial edge e_i={x_i,v_i,v_{i+1}} of rank q(v_i), where v_i and v_{i+1} are its two terminals. If every chosen step strictly decreases endpoint potential, phi(v_{i+1})<phi(v_i), then Delta(v_{i+1})<=Delta(v_i)-1. Consequently after at most Delta_0 strict-decrease steps one reaches an aligned vertex Delta=0. Equivalently, before then either alignment occurs or some maximum-rank terminal edge is potential-charged at its current vertex, with phi(v_{i+1})>=phi(v_i). If p_0>=8, q_0>=4, q_0<p_0, and eta_{v_0} is the local defect from b032348c1a8a, then Delta_0<=1+(8/11)(eta_{v_0}+1).

## Body

Every chosen edge e_i is itself an ascending edge terminal at v_{i+1}, of rank q(v_i). Hence v_{i+1} is active and q(v_{i+1})>=q(v_i) by 8bdbdf84d6bc. If phi(v_{i+1})<phi(v_i), integrality gives phi(v_{i+1})<=phi(v_i)-1, and therefore Delta(v_{i+1})=phi(v_{i+1})-q(v_{i+1})<=phi(v_i)-1-q(v_i)=Delta(v_i)-1. Thus Delta drops by at least one on every strict-potential-decrease step. Since Delta is a nonnegative integer, at most Delta_0 such steps can occur before Delta=0. Therefore a transfer trajectory either reaches an aligned vertex in that many decreasing steps or earlier contains a nondecreasing-potential step phi(v_{i+1})>=phi(v_i), in which case the chosen maximum-rank ascending edge is potential-charged at v_i. For the quantitative final assertion, b032348c1a8a gives p_0-1-q_0<=(8/11)(eta_{v_0}+1) when p_0>=8 and q_0>=4. Adding one yields Delta_0=p_0-q_0<=1+(8/11)(eta_{v_0}+1).
