# /etc/init.d/inici.py
### BEGIN INIT INFO
# Provides:          sample.py
# Required-Start:    $remote_fs $syslog
# Required-Stop:     $remote_fs $syslog
# Default-Start:     2 3 4 5
# Default-Stop:      0 1 6
# Short-Description: Start daemon at boot time
# Description:       Enable service provided by daemon.
### END INIT INFO

import os

os.system("python3 /home/pi/Desktop/Sirah/Python/ManageIrrigationProcessess.py &")
os.system("chromium-browser http://127.0.0.1:1880/ui --kiosk &")
