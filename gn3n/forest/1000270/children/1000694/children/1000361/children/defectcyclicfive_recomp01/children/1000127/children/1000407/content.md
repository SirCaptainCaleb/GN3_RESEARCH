# The three-isolated-defect cube has an exact discrete-gradient size parametrization

## Statement

Let the three isolated cyclic defect edges occur in cyclic order, and for each edge i choose a reference endpoint and encode the selected cut endpoint by x_i in {0,1}. Then, after cyclically labeling the three path components, there are fixed positive integers g_1,g_2,g_3 such that the cube state x=(x_1,x_2,x_3) has component orders
s_1=g_1+x_2-x_1, s_2=g_2+x_3-x_2, s_3=g_3+x_1-x_3.
Consequently every cube state differs from the base gap vector g by a cyclic discrete gradient, each coordinate differs from its base value by at most one, and flipping x_i transfers exactly one vertex between the two components adjacent to defect edge i.

## Body

Fix on each isolated defect edge e_i its two consecutive cyclic cut positions L_i,R_i, with R_i immediately after L_i, and write the chosen cut as c_i=L_i+x_i. Let g_i be the number of vertices in the cyclic interval component from L_i to L_{i+1} under the all-zero choice, with the same convention for which cut endpoint belongs to which adjacent component as in the cyclic-interval construction. Moving c_i from L_i to R_i removes exactly one boundary vertex from the component immediately following c_i and adds it to the component immediately preceding c_i. Therefore the component between cuts i and i+1 gains x_{i+1} from moving its terminal cut forward and loses x_i from moving its initial cut forward. Hence s_i=g_i+x_{i+1}-x_i, cyclically. The transfer and coordinate bounds are immediate.