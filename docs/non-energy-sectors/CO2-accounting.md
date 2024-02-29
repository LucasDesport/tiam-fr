# CO<sub>2</sub> accounting

As the environmental impact of CCS and CCU is very dependent on the nature of the carbon – fossil or climate-neutral – the modeling developed in TIAM-FR ensures transparent accounting of CO<sub>2</sub> emissions in which each sector is responsible only for its direct emissions, illustrated in the figure below.

![Accounting of CO2 fluxes in TIAM-FR](co2-accounting.png)
Fig. 1: Accounting of CO<sub>2</sub> fluxes in TIAM-FR


Regardless the fossil resource powering a process, all the carbon within that resource is emitted as CO<sub>2</sub> into the atmosphere. When the process incorporates a carbon capture unit, a certain proportion of the carbon is released due to imperfect capture efficiency (90% or 60% dependig on the process). However, the amount of the captured CO<sub>2</sub> (CPTCO2) is directed to dummy processes (depicted in yellow in Figure 2). The solver decides whether this CO<sub>2</sub> is used or stored. These sector-specific dummy processes efficiently aggregate the bulk of captured CO<sub>2</sub> into two commodities for storage (SNKCO2) or utilization (CO2FOS).

On one hand, the CCUFOS commodity is transformed by the CCU plant into a fuel (SYNFUEL) containing fossil carbon (90% of the initial amount). It undergoes processing by a sector-specific *FuelTech* before being utilized in the end-use process. In TIMES modeling, *FuelTechs*, or Fuel Technologies, prevent duplicating end-use processes based on the type of fuel they consume. For instance, the model includes a *FuelTech* named FT_TRAMET (Figure 21), handling various methanol commodities to produce a single methanol commodity (TRAMET) for end-use processes in the transport sector (TRA), such as trucks and light vehicles. At this stage of the reference energy system (RES), the reemitted CO<sub>2</sub> is allocated to the sector responsible for its emission, following the fuel's emissions factor.
