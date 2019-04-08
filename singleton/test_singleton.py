from singleton.logger import Logger

if __name__ == '__main__':
    logger_object = Logger()
    logger_object.file_name = "my_log.log"

    logger_object.info("this is a information")
    logger_object.info("this is a information")
    logger_object.error("this is an error")

    logger_object2 = Logger()

    logger_object2.warn("this is a warning")
    logger_object2.debug("this is a debug")
    logger_object2.info("this is another information")
