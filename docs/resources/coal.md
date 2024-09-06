# Coal

In TIAM-FR, coal resources are disaggregated into two commodiy types, namely brown coal and hard coal, as specified in the Internation Energy Agency (IEA) Energy Balance (IEA, 2020). Brown coal and hardcoal are distinguished by their calorific value, ash content, and moisture content. The estimated coal potentials found in (Pye et al., 2020) do not make this disinction and deliver an aggregate potential across regions. In order to allocate coal ressources to the type of coal, we assume that those are split according to the share initially implemented in ETSAP-TIAM (Loulou and Labriet, 2008) between brown coal and hardcoal (Table 1).

Table 1: Assumed shares between brown and hard coal resources
| Resource   | AFR  | AUS | CAN | CHI | CSA | EEU | FSY | IND | JPN | MEA | MEX | ODA | SKO  | USA | WEU |
| ---------- | ---- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ---- | --- | --- |
| Hard coal  | 100% | 87% | 96% | 96% | 83% | 66% | 96% | 87% | 99% | 59% | 95% | 95% | 100% | 79% | 27% |
| Brown coal | 0%   | 13% | 5%  | 4%  | 17% | 34% | 4%  | 13% | 1%  | 41% | 5%  | 5%  | 0%   | 21% | 73% |

According to these shares, intial coal resources of (Pye et al., 2020) are disaggregated into brown coal resources (Table 2) and hard coal resources (Table 3). However, extraction costs (Table 4) are assumed similar regardless the type of coal due to lack of data.

Table 2: Assumed brown coal resources \[EJ\] across regions. Steps refer to cost assumptions located in Table 4
| Step | AFR | AUS    | CAN  | CHI  | CSA   | EEU   | FSU  | IND  | JPN | MEA   | MEX  | ODA  | SKO | USA   | WEU   |
| ---- | --- | ------ | ---- | ---- | ----- | ----- | ---- | ---- | --- | ----- | ---- | ---- | --- | ----- | ----- |
| 1    |  | 274    | 1    | 22   | 73    | 258   | 66   | 351  | 27  | 13259 | 1    | 23   |  | 61    | 1805  |
| 2    | 3   | 5900   | 128  | 395  | 95    | 7146  | 509  | 1802 | 425 | 18144 | 658  | 174  |  | 4094  | 10385 |
| 3    | 3   | 28849  | 906  | 1307 | 460   | 15323 | 1534 | 4088 | 471 | 18157 | 1491 | 1102 |  | 8140  | 14440 |
| 4    | 14  | 63746  | 1703 | 1870 | 558   | 15596 | 1925 | 6202 | 471 | 20112 | 2821 | 2383 |  | 8985  | 28671 |
| 5    | 14  | 66381  | 2197 | 2484 | 2429  | 25031 | 2687 | 7739 | 748 | 20147 |   | 2648 |  | 14025 | 31775 |
| 6    | 27  | 101201 | 2977 | 3045 | 3566  | 25304 | 3076 | 9843 | 748 | 20920 |   | 3907 |  | 14870 | 31819 |
| 7    | 27  |     |   |   | 7713  |    |   |   |  | 31912 |   |   |  |    | 34629 |
| 8    | 31  |     |   |   | 8293  |    |   |   |  | 31948 |   |   |  |    | 49386 |
| 9    | 31  |     |   |   | 8415  |    |   |   |  | 31955 |   |   |  |    | 52490 |
| 10   | 44  |     |   |   | 12553 |    |   |   |  |    |   |   |  |    | 52493 |
| 11   | 44  |     |   |   |    |    |   |   |  |    |   |   |  |    | 55303 |

Table 3: Assumed hard coal resources \[EJ\] across regions. Steps refer to cost assumptions located in Table 4
| Step | AFR   | AUS   | CAN   | CHI   | CSA   | EEU   | FSU   | IND   | JPN   | MEA   | MEX   | ODA   | SKO   | USA   | WEU   |
| ---- | ----- | ----- | ----- | ----- | ----- | ----- | ----- | ----- | ----- | ----- | ----- | ----- | ----- | ----- | ----- |
| 1    | 318   | 1811  | 21    | 506   | 359   | 500   | 1580  | 2393  | 2717  | 18756 | 21    | 409   | 43849 | 236   | 683   |
| 2    | 5243  | 3899  | 2734  | 9200  | 466   | 13829 | 12102 | 12303 | 43376 | 25667 | 13471 | 3083  | 48650 | 15769 | 3928  |
| 3    | 5253  | 19062 | 19390 | 30413 | 2249  | 29654 | 36435 | 27906 | 48064 | 25686 | 30508 | 19503 | 77144 | 31356 | 5462  |
| 4    | 22106 | 42120 | 36446 | 43521 | 2726  | 30182 | 45743 | 42332 | 48089 | 28451 | 57744 | 42198 |       | 34610 | 10844 |
| 5    | 22110 | 43861 | 47022 | 57802 | 11874 | 48440 | 63833 | 52822 | 76281 | 28501 |       | 46879 |       | 54022 | 12018 |
| 6    | 43766 | 66868 | 63722 | 70841 | 17428 | 48969 | 73086 | 67184 | 76306 | 29594 |       | 69168 |       | 57276 | 12035 |
| 7    | 43825 |       |       |       | 37699 |       |       |       |       | 45144 |       |       |       |       | 13097 |
| 8    | 50655 |       |       |       | 40532 |       |       |       |       | 45194 |       |       |       |       | 18679 |
| 9    | 50660 |       |       |       | 41131 |       |       |       |       | 45204 |       |       |       |       | 19853 |
| 10   | 72299 |       |       |       | 61354 |       |       |       |       |       |       |       |       |       | 19854 |
| 11   | 72301 |       |       |       |       |       |       |       |       |       |       |       |       |       | 20917 |

Table 4: Cost of coal extraction \[$/GJ\] across regions to be associated to the steps of Table 2 and Table 3
| Step | AFR | AUS | CAN | CHI | CSA | EEU | FSU | IND | JPN  | MEA  | MEX | ODA | SKO  | USA | WEU |
| ---- | --- | --- | --- | --- | --- | --- | --- | --- | ---- | ---- | --- | --- | ---- | --- | --- |
| 1    | 1.0 | 1.5 | 0.7 | 1.3 | 1.2 | 1.4 | 1.4 | 1.7 | 1.7  | 3.5  | 0.8 | 1.1 | 4.0  | 0.8 | 1.5 |
| 2    | 2.1 | 2.0 | 1.7 | 2.2 | 1.3 | 3.0 | 2.2 | 2.2 | 4.0  | 4.0  | 2.2 | 1.8 | 5.2  | 2.7 | 2.7 |
| 3    | 2.1 | 3.2 | 2.9 | 3.4 | 1.5 | 4.2 | 3.7 | 3.4 | 4.7  | 4.0  | 3.4 | 3.0 | 10.4 | 3.8 | 2.7 |
| 4    | 3.3 | 4.5 | 3.7 | 4.3 | 1.9 | 4.4 | 4.4 | 4.7 | 5.2  | 5.2  | 6.9 | 4.1 |      | 3.9 | 3.9 |
| 5    | 3.3 | 6.5 | 5.8 | 6.7 | 2.7 | 8.4 | 7.3 | 6.7 | 9.3  | 5.2  |     | 5.9 |      | 7.7 | 3.9 |
| 6    | 4.0 | 8.9 | 7.5 | 8.6 | 3.1 | 8.7 | 8.7 | 9.3 | 10.4 | 6.5  |     | 8.2 |      | 7.9 | 4.0 |
| 7    | 4.0 |     |     |     | 4.3 |     |     |     |      | 10.4 |     |     |      |     | 4.4 |
| 8    | 6.6 |     |     |     | 5.4 |     |     |     |      | 10.4 |     |     |      |     | 7.9 |
| 9    | 6.6 |     |     |     | 6.2 |     |     |     |      | 12.9 |     |     |      |     | 7.9 |
| 10   | 7.9 |     |     |     | 8.6 |     |     |     |      |      |     |     |      |     | 8.1 |
| 11   | 8.0 |     |     |     |     |     |     |     |      |      |     |     |      |     | 8.8 |

To reflect that the declared resources are not entirely accessible right off the bat, it is assume that 10% of the resources of each step can be extracted annually.

**References**

IEA, 2020. World Energy Balances - Data product [WWW Document]. IEA. URL https://www.iea.org/data-and-statistics/data-product/world-energy-balances (accessed 11.16.22).  
Pye, S., Bradley, S., Hughes, N., Price, J., Welsby, D., Ekins, P., 2020. An equitable redistribution of unburnable carbon. Nat Commun 11, 3968. https://doi.org/10.1038/s41467-020-17679-3  
Loulou, R., Labriet, M., 2008. ETSAP-TIAM: the TIMES integrated assessment model Part I: Model structure. CMS 5, 7–40. https://doi.org/10.1007/s10287-007-0046-z
