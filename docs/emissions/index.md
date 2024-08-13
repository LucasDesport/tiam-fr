# Emissions

In TIAM-FR, the emissions represented are carbon dioxide (CO<sub>2</sub>), methane (CH<sub>4</sub>), and nitrous oxide (N<sub>2</sub>O). Emissions encompass several sectors namely, fossil fuel combustion, fossil fuel extraction, industrial process CO<sub>2</sub> emissions, industrial process N<sub>2</sub>O emissions, and agricultural CO<sub>2</sub> emissions. 

## Fossil fuel extraction

Emissions due to the extraction of fossil fuel are taken into account through emissions factors calibrated on the amount of fossil fuel extracted.

Table 1: Emissions factors due to fossil fuel extraction
| Case            | Emission | Units | AFR  | AUS  | CAN  | CHI  | CSA  | EEU  | FSU  | IND  | JPN  | MEA  | MEX  | ODA  | SKO  | USA  | WEU  |
| --------------- | -------- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- |
| Gas extraction  | CO<sub>2</sub>      | kg/GJ | 0,87 | 0,87 | 7,27 | 3,00 | 2,15 | 1,71 | 0,75 | 0,68 | 2,44 | 0,89 | 3,75 | 2,15 | 0,22 | 1,96 | 2,10 |
| Oil extraction  | CO<sub>2</sub>      | kg/GJ | 0,87 | 0,87 | 7,27 | 3,00 | 2,15 | 1,71 | 0,75 | 0,68 | 2,44 | 0,89 | 3,75 | 2,15 | 0,22 | 1,96 | 2,10 |
| Coal extraction | CO<sub>2</sub>      | kg/GJ | 4,29 | 4,28 | 3,55 | 3,41 | 2,33 | 2,33 | 1,87 | 1,24 | 1,20 | 1,20 | 1,20 | 1,20 | 1,20 | 0,29 | 0,06 |
| Gas extraction  | CH<sub>4</sub>      | g/GJ |  48   | 2    | 219  | 24   | 277  | 1221 | 568  | 546  | 301  | 19   | 484  | 103  | 199  | 176  | 149  |
| Oil extraction  | CH<sub>4</sub>      | g/GJ | 56   | 9    | 146  | 28   | 18   | 2    | 19   | 4    | 0    | 20   | 20   | 8    | 0    | 29   | 5    |
| Coal extraction | CH<sub>4</sub>      | g/GJ |  69   | 90   | 36   | 116  | 114  | 300  | 317  | 45   | 1    | 127  | 340  | 128  | 1397 | 130  | 390  |

## Fossil fuel combustion emissions

Combustion emissions concern CO<sub>2</sub>, CH<sub>4</sub> and N<sub>2</sub>O. Table 2 reports CO<sub>2</sub> emissions factor based on (EIA, 2022)

Table 2: Emissions factors due to fossil fuel combustion
| Fossil fuel | CO<sub>2</sub> emissions [kgCO<sub>2</sub>/MJ] |
| ------------| ------------------------ | 
| Brown coal  | 98                       | 
| Hard coal   | 109                      | 
| Oven coke   | 120                      | 
| Jet fuel    | 75                       | 
| Kerosene    | 76                       |
| LPG         | 68                       | 
| Fossil gas  | 56                       | 
| Ethane      | 56                       | 
| Working gas | 56                       | 
| Crude oil   | 83                       | 
| Distillates | 77                       | 
| Gasoline    | 75                       |
| Heavy fuel  | 83                       | 
| Lubricants  | 78                       | 
| Naphtha     | 77                       | 

Emissions due to geothermal energy use show an emission factor of 0.03 kgCO<sub>2</sub>/MJ.  

The non-CO<sub>2</sub> emissions are defined according to the end use. Table 3 reports their sectoral emissions factors in t/PJ.

Table 3: Emissions factors due to fossil fuel end-use
| Sector       | Emission | Coal | Heavy fuel oil | Kerosene | LGP  | Fossil gas | Oil  | Gasoline | Solid biomass | Wastes | Oven coke | Petcoke | Blast furnace gas |
| ------------ | -------- | ---- | -------------- | -------- | ---- | ---------- | ---- | -------- | ------------- | ------ | --------- | ------- | ----------------- |
| Agricultural | CH<sub>4</sub>      | 5.00 |                | 1.00     | 5.00 | 5.00       | 2.00 |          |               |        |           |         |                   |
| Agricultural | N<sub>2</sub>O      | 1.40 |                | 0.60     | 0.10 | 0.10       | 0.60 |          |               |        |           |         |                   |
| Commercial   | CH<sub>4</sub>      | 5.00 | 5.00           | 1.00     | 5.00 | 5.00       | 2.00 |          |               |        |           |         |                   |
| Commercial   | N<sub>2</sub>O      | 1.40 | 0.60           | 0.60     | 0.10 | 0.10       | 0.60 |          |               |        |           |         |                   |
| Electricity  | CH<sub>4</sub>      | 5.00 |                |          |      | 5.00       | 2.00 |          | 300.00        | 300.00 |           |         |                   |
| Electricity  | N<sub>2</sub>O      | 1.40 |                |          |      | 0.10       | 0.60 |          | 4.00          | 4.00   |           |         |                   |
| Industrial   | CH<sub>4</sub>      | 5.00 | 5.00           |          | 5.00 | 5.00       | 2.00 |          |               |        | 5.00      | 5.00    |                   |
| Inudstrial   | N<sub>2</sub>O      | 1.40 | 0.60           |          | 0.10 | 0.10       | 0.60 |          |               |        | 0.10      | 0.10    |                   |
| Residential  | CH<sub>4</sub>      | 5.00 | 5.00           | 1.00     | 5.00 | 5.00       | 2.00 |          |               |        |           |         |                   |
| Residential  | N<sub>2</sub>O      | 1.40 | 0.60           | 0.60     | 0.10 | 0.10       | 0.60 |          |               |        |           |         |                   |
| Supply       | CH<sub>4</sub>      | 5.00 |                |          |      | 5.00       | 2.00 |          | 300.00        |        |           |         | 0.00              |
| Supply       | N<sub>2</sub>O      | 1.40 |                |          |      | 0.10       | 0.60 |          | 4.00          |        |           |         | 1.40              |
| Transport    | CH<sub>4</sub>      | 5.00 | 5.00           | 5.53     | 5.00 | 5.00       | 5.00 | 20.00    |               |        |           |         |                   |
| Transport    | N<sub>2</sub>O      | 1.40 | 0.60           | 6.10     | 0.10 | 0.10       | 0.60 | 0.60     |               |        |           |         |                   |

## Process CO<sub>2</sub> emissions

Process CO<sub>2</sub> emissions due to limestone calcination occuring the cement process are detailed in Table 2 of the section dedicated to [cement](../../docs/energy-sectors/industry/cement/index.md).

Process CO<sub>2</sub> emissions due to the oxidation of carbon occuring in steel manufacturing processes are detailed in Appendix 1 of the section dedicated to [iron & steel](../../docs/energy-sectors/industry/iron-steel/index.md).

## Agricultural emissions

Agricultural CO<sub>2</sub> emissions due to land use, land-use changes and forestry (LULUCF) are reported in Table 4 in ktCO<sub>2</sub>.

Table 4: LULUCF CO<sub>2</sub> emissions
| Year | AFR     | AUS    | CAN   | CHI      | CSA     | EEU      | FSU   | IND      | JPN  | MEA  | MEX   | ODA     | SKO   | USA       | WEU      |
| ---- | ------- | ------ | ----- | -------- | ------- | -------- | ----- | -------- | ---- | ---- | ----- | ------- | ----- | --------- | -------- |
| 2018 | 3723510 | 103290 | 30780 | 21787    | 5040750 | \-141416 | 45042 | \-27962  | 5566 | 12   | 30992 | 2345960 | 10828 | \-3034060 | \-612221 |
| 2020 | 3723510 | 103290 | 30780 | 21787    | 5040750 | \-141416 | 45042 | \-27962  | 5566 | 12   | 30992 | 2345960 | 10828 | \-3034060 | \-612221 |
| 2030 | 3012030 | 89048  | 27734 | \-11785  | 2059590 | \-125266 | 40702 | \-33289  | 5020 | 11   | 27206 | 2059590 | 9675  | \-2419940 | \-809377 |
| 2040 | 2368570 | 75420  | 24902 | \-36736  | 1756841 | \-109054 | 36712 | \-401381 | 4519 | 10   | 23073 | 1725370 | 8586  | \-1934120 | \-929606 |
| 2050 | 1825130 | 63277  | 22359 | \-54405  | 1394120 | \-92625  | 33090 | \-58802  | 4065 | 8    | 19389 | 1394120 | 7586  | \-1176970 | \-927299 |
| 2060 | 616759  | 25213  | 9876  | \-82135  | 1096580 | \-89796  | 14281 | \-30818  | 0    | 4    | 0     | 1096580 | 3310  | \-534564  | \-847854 |
| 2070 | 522154  | 21441  | 8927  | \-88776  | 844523  | \-71088  | 12899 | \-18897  | 1589 | 3    | 0     | 844523  | 2917  | \-220966  | \-768410 |
| 2080 | 415218  | 18037  | 8038  | \-79952  | 637950  | \-52381  | 11594 | \-116241 | 1441 | 1390 | 0     | 637950  | 2565  | \-158463  | \-609432 |
| 2090 | 327754  | 15170  | 34834 | \-130580 | 527119  | \-33674  | 10517 | \-113598 | 1309 | 3289 | 0     | 475665  | 2254  | \-108780  | \-314250 |
| 2100 | 384565  | 12717  | 62982 | \-107104 | 468929  | \-14966  | 9507  | \-127728 | 1183 | 4995 | 0     | 350397  | 1977  | \-68413   | \-86776  |

**References**

EIA, 2022. U.S. Energy Information Administration - EIA - Independent Statistics and Analysis [WWW Document]. URL https://www.eia.gov/environment/emissions/co2_vol_mass.php (accessed 10.6.22).

