import os
import zipfile
try:
    from StringIO import StringIO
except ImportError:
    from io import StringIO

from django.http import HttpResponse
from django.conf import settings


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