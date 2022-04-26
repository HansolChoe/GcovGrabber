#!/usr/bin/env python3
"""
    Author: Hansol Choe
    https://github.com/HansolChoe/gcov-grabber

    A gcov wrapper which makes metadata of gcov files.

"""
import os
import subprocess
import pathlib
import argparse
import atexit
import logging

logger = logging.getLogger(__name__)


def parse_args():
    parser = argparse.ArgumentParser(description='gcovg: A gcov wrapper which makes metadata of gcov files.')
    parser.add_argument('-f',
                        '--file',
                        help='file patterns to run gcov. For example: (*.o)',
                        required=True,
                        action='append')
    parser.add_argument('-r',
                        '--root-dir',
                        help='root directory to run gcov',
                        default='.')
    parser.add_argument('-g',
                        '--gcov-path',
                        help='path to gcov',
                        required=False,
                        default='gcov')
    parser.add_argument('-o',
                        '--output',
                        help='output file',
                        required=False,
                        default='gcov_info.json')
    return parser.parse_args()


def handle_cwd():
    cwd = os.getcwd()
    logger.info(f'Current working directory: {cwd}')

    def restore_cwd():
        logger.info(f'Restore working directory to: {cwd}')
        os.chdir(cwd)

    atexit.register(restore_cwd)
    return cwd


def main():
    args = parse_args()
    gcov = args.gcov_path
    old_cwd = handle_cwd()
    root_dir = pathlib.Path(args.root_dir)

    if not pathlib.Path(root_dir).is_dir():
        logger.critical(f'{root_dir} is not a directory')
        exit(1)

    # glob all file's list
    target_file_list = []
    for file in args.file:
        for p in root_dir.rglob(file):
            target_file_list.append(pathlib.Path(p))

    # run gcov and make metadata
    for p in root_dir.rglob(args.file):
        gcov_proc = subprocess.Popen([args.gcov], stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
        out, err = gcov_proc.communicate()





if __name__ == '__main__':
    main()
