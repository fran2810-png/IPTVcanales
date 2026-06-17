import requests

FUENTES = [
    "https://iptv-org.github.io/iptv/index.m3u",
]

playlist = "#EXTM3U\n\n"

for fuente in FUENTES:

    try:

        r = requests.get(fuente, timeout=30)

        if r.status_code == 200:

            texto = r.text.replace("#EXTM3U", "")

            playlist += texto.strip() + "\n\n"

    except:
        pass


try:

    with open("mis_canales.m3u","r",encoding="utf8") as f:

        texto=f.read().replace("#EXTM3U","")

        playlist+=texto

except:

    pass


with open("playlist.m3u","w",encoding="utf8") as f:

    f.write(playlist)
