import os
import requests
import random
url=input("Type vudeo url: ")
name=f"tiktok video{random.randint(1,100000)}"
f=open(f'{name}.mp4',"wb")
url = url.split("?")[0]
url=url.replace(":","%3A")
url=url.replace("/","%2F")
ufr = requests.get(f"https://savevideo.ninja/wp-admin/admin-ajax.php?action=wppress_svd_download&url={url}&key=vid-no-watermark")
f.write(ufr.content)
f.close()
