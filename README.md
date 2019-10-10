## 2019-10-10

motion project
https://motion-project.github.io/

Auflösung der cam:
https://picamera.readthedocs.io/en/release-1.12/fov.html


Als user `motion` die sqlite3 database erzeugen und tabelle anlegen
```
CREATE TABLE security (camera int, filename char(80) not null, frame int, file_type int, time_stamp timestamp without time zone, event_time_stamp timestamp without time zone);
```

Zu motion:
* Motion hat das konzept von einem "(motion) event".
* Ein event kann mehrere frames beinhalten
* Wenn eine weitere motion innerhalb von `event_gap` sekunden erkannt wird, werden die frames zu dem gleichen event gezählt.
* Events werden in der Datenbank über `event_time_stamp` identifiziert.
* Mit `post_capture` kann man die anzahl der frames nach einer bewegung einstellen. wahrscheinlich wichtig für uns wegen motion blur
* Wichtig `threshold` ist wahrscheinlich zu groß um bewegung auf einer kleinen bildflaeche zu erkennen

bei gleicher belichtung - maessiges zimmerlicht, nachmittags
```
3280x2464 -> ungefaehr 1fps
1920x1080 -> 3fps
```

Google Drive Folder für Daten
https://drive.google.com/drive/folders/1CwqrDiGBhyMPjHcpFzJEgv0bM2oV608s?usp=sharing

`rclone` auf raspi pi konfiguriert.

Gelernt wie man cron jobs in systemd konfiguriert:

`/home/pi/.local/share/systemd/user/foobar.service`:
```
[Unit]
Description = some quux

[Service]
Type = oneshot
ExecStart = /home/pi/insects/bin/bla.sh
StandardOutput = journal

[Install]
WantedBy = default.target
```

`/home/pi/.local/share/systemd/user/foobar.timer`:
```
[Timer]
OnCalendar=*-*-* *:*:*

[Install]
WantedBy=default.target
```
