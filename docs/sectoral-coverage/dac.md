# Direct air capture

Only the solid sorbent DAC process is considered in TIAM-FR, as it is the only operational technology currently. It cincludes heat pumps that provide low-temperature heat to regenerate the sorbent.
though, two types of energy supply are considered, i.e. grid electricity and dedicated renewables from wind or solar.  
Techno-economic properties of DAC technologies are extracted from NASEM (2019) using their high assumption and the energy consumption is assumed following the analysis of Herzog (2022), who calculated that 1071 kWh/tCO2 are required to regenerate the sorbent with a 3.5-coefficient-of-performance heat pump. The calculations are based on the assumption that 1 MTpa DAC plants are to be invested in for 20 years lifespan with a capacty factor of 90% and a discrount rate of 8.5%  
In the case where variable renewable energy (VRA) powers the DAC plants, additional captial costs equal to $300/kWh (McQueen et al., 2021) are included to reflect the need for batteries:

$$
C_{battery} = C_{VRA} \cdot 24 \cdot (1-AF_{VRA})
$$

$C_{VRA}$ and $AF_{VRA}$ respectively denote the required installed capacity of VRA and their availability factor.
