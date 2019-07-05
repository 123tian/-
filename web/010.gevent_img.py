import urllib.request
import gevent
from gevent import monkey

monkey.patch_all()

def downloader(img_name,img_url):
  req = urllib.request.urlopen(img_url)
  img_content = req.read()

  with open(img_name,"wb") as f:
    f.write(img_content)


def main():
  gevent.joinall([
    gevent.spawn(downloader,"3.png","https://rpic.douyucdn.cn/asrpic/190702/96291_2126.png"),
    gevent.spawn(downloader,"2.png","https://rpic.douyucdn.cn/asrpic/190702/5551871_2128.png"),
  ])
if __name__ == '__main__':
  main()

