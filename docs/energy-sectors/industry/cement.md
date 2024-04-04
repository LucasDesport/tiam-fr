# Cement

The representation of cement production in TIAM-FR is - with iron and steel - more complex than the res of the industry.  
Figure 1 represents the modeling of the cement industry in TIAM-FR, from energy commodities inputs to cement demand. The cement industry is disaggregated into four steps. The first one computes the optimal fuel mix to feed cement plants, considering substitution rates detailed the subsequent section. The second one processes energy and limestone to produce clinker, that is processed in the third step with other aggregates to produce cement. For the base year, the global cement industry is represented according to IEA’s energy balances (IEA, 2020a) for energy flows and cement demand. Regarding the clinker-to-cement ratio, several references listed in Table 1 are used to calculate the statistic energy efficiency of the existing assets (INMCEMPLA00) in 2018. The shares of aggregates (fly ash blast furnace slags, limestone, and gypsum) are assumed proportionally distributed across regions compared to the global average (IEA, 2020b). Due to lack of data, the material efficiency, the operational cost, and the fixed cost are set for every region to 1.26 tlimestone/tclinker, 21.9 $/tclinker, 1.29 $/tclinker (Griffin et al., 2013), but regional costs of limestone are taken from (Ferrari et al., 2019).

![](cement.png)

The energy consumption of the global cement industry is disaggregated for each regions of TIAM-FR according to the types of energy ; either solid fuels (coal, coke, pet coke, oven coke, municipal waste, biochar, wood biomass, pellets or torrefied pellets), gaseous fuels (natural gas, coke oven gas, liquefied petroleum gas, blast furnace gas, biogas or synthetic biomethane), or liquid fuels (heavy fuel oil, or a predefined mix of fossil (resp. bio-based) diesel and gasoline (INMOIL) (resp. INMBOIL)). This choice is made as the type of kilns and burners in cement plants depend on the state of energy used and other infrastructures such as storage tanks or pipelines that is difficult to consider in TIAM-FR. We isolate heat and electricity because these energy carriers cannot be used in conventional kilns, i.e. they require a substantial capital investment. If the fuels are ultimately processed in cement plants equipped with carbon capture units, the amount of CO<sub>2<\sub> captured is accounted at the same level of the RES. Once CO<sub>2<\sub> is captured, it can be either [stored](non-energy-sectors/co2-transport-and-storage.md) or converted into [synthetic fuels](supply/synthetic-fuels.md) or [minerals](backstop/mineralization.md).  
Assuming that the lifetime of cement plants approximates 40 years (Cembureau, 2018a; IEA, 2020a), the remaining lifetime of current assets is evaluated in Table 2 for each region based on (IEA, 2020d).

Table 1: clinker-to-cement ratio in the base-year across regions of TIAM-FR
| **Region** | **Clinker-to-cement ratio** | **Reference**                        |
| ---------- | --------------------------- | ------------------------------------ |
| **AFR**    | 75%                         | (IEA, 2017)                          |
| **AUS**    | 84%                         | (Global Cement, 2022)                |
| **CAN**    | 83%                         | (Cement Association of Canada, 2010) |
| **CHI**    | 65%                         | (IEA, 2020d)                         |
| **CSA**    | 71%                         | (Rowland, 2021)                      |
| **EEU**    | 82%                         | (IEA, 2017)                          |
| **FSU**    | 85%                         | (IEA, 2017)                          |
| **IND**    | 73%                         | (Rowland, 2021)                      |
| **JPN**    | 83%                         | (Taiheiyo Cement, n.d.)              |
| **MEA**    | 80%                         | (IEA, 2017)                          |
| **MEX**    | 77%                         | (Rowland, 2021)                      |
| **ODA**    | 78%                         | (IEA, 2017)                          |
| **SKO**    | 92%                         | (Andrew, 2019)                       |
| **USA**    | 89%                         | (Rowland, 2021)                      |
| **WEU**    | 74%                         | (Cembureau, 2018b)                   |

Table 2: Remaining lifetime of existing assets across regions of TIAM-FR
| **AFR** | **AUS** | **CAN** | **CHI** | **CSA** | **EEU** | **FSU** | **IND** | **JPN** | **MEA** | **MEX** | **ODA** | **SKO** | **USA** | **WEU** |
| ------- | ------- | ------- | ------- | ------- | ------- | ------- | ------- | ------- | ------- | ------- | ------- | ------- | ------- | ------- |
| 26      | 26      | 22      | 28      | 24      | 27      | 21      | 27      | 18      | 26      | 24      | 26      | 26      | 21      | 27      |

## Fuel-switching measures



## References

IEA, 2020. World Energy Balances – Analysis [WWW Document]. IEA. URL https://www.iea.org/reports/world-energy-balances-overview (accessed 3.14.22).  
Andrew, R.M., 2019. Global CO2 emissions from cement production, 1928–2018. Earth System Science Data 11, 1675–1710. https://doi.org/10.5194/essd-11-1675-2019  
Cembureau, 2018. Clinker Substitution [WWW Document]. Cembureau. URL https://lowcarboneconomy.cembureau.eu/5-parallel-routes/resource-efficiency/clinker-substitution/ (accessed 11.29.23).  
Cement Association of Canada, 2010. Canadian Cement Industry - Sustainability Report [WWW Document]. URL https://www.atlanticconcrete.ca/images/ENGLISH_FINAL_2010_SD_Report_Mar17.pdf (accessed 11.29.23).  
Global Cement, 2022. Slashing cement’s CO2 emissions Down Under [WWW Document]. URL https://www.globalcement.com/news/item/14855-slashing-cement-s-co2-emissions-down-under (accessed 11.29.23).  
IEA, 2020. Energy Technology Perspectives 2020. Energy Technology Perspectives 400.  
Rowland, J., 2021. A Net-Zero Cement and Concrete Industry – Cement Products. URL https://cementproducts.com/2021/09/18/a-net-zero-cement-and-concrete-industry/ (accessed 11.29.23).  
Taiheiyo Cement, n.d. ESG Data [WWW Document]. URL https://www.taiheiyo-cement.co.jp/english/csr/pdf/data/2022/rep_14.pdf (accessed 11.29.23).  
Griffin, P., Hammond, G., Norman, J., 2013. Industrial Energy Use from a Bottom-Up Perspective: Developing the Usable Energy Database (Beta version) 53.  
Ferrari, N., Mancuso, L., Burnard, K., Consonni, F., 2019. Effects of plant location on cost of CO2 capture. International Journal of Greenhouse Gas Control 90, 102783. https://doi.org/10.1016/j.ijggc.2019.102783  
IEA, 2020. CCUS in clean energy transitions. Energy Technology Perspectives 174.  
Cembureau, 2018. Thermal Energy Efficiency [WWW Document]. Cembureau. URL https://lowcarboneconomy.cembureau.eu/5-parallel-routes/energy-efficiency/thermal-energy-efficiency/ (accessed 11.30.23).    
IEA, 2020. Energy Technology Perspectives 2020. Energy Technology Perspectives.  

