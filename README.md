# E-handel

*Vi använde Python 3.14.7 för det här projektet.*

## Gruppmedlemmar
* Christoffer
* Felicia
* Jordan
* Roshima
* Wansiri
* Yvette

## Roller och ansvar

* Roshima: Fråga 4, genomsnittligt ordervärde (AOV) och spridning, inklusive histogram, boxplot och funktionerna `compute_aov`, `find_outliers` och `order_spread`
* Wade-Possible: Fråga 6, Eventuella Avvikelser. Analysera försäljningsdata för att beräkna avvikelser (anomalier) i dagsintäkter och visualisera i ett diagram.
## 🚀 Funktioner
- **IQR-gränser:** Beräknar kvartiler (Q1, Q3) och karterar undre/övre gränser för intäkter.
- **Anomalidetektion:** Identifierar avvikande dagsintäkter med hjälp av Z-score (`> 2.5` standardavvikelser).
- **Datavisualisering:** Skapar en graf med Matplotlib som markerar avvikande dagar med blå punkter.
