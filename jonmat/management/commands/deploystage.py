import mimetypes
from http.server import SimpleHTTPRequestHandler

import os
import glob
from django.conf import settings
from django.core.management import BaseCommand
import boto3
from boto3.s3.transfer import S3Transfer


class Command(BaseCommand):
    def _all_files(self):
        return glob.iglob(settings.DISTILL_DIR + '/**', recursive=True)

    def handle(self, *args, **options):
        session = boto3.session.Session(region_name='ap-northeast-2')
        client = session.client('s3', config=boto3.session.Config(signature_version='s3v4'))
        transfer = S3Transfer(client)

        for filename in self._all_files():
            if os.path.isdir(filename):
                continue

            _, ext = os.path.splitext(filename)
            mime = mimetypes.types_map.get(ext, 'text/html')

            relpath = os.path.relpath(filename, settings.DISTILL_DIR)
            print(relpath)
            transfer.upload_file(filename, 'jonmat2', relpath, extra_args={'ContentType': mime})
