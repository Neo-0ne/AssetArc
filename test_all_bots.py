import os
import subprocess
import logging

logging.basicConfig(filename='test_log.txt', level=logging.INFO, format='%(asctime)s - %(message)s')

def test_bots():
    bot_dirs = [d for d in os.listdir('.') if os.path.isdir(d)]
    for bot in bot_dirs:
        script_path = os.path.join(bot, 'main.py')
        if os.path.isfile(script_path):
            try:
                result = subprocess.run(['python', script_path], capture_output=True, text=True, timeout=30)
                logging.info(f'Bot: {bot}, Output: {result.stdout.strip()}')
                if result.stderr:
                    logging.error(f'Bot: {bot}, Errors: {result.stderr.strip()}')
            except Exception as e:
                logging.error(f'Bot: {bot}, Exception: {str(e)}')

if __name__ == '__main__':
    test_bots()
