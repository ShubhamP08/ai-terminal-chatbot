import subprocess
import shlex

class CommandExecutor:
    def __init__(self):
        # Initialize the CommandExecutor
        pass

    def execute_command(self, command: str, timeout: int = 10):
        # Show the command
        print(f'Command to execute: {command}')  
        
        # Ask for user confirmation
        confirm = input('Do you want to execute this command? (yes/no): ')
        if confirm.lower() != 'yes':
            print('Command execution canceled.')
            return
        
        # Execute the command with a timeout
        try:
            print('Executing command...')
            process = subprocess.run(shlex.split(command), timeout=timeout, capture_output=True, text=True)
            print('Command output (stdout):')
            print(process.stdout)
            print('Command output (stderr):')
            print(process.stderr)
        except subprocess.TimeoutExpired:
            print('Command execution timed out.')
        except Exception as e:
            print(f'An error occurred: {e}')

# Example usage:
# if __name__ == '__main__':
#     executor = CommandExecutor()
#     executor.execute_command('echo Hello World')
