import logging
import os
import glob
import exifread
import shutil

def _move (file_dir:str, destination_dir:str, dry_run=False, copy=False):
    with open(file_dir, 'rb') as f:
        tags = exifread.process_file(f)
        if len(tags) == 0:
            logging.warning('Image {} has no valid date and is ignored. '.format(file_dir))
            return

    ymd = tags['Image DateTime'].values.split(' ')[0].split(':')
    y_str = str(ymd[0])
    ym_str = y_str + '_' + str(ymd[1])
    ymd_str = ym_str + '_' + str(ymd[2])
    destination_dir = os.path.join(destination_dir, y_str, ym_str, ymd_str)

    filename, extension = os.path.splitext(file_dir)
    file_family = glob.glob(filename+'.*') # all files with the same name, including sidecar files

    if not os.path.exists(destination_dir):
        if not dry_run:
            os.makedirs(destination_dir)

    for f in file_family:
        if copy:
            logging.info('Copying from {} to {}'.format(f, destination_dir))
            if not dry_run:
                try:
                    shutil.copy(f, destination_dir)
                except shutil.Error as err:
                    logging.error(err)
        else:
            logging.info('Moving from {} to {}'.format(f, destination_dir))
            if not dry_run:
                try:
                    shutil.move(f, destination_dir)
                except shutil.Error as err:
                    logging.error(err)


def photomover(input_dir:str, output_dir:str, dry_run=False, copy=False):

    assert os.path.exists(input_dir), 'Input directory {} does not exist. '.format(input_dir)

    if not os.path.exists(output_dir):
        if not dry_run:
            os.mkdir(output_dir)
        logging.warning('Output directory {} does not exit, creating new directory. '.format(output_dir))




    compact_types = ('*.jpg', '*.JPG',
                     '*.jpeg', '*.JPEG',
                     '*.png', '*.PNG')
    raw_types = ('*.nef', '*.NEF',
                 '*.CR2', '*.cr2')

    compact_files = []
    for ftype in compact_types:
        compact_files.extend(glob.glob(input_dir + '/**/' + ftype, recursive=True))

    raw_files = []
    for ftype in raw_types:
        raw_files.extend(glob.glob(input_dir + '/**/' + ftype, recursive=True))

    compact_dir = os.path.join(output_dir, 'compact')
    if not os.path.exists(compact_dir) and compact_files:
        if not dry_run:
            os.mkdir(compact_dir)
        logging.warning('Compact files directory {} does not exit, creating new directory. '.format(compact_dir))

    raw_dir = os.path.join(output_dir, 'raw')
    if not os.path.exists(raw_dir) and raw_files:
        if not dry_run:
            os.mkdir(raw_dir)
        logging.warning('Raw files directory {} does not exit, creating new directory. '.format(raw_dir))

    for f in compact_files:
        _move(f, compact_dir, dry_run, copy)

    for f in raw_files:
        _move(f, raw_dir, dry_run, copy)
