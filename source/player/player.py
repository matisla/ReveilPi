import os, time

def lire(fichier):
    os.system('omxplayer -o local -r {}'.format(fichier) )

    time.sleep(3)
    os.system('echo -n q > /home/pi/bin/omfifo')

if __name__ == '__main__':
    lire('../music/Roxette-The_Look.mp3')
