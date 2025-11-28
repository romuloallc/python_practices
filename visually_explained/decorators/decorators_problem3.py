import time

# TODO create the mission_timer decorator and decorate both functions
def mission_timer(base_fn):
    def enhanced_fn(*args, **kwargs):
        print("3...")
        print("2...")
        print("1...")
        start_time = time.time()
        result = base_fn(*args, **kwargs)
        end_time = time.time()
        print(f"Mission duration: {end_time - start_time} seconds")
        print(" ")
        return result
    return enhanced_fn
    
@mission_timer
def launch_probe(target):
    print(f"Launching probe toward {target}...")
    time.sleep(1)
    return f"Probe successfully en route to {target}."

@mission_timer
def deploy_satellite(orbit_type, altitude_km):
    print(f"Deploying satellite into {orbit_type} orbit at {altitude_km} km...")
    time.sleep(2)

# Call both functions

def main():
    deploy_satellite("polar", 800)

    result = launch_probe("Europa")
    print("Stored mission result:", result)


if __name__ == "__main__":
    main()
