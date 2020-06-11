import fbchat
from getpass import getpass

username = str(input("Enter your username: "))
client = fbchat.Client(username, getpass())
number_of_friends = int(input("Number of friends: "))

for i in range(number_of_friends):
  name = str(input("Name: "))
  friends = client.searchForUsers(name)
  friend = friends[0]
  
  while True:
    msg = str(input("Enter a message: "))
    sent = client.sendMessage(msg, thread_id=friend.uid)
    if sent:
        print("Message was sent!")