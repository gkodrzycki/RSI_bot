# Bot
Simple bot fetching data from Bybit, calculating RSI and sending message on  dedicated discord channel  when certain values of RSI are reached 

## Pre-requirements
Create `.env` file containing \
`DISCORD_TOKEN`={app token for discord} \
`DISCORD_GUILD_NAME`={name of discord guild (server)} \
`DISCORD_CHANNEL_ID`={id of channel where messages are supposed to appear} \
`BYBIT_API_KEY`={BYBIT api key id}\
`BYBIT_API_SECRET`={secret for BYBIT api key}

## Usage
Build  
`docker build -t discord_bot .` \
Run \
`docker run -it discord_bot`
