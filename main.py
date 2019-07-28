import os
import argparse
import logging
from PIL import Image
from PIL.ExifTags import TAGS

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

    args = arg_parser.parse_args()
    input_dir = args.input
    output_dir = args.output
    dry_run = args.dry_run


    if not os.path.exists(input_dir):
        os.mkdir(input_dir)
        logging.warning('Input directory {} does not exit, creating new directory. '.format(input_dir))
    if not os.path.exists(output_dir):
        os.mkdir(output_dir)
        logging.warning('Output directory {} does not exit, creating new directory. '.format(output_dir))


    print(input_dir)
    print(output_dir)
    print(dry_run)


if __name__ == '__main__':
    main()