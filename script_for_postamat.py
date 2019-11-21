import argparse
import requests
import json
from postamat import Postamat


if __name__ == "__main__":
	parser = argparse.ArgumentParser()
	message1 = "if you wanna create Postamat's objects write one or a few ids separated by a space"
	parser.add_argument("--id", nargs="*", help=message1)
	message2 = "if you wanna know does Postamat's working choose ids and write yes"
	parser.add_argument("--is_working", help=message2)
	args = parser.parse_args()
	postamat_list = []
	for i in args.id:
		response = requests.get(f"https://api.tport.online/v2/public-stations/{i}/")
		if response.status_code == 200:
			response.encoding='utf-8'
			content = json.loads(response.text)
			postamat_list.append(
						Postamat(id_=content["id"], name=content["name"],
						address=content["address"], address_struct=content["address_struct"],
						status=content["status"], is_automated=content["is_automated"],
						accept_payments=content["accept_payments"], accept_cash=content["accept_cash"], 
						accept_card=content["accept_card"], bank_terminal=content.get("bank_terminal"),
						working_hours=content["working_hours"], 
						type_=content.get("type"), status_code=content.get("status_code"), 
						lat=content.get("lat"), lng=content.get("lng"), 
						description=content.get("description")
						))
		else:
			print("this id does not exist")
	for i in postamat_list:
		i.say_status()
	if args.id and args.is_working == 'yes':
		for i in postamat_list:
			i.is_working_now()
		
		
	
