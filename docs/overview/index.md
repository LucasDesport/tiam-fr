# Overview

TIAM-FR is the French version of the TIMES Integrated Assessment Model (TIAM). TIAM is the global version of the TIMES family models developed
under the Energy Technology System Analysis Program (ETSAP, 2021). The Integrated MARKAL -EFOM  System (or TIMES) is the successor of two model 
paradigms known as MARKAL and EFOM, which respectively model market allocations and commodities fluxes and were developed in the early 1980s by 
ETSAP. TIMES is a generator of partial equilibrium techno-economic models representing the energy system of geographical areas – or regions – on
a long-term horizon. It enables an assessment and discussion of the evolution of energy systems from a technological perspective and according
to climate policies (taxes, agreements, etc.). It has been used for a wide range of applications at the local level
(Andrade, 2022; Genave, 2021; Selosse et al., 2018), national level (Assoumou, 2006; Doudard, 2017; Gaur et al., 2022; Millot et al., 2020; Seljom and Tomasgard, 2017),
continental level (Postic, 2015; Siggini, 2022), and global level (Boubault and Maïzi, 2019; Kang, 2017; Morfeldt et al., 2015; Seck et al., 2022a; Selosse, 2019).
As part of the TIMES model family, TIAM-FR is a linear programming partial equilibrium model. It is categorized as a bottom-up model because of 
its technology-rich description of the energy system, depicting and tracking how energy is extracted, transformed, and used in the world. Linear
programming is formulated in the GAMS (General Algebraic Modelling System) language and solved with the linear programming optimizer CPLEX, by 
minimizing the total discounted cost of the energy system. The main results that can be discussed with TIAM-FR are the levels of GHG emissions, 
the primary energy use, the final energy use, the technologies processing final energy and satisfying energy demand, the marginal cost of 
producing energy or material commodities, and the total cost of satisfying global energy demand. 

