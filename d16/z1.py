import subprocess

ip_lists = ['192.168.1.1', '192.168.1.100', '8.8.8.8', '1.1.1.1']


def ping_ip_addresses(ip):
    alive = []
    die = []
    all = {}
    for i in ip:
        if subprocess.run("ping" + " i").returncode == 0:
            print(i + " Пингуется!")
            alive.append(i)
        else:
            print(i + " Не пингуется")
            die.append(i)
    all["ALIVE"] = alive
    all["DIE"] = die
    return all

if __name__ == "__main__":
    getip = ping_ip_addresses(ip_lists)
    print(getip)