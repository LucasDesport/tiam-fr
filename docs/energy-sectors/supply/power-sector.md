# Power sector

The power sector encompasses two energy commodities, namely centralized electricity and decentralized electricity. 
* Centralized electricity can be generated using various fuels and technologies and is consumed directly in end-use sectors.
* Decentralized electricity, is specifically generated from wind, solar, or bioenergy without carbon capture and storage (CCS). It is primarily used in the production of [hydrogen](hydrogen.png) or [synthetic fuels](synthetic-fuels.md).
The power sector can be decarbonized with carbon capture and storage technologies as well as renewables.

## Technologies

###  Fossil fuel with and without CCS

The techno-economics assumed for the various fossil-fired plants are listed in Table 1 without CCS and in Table 2 with CCS. The annual availability factor and the discount rate are uniformely and empirically set to 90% and 10% respectively for all technologies. The construction duration of assets is 4 years (Irlam, 2017) regardless the unit is equipped with carbon capture, but the lifespan of assets equiped with carbon capture is 25 years againt 30 years. The regional variation of techno-economics is taken into consideration based on the findings of Ferrari et al. (2019). Carbon capture becomes available as of 2030.

Table 1: Techno-economic assumptions of fossil-fired power plants without CCS
| Fossil fuel plant                                         | CAPEX  | Fixed O&M | Variable O&M | Efficiency |
| --------------------------------------------------------- | ------ | --------- | ------------ | ---------- |
| Units                                                     | [$/kW] | [$/kW]    | [$/GJ]       |            |
| Coal-fired plant - atmospheric fluidized bed              | 1961   | 89        |              | 44%        |
| Coal-fired plant - Integrated Gasification Combined Cycle | 2265   | 74        | 3.1          | 38%        |
| Coal-fired plant - Pulverized coal subcritical            | 1429   | 38        | 2.5          | 37%        |
| Coal-fired plant - Pulverized coal supercritical          | 1468   | 41        | 1.2          | 36%        |
| Coal-fired plant - Pulverized coal ultra supercritical    | 1665   | 44        | 1.1          | 41%        |
| Gas-fired plant - Fuel cells                              | 4234   | 64        |              | 54%        |
| Gas-fired plant - Steam turbine                           | 1188   | 27        | 0.1          | 40%        |
| Gas-fired plant - Combined Cycle                          | 429    | 23        | 0.2          | 61%        |
| Advanced oil-gas turbine                                  | 339    | 17        |              | 40%        |
| Oil-fired plant - Base-load generation                    | 749    | 3         | 2.8          | 37%        |
| Oil-fired plant - Peak-load generation                    | 672    | 8         | 4.3          | 32%        |
| Oil-fired plant - Steam turbine                           | 1188   | 27        | 0.1          | 40%        |

Table 2: Techno-economic assumptions of fossil-fired power plants with CCS
| Fossil fuel plant                                          | CAPEX  | Fixed O&M | Variable O&M | Efficiency | Capture rate | Reference |
| ---------------------------------------------------------- | ------ | --------- | ------------ | ---------- | ------------ | --------- |
| Units                                                      | [$/kW] | [$/kW]    | [$/GJ]       |            |              |           |
| NGCC with post capture                                     | 1366   | 40        | 0.3          | 55%        | 90.0%        | GCCSI     |
| Advanced turbines with post capture                        | 763    | 24        | 0.7          | 36%        | 90.0%        | GCCSI     |
| NGCC with post capture 90%                                 | 1211   | 45        | 0.3          | 56%        | 90.0%        | IEAGHG    |
| NGCC with post capture 98,5%                               | 1305   | 48        | 0.4          | 54%        | 98.5%        | IEAGHG    |
| NGCC with post capture 90% FGR                             | 1149   | 43        | 0.2          | 56%        | 90.0%        | IEAGHG    |
| NGCC with post capture 98,5% FGR                           | 1210   | 45        | 0.2          | 55%        | 98.5%        | IEAGHG    |
| IGCC with post capture                                     | 4874   | 96        | 5.6          | 31%        | 90.0%        | GCCSI     |
| Supercritical pulverized coal with oxycombustion           | 3479   | 64        | 1.6          | 29%        | 90.0%        | GCCSI     |
| Supercritical pulverized coal with oxycombustion ITM       | 3204   | 58        | 1.5          | 29%        | 90.0%        | GCCSI     |
| Ultrasupercritical pulverized coal with oxycombustion      | 3343   | 61        | 1.4          | 37%        | 90.0%        | GCCSI     |
| Supercritical pulverized coal with post capture1           | 3454   | 55        | 4.6          | 33%        | 90.0%        | GCCSI     |
| Supercritical pulverized coal with post capture2           | 3479   | 66        | 2.3          | 29%        | 90.0%        | GCCSI     |
| Ultrasupercritical pulverized coal with post capture       | 3420   | 64        | 2.0          | 33%        | 90.0%        | GCCSI     |
| Ultrasupercritical pulverized coal with post capture 90%   | 3585   | 80        | 3.3          | 37%        | 90.0%        | IEAGHG    |
| Ultrasupercritical pulverized coal with post capture 98,5% | 3797   | 85        | 3.7          | 35%        | 98.5%        | IEAGHG    |

### Bioenergy with and without CCS

The techno-economic assumptions for bioenergy-fired plants, as summarized in Table 3, are based on data from Kang (2017). To account for the additional costs of integrating a carbon capture unit, we assume that the required effort is equivalent to that for coal-fired power plants. Therefore, we apply the same scaling factor used for coal (Table 4).

Table 3: Techno-economic assumptions of bioenergy-fired power plants without CCS
| Technology                          | CAPEX  | Fixed O&M | Variable O&M | Efficiency | Availability factor |
| ----------------------------------- | ------ | --------- | ------------ | ---------- | ------------------- |
| Units                               | [$/kW] | [$/kW]    | [$/GJ]       |            |                     |
| Pellet direct combustion            | 1898   | 67        | 3.3          | 39%        | 85%                 |
| Pellet gasification                 | 2149   | 86        | 4.5          | 40%        | 90%                 |
| Torrefied pellets direct combustion | 1898   | 67        | 3.3          | 39%        | 85%                 |
| Torrefied pellets gasification      | 2149   | 86        | 4.5          | 41%        | 90%                 |

Table 4: Techno-economic assumptions of bioenergy-fired power plants with CCS
| Technology                                              | CAPEX  | Fixed O&M | Variable O&M | Efficiency |
| ------------------------------------------------------- | ------ | --------- | ------------ | ---------- |
| Units                                                   | [$/kW] | [$/kW]    | [$/GJ]       |            |
| Pellet direct combustion with carbon capture            | 3419   | 99        | 6.5          | 28%        |
| Pellet gasification with carbon capture                 | 3932   | 112       | 8.2          | 30%        |
| Torrefied pellets direct combustion with carbon capture | 3419   | 99        | 6.5          | 28%        |
| Torrefied pellets gasification with carbon capture      | 3932   | 112       | 8.2          | 29%        |

#### Co-firing with and without CCS

Co-firing coal and bioenergy can take many forms: the substitution rate of biomass can vary from 5% to 40% with different types of biomass considered (solid biomass, pellets, or torrefied pellets)

Table 5
|                                                 | CAPEX  | Fixed O&M | Variable O&M | Efficiency | Input Share | Input Share | Input Share | Input Share |
| ----------------------------------------------- | --------- | -------- | -------- | ------- | -------- | -------- | -------- | -------- |
| Units                                           | [$/kW]    | [$/kW]   | [$/GJ]   |         | Solid biomass   | Coal   | Pellets   | Torrefied pellets   |   
| Air Blown IGCC.Co-Firing. Co-milling       | 2746      | 96       | 0.62     | 47%     |          | 90%      | 10%      |          |
| Air Blown IGCC.Co-Firing. Parallel         | 3159      | 126      | 0.62     | 47%     |          | 90%      | 10%      |          |
| Air Blown IGCC.Co-Firing. Seperate feeding | 2987      | 149      | 0.62     | 47%     |          | 90%      | 10%      |          |
| Air Blown IGCC.Co-Firing. Parallel         | 3159      | 126      | 0.62     | 47%     |          | 80%      | 20%      |          |
| Air Blown IGCC.Co-Firing. Seperate feeding | 2987      | 149      | 0.62     | 47%     |          | 80%      | 20%      |          |
| Air Blown IGCC.Co-Firing. Parallel         | 3159      | 126      | 0.62     | 47%     |          | 60%      | 40%      |          |
| Air Blown IGCC.Co-Firing. Parallel         | 3159      | 126      | 0.62     | 46%     | 10%      | 90%      |          |          |
| Air Blown IGCC.Co-Firing. Seperate feeding | 2987      | 149      | 0.62     | 46%     | 10%      | 90%      |          |          |
| Air Blown IGCC.Co-Firing. Parallel         | 3159      | 126      | 0.62     | 45%     | 20%      | 80%      |          |          |
| Air Blown IGCC.Co-Firing. Seperate feeding | 2987      | 149      | 0.62     | 45%     | 20%      | 80%      |          |          |
| Air Blown IGCC.Co-Firing. Parallel         | 3159      | 126      | 0.62     | 44%     | 40%      | 60%      |          |          |
| Air Blown IGCC.Co-Firing. Co-milling        | 2746      | 96       | 0.62     | 46%     | 5%       | 95%      |          |          |
| Air Blown IGCC.Co-Firing. Co-milling       | 2746      | 96       | 0.62     | 47%     |          | 90%      |          | 10%      |
| Air Blown IGCC.Co-Firing. Parallel         | 3159      | 126      | 0.62     | 47%     |          | 90%      |          | 10%      |
| Air Blown IGCC.Co-Firing. Seperate feeding | 2987      | 149      | 0.62     | 47%     |          | 90%      |          | 10%      |
| Air Blown IGCC.Co-Firing. Co-milling       | 2746      | 96       | 0.62     | 47%     |          | 80%      |          | 20%      |
| Air Blown IGCC.Co-Firing. Parallel         | 3159      | 126      | 0.62     | 47%     |          | 80%      |          | 20%      |
| Air Blown IGCC.Co-Firing. Seperate feeding | 2987      | 149      | 0.62     | 47%     |          | 80%      |          | 20%      |
| Air Blown IGCC.Co-Firing. Co-milling       | 2746      | 96       | 0.62     | 47%     |          | 60%      |          | 40%      |
| Air Blown IGCC.Co-Firing. Parallel         | 3159      | 126      | 0.62     | 47%     |          | 60%      |          | 40%      |
| Air Blown IGCC.Co-Firing. Seperate feeding | 2987      | 149      | 0.62     | 47%     |          | 60%      |          | 40%      |
| Pulverized Coal.Co-Firing. Co-milling      | 2067      | 72       | 0.70     | 47%     |          | 90%      | 10%      |          |
| Pulverized Coal.Co-Firing. Parallel        | 2480      | 99       | 0.70     | 47%     |          | 90%      | 10%      |          |
| Pulverized Coal.Co-Firing. Seperate feeding | 2308      | 115      | 0.70     | 47%     |          | 90%      | 10%      |          |
| Pulverized Coal.Co-Firing. Parallel        | 2480      | 99       | 0.70     | 47%     |          | 80%      | 20%      |          |
| Pulverized Coal.Co-Firing. Sperate feeding | 2308      | 115      | 0.70     | 47%     |          | 80%      | 20%      |          |
| Pulverized Coal.Co-Firing. Parallel        | 2480      | 99       | 0.70     | 47%     |          | 60%      | 40%      |          |
| Pulverized Coal.Co-Firing. Parallel        | 2480      | 99       | 0.70     | 46%     | 10%      | 90%      |          |          |
| Pulverized Coal.Co-Firing. Seperate feeding | 2308      | 115      | 0.70     | 46%     | 10%      | 90%      |          |          |
| Pulverized Coal.Co-Firing. Parallel        | 2480      | 99       | 0.70     | 46%     | 20%      | 80%      |          |          |
| Pulverized Coal.Co-Firing. Seperate feeding | 2308      | 115      | 0.70     | 46%     | 20%      | 80%      |          |          |
| Pulverized Coal.Co-Firing. Parallel        | 2480      | 99       | 0.70     | 45%     | 40%      | 60%      |          |          |
| Pulverized Coal.Co-Firing. Co-milling       | 2067      | 72       | 0.70     | 46%     | 5%       | 95%      |          |          |
| Pulverized Coal.Co-Firing. Co-milling      | 2067      | 72       | 0.70     | 47%     |          | 90%      |          | 10%      |
| Pulverized Coal.Co-Firing. Parallel        | 2480      | 99       | 0.70     | 47%     |          | 90%      |          | 10%      |
| Pulverized Coal.Co-Firing. Seperate feeding | 2308      | 115      | 0.70     | 47%     |          | 90%      |          | 10%      |
| Pulverized Coal.Co-Firing. Co-milling      | 2067      | 72       | 0.70     | 47%     |          | 80%      |          | 20%      |
| Pulverized Coal.Co-Firing. Parallel        | 2480      | 99       | 0.70     | 47%     |          | 80%      |          | 20%      |
| Pulverized Coal.Co-Firing. Seperate feeding | 2308      | 115      | 0.70     | 47%     |          | 80%      |          | 20%      |
| Pulverized Coal.Co-Firing. Co-milling      | 2067      | 72       | 0.70     | 47%     |          | 60%      |          | 40%      |
| Pulverized Coal.Co-Firing. Parallel        | 2480      | 99       | 0.70     | 47%     |          | 60%      |          | 40%      |
| Pulverized Coal.Co-Firing. Seperate feeding | 2308      | 115      | 0.70     | 47%     |          | 60%      |          | 40%      |

Table 6
| Technology                                                     | CAPEX  | Fixed O&M | Variable O&M | Efficiency | Input share   | Input Share | Input Share | Input Share |
| -------------------------------------------------------------- | ------ | --------- | ------------ | ---------- | -------- | -------- | -------- | -------- |
| Units                                                          | [$/kW] | [$/kW]    | [$/GJ]       |            | Solid biomass | Coal | Pellets | Torrefied pellets |
| Air Blown IGCC.Co-Firing. Co-milling with carbon capture       | 4947   | 142.0     | 1.4          | 37%        |               | 90% | 10% |  |
| Air Blown IGCC.Co-Firing. Parallel with carbon capture         | 5690   | 186.7     | 1.4          | 37%        |               | 90% | 10% |  |
| Air Blown IGCC.Co-Firing. Seperate feeding with carbon capture | 5381   | 220.7     | 1.4          | 37%        |               | 90% | 10% |  |
| Air Blown IGCC.Co-Firing. Parallel with carbon capture         | 5690   | 186.7     | 1.4          | 37%        |               | 80% | 20% |  |
| Air Blown IGCC.Co-Firing. Seperate feeding with carbon capture | 5381   | 220.7     | 1.4          | 37%        |               | 80% | 20% |  |
| Air Blown IGCC.Co-Firing. Parallel with carbon capture         | 5690   | 186.7     | 1.4          | 37%        | 10%           | 90% |  |  |
| Air Blown IGCC.Co-Firing. Seperate feeding with carbon capture | 5381   | 220.7     | 1.4          | 37%        | 10%           | 90% |  |  |
| Air Blown IGCC.Co-Firing. Parallel with carbon capture         | 5690   | 186.7     | 1.4          | 36%        | 20%           | 80% |  |  |
| Air Blown IGCC.Co-Firing. Seperate feeding with carbon capture | 5381   | 220.7     | 1.4          | 36%        | 20%           | 80% |  |  |
| Air Blown IGCC.Co-Firing. Parallel with carbon capture         | 5690   | 186.7     | 1.4          | 35%        | 40%           | 60% |  |  |
| Air Blown IGCC.Co-Firing. Co-milling with carbon capture       | 4947   | 142.0     | 1.4          | 37%        | 5%            | 95% |  |  |
| Pulverized Coal.Co-Firing. Co-milling with carbon capture      | 3724   | 106.9     | 1.4          | 38%        |               | 90% | 10% |  |
| Pulverized Coal.Co-Firing. Parallel with carbon capture        | 4467   | 146.6     | 1.4          | 38%        |               | 90% | 10% |  |
| Pulverized Coal.Co-Firing. Sperate feeding with carbon capture | 4158   | 170.5     | 1.4          | 38%        |               | 90% | 10% |  |
| Pulverized Coal.Co-Firing. Parallel with carbon capture        | 4467   | 146.6     | 1.4          | 38%        |               | 80% | 20% |  |
| Pulverized Coal.Co-Firing. Sperate feeding with carbon capture | 4158   | 170.5     | 1.4          | 38%        |               | 80% | 20% |  |
| Pulverized Coal.Co-Firing. Prallel with carbon capture         | 4467   | 146.6     | 1.4          | 38%        |               | 60% | 40% |  |
| Pulverized Coal.Co-Firing. Parallel with carbon capture        | 4467   | 146.6     | 1.4          | 37%        | 10%           | 90% |  |  |
| Pulverized Coal.Co-Firing. Sperate feeding with carbon capture | 4158   | 170.5     | 1.4          | 39%        | 10%           | 90% |  |  |
| Pulverized Coal.Co-Firing. Parallel with carbon capture        | 4467   | 146.6     | 1.4          | 37%        | 20%           | 80% |  |  |
| Pulverized Coal.Co-Firing. Sperate feeding with carbon capture | 4158   | 170.5     | 1.4          | 37%        | 20%           | 80% |  |  |
| Pulverized Coal.Co-Firing. Prallel with carbon capture         | 4467   | 146.6     | 1.4          | 36%        | 40%           | 60% |  |  |
| Pulverized Coal.Co-Firing. Co-milling with carbon capture      | 3724   | 106.9     | 1.4          | 35%        | 5%            | 95% |  |  |
| Pulverized Coal.Co-Firing. Co-milling with carbon capture      | 3724   | 106.9     | 1.4          | 38%        |               | 90% |  | 10% |
| Pulverized Coal.Co-Firing. Parallel with carbon capture        | 4467   | 146.6     | 1.4          | 38%        |               | 90% |  | 10% |
| Pulverized Coal.Co-Firing. Sperate feeding with carbon capture | 4158   | 170.5     | 1.4          | 38%        |               | 90% |  | 10% |
| Pulverized Coal.Co-Firing. Co-milling with carbon capture      | 3724   | 106.9     | 1.4          | 38%        |               | 80% |  | 20% |
| Pulverized Coal.Co-Firing. Parallel with carbon capture        | 4467   | 146.6     | 1.4          | 38%        |               | 80% |  | 20% |
| Pulverized Coal.Co-Firing. Sperate feeding with carbon capture | 4158   | 170.5     | 1.4          | 38%        |               | 80% |  | 20% |
| Pulverized Coal.Co-Firing. Co-milling with carbon capture      | 3724   | 106.9     | 1.4          | 38%        |               | 60% |  | 40% |
| Pulverized Coal.Co-Firing. Prallel with carbon capture         | 4467   | 146.6     | 1.4          | 38%        |               | 60% |  | 40% |
| Pulverized Coal.Co-Firing. Sperate feeding with carbon capture | 4158   | 170.5     | 1.4          | 38%        |               | 60% |  | 40% |

### Renewables

#### Hydropower

#### Solar

#### Wind

#### Ocean

## Modeling

## Constraints

## References

Irlam, L., 2017. Global CCS Institute : Global Costs of Carbon Capture and Storage. Global CCS Institute.  
IEAGHG, 2020. Techno-Economic Benchmarks for Fossil Fuel-Fired Power Plants with CO2 Capture (No. 2020– 07).  
Ferrari, N., Mancuso, L., Burnard, K., Consonni, F., 2019. Effects of plant location on cost of CO2 capture. International Journal of Greenhouse Gas Control 90, 102783. https://doi.org/10.1016/j.ijggc.2019.102783
