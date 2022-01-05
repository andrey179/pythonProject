import pywhatkit
from openxl2 import DataComponents

if __name__ == '__main__':
    pywhatkit.sendwhatmsg(DataComponents.get_phone,
                          DataComponents.get_message,
                          DataComponents.get_hours,
                          DataComponents.get_minutes)
