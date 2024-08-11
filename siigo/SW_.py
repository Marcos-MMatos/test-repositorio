import telnetlib

host ="192.168.10.1"
password = "cisco"

tn = telnetlib.Telnet(host)
tn.read_until(b'Password:')
tn.write(password.encode('ascii') + b"\n")

tn.write(b"enable\n")
tn.write()