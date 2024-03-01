# Direct air capture

Only the solid sorbent DAC process is considered in TIAM-FR, as it is the only operational technology currently. It cincludes heat pumps that provide low-temperature heat to regenerate the sorbent.
though, two types of energy supply are considered, i.e. grid electricity and dedicated renewables from wind or solar.  
Techno-economic properties of DAC technologies are extracted from NASEM (2019) using their high assumption and the energy consumption is assumed following the analysis of Herzog (2022), who calculated that 1071 kWh/tCO2 are required to regenerate the sorbent with a 3.5-coefficient-of-performance heat pump. The calculations are based on the assumption that 1 Mtpa DAC plants are to be invested in for 20 years lifespan with a capacty factor of 90% and a discrount rate of 8.5% . 
In the case where variable renewable energy (VRA) powers the DAC plants, additional captial costs equal to $300/kWh (McQueen et al., 2021) are included to reflect the need for batteries:

$$
C_{battery} = C_{VRA} \cdot 24 \cdot (1-AF_{VRA}) \tag{1}
$$

$C_{VRA}$ and $AF_{VRA}$ respectively denote the required installed capacity of VRA and their availability factor. As DAC plants are run 90% of the time, the renewable capacities need to be oversized according to their capacity factor, which is estimated on average at 20%. The capacity of VRA is thus calculated following equation (2): 

$$
C_{VRA}= \frac{T_{ec}}{8760 \cdot AF_{VRA}} \tag{2}
$$

Where $T_{ec}$ is the total energy consumption in MWh/tCO2,

The assumed techno-economic parameters are summarized in the following table.

Table 1: Techno-economic properties of DAC in TIAM-FR
|               |Units|SNKDACSSGRD|SNKDACSSVRA|
|---------------|-----|-----------|-----------|
|Efficiency     |PJ/kt|     0.0046|     0.0046|
|Investment cost|M$/kt|      2.099| 2.892     |
|Fixed operation cost|M$/kt|      0.0222| 0.0222|
|Variable operational cost|M$/kt|0.0080|0.0080|
|Lifespan|years|20|20|
|Discount rate||8.5%|8.5%|

The DAC units generate an certain amount of atmospheric CO2 captured which can be either [utilized](synthetic-fuels.md) or [stored](co2-storage.md). For more details on the techno-economic assumptions, please consult (Desport et al., 2024)

## References
NASEM, 2019. Negative Emissions Technologies and Reliable Sequestration: A Research Agenda. National Academies Press, Washington, D.C. https://doi.org/10.17226/25259  
Herzog, H., 2022. Chapter 6. Direct Air Capture, in: Bui, M., Mac Dowell, N. (Eds.), Energy and Environment Series. Royal Society of Chemistry, Cambridge, pp. 115–137. https://doi.org/10.1039/9781839165245-00115  
McQueen, N., Gomes, K.V., McCormick, C., Blumanthal, K., Pisciotta, M., Wilcox, J., 2021. A review of direct air capture (DAC): scaling up commercial technologies and innovating for the future. Prog. Energy 3, 032001. https://doi.org/10.1088/2516-1083/abf1ce  
Desport, L., Gurgel, A., Morris, J., Herzog, H., Chen, Y.-H.H., Selosse, S., Paltsev, S., 2024. Deploying direct air capture at scale: How close to reality? Energy Economics 129, 107244. https://doi.org/10.1016/j.eneco.2023.107244
