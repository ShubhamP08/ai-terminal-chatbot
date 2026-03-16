import logging
import os

# Configure logging
log_file = 'command_execution_history.log'
logging.basicConfig(filename=log_file,
                    level=logging.INFO,
                    format='%(asctime)s - %(message)s')

class CommandLogger:
    @staticmethod
    def log_command(command, result):
        logging.info(f'Command: {command} | Result: {result}')

# Example usage
if __name__ == '__main__':
    command = 'example_command'
    result = 'success'
    CommandLogger.log_command(command, result)