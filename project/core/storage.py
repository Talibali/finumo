import os


def upload_to(instance, filename):
    """Upload dynamically to define a custom path structure\
    Media directory: media/{company_id}/{type_of_media}/fileName
    """
    return os.path.join('media', filename.lower())


def profile_photo_path(instance, filename):
    """ file will be uploaded to MEDIA_ROOT/user/<id>/profile_photo/<filename> """
    return 'user/{0}/profile/{1}'.format(instance.id, filename)