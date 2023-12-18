import argparse

from app import views, __version__, patterns


def get_command_line_args():
    parser = argparse.ArgumentParser(
        prog="game-of-life",
        description="Conway's Game of Life CLI application",
    )

    parser.add_argument("--version", action="version", version=f"%(prog)s v{__version__}")
    parser.add_argument(
        "-p",
        "--pattern",
        choices=[pat.name for pat in patterns.get_all_patterns()],
        default="Blinker",
        help="pick a pattern for the Game of Life (default: %(default)s)",
    )
    parser.add_argument(
        "-a",
        "--all",
        action="store_true",
        help="show all available patterns",
    )
    parser.add_argument(
        "-v",
        "--view",
        choices=views.__all__,
        default="CursesView",
        help="display life grid in a specific view (default: %(default)s)",
    )  # TODO: unnecessary?
    parser.add_argument(
        "-g",
        "--gen",
        metavar="GENERATIONS_COUNT",
        type=int,
        default=10,
        help="number of generations (default: %(default)s)",
    )
    parser.add_argument(
        "-f",
        "--fps",
        metavar="FRAMES_PER_SECOND",
        type=int,
        default=4,
        help="frames per second (default: %(default)s)",
    )
    return parser.parse_args()