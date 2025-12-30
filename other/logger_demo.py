
class LoggerManager:

    @staticmethod
    def get_logger(type_logger):
        pattern_output = ConsolePattern()
        if type_logger == 'console':
            pattern_output = ConsolePattern()
        elif type_logger == 'file':
            pattern_output = FilePattern()

        return Logger(pattern_output)


class Logger:
    def __init__(self, pattern_output):
        self.pattern = pattern_output


    def log(self,message):
        self.pattern.write(f"log:{message}")

    def info(self, message):
        self.pattern.write(f"info:{message}")

    def warning(self, message):
        self.pattern.write(f"warning:{message}")

    def error(self, message):
        self.pattern.write(f"error:{message}")

class ConsolePattern:
    def __init__(self):
        pass

    def write(self,msg):
        print(msg)

class FilePattern:
    def __init__(self):
        pass

    @staticmethod
    def write(msg):
        with open('log.txt','a') as f:
            f.writelines(msg+"\n")
            f.close()