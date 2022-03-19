# first whatsapp web scan with your mobail 

# pip install pywhatkit
# pip install flask
import pywhatkit
number = 6260702385
msg = "Halo"
time_h = 17 # 24 hour formet
time_m = 4 # minut
pywhatkit.sendwhatmsg(f"+91{number}",msg,time_h,time_m)

