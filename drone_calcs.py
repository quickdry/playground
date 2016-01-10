def fade(rssi,noise):
    return (float(rssi)-noise)/2

def rangemultiplier(fade):
    """fade multiplier"""
    return 2**(fade/float(6))

def range(current_range,rssi,noise):
    """range may be any type of distance measure"""
    return current_range*rangemultiplier(fade(rssi,noise))
    
