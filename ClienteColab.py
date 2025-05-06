from requests import get
import requests
from bs4 import BeautifulSoup
from time import sleep
from os.path import exists
from json import load, dump
from google.colab import output
from ipywidgets import widgets
from jupyter_ui_poll import ui_events
drive_path = '/content/drive/MyDrive/minecraft'
SERVERCONFIG = f'{drive_path}/server_list.txt'
# @title Create Server
# @markdown ####**Create your server.**
server_name = "Tralaleritos" # @param {type:"string"}
if server_name == "": ERROR("Please insert a name for your server.")
# GUIDANCE
choice = input('Do you want to show(s)/hide(h) tunnels info? - ')
if 's' in choice: clear_output(); print("\n\n- **[Ngrok](https://ngrok.com)**\n  + Follow the prompts.\n  + The IP will change whenever you restart the server.\n\n- **[Cloudflare's argo](https://www.cloudflare.com/)** :\n    - If the 'Your free tunnel has started!' notification appears => Done.\n    - Access to your server:\n    1. Download [Cloudflared client](https://github.com/cloudflare/cloudflared/releases/).\n    2. Launch the binary with `<your Cloudflare file name> access tcp --hostname <tunnel_address> --url 127.0.0.1:25565` (note: tunnel_address is your address which has been set on your Cloudflare).\n    4. Finally, connect to `127.0.0.1:25565` from the minecraft client which is located in that machine.\n\n- **[Localtonet](https://localtonet.com/)**:\n  1. Navigate to [TCP-UDG](https://localtonet.com/tunnel/tcpudp) page. Select TCP in Protocol Types.\n  2. Get your authtoken from [Authtoken](https://localtonet.com/usertoken).\n  3. Pick the server you'd like your tunnel to operate on.\n  4. Input the IP and Port values the tunnel will listen to, in this case, for Minecraft, it's typically IP: 127.0.0.1 and Port: 25565.\n  5. Finally, create and start your tunnel by pressing the Start button.\n  - Read more on [how-to-use-localtonet-with-minecraft](https://localtonet.com/documents/using-localtonet-with-minecraft)\n\n- **[Zrok](https://zrok.io/)**:\n  1. Download the zrok app through [link](https://docs.zrok.io/docs/getting-started/)\n  2. Open the shell. Type `zrok invite` to sign up and get the authtoken\n  3. Follow the prompts\n  4. Acess to https://api.zrok.io to get fully management\n   - Read more on https://docs.zrok.io/docs/getting-started. \n\n- **[PlayIt](https://playit.gg/)**: follow the prompts."); sleep(20)
clear_output()

#---------------------------------------------------------------------------------- SNALL FUNCTION ------------------------------------------------------------------------------------#
def SERVERSJAR(command, server_type=None, version=None):
  #Get the download URL (jar) AND return the detailed versions for each software (all)
  if command == "GetVersions":
    if server_type == None: ERROR("No server type specified.")
    Server_Jars_All = {
      'paper': 'https://api.papermc.io/v2/projects/paper', 'velocity': 'https://api.papermc.io/v2/projects/velocity',
      'purpur': 'https://api.purpurmc.org/v2/purpur',
      'mohist': 'https://mohistmc.com/api/v2/projects/mohist', 'banner': 'https://mohistmc.com/api/v2/projects/banner',
      'folia': 'https://api.papermc.io/v2/projects/folia'
    }
    if server_type == 'vanilla' or server_type=='snapshot':
      rJSON = GET('https://launchermeta.mojang.com/mc/game/version_manifest.json').json()
      if server_type == 'vanilla': server_type = 'release'
      if version != 'vanilla - latest_version': server_version = [hit["id"] for hit in rJSON["versions"] if hit["type"] == server_type]
      else:
        return rJSON['latest']['release']

    elif server_type == 'paper' or  server_type == 'velocity' or server_type == 'purpur' or server_type == 'mohist' or server_type == 'banner' or server_type == 'folia':
      rJSON = GET(Server_Jars_All[server_type]).json()
      server_version = [hit for hit in rJSON["versions"]]

    elif server_type == 'fabric':
      rJSON = GET('https://meta.fabricmc.net/v2/versions/game').json()
      server_version = [hit['version'] for hit in rJSON if hit['stable'] == True]

    elif server_type == 'forge':
      from bs4 import BeautifulSoup
      rJSON = GET('https://files.minecraftforge.net/net/minecraftforge/forge/index.html')
      soup = BeautifulSoup(rJSON.content, "html.parser")
      server_version = [tag.text for tag in soup.find_all('a') if '.' in tag.text and '\n' not in tag.text]
    elif server_type == "bedrock":
      import requests
      from bs4 import BeautifulSoup

      URL = "https://www.minecraft.net/en-us/download/server/bedrock/"
      BACKUP_URL = "https://raw.githubusercontent.com/ghwns9652/Minecraft-Bedrock-Server-Updater/main/backup_download_link.txt"
      HEADERS = {"User-Agent": "Mozilla/5.0 (X11; CrOS x86_64 12871.102.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.141 Safari/537.36"}

      try:
          page = requests.get(URL, headers=HEADERS, timeout=5)

          soup = BeautifulSoup(page.content, "html.parser")

          a_tag_res = []
          for a_tags in soup.findAll('a', attrs={"aria-label":"Download Minecraft Dedicated Server software for Ubuntu (Linux)"}):
            a_tag_res.append(a_tags['href'])

          download_link=a_tag_res[0]

      except requests.exceptions.Timeout:
          LOG("timeout raised, recovering")
          page = requests.get(BACKUP_URL, headers=HEADERS, timeout=5)

          download_link=page.text
      server_version = download_link.split('bedrock-server-')[1].split(".zip")[0]
    elif server_type == "arclight":
      LOG('Before going deeper, please check out https://github.com/IzzelAliz/Arclight')
      rJSON = GET('https://files.hypoglycemia.icu/v1/files/arclight/minecraft').json()['files']
      server_version  = [hit['name'] for hit in rJSON]
    return server_version

  elif command == "GetDownloadUrl":
    if version == None: ERROR("No version specified.")
    # RETURN DOWNLOAD URL
    if server_type == 'vanilla' or server_type=='snapshot':
      rJSON = GET('https://launchermeta.mojang.com/mc/game/version_manifest.json').json()
      if server_type == 'vanilla': server_type = 'release'
      for hit in rJSON["versions"]:
        if hit["type"] == server_type and hit['id'] == version:
          return GET(hit['url']).json()["downloads"]['server']['url']

    elif server_type == 'paper' or  server_type == 'velocity' or server_type == 'folia':
      build = GET(f'https://api.papermc.io/v2/projects/{server_type}/versions/{version}').json()["builds"][-1]
      jar_name = GET(f'https://api.papermc.io/v2/projects/{server_type}/versions/{version}/builds/{build}').json()["downloads"]["application"]["name"]
      return f'https://api.papermc.io/v2/projects/{server_type}/versions/{version}/builds/{build}/downloads/{jar_name}'

    elif server_type == 'purpur':
      build = GET(f'https://api.purpurmc.org/v2/purpur/{version}').json()["builds"]["latest"]
      return f'https://api.purpurmc.org/v2/purpur/{version}/{build}/download'

    elif server_type == 'mohist' or server_type == 'banner':
      return GET(f'https://mohistmc.com/api/v2/projects/{server_type}/{version}/builds').json()["builds"][-1]["url"]

    elif server_type == 'fabric':
      installerVersion = GET('https://meta.fabricmc.net/v2/versions/installer').json()[0]["version"]
      fabricVersion = GET(f'https://meta.fabricmc.net/v2/versions/loader/{version}').json()[0]["loader"]["version"]
      return "https://meta.fabricmc.net/v2/versions/loader/" + version + "/" + fabricVersion + "/" + installerVersion + "/server/jar"

    elif server_type == 'forge':
      from bs4 import BeautifulSoup
      rJSON = GET(f'https://files.minecraftforge.net/net/minecraftforge/forge/index_{version}.html')
      soup = BeautifulSoup(rJSON.content, "html.parser")
      tag =  soup.find('a', title="Installer"); tag = str(tag); tag = tag[tag.find('"') + 1 :]
      link = tag[:tag.find('"')]; link = link[link.find('=') + 1:]; link = link[link.find('=') + 1:]
      return link

    elif server_type == 'arclight':
      rJSON = GET(f'https://files.hypoglycemia.icu/v1/files/arclight/minecraft/{version}/loaders').json()
      LOG('Available type: '); print([hit['name'] for hit in rJSON['files']])
      build = input(' Type: '); choice = input('Stable(st) or Snapshot(sn): ')
      if 'sn' in choice.lower(): choice = 'latest-snapshot';
      else: choice = "latest-stable";
      return f'https://files.hypoglycemia.icu/v1/files/arclight/minecraft/{version}/loaders/{build}/{choice}'

    elif server_type == 'bedrock':
      LOG('Selecting latest version available...')
      import requests
      from bs4 import BeautifulSoup

      URL = "https://www.minecraft.net/en-us/download/server/bedrock/"
      BACKUP_URL = "https://raw.githubusercontent.com/ghwns9652/Minecraft-Bedrock-Server-Updater/main/backup_download_link.txt"
      HEADERS = {"User-Agent": "Mozilla/5.0 (X11; CrOS x86_64 12871.102.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.141 Safari/537.36"}

      try:
          page = requests.get(URL, headers=HEADERS, timeout=5)

          soup = BeautifulSoup(page.content, "html.parser")

          a_tag_res = []
          for a_tags in soup.findAll('a', attrs={"aria-label":"Download Minecraft Dedicated Server software for Ubuntu (Linux)"}):
            a_tag_res.append(a_tags['href'])

          download_link=a_tag_res[0]

      except requests.exceptions.Timeout:
          LOG("timeout raised, recovering")
          page = requests.get(BACKUP_URL, headers=HEADERS, timeout=5)

          download_link=page.text

      return download_link
    else: ERROR('Wrong server type.')
  elif command == "GetServerTypes": return ['vanilla','snapshot','paper','purpur','mohist', "arclight",'velocity', 'banner', 'fabric',"folia", 'forge', 'bedrock']
  else: ERROR("Not a valid command.")
#---------------------------------------------------------------------------------- MAIN CODE ------------------------------------------------------------------------------------#
LOG(f"\nColab Version: {colabversion}")
# Auditing whether file is existed.
if exists(f'{drive_path}/{server_name}'): ERROR('Server already exists. If you want to change server software go to the "Change Server Software" cell.')
# Create folder
MKDIR(f'{drive_path}/{server_name}')
LOG('Checking if folder created. Please wait.')
sleep(40)
LOG("Select your server type:")
stdrop = widgets.Dropdown(description="Server Type:", options=[""]+SERVERSJAR("GetServerTypes")) # Ask for server type
display(stdrop)
with ui_events() as poll:
    while stdrop.value == '':
        poll(10)          # React to UI events (upto 10 at a time)
        sleep(0.1)
stdrop.close()
server_type=stdrop.value                                                                        # End asking
#print("\n")
LOG(f'Choosen server type: {server_type}')
if server_type != "bedrock": # Check if server type isn't bedrock.
  LOG("Select your server version:")
  svdrop = widgets.Dropdown(description="Server version: ", style={'description_width': 'initial'}, options=['']+SERVERSJAR("GetVersions", server_type=server_type)) # Ask for server version
  display(svdrop)
  with ui_events() as poll:  # Wait until user chooses.
    while svdrop.value == '':
      poll(10)
      sleep(0.1)
  svdrop.close()
  version=svdrop.value
 # print("\n")                                                                                                                                                       # End asking
  LOG(f'\nChoosen server version: {version}')
else:
  version=SERVERSJAR("GetVersions", server_type=server_type)
  LOG("Using latest bedrock version")
LOG("Select a Tunnel provider:")
tunnelsrvs = widgets.Dropdown(description="Tunnel Service: ", style={'description_width': 'initial'}, options=['','ngrok', 'argo', 'zrok', 'playit', 'localtonet', 'localxpose', 'tailscale', "minekube-gate"]) # Ask for server version
display(tunnelsrvs)
with ui_events() as poll:  # Wait until user chooses.
    while tunnelsrvs.value == '':
        poll(10)
        sleep(0.1)
tunnelsrvs.close()
tunnel_service=tunnelsrvs.value                                                                                   # End asking
#print("\n")
LOG(f'Choosen Tunnel service: {tunnel_service}')
#print("\n")
# Load serverconfig
serverconfig = load(open(SERVERCONFIG))
serverconfig['server_list'] += [server_name]
serverconfig['server_in_use'] = server_name
if tunnel_service == 'ngrok':
  LOG("Tunnel Settings:")
  LOG('Get your authtoken from https://dashboard.ngrok.com/get-started/your-authtoken')
  token = input('Your authtoken: ')
  if token == "":
    ERROR("\nNo token provided")
  serverconfig['ngrok_proxy']['authtoken'] = token
  LOG('Available Regions:', ' ap - Asia/Pacific (Singapore)', ' au - Australia (Sydney)', ' eu - Europa (Frankfurt - Germany)', ' in - India (Mumbai)', ' jp - Japan (Tokyo)', ' sa - America (São Paulo - Brazil)', ' us - United States (Ohio)', sep='\n')
  serverconfig['ngrok_proxy']['region'] = input('Region: ')
elif tunnel_service == 'zrok':
  # Settings variable
  LOG("Tunnel Settings:")
  if "zrok_proxy" not in serverconfig:
    serverconfig["zrok_proxy"] = {"authtoken": ""}
  token = input('Your zrok token: ')
  if token == "":
    ERROR("\nNo token provided")
  serverconfig['zrok_proxy']['authtoken'] = token
elif tunnel_service == 'localtonet':
  LOG("Tunnel Settings:")
  LOG('Get your authtoken from https://localtonet.com/usertoken')
  if "localtonet_proxy" not in serverconfig:
    serverconfig["localtonet_proxy"] = {"authtoken": ""}
  token = input('Your localtonet token: ')
  if token == "":
    ERROR("\nNo token provided")
  serverconfig['localtonet_proxy']['authtoken'] = token
elif tunnel_service == 'localxpose':
  LOG("Tunnel Settings:")
  LOG('Get your authtoken from https://localxpose.io/dashboard/access')
  if "localxpose_proxy" not in serverconfig:
    serverconfig["localxpose_proxy"] = {"authtoken": ""}
  token = input('Your localxpose token: ')
  if token == "":
    ERROR("\nNo token provided.")
  serverconfig['localxpose_proxy']['authtoken'] = token
elif tunnel_service == 'tailscale':
  LOG("Tunnel Settings:")
  LOG('Get your authtoken from https://login.tailscale.com/admin/settings/keys . Make sure to select reusable')
  if "tailscale_proxy" not in serverconfig:
    serverconfig["tailscale_proxy"] = {"authtoken": ""}
  if "machine_info" not in serverconfig["tailscale_proxy"]:
    serverconfig["tailscale_proxy"]["machine_info"] = ""
  sleep(10)
  token = input('Your tailscale token: ')
  if token == "":
    ERROR("\nNo token provided.")
  serverconfig['tailscale_proxy']['authtoken'] = token
elif tunnel_service == 'minekube-gate':
  LOG('Get your token from https://app.minekube.com/orgs')
  if "minekube-gate_proxy" not in serverconfig:
    serverconfig["minekube-gate_proxy"] = {"token": ""}
  token = input('Your minekube token: ')
  if token == "":
    ERROR("\nNo token provided")
  serverconfig["minekube-gate_proxy"]['token'] = token

dump(serverconfig, open(SERVERCONFIG, 'w'))
# Set up colabconfig
colabconfig = {"server_type": server_type, "server_version": version, "tunnel_service" : tunnel_service}
dump(colabconfig, open(COLABCONFIG(server_name),'w'))
# Download jar file
if server_type == "bedrock":
  DOWNLOAD_FILE(url = SERVERSJAR("GetDownloadUrl", server_type, version), path = f"{drive_path}/{server_name}", file_name='bedrock-server.zip', force=True, headers={"User-Agent":"Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; BEDROCK-UPDATER)"})
  LOG("Unzipping bedrock server zip.")
  ! unzip {drive_path}/{server_name}/bedrock-server.zip -d {drive_path}/{server_name} >/dev/null && $log "Successfully unzipped" || echo "unzip error."
  LOG("Unzipped successfully")
  sleep(10)
  LOG('\nCompleted!')
else:
  if server_type == 'forge': jarname = 'forge-installer.jar' # The jar file name (forge need a special process)
  else: jarname = JAR_LIST_RUN(version)[server_type]
  DOWNLOAD_FILE(url= SERVERSJAR("GetDownloadUrl", server_type, version), path = f"{drive_path}/{server_name}", file_name= jarname)
  sleep(40)
  LOG('\nCompleted!')