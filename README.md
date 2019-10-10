## 2019-10-10

motion project
https://motion-project.github.io/

Auflösung der cam:
https://picamera.readthedocs.io/en/release-1.12/fov.html


Als user `motion` die sqlite3 database erzeugen und tabelle anlegen
```
CREATE TABLE security (camera int, filename char(80) not null, frame int, file_type int, time_stamp timestamp without time zone, event_time_stamp timestamp without time zone);
```

Motion hat das konzept von einem "event".
Ein event zeichnet mehrere frames auf.
Wenn eine weitere motion innerhalb von `event_gap` sekunden erkannt wird,
werden die frames zu dem gleichen event gezaehlt.
Events werden in der Datenbank ueber `event_time_stamp` identifiziert.

bei gleicher belichtung - maessiges zimmerlicht, nachmittags
3280x2464 -> ungefaehr 1fps
1920x1080 -> 3fps
