Um Irrelevanz zu eliminieren unterteilen wir das Bild in Blöcke, Transfomieren jeden Block unabhängig und führen die [[Quantisierung]] und Kodierung der Koeffizienten auf diesen Blöcken durch.
Eliminierung von Irrelevanz wird bspw bei der [[Kompression bei JPEG]] verwendet.

## Quantisierung/Schwellwert-Kodierung
Mithilfe von Bildtransformation und anwenden von Quantisierung können viele irrelevante Informationen entfernt werden. Da die wichtigsten Informationen bei Dekorrelierten Transformationen häufig an typischen Stellen liegen (idR nahe des Ursprungs) können die transformierten Bilder noch skaliert werden, um weitere irrelevante Informationen zu entfernen

![[Pasted image 20230928135055.png# 5/6 left shadow|Quantisierung mithilfe eines Schwellwerts(konkret 26) ohne vorherige Skalierung]]
![[Pasted image 20230928135309.png# 5/6 left shadow|Quantisierung mithilfe eines Schwellwertes(26) nachdem mit einer Matrix skaliert wurde]]