```python
import requests
from bs4 import BeautifulSoup
from getpass import getpass

# Function to login to Facebook using cookies
def login_to_facebook(cookies):
    login_url = 'https://www.facebook.com/'
    login_data = {'email': 'your_email@example.com', 'pass': 'your_password'}
    
    login_request = requests.get(login_url, cookies=cookies)
    login_form = BeautifulSoup(login_request.content, 'html.parser').find('form', {'id': 'login_form'})
    
    login_data['csrf_token'] = login_form.find('input', {'name': 'csrf_token'})['value']
    
    login_response = requests.post(login_url, cookies=cookies, data=login_data)
    
    if 'logout' in login_response.text:
        print("Logged in successfully.")
    else:
        print("Login failed.")

# Function to get the list of friends
def get_friend_list(cookies):
    friend_list_url = 'https://www.facebook.com/me/friends/'
    friend_list_response = requests.get(friend_list_url, cookies=cookies)
    soup = BeautifulSoup(friend_list_response.content, 'html.parser')
    friends = soup.find_all('a', {'class': 'fwb fcg'})
    
    return [friend.get_text() for friend in friends]

# Function to guess password of a friend
def guess_password(cookies, friend_name):
    guessed_passwords = {}
    
    # Placeholder for storing guessed passwords
    while True:
        guess = input(f"Enter guess for {friend_name}'s password: ")
        if guess == 'exit':
            break
        guessed_passwords[friend_name] = guess
    
    return guessed_passwords

# Main script
def main():
    # Placeholder for your Facebook ID and password
    email = 'your_email@example.com'
    password = getpass('Your Facebook password: ')
    
    # Get login cookies
    login_cookies = login_to_facebook(email, password)
    
    if login_cookies:
        friend_list = get_friend_list(login_cookies)
        print("Your friend list:")
        print(', '.join(friend_list))
        
        # Option to guess passwords of friends
        for i, friend in enumerate(friend_list):
            print(f"{i+1}. {friend}")
            guess_passwords = guess_password(login_cookies, friend)
            print(f"Guessed passwords for {friend}: {guess_passwords}")
    
    else:
        print("Failed to login.")

# Run the script
main()
```
