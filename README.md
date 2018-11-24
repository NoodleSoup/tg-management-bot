# TG-Management-Bot
TG-Management-Bot is an all-powerful plugin-wielding chat management bot for Telegram written in Python.

# How to make your own clone
>You will have to clone this project and edit the main.py to add your own bot token first.

- To run it on your PC:
  1. Open terminal in the bot's directory and type:
  ```
  python setup.py
  ```
  2. Wait for it to complete and type:
  ```
  python main.py
  ```
  and that's it.

- To run it on an SSH screen:
  1. Firstly you'll have to create a `screen` and gie it a name.
  ```
  screen -S bot
  ```
  this will create the screen with the name `bot`, you can choose whatever name you like.
  2. Move to the bot's directory and type:
  ```
  python setup.py
  ```
  3. Wait for it to complete and type:
  ```
  python main.py
  ```
  >Now, to detach from the screen at let it run on the server, press Ctrl+A followed by D.
  
  and that's it.
  
  >Note: To reattach to the screen type `screen -r bot`.
  
