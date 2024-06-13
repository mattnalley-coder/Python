import os

def create_pcap_files(input_file):
    with open(input_file, 'r') as f:
        lines = f.readlines()

    for line in lines:
        parts = line.strip().split(':')
        if len(parts) == 4:
            mac, _, bssid, password = parts
            output_file = "{}_{}.pcap.cracked".format(bssid, mac)
            if not os.path.exists(output_file):
                with open(output_file, 'w') as f:
                    f.write(password)
            else:
                print("File '{}' already exists, skipping.".format(output_file))

if __name__ == "__main__":
    input_file = "wpa-sec.cracked.potfile"
    if os.path.exists(input_file):
        create_pcap_files(input_file)
        print("PCAP files created successfully.")
    else:
        print("Input file '{}' not found.".format(input_file))
