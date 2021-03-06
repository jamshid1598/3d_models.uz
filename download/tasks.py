from celery import shared_task
import os  
from zipfile import ZipFile, ZIP_DEFLATED


@shared_task
def get_zip_file(request, file_paths):

    # Folder name in ZIP archive which contains the above files
    # E.g [thearchive.zip]/somefiles/file2.txt
    # FIXME: Set this to something better
    zip_subdir = "somefiles"
    zip_filename = "%s.zip" % zip_subdir


    # The zip compressor
    zf = ZipFile(zip_filename, "w")

    for fpath in file_paths:
        # Calculate path for file in zip
        fdir, fname = os.path.split(fpath)
        zip_path = os.path.join(zip_subdir, fname)

        # Add file, at correct path
        zf.write(fpath, compress_type=ZIP_DEFLATED)

    # Must close zip for all contents to be written
    zf.close()