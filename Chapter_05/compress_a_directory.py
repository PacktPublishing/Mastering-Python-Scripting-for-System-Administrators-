from shutil import make_archive
import os
archive_name = os.path.expanduser(os.path.join('~', 'work1'))
root_dir = os.path.expanduser(os.path.join('~', '.ssh'))
make_archive(archive_name, 'gztar', root_dir)

