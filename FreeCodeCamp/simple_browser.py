import socket
import ssl
import re
import urllib.request, urllib.parse, urllib.error

def get_socket (url, host):
  sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

  context = ssl.create_default_context()
  secure_sock = context.wrap_socket(sock, server_hostname="github.com")

  secure_sock.connect(("github.com", 443))
  cmd_str = f"GET {url} HTTP/1.1\r\nHost: {host}\r\nConnection: close\r\n\r\n"
  cmd = cmd_str.encode()
  secure_sock.send(cmd)
  response = b""
  while True:
    data = secure_sock.recv(4096)
    if not data:
      print("Data unavailable")
      break
    response += data
  secure_sock.close()
  return response.decode()

def get_links(url):
  fhand = urllib.request.urlopen(url)
  response = ""
  links = []
  if (fhand):
      for l in fhand:
        response += l.decode()
        links += re.findall(r"http[^\"\']+", response)
      return links


def get_urllib(url):
  links = [url]
  links += get_links(url)
  links = set(links)

  for link in links:
    fhand = urllib.request.urlopen(url)
    response = ""
    li = link.split("/")
    filename = li[len(li)-1]

    for line in fhand:
      response += line.decode()
    if (filename):
      print(f"Saving file from {link}")
      extension = str(re.findall("\.\S+",filename))
      if(extension == "com" or extension == None):
        with open(f"scraper/{filename}.html", "+a") as file:
          file.write(response)
      else:
        with open(f"scraper/{filename}", "+a") as file:
          file.write(response)
    else:
      print(f"No file to save")




# resp_socket = get_socket("/DrPedroEmanuel/R-Anthropic-Assistant/blob/main/README.md", "github.com")
# response_str = re.findall(r"(?s)<!DOC.*$", resp_socket)
# resp_socket = resp_socket.join(response_str)

#response = r"https://github.githubassets.com/assets/light-605318cbe3a1.css"
#link = response.split("/")
#print(link[len(link)-1])

resp_urllib = get_urllib("https://github.com/DrPedroEmanuel/R-Anthropic-Assistant/blob/main/README.md")
#mylinks = get_links("https://github.com/DrPedroEmanuel/R-Anthropic-Assistant/blob/main/README.md")
#print(mylinks)
# with open ("gh_readme.html", "+a") as file:
  # file.write(resp_socket)
