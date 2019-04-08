class Logger(object):
    class __logger():
        def __init__(self):
            self.file_name = "basic"

        def set_file_name(self, file_name):
            self.file_name = file_name

        def _write_log(self, level, msg):
            with open(self.file_name, "a") as log_file:
                log_file.write("[{0}] {1}\n".format(level, msg))

        def critical(self, msg):
            self._write_log("CRITICAL", msg)

        def error(self, msg):
            self._write_log("ERROR", msg)

        def warn(self, msg):
            self._write_log("WARN", msg)

        def info(self, msg):
            self._write_log("INFO", msg)

        def debug(self, msg):
            self._write_log("DEBUG", msg)

    instance = None

    def __new__(cls):
        if not Logger.instance:
            Logger.instance = Logger.__logger()
        return Logger.instance
