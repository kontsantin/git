import requests

url = 'https://drom.ru/'
utf8_header = {'Content-Type': 'text/html; charset=utf-8'}
def parse_title():
    response = requests.get(url, headers=utf8_header)
    if response.status_code == 200:
        return response.text.split('<title>')[1].split('</title>')[0]
    else:
        return None

print(parse_title())


def main():
    print("This is a remote change to create a conflict!")

def main():
    print("This is a remote change to create a conflict!")
    
def main():
    print("This is a remote change to create a conflict!")
    
if __name__ == "__main__":
    main()
