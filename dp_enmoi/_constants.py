from arg_parser import parser

AUTO_INSTALL = False
REQUIRED_DOTENV_VERSION = 1.0.0
DEBUG = False
LOGGING = True
QUIET = False
REQUIREMENTS_PATH = "./requirements.txt"
LOGS_DIR = "./utils/donmor.log"

args = parser.args()

if args:
    AUTO_INSTALL = args.auto
    DEBUG = args.debug
    LOGGING = args.logging
    QUIET = args.quiet
    CUSTOM = args.custom




