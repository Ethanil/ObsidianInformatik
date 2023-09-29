Das Ziel von einen regionenbasierten Verfahren ist das Bild in Zonen mit maximaler Homohenität(z.B. Grauwert, Farbe etc) aufzuteilen.
Der Vorteil von regionbasiertem Verfahren ist, dass wir Informationen über die Nachbarschaft haben und es Robust bei verrauschten Bildern ist

## Region Growing(Bottom up)
1. Wir setzen $n$ Startpunkte(Seed Points), welche unsere initialen Regionen darstellen, dies tun wir entweder zufällig oder Aufgrund von Beurteilung des Bildinhalts
2. Wir untersuchen die [[Nachbarschaft]](4 oder 8) und treffen folgende Fallunterscheidung

|                                      | Gehört noch zu keiner Region     | Gehört zu einer anderen Region  |
| ------------------------------------ | -------------------------------- | ------------------------------- |
| Erfüllt Homogenitätskriterium        | Wird der Region zugeordnet       | Regionen werden vereinigt       |
| Erfülllt Homogenitätskriterium nicht | Wird der Region nicht zugeordnet | Regionen werden nicht vereinigt |
3. Wiederhole 1. und 2. bis keine Änderungen mehr eintreten
## Split & Merge(Top down)
Bei Split & Merge unterteilen wir das Bild in Quadrate entsprechend eines Homogenitätskriterium. Nach dem Split mergen wir die entstandenen Regionen.
![[Pasted image 20230929125153.png# 5/6 left shadow|Zuerst wird gesplittet und die gesplitteten regionen dann wieder gemerged(wobei die blauen Regionen auf magische Art und Weise wussten dass sie zusammengehören (= ))]]

## Wasserscheide-Segmentierung
Bei der Wasserscheiden-Segmentierung "füllen wir das Bild mit Wasser", wir definieren also eine gewissen Tiefe und fangen an jeden Pixel mit der niedrigsten Tiefe zu markieren, bis zwei Regionen sich vereinigen würden. Wir gehen einen Schritt zurück, [[Dilatation|dilatieren]] diese beide Regionen, außer an den Stellen, die die beiden Regionen verbinden würden und erschaffen zwischen diesen beiden Regionen dann einen "Damm", also eine Kante.