# Installation Steps for the MT5 Trading Bot

## Prerequisites:
1. **MetaTrader 5 Installed**: Ensure you have MetaTrader 5 installed on your computer.
2. **Basic Knowledge of Trading**: Familiarize yourself with trading principles.

## Installation Steps:
### Step 1: Clone the Repository
Open your terminal or command prompt and run:
```bash
git clone https://github.com/StanT254/mt5-trading-bot.git
cd mt5-trading-bot
```

### Step 2: Copy Files to MetaTrader Directory
1. Navigate to the cloned repository in your file explorer.
2. Locate the `mt5-trading-bot` folder.
3. Copy the contents of the folder into the MetaTrader `MQL5\\Experts` directory, typically found at:
```
C:\Program Files\MetaTrader 5\MQL5\Experts\
```

### Step 3: Restart MetaTrader
Close and reopen MetaTrader 5 to load the new trading bot.

### Step 4: Attach the Bot to a Chart
1. Open a chart for the financial instrument you want to trade.
2. Find the bot under `Navigator` > `Expert Advisors`.
3. Drag and drop the bot onto the chart.

### Step 5: Configure Settings
Set your preferences in the settings window before starting the bot.

### Step 6: Start the Bot
After configuring, click `OK` to start trading. Your bot is now ready to operate!