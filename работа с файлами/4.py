with open("config_sw1", 'r') as f:
    for line in f:
        if not line.startswith("!"):
            print(line.rstrip())