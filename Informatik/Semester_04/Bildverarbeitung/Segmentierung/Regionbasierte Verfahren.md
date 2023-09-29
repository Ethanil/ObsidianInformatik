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