import unittest
from unittest.mock import patch, MagicMock
from your_module import CommandExecutor  # Adjust the import based on your module structure


class TestCommandExecutor(unittest.TestCase):

    @patch('subprocess.run')
    def test_execute_command_success(self, mock_subprocess):
        # Arrange
        mock_subprocess.return_value = MagicMock(returncode=0, stdout='Success', stderr='')
        executor = CommandExecutor()
        
        # Act
        result = executor.execute('echo Success')
        
        # Assert
        self.assertEqual(result, 'Success')
        mock_subprocess.assert_called_once_with('echo Success', shell=True, text=True, capture_output=True)

    @patch('subprocess.run')
    def test_execute_command_failure(self, mock_subprocess):
        # Arrange
        mock_subprocess.return_value = MagicMock(returncode=1, stdout='', stderr='Error')
        executor = CommandExecutor()
        
        # Act
        result = executor.execute('invalid_command')
        
        # Assert
        self.assertEqual(result, 'Error')
        mock_subprocess.assert_called_once_with('invalid_command', shell=True, text=True, capture_output=True)


if __name__ == '__main__':
    unittest.main()