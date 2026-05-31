import requests
import time
from concurrent.futures import ThreadPoolExecutor
from colorama import init, Fore, Style
import argparse

init(autoreset=True)

def print_banner():
    print(Fore.LIGHTCYAN_EX + Style.BRIGHT + """
    ╔═══════════════════════════════╗
    ║      OSINT Username Tool      ║
    ║       поиск юзеров v1.0       ║
    ╚═══════════════════════════════╝
    """ + Style.RESET_ALL)


class OSINTScanner:
    def __init__(self, username, timeout=5):
        self.username = username
        self.timeout = timeout
        self.results = []

    def get_urls(self):
        return [
            f"https://github.com/{self.username}",
            f"https://www.reddit.com/user/{self.username}",
            f"https://steamcommunity.com/id/{self.username}",
            f"https://twitch.tv/{self.username}",
            f"https://youtube.com/{self.username}",
        ]

    def check_site(self, url):
        try:
            response = requests.get(url, timeout=self.timeout)
            if response.status_code == 200:
                return ("found", url)
            else:
                return ("not_found", url)
        except requests.exceptions.Timeout:
            return ("timeout", url)
        except requests.exceptions.ConnectionError:
            return ("error", url)

    def scan(self):
        urls = self.get_urls()
        with ThreadPoolExecutor(max_workers=10) as executor:
            self.results = list(executor.map(self.check_site, urls))
        return self.results

    def print_results(self):
        for i, (status, url) in enumerate(self.results, start=1):
            if status == "found":
                print(f"{i}. {Fore.GREEN}[НАЙДЕН]     {url}")
            elif status == "not_found":
                print(f"{i}. {Fore.RED}[Не найден]  {url}")
            elif status == "timeout":
                print(f"{i}. {Fore.YELLOW}[Таймаут]    {url}")
            else:
                print(f"{i}. {Fore.RED}[Ошибка]     {url}")

        found_count = sum(1 for status, url in self.results if status == "found")
        print(f"\n{Fore.GREEN}Найдено: {Fore.CYAN}{found_count} из {len(self.results)}")

parser = argparse.ArgumentParser(description="OSINT поиск никнеймов")
parser.add_argument("--username", help="Никнейм для поиска")
parser.add_argument("--timeout", type=int, default=5, help="Таймаут в секундах")
args = parser.parse_args()


print_banner()
start = time.time()
scanner = OSINTScanner(username=args.username, timeout=args.timeout)
scanner.scan()
scanner.print_results()
end = time.time()
#save_results(args.username, results)
print(f"\n{Fore.GREEN}Проверка заняла: {Fore.CYAN}{end - start:.2f} сек")