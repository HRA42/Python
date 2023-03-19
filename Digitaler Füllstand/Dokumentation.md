# Digitaler Füllstand

## Projekt Vorstellung 
Wir möchten digital den Füllstand einer beliebigen Flüssigkeit ermitteln. Sollte der Flüssigkeitsspiegel zu niedrig sein, leuchtet eine LED Rot auf und ein Alarm ertönt, zusätzlich warden noch Umweltparameter wie Termperatur, Luftdruck und die gemessene Höhe ausgegeben. Die Ausgabe der Umweltparameter soll helfen bei schnellerem Absinken des Flüssigkeitsspiegels, als dies zu erwarten wäre, die Ursache einschätzen zu können und Gegenmaßnahmen zu ermöglichen.

Wir haben uns für die Umsetzung in Python entschieden, da wir nicht erwarten, dass eine größere Datenmenge sehr schnell zu verabreiten sein muss. Daher haben wir uns für den Raspberry Pi entschieden, da dieser für kleine Python Projekte mit unterschiedlichen Sensoren und Aktoren hervorragend geeignet ist und die Kosten überschaubar sind.

## Bauteilübersicht

- 1 x Raspberry Pi Model 4b mit 8 GB RAM
- 1 x Piezzo Buzzer Modul
- 1 x 2 Farben LED
- 1 x Ultraschallsensor
- 1 x Pegelumsetzer von 5 V zu 3,3 V
- 1 x Luftdruck und Temperatursensor (BMP280)

## Abhängigkeiten
Für den BMP280 Sensor (Luftdruck und Temperatur) müssen folgende Schritte am Raspberry Pi durchgeführt werden:

Zuerst muss die Adafruit Bibliothek sowie die Abhängigkeiten für den IC2 Bus über den Debian Paketmanager apt installiert werden:

    sudo pip3 install -y adafruit-circuitpython-bmp280 python3-smbus i2c-tools

Für die Kommunikation mit dem IC2 Bus des Raspberry Pi muss eine Änderung an der Boot Konfiguration vogenommen werden.
    
    sudo nano /boot/config.txt

Dort muss folgende Zeile am Ende der Datei angefügt werden, falls sie noch nicht in der Datei steht:

    dtparam=i2c_arm=on

Drücken sie danach folgende Tastenkombination um die Datei zu speichern:

    Strg+X -> Y -> Enter

Zum Abschluss muss der Raspberry Pi neugestartet werden und danach kann das Projekt gestartet werden. 

## Aufbau

![RaspberryPi_Projekt](https://user-images.githubusercontent.com/44985923/150574835-c2144ca4-cd50-4099-9662-5d09426fd64a.png)

Die Zeichnung entstand in Fritzing. 
Bis auf der Luftdruck Sensor und der Pegelumsetzer sind alle Bautteile so im Original im Einsatz.

## Besonderheiten
Die Besonderheit bei diesem Projekt liegt in der Abstandsberechnung des Ultraschall Sensors.
Zuerst wird ein Ultraschall Signal für 10 u Sekunden ausgesendet und danach eine Zeit fest gelegt. Kommt der Schall dann nach einer Zeit zurück wird erneut eine Zeit gestoppt.

![Besonderheit1](https://user-images.githubusercontent.com/44985923/151138022-caca1303-0c47-4ad2-a4e2-acc1852be984.png)

Anschließend wird der Abstand berechnet. Dafür wird zuerst die Dauer zwischen Aussenden und Eintreffen des Ultraschall bestimmt und dann über die Schallgeschwindigkeit der Abstand bestimmt. 

![Besonderheit2](https://user-images.githubusercontent.com/44985923/151138091-7b613b3e-6f49-404c-9a32-e5392d96e85f.png)

Dazu wird die Dauer mit der Schallgeschwindigkeit multipliziert und mal 100 multipliziert um eine Ausgabe in cm zu erhalten sodass dann ein Messergebnis im Sensor Bereich, 2 cm – 300 cm, vorliegt.
Dies wird zum Abschluss noch über eine Fehlerkontrolle sichergestellt und der Abstand wird dem Benutzer ausgegeben.

![Besonderheit3](https://user-images.githubusercontent.com/44985923/151138121-3955b349-b969-47c0-b9ea-ac3e6f26b5d2.png)