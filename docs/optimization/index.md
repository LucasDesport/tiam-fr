# Optimization

In linear programming, an optimization problem consists in minimizing or maximizing an objective function which is expressed by decision variables subject to constraints. In TIAM-FR, the optimization problem determines the partial economic equilibrium  of the energy system, or the total discounted cost minimized over all periods of the model’s horizon, while respecting any technical, environmental, and policy constraints, represented in the matrix $B$ and vector $b$ of the following equation.

$$
\min c \cdot X
$$

$$
s.t. \forall t \in T, \forall i \in I, Q_{k,i} (t) \geq D_i (t)
$$

$$
B \cdot X \geq b
$$

Thus, the solver minimizes the total discounted cost $c$ of invesment decisions $X$ at each period $t$ and for all demands $i$, quch that the installed capcities $Q_{k,i}$ satisfy the exogenous demand for energy services $D_i$. The vector of variables include activity levels of technologies, total installed capacities of technologies, additional capacities, quantities of commodity consumed or produced within processes, quantities of commodities stored or discharged, quantities of commodities traded across regions.  
the objective function corresponds to the net present value $NPV$ of the total discounted cost of the energy system of each region $Cost_{r,t}$, which can be expressed as follows:

$$
NPV = \sum_r \sum_t (1+d_{r,t})^{BY-t} \cdot Cost_{r,t} 
$$

where $BY$ is the base year, which is 2018 in TIAM-FR.

In TIAM-FR, the linear program is formulated in GAMS (General Algebraic Modelling System) and solved with the linear programming optimizer CPLEX, by 
minimizing the total discounted cost of the energy system. 

For an exhaustive and comprehensive description of optimization problems in TIMES models, please consult the [ETSAP documentation](https://github.com/etsap-TIMES/TIMES_Documentation/blob/master/Documentation_for_the_TIMES_Model-Part-II.pdf).
