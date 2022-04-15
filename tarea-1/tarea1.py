#!/usr/bin/env python3

import sys
import re
import logging
from queue import LifoQueue

logging.basicConfig(
    filename="tarea1.log",
    filemode='w',
    format='%(process)d %(asctime)s %(levelname)s: %(message)s',
    datefmt='%m/%d/%Y %I:%M:%S',
    level=logging.DEBUG
)

MAX_STACK_SIZE = 2
MAX_STRING_LENGTH = 15
STRING_PATTERN = re.compile(r"[A-Za-z0-9%@\-_\[\]{}!?]+")

logging.info("Starting...")
logging.info(f'Creating stack of size: {MAX_STACK_SIZE}')
stack = LifoQueue(maxsize=MAX_STACK_SIZE)
logging.info("Stack created")

logging.info("Giving welcome to user")

PATTERN_MESSAGE = "\n  English lowercase letters: abcdefghijklmnopqrstuvwxyz\n  English uppercase letters: ABCDEFGHIJKLMNOPQRSTUVWXYZ\n  Numbers: 1234567890\n  Symbols: %@-_[]{}!?\n"

print("\nWelcome to StringCompare\n")
print(
    f'Please remember that the string must have a maximum of {MAX_STRING_LENGTH} chars, that the Stack only saves {MAX_STACK_SIZE} strings and than you can only use:')
print(PATTERN_MESSAGE)
print("To stop the program press CTRL+C\n")


def check_string(string):
    logging.info(f'Checking Max length')
    if len(string) <= MAX_STRING_LENGTH:
        logging.info(f'String length: OK')
    else:
        logging.warning(
            f'String length excedes maximun length of {MAX_STRING_LENGTH}')
        return (False, "l")
    logging.info(f'Checking Regex')
    if re.fullmatch(STRING_PATTERN, string):
        logging.info(f'Regex check: VALID')
        return (True, "")
    else:
        logging.warning(f'Regex check: NOT VALID')
        return (False, "r")


def compare_strings(stack):
    logging.info("Comparing strings")
    s1 = stack.get()
    s2 = stack.get()
    logging.info(f'Comparing strings s1: {s1} and s2: {s2}')
    logging.info(f'Result {s1 == s2}')
    if s1 == s2:
        print(f'{s1} == {s2}\nStrings are equal')
    else:
        print(f'{s1} =/= {s2}\nStrings are not equal')


def empty_stack(stack):
    logging.info("Emptying stack")
    while stack.qsize() != 0:
        stack.get()
    logging.info("Stack emptied")


while True:
    if not stack.full():
        logging.info("Asking for input")
        string = input(f'Please enter the string: ').strip()
        logging.info(f'Received input: {string}')

        result, err = check_string(string)
        if result:
            stack.put(string)
            print(f'String {string} saved')
        elif err == "l":
            print(
                f'String {string} excedes the length of {MAX_STRING_LENGTH}, please try again')
        elif err == "r":
            print(
                f'String {string} does not match the pattern: {PATTERN_MESSAGE}please try again')
    else:
        logging.info("Stack full")
        logging.info("Offering user to compare strings")

        print("Do you wish to compare the saved strings?")
        print("  Yes, and exit (1)")
        print("  Yes, and empy the stack (2)")
        print("  No, and exit (3)")
        print("  No, and empty the stack (4)")

        choice = int(input("1/2/3/4: "))
        logging.info(f'User input {choice}')
        if choice == 1:
            compare_strings(stack)
            logging.info("Closing program")
            print("Bye")
            sys.exit()
        elif choice == 2:
            compare_strings(stack)
        elif choice == 3:
            logging.info("Closing program")
            print("Bye")
            sys.exit()
        elif choice == 4:
            empty_stack(stack)
