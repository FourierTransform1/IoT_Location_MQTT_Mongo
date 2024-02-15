
# 1 metre = 0.00000899*cos(lat) degree

def walkingEast(latitude, longitude, steps):
    longitude += (0.0000123*steps)   # 0.0000123 is around one step east 
    return latitude, longitude


# -0.0000123 = one step west --- 1 metre = 0.00000899*cos(lat) degree
def walkingWest(latitude, longitude, steps):
    longitude -= (0.0000123*steps)      # one step west 
    return latitude, longitude


# 0.0000056 = one step east --- 1 metre = 0.00000899*cos(lat) degree
def walkingNorth(latitude, longitude, steps):
    latitude += (0.0000056*steps)      # 0.00056 is one step North 
    return latitude, longitude


# 0.0000056 = one step east --- 1 metre = 0.00000899*cos(lat) degree
def walkingSouth(latitude, longitude, steps):
    latitude -= (0.0000056*steps)      # one step South 
    return latitude, longitude


