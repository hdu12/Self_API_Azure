from wakeonlan import send_magic_packet
def wol(mac):
    send_magic_packet(mac)
    return 'succeed'