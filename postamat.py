from datetime import datetime


class Postamat:
	def __init__(self, id_, name, address, address_struct, status, is_automated,
					accept_payments, accept_cash, accept_card, bank_terminal, 
					working_hours, type_=None, status_code=None, lat=None, 
					lng=None, description=None):
		self.id = id_
		self._name = name
		self.address = address
		self._address_struct = address_struct
		self._status = status
		self.is_automated = is_automated
		self._accept_payments = accept_payments
		self.accept_cash = accept_cash
		self.accept_card = accept_card
		self.bank_terminal = bank_terminal
		self._working_hours = working_hours
		self.type = type_
		self.status_code = status_code
		self.lat = lat
		self.lng = lng
		self.description = description
		
		
	@property
	def name(self):
		return self._name
		
	@property
	def address_struct(self):
		return self._address_struct
		
	@property
	def status(self):
		return self._status
	
	@property
	def accept_payments(self):
		return self._accept_payments
		
	@property
	def working_hours(self):
		return self._working_hours
	
	
	def is_working_now(self):
		day = datetime.weekday(datetime.now())
		try:
			schedule = self.working_hours[day]
			time_now = datetime.now().time()
			time_open = datetime.strptime(schedule['time_open'], "%H:%M").time()
			time_close = datetime.strptime(schedule['time_close'], "%H:%M").time()
			if time_now > time_open and time_now < time_close:
				print(f"this postamat (id={self.id}) is working")
			else:
				print(f"this postamat (id={self.id}) doesn't work now")
		except:
			print(f"this postamat (id={self.id}) doesn't work today")
			
	
	def say_status(self):
		print(f"postamat's with id={self.id} status is \'{self.status}\'")
	
	
	def __str__(self):
		return f"{self.name} {self.address}, id={self.id}"
			
		
		


