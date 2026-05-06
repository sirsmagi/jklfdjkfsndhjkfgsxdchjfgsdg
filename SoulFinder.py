import requests
import os
import phonenumbers
from phonenumbers import geocoder
from phonenumbers import carrier
from rich import print

while True:

	if os.name == "nt":
		os.system("cls")
	else:
		os.system("clear")

	print(r"[#00BFFF]  _________            .__  ___________.__            .___             [/#00BFFF]")
	print(r"[#00BFFF] /   _____/ ____  __ __|  | \_   _____/|__| ____    __| _/___________  [/#00BFFF]")
	print(r"[#80DFFF] \_____  \ /  _ \|  |  \  |  |    __)  |  |/    \  / __ |/ __ \_  __ \ [/#80DFFF]")
	print(r"[#80DFFF] /        (  <_> )  |  /  |__|     \   |  |   |  \/ /_/ \  ___/|  | \/ [/#80DFFF]")
	print(r"[#FFFFFF]/_______  /\____/|____/|____/\___  /   |__|___|  /\____ |\___  >__|   [/#FFFFFF]")
	print(r"[#FFFFFF]        \/                       \/            \/      \/    \/ [/#FFFFFF]")

	print("[#00BFFF](created by Dexter Morgan XD)")

	print(r"[#FFFFFF][1]Поиск[#80DFFF] по [#00BFFF]номеру ")
	print(r"[#FFFFFF][2]Поиск[#80DFFF] по [#00BFFF]username ")
	print(r"[#FFFFFF][3]Поле[#80DFFF]зные сайты по [#00BFFF]OSINT ")
	print(r"[#FFFFFF][0]Вы[#80DFFF]хо[#00BFFF]д")

	what = int(input("==>"))

	if what == 1:
		if os.name == "nt":

			os.system('cls')

			print(r"[#00BFFF]  _________            .__  ___________.__            .___             [/#00BFFF]")
			print(r"[#00BFFF] /   _____/ ____  __ __|  | \_   _____/|__| ____    __| _/___________  [/#00BFFF]")
			print(r"[#80DFFF] \_____  \ /  _ \|  |  \  |  |    __)  |  |/    \  / __ |/ __ \_  __ \ [/#80DFFF]")
			print(r"[#80DFFF] /        (  <_> )  |  /  |__|     \   |  |   |  \/ /_/ \  ___/|  | \/ [/#80DFFF]")
			print(r"[#FFFFFF]/_______  /\____/|____/|____/\___  /   |__|___|  /\____ |\___  >__|   [/#FFFFFF]")
			print(r"[#FFFFFF]        \/                       \/            \/      \/    \/ [/#FFFFFF]")

			
			print("[#00BFFF] Введите номер (+1999999999):")

			numwhat = input("==>")

			number = phonenumbers.parse(numwhat, None)

			print(number,geocoder.description_for_number(number,"en"), carrier.name_for_number(number,"en"))

			if phonenumbers.is_valid_number(number):
				print("[#FFFFFF]Но[#80DFFF]мер ва[#00BFFF]лидный")
			else:
				print("[#FFFFFF]Но[#80DFFF]мер нева[#00BFFF]лидный")


		if os.name == "posix":

			os.system('clear')

			print(r"[#00BFFF]  _________            .__  ___________.__            .___             [/#00BFFF]")
			print(r"[#00BFFF] /   _____/ ____  __ __|  | \_   _____/|__| ____    __| _/___________  [/#00BFFF]")
			print(r"[#80DFFF] \_____  \ /  _ \|  |  \  |  |    __)  |  |/    \  / __ |/ __ \_  __ \ [/#80DFFF]")
			print(r"[#80DFFF] /        (  <_> )  |  /  |__|     \   |  |   |  \/ /_/ \  ___/|  | \/ [/#80DFFF]")
			print(r"[#FFFFFF]/_______  /\____/|____/|____/\___  /   |__|___|  /\____ |\___  >__|   [/#FFFFFF]")
			print(r"[#FFFFFF]        \/                       \/            \/      \/    \/ [/#FFFFFF]")

			print("[#00BFFF] Введите номер (+1999999999):")

			numwhat = input("==>")

			number = phonenumbers.parse(numwhat, None)

			print(number,geocoder.description_for_number(number,"en"), carrier.name_for_number(number,"en"))

			if phonenumbers.is_valid_number(number):
				print("[#FFFFFF]Но[#80DFFF]мер ва[#00BFFF]лидный")
			else:
				print("[#FFFFFF]Но[#80DFFF]мер нева[#00BFFF]лидный")

	if what	== 2:
		if os.name == "nt":

			os.system("cls")

			print(r"[#00BFFF]  _________            .__  ___________.__            .___             [/#00BFFF]")
			print(r"[#00BFFF] /   _____/ ____  __ __|  | \_   _____/|__| ____    __| _/___________  [/#00BFFF]")
			print(r"[#80DFFF] \_____  \ /  _ \|  |  \  |  |    __)  |  |/    \  / __ |/ __ \_  __ \ [/#80DFFF]")
			print(r"[#80DFFF] /        (  <_> )  |  /  |__|     \   |  |   |  \/ /_/ \  ___/|  | \/ [/#80DFFF]")
			print(r"[#FFFFFF]/_______  /\____/|____/|____/\___  /   |__|___|  /\____ |\___  >__|   [/#FFFFFF]")
			print(r"[#FFFFFF]        \/                       \/            \/      \/    \/ [/#FFFFFF]")

			print("[#00BFFF] Введите username:")

			whatuse = input("==>")

			print("[#FFFFFF]Про[#80DFFF]верьте ссыл[#00BFFF]ки:")

			print(f"https://www.facebook.com/{whatuse}")
			print(f"https://www.instagram.com/{whatuse}")
			print(f"https://www.tiktok.com/@{whatuse}")
			print(f"https://t.me/{whatuse}")
			print(f"https://www.youtube.com/@{whatuse}")
			print(f"https://github.com/{whatuse}")

			r = requests.get(f"https://vk.com/{whatuse}")

			if r.status_code == 200:
				print(f"vk - найден!!! ссылка - https://vk.com/{whatuse}")
			else:
				print("vk - не найден:(")
		if os.name == "posix":

			os.system("clear")

			print(r"[#00BFFF]  _________            .__  ___________.__            .___             [/#00BFFF]")
			print(r"[#00BFFF] /   _____/ ____  __ __|  | \_   _____/|__| ____    __| _/___________  [/#00BFFF]")
			print(r"[#80DFFF] \_____  \ /  _ \|  |  \  |  |    __)  |  |/    \  / __ |/ __ \_  __ \ [/#80DFFF]")
			print(r"[#80DFFF] /        (  <_> )  |  /  |__|     \   |  |   |  \/ /_/ \  ___/|  | \/ [/#80DFFF]")
			print(r"[#FFFFFF]/_______  /\____/|____/|____/\___  /   |__|___|  /\____ |\___  >__|   [/#FFFFFF]")
			print(r"[#FFFFFF]        \/                       \/            \/      \/    \/ [/#FFFFFF]")

			print("[#00BFFF] Введите username:")

			whatuse = input("==>")

			print("[#FFFFFF]Про[#80DFFF]верьте ссыл[#00BFFF]ки:")

			print(f"https://www.facebook.com/{whatuse}")
			print(f"https://www.instagram.com/{whatuse}")
			print(f"https://www.tiktok.com/@{whatuse}")
			print(f"https://t.me/{whatuse}")
			print(f"https://www.youtube.com/@{whatuse}")
			print(f"https://vk.com/{whatuse}")
			print(f"https://github.com/{whatuse}")

			r = requests.get(f"https://vk.com/{whatuse}")

			if r.status_code == 200:
				print(f"vk - найден!!! ссылка - https://vk.com/{whatuse}")
			else:
				print("vk - не найден:(")

	if what == 3:
		if os.name	== "nt":

			os.system("cls")

			print(r"[#00BFFF]  _________            .__  ___________.__            .___             [/#00BFFF]")
			print(r"[#00BFFF] /   _____/ ____  __ __|  | \_   _____/|__| ____    __| _/___________  [/#00BFFF]")
			print(r"[#80DFFF] \_____  \ /  _ \|  |  \  |  |    __)  |  |/    \  / __ |/ __ \_  __ \ [/#80DFFF]")
			print(r"[#80DFFF] /        (  <_> )  |  /  |__|     \   |  |   |  \/ /_/ \  ___/|  | \/ [/#80DFFF]")
			print(r"[#FFFFFF]/_______  /\____/|____/|____/\___  /   |__|___|  /\____ |\___  >__|   [/#FFFFFF]")
			print(r"[#FFFFFF]        \/                       \/            \/      \/    \/ [/#FFFFFF]")

			print("[#00BFFF]https://geohints.com/ - сборник данных которые помогут если есть фото жертвы(на улице)")
			print("[#00BFFF]https://osintframework.com/ - карта всех инструментов")
			print("[#00BFFF]https://haveibeenpwned.com/ - проверка утечек данных")

		if os.name	== "posix":

			os.system("clear")

			print(r"[#00BFFF]  _________            .__  ___________.__            .___             [/#00BFFF]")
			print(r"[#00BFFF] /   _____/ ____  __ __|  | \_   _____/|__| ____    __| _/___________  [/#00BFFF]")
			print(r"[#80DFFF] \_____  \ /  _ \|  |  \  |  |    __)  |  |/    \  / __ |/ __ \_  __ \ [/#80DFFF]")
			print(r"[#80DFFF] /        (  <_> )  |  /  |__|     \   |  |   |  \/ /_/ \  ___/|  | \/ [/#80DFFF]")
			print(r"[#FFFFFF]/_______  /\____/|____/|____/\___  /   |__|___|  /\____ |\___  >__|   [/#FFFFFF]")
			print(r"[#FFFFFF]        \/                       \/            \/      \/    \/ [/#FFFFFF]")

			print("[#00BFFF]https://osintframework.com/ - карта всех инструментов")
			print("[#00BFFF]https://haveibeenpwned.com/ - проверка утечек данных")



	if what == 0:
		if os.name == "nt":

			os.system("cls")

			break

		if os.name == "posix":

			os.system("clear")

			break

	input("")
