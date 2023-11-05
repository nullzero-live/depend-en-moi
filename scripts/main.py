from DependMLMoi.depend_ml import run_setup
from DependMLMoi.arg_parser import parse_args

if __name__ == "__main__":
    args = parse_args()
    run_setup(auto_install=args.auto, args=args)