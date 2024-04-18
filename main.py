time = 0
serial_str = ""
result2 = False
web_title = ""
html = ""
LED_statusString = ""
LED_buttonString = ""
"""

ESP8266 ESP-01 Wifi control via AT commands on BBC micro:bit

by Alan Wang

"""
# for wifi connection
def wait_for_response(str2: str):
    global time, serial_str, result2
    time = input.running_time()
    while True:
        serial_str = "" + serial_str + serial.read_string()
        if len(serial_str) > 200:
            serial_str = serial_str.substr(len(serial_str) - 200, 0)
        if serial_str.includes(str2):
            result2 = True
            break
        if input.running_time() - time > 300000:
            break
    return result2
# generate HTML
def getHTML(normal: bool):
    global web_title, html, LED_statusString, LED_buttonString
    web_title = "ESP8266 (ESP-01) Wifi on BBC micro:bit"
    # HTTP response
    html = "" + html + "HTTP/1.1 200 OK\r\n"
    html = "" + html + "Content-Type: text/html\r\n"
    html = "" + html + "Connection: close\r\n\r\n"
    html = "" + html + "<!DOCTYPE html>"
    html = "" + html + "<html>"
    html = "" + html + "<head>"
    html = "" + html + "<link rel=\"icon\" href=\"data:,\">"
    html = "" + html + "<title>" + web_title + "</title>"
    # mobile view
    html = "" + html + "<meta name=\"viewport\" content=\"width=device-width, initial-scale=1\">"
    html = "" + html + "</head>"
    html = "" + html + "<body>"
    html = "" + html + "<div style=\"text-align:center\">"
    html = "" + html + "<h1>" + web_title + "</h1>"
    html = "" + html + "<br>"
    # generate status text
    if normal:
        LED_status = 0
        if LED_status:
            LED_statusString = "ON"
            LED_buttonString = "TURN IT OFF"
        else:
            LED_statusString = "OFF"
            LED_buttonString = "TURN IT ON"
        html = "" + html + "<h3>LED STATUS: " + LED_statusString + "</h3>"
        html = "" + html + "<h3>Light Level STATUS: " + str(input.light_level()) + "</h3>"
        html = "" + html + "<h3>Temp STATUS: " + str(input.temperature()) + "</h3>"
        html = "" + html + "<br>"
        # generate buttons
        html = "" + html + "<input type=\"button\" onClick=\"window.location.href='LED'\" value=\"" + LED_buttonString + "\">"
        html = "" + html + "<br>"
    else:
        html = "" + html + "<h3>ERROR: REQUEST NOT FOUND</h3>"
    html = "" + html + "<br>"
    html = "" + html + "<input type=\"button\" onClick=\"window.location.href='/'\" value=\"Home\">"
    html = "" + html + "</div>"
    html = "" + html + "</body>"
    html = "" + html + "</html>"
    return html