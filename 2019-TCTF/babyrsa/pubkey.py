from sage.all import GF, PolynomialRing

P=PolynomialRing(GF(2),'x')
e = 31337
n = P('x^2048 + x^2046 + x^2043 + x^2040 + x^2036 + x^2035 + x^2034 + x^2033 + x^2031 + x^2029 + x^2025 + x^2024 + x^2022 + x^2019 + x^2018 + x^2017 + x^2012 + x^2007 + x^2006 + x^2004 + x^2000 + x^1999 + x^1998 + x^1997 + x^1993 + x^1992 + x^1991 + x^1986 + x^1982 + x^1981 + x^1979 + x^1978 + x^1977 + x^1975 + x^1970 + x^1964 + x^1963 + x^1962 + x^1961 + x^1960 + x^1959 + x^1958 + x^1955 + x^1954 + x^1952 + x^1951 + x^1949 + x^1947 + x^1942 + x^1939 + x^1938 + x^1936 + x^1934 + x^1933 + x^1932 + x^1930 + x^1928 + x^1927 + x^1923 + x^1922 + x^1919 + x^1918 + x^1915 + x^1914 + x^1913 + x^1912 + x^1911 + x^1910 + x^1908 + x^1903 + x^1902 + x^1900 + x^1899 + x^1897 + x^1893 + x^1891 + x^1890 + x^1886 + x^1881 + x^1880 + x^1879 + x^1878 + x^1875 + x^1874 + x^1873 + x^1872 + x^1871 + x^1870 + x^1869 + x^1865 + x^1863 + x^1862 + x^1860 + x^1856 + x^1855 + x^1853 + x^1852 + x^1845 + x^1841 + x^1839 + x^1837 + x^1836 + x^1835 + x^1833 + x^1832 + x^1829 + x^1828 + x^1827 + x^1826 + x^1824 + x^1823 + x^1822 + x^1821 + x^1820 + x^1819 + x^1818 + x^1817 + x^1813 + x^1812 + x^1810 + x^1809 + x^1808 + x^1807 + x^1803 + x^1799 + x^1797 + x^1796 + x^1794 + x^1792 + x^1790 + x^1786 + x^1783 + x^1782 + x^1779 + x^1778 + x^1776 + x^1775 + x^1774 + x^1772 + x^1767 + x^1766 + x^1765 + x^1764 + x^1763 + x^1762 + x^1759 + x^1757 + x^1756 + x^1754 + x^1753 + x^1752 + x^1750 + x^1749 + x^1741 + x^1734 + x^1730 + x^1729 + x^1726 + x^1725 + x^1723 + x^1722 + x^1721 + x^1716 + x^1714 + x^1713 + x^1712 + x^1710 + x^1709 + x^1706 + x^1705 + x^1703 + x^1702 + x^1700 + x^1698 + x^1693 + x^1692 + x^1691 + x^1690 + x^1683 + x^1682 + x^1681 + x^1680 + x^1679 + x^1677 + x^1672 + x^1670 + x^1669 + x^1666 + x^1663 + x^1662 + x^1661 + x^1659 + x^1655 + x^1653 + x^1651 + x^1649 + x^1648 + x^1647 + x^1646 + x^1644 + x^1643 + x^1642 + x^1640 + x^1639 + x^1638 + x^1634 + x^1633 + x^1628 + x^1620 + x^1619 + x^1618 + x^1616 + x^1614 + x^1611 + x^1610 + x^1608 + x^1605 + x^1604 + x^1603 + x^1599 + x^1597 + x^1595 + x^1594 + x^1590 + x^1588 + x^1587 + x^1585 + x^1583 + x^1580 + x^1579 + x^1577 + x^1574 + x^1573 + x^1572 + x^1568 + x^1566 + x^1565 + x^1563 + x^1562 + x^1560 + x^1555 + x^1554 + x^1552 + x^1550 + x^1549 + x^1548 + x^1545 + x^1544 + x^1542 + x^1540 + x^1538 + x^1537 + x^1536 + x^1535 + x^1534 + x^1533 + x^1532 + x^1531 + x^1528 + x^1526 + x^1525 + x^1523 + x^1522 + x^1521 + x^1519 + x^1517 + x^1515 + x^1510 + x^1509 + x^1506 + x^1504 + x^1502 + x^1499 + x^1498 + x^1497 + x^1488 + x^1483 + x^1480 + x^1477 + x^1472 + x^1471 + x^1469 + x^1468 + x^1467 + x^1466 + x^1464 + x^1462 + x^1457 + x^1456 + x^1455 + x^1454 + x^1453 + x^1452 + x^1448 + x^1446 + x^1444 + x^1443 + x^1442 + x^1441 + x^1440 + x^1436 + x^1435 + x^1431 + x^1428 + x^1425 + x^1424 + x^1422 + x^1420 + x^1415 + x^1414 + x^1411 + x^1410 + x^1408 + x^1406 + x^1405 + x^1403 + x^1402 + x^1399 + x^1397 + x^1396 + x^1395 + x^1394 + x^1393 + x^1391 + x^1388 + x^1385 + x^1377 + x^1376 + x^1372 + x^1371 + x^1370 + x^1369 + x^1367 + x^1363 + x^1361 + x^1357 + x^1355 + x^1354 + x^1349 + x^1343 + x^1339 + x^1338 + x^1337 + x^1336 + x^1335 + x^1332 + x^1329 + x^1327 + x^1326 + x^1324 + x^1321 + x^1315 + x^1314 + x^1312 + x^1310 + x^1309 + x^1305 + x^1304 + x^1303 + x^1302 + x^1299 + x^1298 + x^1296 + x^1295 + x^1293 + x^1291 + x^1290 + x^1289 + x^1284 + x^1283 + x^1282 + x^1281 + x^1280 + x^1278 + x^1277 + x^1276 + x^1275 + x^1272 + x^1270 + x^1269 + x^1268 + x^1267 + x^1259 + x^1257 + x^1254 + x^1252 + x^1251 + x^1249 + x^1247 + x^1246 + x^1244 + x^1240 + x^1238 + x^1233 + x^1232 + x^1229 + x^1222 + x^1219 + x^1217 + x^1211 + x^1209 + x^1208 + x^1205 + x^1204 + x^1203 + x^1202 + x^1200 + x^1197 + x^1196 + x^1195 + x^1193 + x^1192 + x^1189 + x^1187 + x^1186 + x^1185 + x^1184 + x^1183 + x^1182 + x^1181 + x^1177 + x^1176 + x^1173 + x^1170 + x^1167 + x^1166 + x^1162 + x^1161 + x^1160 + x^1159 + x^1158 + x^1156 + x^1155 + x^1154 + x^1153 + x^1151 + x^1146 + x^1143 + x^1141 + x^1139 + x^1138 + x^1137 + x^1135 + x^1131 + x^1129 + x^1128 + x^1125 + x^1124 + x^1122 + x^1116 + x^1115 + x^1114 + x^1112 + x^1111 + x^1107 + x^1106 + x^1105 + x^1104 + x^1103 + x^1102 + x^1098 + x^1097 + x^1095 + x^1094 + x^1092 + x^1088 + x^1087 + x^1085 + x^1077 + x^1076 + x^1075 + x^1072 + x^1069 + x^1068 + x^1061 + x^1060 + x^1059 + x^1057 + x^1055 + x^1054 + x^1053 + x^1050 + x^1047 + x^1046 + x^1044 + x^1043 + x^1042 + x^1036 + x^1029 + x^1025 + x^1024 + x^1023 + x^1022 + x^1019 + x^1016 + x^1013 + x^1012 + x^1010 + x^1008 + x^1007 + x^1006 + x^1004 + x^1000 + x^996 + x^995 + x^993 + x^992 + x^989 + x^985 + x^983 + x^978 + x^977 + x^975 + x^972 + x^971 + x^970 + x^969 + x^967 + x^963 + x^957 + x^956 + x^952 + x^950 + x^948 + x^945 + x^942 + x^941 + x^940 + x^938 + x^937 + x^936 + x^935 + x^932 + x^931 + x^930 + x^928 + x^927 + x^926 + x^923 + x^921 + x^918 + x^916 + x^914 + x^913 + x^909 + x^906 + x^905 + x^904 + x^902 + x^897 + x^895 + x^892 + x^889 + x^888 + x^887 + x^886 + x^885 + x^884 + x^882 + x^881 + x^879 + x^876 + x^870 + x^868 + x^867 + x^865 + x^862 + x^861 + x^859 + x^858 + x^856 + x^854 + x^848 + x^847 + x^846 + x^843 + x^839 + x^837 + x^836 + x^832 + x^831 + x^830 + x^829 + x^826 + x^823 + x^821 + x^820 + x^817 + x^815 + x^812 + x^809 + x^808 + x^805 + x^803 + x^802 + x^800 + x^799 + x^797 + x^795 + x^793 + x^792 + x^788 + x^786 + x^784 + x^780 + x^775 + x^774 + x^770 + x^768 + x^766 + x^764 + x^761 + x^760 + x^753 + x^752 + x^751 + x^750 + x^747 + x^744 + x^742 + x^741 + x^737 + x^734 + x^732 + x^728 + x^727 + x^724 + x^722 + x^721 + x^719 + x^717 + x^715 + x^714 + x^713 + x^710 + x^709 + x^705 + x^703 + x^701 + x^698 + x^697 + x^695 + x^690 + x^687 + x^685 + x^684 + x^682 + x^681 + x^680 + x^677 + x^676 + x^674 + x^673 + x^672 + x^671 + x^670 + x^669 + x^665 + x^663 + x^659 + x^652 + x^651 + x^650 + x^649 + x^648 + x^647 + x^646 + x^645 + x^642 + x^640 + x^638 + x^632 + x^631 + x^630 + x^629 + x^627 + x^626 + x^623 + x^622 + x^621 + x^620 + x^616 + x^615 + x^610 + x^605 + x^602 + x^601 + x^600 + x^599 + x^598 + x^596 + x^594 + x^593 + x^591 + x^583 + x^581 + x^579 + x^578 + x^577 + x^576 + x^575 + x^573 + x^572 + x^571 + x^570 + x^569 + x^565 + x^563 + x^562 + x^561 + x^559 + x^557 + x^555 + x^552 + x^551 + x^546 + x^544 + x^542 + x^541 + x^540 + x^539 + x^538 + x^537 + x^535 + x^533 + x^530 + x^527 + x^523 + x^522 + x^520 + x^519 + x^515 + x^513 + x^511 + x^509 + x^507 + x^505 + x^504 + x^503 + x^499 + x^497 + x^496 + x^495 + x^493 + x^492 + x^488 + x^486 + x^481 + x^480 + x^479 + x^478 + x^477 + x^472 + x^470 + x^468 + x^467 + x^464 + x^463 + x^460 + x^459 + x^455 + x^454 + x^453 + x^446 + x^445 + x^444 + x^443 + x^440 + x^438 + x^437 + x^432 + x^431 + x^428 + x^427 + x^426 + x^420 + x^419 + x^416 + x^415 + x^414 + x^413 + x^412 + x^411 + x^405 + x^404 + x^401 + x^396 + x^393 + x^392 + x^391 + x^388 + x^387 + x^383 + x^381 + x^380 + x^377 + x^376 + x^369 + x^364 + x^362 + x^358 + x^357 + x^356 + x^355 + x^353 + x^351 + x^349 + x^340 + x^339 + x^338 + x^337 + x^336 + x^335 + x^334 + x^332 + x^330 + x^328 + x^327 + x^326 + x^324 + x^320 + x^318 + x^316 + x^315 + x^309 + x^302 + x^298 + x^292 + x^291 + x^290 + x^289 + x^287 + x^286 + x^285 + x^284 + x^281 + x^279 + x^278 + x^276 + x^274 + x^273 + x^272 + x^271 + x^267 + x^266 + x^264 + x^263 + x^262 + x^260 + x^259 + x^256 + x^254 + x^253 + x^252 + x^251 + x^249 + x^248 + x^247 + x^245 + x^244 + x^241 + x^239 + x^235 + x^234 + x^233 + x^232 + x^231 + x^230 + x^226 + x^224 + x^221 + x^219 + x^218 + x^216 + x^215 + x^214 + x^209 + x^207 + x^206 + x^202 + x^201 + x^198 + x^197 + x^194 + x^193 + x^192 + x^191 + x^189 + x^188 + x^183 + x^182 + x^181 + x^180 + x^179 + x^178 + x^177 + x^175 + x^172 + x^169 + x^168 + x^166 + x^165 + x^164 + x^163 + x^158 + x^157 + x^153 + x^152 + x^149 + x^147 + x^146 + x^144 + x^140 + x^139 + x^136 + x^128 + x^127 + x^126 + x^124 + x^123 + x^122 + x^121 + x^116 + x^115 + x^113 + x^112 + x^109 + x^108 + x^107 + x^106 + x^104 + x^103 + x^102 + x^101 + x^100 + x^99 + x^97 + x^95 + x^94 + x^93 + x^92 + x^87 + x^84 + x^83 + x^82 + x^80 + x^79 + x^78 + x^76 + x^73 + x^70 + x^69 + x^68 + x^67 + x^66 + x^65 + x^63 + x^60 + x^59 + x^57 + x^55 + x^52 + x^51 + x^47 + x^46 + x^45 + x^43 + x^42 + x^40 + x^36 + x^35 + x^30 + x^29 + x^28 + x^27 + x^23 + x^20 + x^17 + x^14 + x^9 + x^7 + x^3 + 1')
