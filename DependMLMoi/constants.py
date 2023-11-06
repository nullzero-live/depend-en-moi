from DependMLMoi.arg_parser import parse_args

args = parse_args()
print(args)

#Default
NAME = ""
AUTO_INSTALL = False
TYPE = "LLM"
REQUIRED_DOTENV_VERSION = "1.0.0"
LEVEL = "DEBUG"
DEBUG = False
LOGGING = True
QUIET = False
CUSTOM = []
REQUIREMENTS_PATH = "./requirements.txt"
LOGS_DIR = "./utils/donmor.log"




if args:
    NAME = args.name
    AUTO_INSTALL = args.auto
    TYPE = args.type
    REQUIRED_DOTENV_VERSION = args.version
    LEVEL = args.level
    DEBUG = args.debug
    LOGGING = args.logging
    QUIET = args.quiet
    CUSTOM = args.custom
   




