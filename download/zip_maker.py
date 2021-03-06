
import os
import zipfile
try:
    from StringIO import StringIO
except ImportError:
    from io import StringIO

from django.http import HttpResponse
from django.conf import settings

# def zip_maker(filenames):
#     zip_subdir = str(settings.MEDIA_ROOT)
#     zip_filename = "%s.zip" % zip_subdir

#     s = StringIO()

#     zf = zipfile.ZipFile(s, "w")

#     for fpath in filenames:
#         fdir, fname = os.path.split(fpath)
#         zip_path = os.path.join(zip_subdir, fname)

#         zf.write(fpath, zip_path)

#     zf.close()

#     resp = HttpResponse(s.getvalue(), mimetype = "application/x-zip-compressed")
#     resp['Content-Disposition'] = 'attachment; filename=%s' % zip_filename

#     return resp




from io import BytesIO

def zip_maker(filelist):
    byte_data = BytesIO()
    zip_file = zipfile.ZipFile(byte_data, "w")

    for file in filelist:
        filename = os.path.basename(os.path.normpath(file))
        zip_file.write(file, filename)
    zip_file.close()

    response = HttpResponse(byte_data.getvalue(), content_type='application/zip')
    response['Content-Disposition'] = 'attachment; filename=files.zip'

    zip_file.printdir()

    return response

# file:///home/jamshid/Instant%20Company/3D%20Marketing/3d_model_backend_raximjon_aka/3d_models/media/3D_File/2021/02/25/IMG_20180131_235840_953_2.jpg
# file:///home/jamshid/Instant%20Company/3D%20Marketing/3d_model_backend_raximjon_aka/3d_models/media_root/3D_File/2021/02/25/IMG_20180131_235840_953_2.jpg