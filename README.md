# SYN Flood

This Python script is designed to perform a SYN Flood attack, which is a type of Denial-of-Service (DoS) attack that involves sending numerous SYN packets to a specified target IP address and port. The script utilizes IP spoofing to obscure the source IP address of the packets, making it harder to trace the attack back to its origin. It requires root privileges to run and can target any specified IP and port, defaulting to the local gateway if no arguments are provided

### install

```bash
git clone https://github.com/savasick/synflood.git
cd synflood
python3 -m venv venv
source venv/bin/activate
pip3 install -r requirements.txt
```

### usage

send to router-IP 80-port (Can disrupt LAN network and make it unavailable)
```bash
sudo python3 synflood.py
```

send to 192.168.5.110-IP 443-port
```bash
sudo python synflood.py 192.168.5.110 443
```
