#!/usr/bin/env python
# encoding: utf-8
"""
pythonTemplate/app.py
Created by mhedd on 2019-10-09.
Last updated by mhedd on 2019-10-09.
Copyright (c) 2019 MGM Resorts Int. All rights reserved.
"""
import sys
import logging
import optparse

# Globals
LOG = None
COMMIT_MODE = False


def process_command_line(argv):
    """
    Return a 2-tuple: (settings object, args list).
    `argv` is a list of arguments, or `None` for ``sys.argv[1:]``.
    """
    global LOG
    global COMMIT_MODE
    if argv is None:
        argv = sys.argv[1:]

    # initialize the parser object:
    parser = optparse.OptionParser(
        formatter=optparse.TitledHelpFormatter(width=78),
        add_help_option=None)

    # define options here:
    parser.add_option("-v", "--verbose", dest="verbose", default=False,
                      action='store_true', help="write debug level logs to log")
    parser.add_option("-L", "--log", dest="logfile", help="write log output to logfile")
    parser.add_option("-C", "--commit", dest="commit", default=False, action='store_true', 
                      help="if true, will Commit the data change; if false this script will just log what would have happened if set to true.")
    parser.add_option(  # customized description; put --help last
        '-h', '--help', action='help',
        help='Show this help message and exit.')
    options, args = parser.parse_args(argv)

    # set up logging
    log_file = None
    log_level = logging.INFO
    if options.verbose:
        log_level = logging.DEBUG

    if options.logfile:
        log_file = options.logfile

    LOG = set_logging(log_file, log_level)

    # Check for required arguments

    # Set commit_mode
    COMMIT_MODE = options.commit

    return options, args


def main(argv=None):
    settings, args = process_command_line(argv)
    # Main logic goes here

    LOG.info("Process completed.")
    return 0


def set_logging(logfile=None, log_level=logging.INFO):
    console_level = log_level
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.DEBUG)
    # create formatter to add to the handlers
    formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
    # create console handler
    ch = logging.StreamHandler()
    ch.setLevel(console_level)
    ch.setFormatter(formatter)
    logger.addHandler(ch)

    # add the handlers to logger
    if logfile:
        file_level = logging.DEBUG
        fh = logging.FileHandler(logfile)
        fh.setLevel(file_level)
        fh.setFormatter(formatter)
        logger.addHandler(fh)

    return logger


if __name__ == '__main__':
    status = main()
    sys.exit(status)
