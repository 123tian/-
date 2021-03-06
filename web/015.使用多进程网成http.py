import socket
import re
import multiprocessing

def service_client(new_socket):
  """为这个客户端返回数据"""

  # http: // 127.0.0.1: 7890 / index.html

  # 1. 接收浏览器发送过来的请求，即http请求
  # GET / HTTP/1.1
  # ……
  request = new_socket.recv(1024).decode("utf-8")
  # decode("utf-8") 解码

  print(request)

  # 切割 （行）
  request_lines = request.splitlines()
  print("")
  print(">"*20)
  print(request_lines)

  # GET /index.html HTTP/1.1
  # get post put del
  ret = re.match(r"[^/]+(/[^ ]*)", request_lines[0])  # GET /index.html HTTP/1.1

  if ret:
    file_name = ret.group(1)
    print("*"*30, file_name)


  # 2. 返回http格式的数据给浏览器
  # 2.1 准备发送给浏览器的数据：Header
  response = "HTTP/1.1 200 OK\r\n"  # /r/n 换行 /r:兼容所有的浏览器

  response += "\r\n"  # 用空行区分 那个是头  那个是体

  # 2.2 准备发送给浏览器的数据：Body
  # response += "<h1>hahaha</h1>"

  # f = open("../shouye/index.html", "rb")
  try:
    f = open("../shoye" + file_name, "rb")
  except:
    response = "HTTP/1.1 404 NO             T FOUND\r\n"  # \r\n兼容微软的
    response += "\r\n"
    response += "---file not found--"
    new_socket.send(response.encode("utf-8"))
    new_socket.send(html_content)
  else:
    html_content = f.read()
    f.close()

    response = "HTTP/1.1 200 OK\r\n"  # \r\n兼容微软的
    response += "\r\n"

  # 将response Header发送给浏览器
  new_socket.send(response.encode("utf-8"))
  # 将response Body发送给浏览器
  new_socket.send(html_content)


  # 关闭套接字
  new_socket.close()

def main():
  """用来完成整体的控制"""
  # 1. 创建套接字
  tcp_server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
  tcp_server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

  # 2. 绑定端口
  tcp_server_socket.bind(("", 7890))

  # 3. 变为监听套接字（最大连接数是128）
  tcp_server_socket.listen(128)  # 128 ： 最大连接数

  while True:
    # 4. 等待新客户端的链接
    new_socket, client_addr = tcp_server_socket.accept()

    # 5. 为这个客户端服务
    p =  multiprocessing.Process(target=service_client, args=(new_socket ,))
    p.start()


    new_socket.close()
      # 6.关闭监听套接字
  tcp_server_socket.close()



if __name__ == "__main__":
  main()
