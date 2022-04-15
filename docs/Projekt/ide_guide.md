---
title: "IDE Guide"
---

Dieser Guide dient als Einführung in die Installation und Einrichtung einer _anständigen_
Entwicklungsumgebung mit JetBrains IDEs und Remote-Debugging.

## Lizenz

Remote-debugging erfordert eine kommerzielles JetBrains IDE (PyCharm Professional, IntelliJ
Ultimate) mit Python-Plugin. Schüler und Bildungseinrichtungen können kostenlos eine kommerzielle
Lizenz für die meisten JB-Produkte beantragen.

[!ref JetBrains Lizenen für Schüler](https://www.jetbrains.com/de-de/community/education/#students)

Es empfiehlt sich, seinen Schülerstatus bei GitHub zu bestätigen, und dann sein JetBrains-Konto mit
dem verifizierten GitHub-Konto zu verknüpfen, um über GitHub schnell weitere Vorteile zu erlangen.

[!ref GitHub Student Benefit](https://education.github.com/benefits)

Die Zeit bis zur Überprüfung des Antrags lässt sich mit der 30-Tägigen Testversion der IDEs
überbrücken

## IDE-Wahl

Bei den kommerziellen JetBrains-Produkten mit Python unterstützung handelt es sich um _PyCharm
Professional_ und _IntelliJ IDEA Ultimate mit Python-Plugin_. Von nun an werden diese als _PyCharm_
bzw. _IntelliJ_ bezeichnet.

## Installation

=== Portable Installation

Portable Installationen ermöglichen es, Software mitsamt Benutzerdaten auf einem tragbaren
Datenträger (USB-Stick) zu installieren. Pfade der Benutzerdaten können über eine Datei gesetzt
werden und ermöglichen somit die portable Nutzung. Mehr darüber findet
sich [hier](https://intellij-support.jetbrains.com/hc/en-us/articles/207240985-Changing-IDE-default-directories-used-for-config-plugins-and-caches-storage).


Portapps bietet eine Automation für IntelliJ, und verteilt mit diesem Verfahren eine Installation
von IntelliJ die Portable ausführbar ist.

[!ref IntelliJ Portable bei Portapps](https://portapps.io/app/intellij-idea-ultimate-portable/)

Das Verfahren würde sich auch mit anderen JB-Produkten wie PyCharm verwenden und, z.B. mit einem
Powershell-Skript automatisieren.

==- Normale Installation

Möglicherweise kann man ein eigenes Gerät mit Administratorrechten verwenden. JetBrains
Software-Installationen lassen sich am besten über die [JetBrains-Toolbox](https://www.jetbrains.com/de-de/toolbox-app/) verwalten. Alternativ lässt
sich die Software auch einzeln auf der Website des Herstellers herunterladen. Um die Konfiguration
zu erleichtern, empfiehlt es sich PyCharm zu verwenden.

===

Die IDE muss danach einmalig aktiviert werden. Hierzu meldet man sich mit dem eigenen JetBrains-Konto
an und aktiviert entweder die Testversion oder nutzt die Schülerlizenz.

Bei der Wahl von IntelliJ muss anschließend das [Python-Plugin](https://plugins.jetbrains.com/plugin/631-python) installiert werden.
Dazu einfach innerhalb der des Plugin-Marketplace nach "Python" suchen und das Plugin installieren.

[!ref Plugins installieren](https://www.jetbrains.com/help/idea/managing-plugins.html)

## Remote-Debugging

JetBrains bietet Dokumentation zum Remote-Debugging an. Die Vorgehensweise ist bei den IDEs beinahe identisch.

[!ref IntelliJ Remote-Debugging](https://www.jetbrains.com/help/idea/remote-debugging-with-product.html)

[!ref PyCharm Remote-Debugging](https://www.jetbrains.com/help/pycharm/remote-debugging-with-product.html)

Diese Webseiten enthalten auch weitere hilfreiche Dokumentationen zu den IDEs.

## Verbindung mit RPIs (für eigene Geräte)

Da uns die Nutzung des Netzwerks der Raspberry Pis unerklärlich untersagt ist, muss bei Verwendung eigener
Geräte der Raspberry Pi über ein LAN-Kabel (ggf. mit USB-LAN-Adapter) direkt mit dem Gerät verbunden werden.
Das scheint nur zu funktionieren, wenn der Raspberry Pi selber eine Internetverbindung hat.
Als Address des RPIs für die IDE kann man womöglich <Hostname>.local verwenden. <br>
Beispiel: raspberry5.local<br>
Diese umständliche und unzuverlässige Methode könnte man vermeiden, indem man die von der 
OTH bereitgestellten Laptops verwendet oder wenn man einfach das isolierte Netzwerk der OTH benutzen
dürfte, in dem auch die RPIs erreichbar ist. Es handelt sich hierbei um ein kleines, wahrscheinlich
komplett isoliertes Netzwerk mit einer Fritz!Box als Router; sowohl die Wahrscheinlichkeit, 
dass ein Gerät kompromittiertes ist, als auch dass ein kompromittiertes Gerät einen
ansatzweise ernstzunehmenden Schaden anrichtet, ist unbedeutend klein.