from scapy.all import sniff, IP, Raw

def packet_callback(packet):
    if IP in packet:
        src_ip = packet[IP].src
        dst_ip = packet[IP].dst
        proto = packet[IP].proto

        print(f"Source IP: {src_ip}")
        print(f"Destination IP: {dst_ip}")
        print(f"Protocol: {proto}")

        if Raw in packet:
            payload = packet[Raw].load
            print(f"Payload: {payload.hex()}")

# Start capturing packets
print("Starting packet capture...")
sniff(prn=packet_callback, store=0)
