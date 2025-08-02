import argparse

from fedcomp.manager import start_server


def main():
    parser = argparse.ArgumentParser(prog="fedcomp manager")
    subparsers = parser.add_subparsers(dest="command")

    # Control panel (FastAPI server)
    parser_server = subparsers.add_parser("start_server")
    parser_server.add_argument("--host", default="127.0.0.1")
    parser_server.add_argument("--port", type=int, default=8000)

    args = parser.parse_args()

    if args.command == "start_server":
        start_server(args.host, args.port)
    else:
        parser.print_help()
