# Civitai status bot

This discord bot monitors the status of a website and sends messages to a specified Discord channel. The bot checks if any of the key-values (related to various services) fall below 85% for more than 2 minutes. If it detects issues, it sends a message stating there are problems with the website. When the key-values go above 90%, the bot sends a message indicating that services are good.

## Usage

1. Install Python 3.6 or higher, if not already installed.
2. Install the required libraries using the following command:

```python
pip install requests discord.py
```


3. Replace `your_bot_token` in the code with your own Discord bot token, and `your_channel_id` with the desired channel ID where the bot will send messages.
4. Run the script with the following command:
    
```python
python bot.py
```
The bot will start running and send messages to the specified Discord channel about the status of the website services.

## Key-Values Monitored

The bot monitors the following key-values:

- Database (2_24)
- Model Scanner (3_24)
- Model Scanner Large (4_24)
- Discord Notification Server (5_24)
- Main Site (7_24)
- API (8_24)

The bot renames these key-values to make them more human-readable.