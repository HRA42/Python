# Abhängigkeiten importieren
import RPi.GPIO as GPIO
import time
import board
import adafruit_bmp280

# Pin Modus auswählen
GPIO.setmode(GPIO.BCM)

# PiezoBuzzer initialisieren
Piezo_Buzzer_Pin = 13
GPIO.setup(Piezo_Buzzer_Pin, GPIO.OUT)

# LED Initialisieren
LED_ROT = 6
LED_GRUEN = 12
GPIO.setup(LED_ROT, GPIO.OUT, initial=GPIO.LOW)  # Default: Aus
GPIO.setup(LED_GRUEN, GPIO.OUT, initial=GPIO.LOW)  # Default: Aus

# Temperatur und Luftdruck Sensor initialisieren
i2c = board.I2C()  # benutzt board.SCL und board.SDA
bmp280 = adafruit_bmp280.Adafruit_BMP280_I2C(i2c)
bmp280.sea_level_pressure = 1027.3  # notwendig für Höhenberechnung...

# Ultraschall Sensor initialisieren
Trigger_AusgangsPin = 26
Echo_EingangsPin = 20
# speichert den Abstand global
abstand = 0
GPIO.setup(Trigger_AusgangsPin, GPIO.OUT)
GPIO.setup(Echo_EingangsPin, GPIO.IN)
GPIO.output(Trigger_AusgangsPin, False)
# Pause zwischen den Messungen des Ultraschallsensors in Sekunden
sleeptime = 0.8


def Piezo_Buzzer(freq):
    # passiven Piezo-Buzzer mit Frequenz initialisieren
    pwm = GPIO.PWM(Piezo_Buzzer_Pin, freq)
    pwm.start(50)
    time.sleep(3)
    pwm.stop()


def rote_LED():
    # Rote LED anschalten
    GPIO.output(LED_ROT, GPIO.HIGH)
    GPIO.output(LED_GRUEN, GPIO.LOW)


def gruene_LED():
    # Gruene LED anschalten
    GPIO.output(LED_ROT, GPIO.LOW)
    GPIO.output(LED_GRUEN, GPIO.HIGH)


def Temp_Pressure_Sensor():
    print("Temperatur: " + str(round(bmp280.temperature)) + " C")
    print("Luftdruck: " + str(round(bmp280.pressure)) + " hPa")
    print("Höhe: " + str(round(bmp280.altitude)) + " meter")


def Ultraschall_Sensor():
    # Messung startet mit 10us Ultraschall
    GPIO.output(Trigger_AusgangsPin, True)
    time.sleep(0.00001)
    GPIO.output(Trigger_AusgangsPin, False)
    # Stoppuhr starten für Abstandsmessung
    EinschaltZeit = time.time()
    while GPIO.input(Echo_EingangsPin) == 0:
        EinschaltZeit = time.time()
    # Stoppuhr Ausschalten
    while GPIO.input(Echo_EingangsPin) == 1:
        AusschaltZeit = time.time()
    Dauer = AusschaltZeit - EinschaltZeit
    global abstand
    abstand = (Dauer * 34300) / 2  # Abstand mit Schallgeschwindigkeit berechnen (dividiert durch 2, da Hin und Rückweg)
    if abstand < 2 or (round(abstand) > 300):  # Wenn Abstand zu klein bzw. groß starte Messung erneut
        print("Abstand ausserhalb der Messreichweite! Erneut Versuchen in 5 Sekunden")
        print("Der Abstand ist: " + str(round(abstand)) + " cm")
        time.sleep(5)
        Ultraschall_Sensor()
    else:
        print("Der Abstand ist: " + str(round(abstand)) + " cm")


try:
    while True:
        # Abstandsmessung starten
        Ultraschall_Sensor()
        if abstand < 20:  # wenn zu wenig Flüssigkeit dann .....
            print("Zu wenig Flüssigkeit!")
            rote_LED()
            Piezo_Buzzer(500)  # Frequenz 500 Hz übergeben
            Temp_Pressure_Sensor()
            time.sleep(5)
            continue  # Abstand nochmal messen
        else:
            gruene_LED()
            print("Genug Flüssigkeit vorhanden - Keine Maßnahme erforderlich")
            time.sleep(60)
            continue

# Aufräumen nach Programm Ende
except KeyboardInterrupt:
    GPIO.cleanup()
    print("\n GPIO CLEAN!")
