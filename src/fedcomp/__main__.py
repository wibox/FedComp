import argparse

from fedcomp.manager import hello, start_server


def main():
    parser = argparse.ArgumentParser(prog="fedcomp")
    subparsers = parser.add_subparsers(dest="command", required=True)

    # Hello world and info display
    hello_parser = subparsers.add_parser("hello")
    hello_parser.add_argument("--info", type=str, default="all", choices=["all", "operating"])
    # Control panel (FastAPI server)
    parser_server = subparsers.add_parser("start_server")
    parser_server.add_argument("--host", type=str, default="127.0.0.1")
    parser_server.add_argument("--port", type=int, default=8000)

    args = parser.parse_args()

    if args.command == "hello":
        print(hello(args.info))
    elif args.command == "start_server":
        start_server(args.host, args.port)
    else:
        parser.print_help()
