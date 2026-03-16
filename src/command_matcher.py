from fuzzywuzzy import process

class CommandMatcher:
    def __init__(self, command_db):
        self.command_db = command_db

    def match_command(self, user_input):
        best_match = process.extractOne(user_input, self.command_db)
        return best_match

# Example usage:
if __name__ == '__main__':
    commands = ['open file', 'close file', 'save file', 'exit']
    matcher = CommandMatcher(commands)
    user_input = 'open a document'
    print(matcher.match_command(user_input))