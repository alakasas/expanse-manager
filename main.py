import argparse

from my_functions.add import add
from my_functions.list import list_csv
from my_functions.delete import delete
from my_functions.update import update
from my_functions.reset import reset

parser = argparse.ArgumentParser()
subparsers = parser.add_subparsers(dest="command", help="")

parser_add = subparsers.add_parser("add")
parser_add.add_argument("-name", type=str)
parser_add.add_argument("-amount", "-a", type=float)

parser_add = subparsers.add_parser("update")
parser_add.add_argument("-id", type=int)
parser_add.add_argument("-name", type=str)
parser_add.add_argument("-amount", "-a", type=float)

parser_add = subparsers.add_parser("list")

parser_add = subparsers.add_parser("delete")
parser_add.add_argument("-id", type=int)

parser_add = subparsers.add_parser("reset")
parser_add.add_argument("-id", action="store_true")
parser_add.add_argument("-all", action="store_true")

args = parser.parse_args()

#----------------------------------------------------

match args.command:
    case "add":
        add(args.name, args.amount)
    case "list":
        list_csv()
    case "delete":
        delete(args.id)
    case "update":
        update(args.id, args.name, args.amount)
    case "reset":
        reset(args.id, args.all)
        



