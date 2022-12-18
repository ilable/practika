infiles = [
    "sh_cdp_n_sw1.txt",
    "sh_cdp_n_r1.txt",
    "sh_cdp_n_r2.txt",
    "sh_cdp_n_r3.txt",
]


def create_network_map(filenames):
    for file in filenames:
        with open(file, mode="r+") as f:
            file = f.read()
            q = {}
            file = file.split('\n')
            for line in file:
                main = []
                second = []
                if line.find('SW') != -1:
                    main_machine = "SW"
                elif line.find('Eth') != -1:
                    second_machine, main_eth, main_inter, *other, second_eth, second_inter = line.split()
                    main.append(main_machine)
                    second.append(second_machine)
                    main_interface = main_eth + main_inter
                    second_interface = second_eth + second_inter
                    main.append(main_interface)
                    second.append(second_interface)
                    main_tuple = tuple(main)
                    second_tuple = tuple(second)
                    q[main_tuple] = second_tuple
        return q


if __name__ == "__main__":
    q = create_network_map(infiles)
    print(q)

