import requests
import prettyprinter
from prettyprinter import pprint
import os

class ReqFD:
    def __init__(self, url, api_key=None, headers=None):
        self.url = url
        self.api_key = api_key
        self.headers = headers or {}

    def GET(self):
        if self.api_key:
            self.headers['Authorization'] = f'token {self.api_key}'
        response_GET = requests.get(self.url, headers=self.headers)
        pprint(response_GET.json())

    def POST(self):
        if self.api_key:
            self.headers['Authorization'] = f'token {self.api_key}'
        response_POST = requests.post(self.url, headers=self.headers)
        pprint(response_POST.json())

    def PUT(self):
        if self.api_key:
            self.headers['Authorization'] = f'token {self.api_key}'
        response_PUT = requests.put(self.url, headers=self.headers)
        pprint(response_PUT.json())

    def DELETE(self):
        if self.api_key:
            self.headers['Authorization'] = f'token {self.api_key}'
        response_DELETE = requests.delete(self.url, headers=self.headers)
        pprint(response_DELETE.json())

def get_user_input():
    url = input("Enter the URL: ")
    api_key = input("Enter the API key (or press Enter to skip): ")
    headers = {}
    while True:
        header_name = input("Enter a header name (or press Enter to skip): ")
        if not header_name:
            break
        header_value = input(f"Enter the value for header '{header_name}': ")
        headers[header_name] = header_value
    return url, api_key, headers

def main():
    url, api_key, headers = get_user_input()
    req_fd = ReqFD(url, api_key, headers)

    while True:
        print("\nChoose an operation:")
        print("1. GET")
        print("2. POST")
        print("3. PUT")
        print("4. DELETE")
        print("5. Quit")

        choice = input("Enter your choice: ")
        if choice == '1':
            req_fd.GET()
        elif choice == '2':
            req_fd.POST()
        elif choice == '3':
            req_fd.PUT()
        elif choice == '4':
            req_fd.DELETE()
        elif choice == '5':
            print("Exiting the interface.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
