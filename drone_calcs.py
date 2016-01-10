def fade(rssi,noise):
	return (float(rssi)-noise)/2

def rangemultiplier(fade):
	return 2**(fade/float(6))

def range(current_range,rssi,noise):
	return current_range*rangemultiplier(fade(rssi,noise))