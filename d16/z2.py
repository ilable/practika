ipad = ['8.8.4.4', '1.1.1.1-3', '172.21.41.128-172.21.41.132']


def convert_ranges_to_ip_list(ip):
    keyer = {}
    for i, addrs in enumerate(ip):
        addrs = addrs.split(".")
        keyer[i] = addrs
        for tiresha in keyer[i]:
            if "-" in tiresha:
                if len(keyer[i]) > 4:
                    more = keyer[i]
                    r1 = int((more[more.index(tiresha)].split("-"))[0])
                    r2 = int(more[-1])
                    getindex = more.index(tiresha)
                    keyer[i].remove(keyer[i][-1])
                    keyer[i].remove(keyer[i][-2])
                    keyer[i].remove(keyer[i][-3])

                    for rm in range(r1 + 1, r2 + 1):
                        rm += 1
                        keyer[i][getindex] = str(rm)
                        print(".".join(keyer[i]))
                else:
                    small = keyer[i]
                    ranguage_zmoll = int((small[small.index(tiresha)].split("-")[-1])) - int((small[small.index(tiresha)].split("-")[0]))
                    getindex = small.index(tiresha)
                    for rz in range(ranguage_zmoll + 1):
                        rz = rz + 1
                        keyer[i][getindex] = str(rz)
                        print(".".join(keyer[i]))


if __name__ == "__main__":
    k = convert_ranges_to_ip_list(ipad)
