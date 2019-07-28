import os
import argparse
import logging
from photomover import photomover

def main():
    arg_parser = argparse.ArgumentParser()
    arg_parser.add_argument(
        '-i', '--input',
        help = 'input directory',
        type = str,
        default = r'.'
    )
    arg_parser.add_argument(
        '-o', '--output',
        help = 'output directory',
        type = str,
        default = r'./output/'
    )
    arg_parser.add_argument(
        '-d', '--dry_run',
        help = 'dry run',
        action='store_true'
    )
    arg_parser.add_argument(
        '-c', '--copy',
        help = 'perform copy action instead of move',
        action='store_true'
    )

    args = arg_parser.parse_args()
    input_dir = args.input
    output_dir = args.output
    dry_run = args.dry_run
    copy = args.copy

    logging.getLogger().setLevel(logging.INFO)

    photomover(input_dir, output_dir, dry_run, copy)


if __name__ == '__main__':
    main()