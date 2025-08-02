import os
import subprocess
import logging

logging.basicConfig(filename='test_log.txt', level=logging.INFO, format='%(asctime)s - %(message)s')

def find_bot_script(bot_dir):
    bot_name = os.path.basename(bot_dir).replace('_Bot', '').replace('_Combined', '').replace('_Expanded', '').lower()
    possible_script_names = [f'{bot_name}.py', f'{os.path.basename(bot_dir)}.py', 'main.py', f'{bot_name}_bot.py', 'suggest_service_bot.py']
    print(f"Possible script names for {os.path.basename(bot_dir)}: {possible_script_names}")

    for root, dirs, files in os.walk(bot_dir):
        for script_name in possible_script_names:
            if script_name in files:
                return os.path.join(root, script_name)
    return None

def test_bots():
    print("Starting bot tests...")
    bot_dirs = [os.path.join('assetarc/bots', d) for d in os.listdir('assetarc/bots') if os.path.isdir(os.path.join('assetarc/bots', d))]
    print(f"Found {len(bot_dirs)} bot directories.")
    for bot_dir in bot_dirs:
        bot = os.path.basename(bot_dir)
        print(f"Testing bot: {bot}")
        script_path = find_bot_script(bot_dir)

        if script_path:
            print(f"Found script for {bot}: {script_path}")
            try:
                result = subprocess.run(['python', script_path], capture_output=True, text=True, timeout=30)
                logging.info(f'Bot: {bot}, Output: {result.stdout.strip()}')
                if result.stderr:
                    logging.error(f'Bot: {bot}, Errors: {result.stderr.strip()}')
            except Exception as e:
                logging.error(f'Bot: {bot}, Exception: {str(e)}')
        else:
            print(f"Script not found for {bot}")

if __name__ == '__main__':
    test_bots()
