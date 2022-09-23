from flask_frozen import Freezer
from app import app

import os
import boto3
from glob import glob

AWS_BUCKET = "tidbitstatistics.com"
BUILD_DIRECTORY = "app/build/"

app.config["FREEZER_REMOVE_EXTRA_FILES"] = False
freezer = Freezer(app)


if __name__ == "__main__":
    # errors.html doesn't copy over so have to do manually if updated
    freezer.freeze()

    all_files = []
    for root, directories, files in os.walk(BUILD_DIRECTORY, topdown=False):
        for name in files:
            if not name.endswith(".DS_Store"):
                all_files.append(os.path.join(root, name))

    s3 = boto3.resource("s3")

    bucket = s3.Bucket(AWS_BUCKET)

    def file_type_finder(file):  # can't find a more pythonic way to do this
        if file.endswith(".css"):
            return "text/css"
        elif file.endswith(".js"):
            return "text/javascript"
        elif file.endswith(".html"):
            return "text/html"
        elif file.endswith(".svg"):
            return "image/svg+xml"
        elif file.endswith(".woff"):
            return "application/font-woff"
        else:
            return ""

    file_names_and_types = {f: file_type_finder(f) for f in all_files}

    for file_name, file_type in file_names_and_types.items():
        bucket.upload_file(
            file_name,
            file_name.replace(BUILD_DIRECTORY, ""),
            ExtraArgs={"ContentType": file_type},
        )
        print(f'Uploaded {file_name} to {file_name.replace(BUILD_DIRECTORY, "")}')
