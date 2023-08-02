class Tv:

	volume_range = range(0,101)
	active_channel_range = range(1,11)
	input_options = ["Anthena", "HDMI1", "HDMI2", "HDMI3"]
	size_options = [42, 50, 55, 65, 75]

	def __init__(self, active_channel:int, _input:str, size, on=False, volume=0):
		self.on = on
		self.volume = volume 
		self.active_channel = active_channel
		self.input = _input
		self.size = size 

	def switch_on(self):
		if self.on == False:
			self.on = True
		else:
			print('TV is already on')

	def switch_off(self):
		if self.on == True:
			self.on = False
		else:
			print("TV is already off")

	def set_volume(self, new_volume):
		if new_volume in volume_range:
			self.volume = new_volume
		else:
			print('Please select a volume value between 0 and 100')

	def change_channel(self, new_channel):
		if new_channel in active_channel_range:
			self.active_channel = new_channel
		else:
			print('Please select a channel between 1 and 10')

	def set_input(self, new_input):
		if new_input in input_options:
			self.input = new_input
		else:
			print('Please select one of the following inputs: "Anthena", "HDMI1", "HDMI2", "HDMI3" ')
