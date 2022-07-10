from huawei_lte_api.Client import Client
from huawei_lte_api.Connection import Connection
from huawei_lte_api.enums.net import NetworkModeEnum

with Connection('http://YOUR_USERNAME:YOUR_PASSWORD@YOUR_HUAWEI_IP/') as connection:
    client = Client(connection)
    print("{}'s network is being refreshed...".format(client.device.basic_information()['devicename']))
    client_network_mode = client.net.net_mode()
    client.net.set_net_mode(client_network_mode['LTEBand'], client_network_mode['NetworkBand'], NetworkModeEnum.MODE_3G_ONLY)
    client.net.set_net_mode(client_network_mode['LTEBand'], client_network_mode['NetworkBand'], NetworkModeEnum.MODE_4G_ONLY)
    print("Done!")