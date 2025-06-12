import getpass
import os
import socket

class SimpleShell:
    def __init__(self):
        self.user = getpass.getuser()
        self.hostname = socket.gethostname()
        self.update_prompt()

    def update_prompt(self):
        base_cwd = os.path.basename(os.getcwd()) or '/'
        self.prompt = f"{self.user}@{self.hostname}:{base_cwd}$ "

    def run(self):
        while True:
            command = input(self.prompt).strip()
            if not command:
                continue
            if command in ("exit", "quit"):
                break
            if command in ("cd\\", "cd/"):
                self.change_directory("/")
            elif command.startswith("cd "):
                self.change_directory(command[3:].strip())
            elif command == "ls":
                self.list_directory()
            elif command == "clear":
                self.clear_screen()
            elif command.startswith("mkdir "):
                self.make_directory(command[6:].strip())
            elif command.startswith("touch "):
                self.touch(command[6:].strip())
            else:
                print(f"Command not found: {command}")

    def change_directory(self, path):
        if path.startswith("~"):
            path = os.path.expanduser(path)
        try:
            os.chdir(path)
            self.update_prompt()
        except Exception as e:
            print(f"cd: {e}")

    def list_directory(self):
        try:
            for f in os.listdir(os.getcwd()):
                print(f)
        except Exception as e:
            print(f"ls: {e}")

    def clear_screen(self):
        os.system('cls' if os.name == 'nt' else 'clear')

    def make_directory(self, name):
        try:
            os.mkdir(name)
        except Exception as e:
            print(f"mkdir: {e}")

    def touch(self, filename):
        try:
            with open(filename, 'a'):
                os.utime(filename, None)
        except Exception as e:
            print(f"touch: {e}")

if __name__ == "__main__":
    SimpleShell().run()