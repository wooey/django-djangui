import shutil

from ..models import Script, DjanguiFile, DjanguiJob
from ..backend import utils

class FileCleanupMixin(object):
    def tearDown(self):
        for i in DjanguiFile.objects.all():
            utils.get_storage().delete(i.filepath.path)
        # delete job dirs
        for i in DjanguiJob.objects.all():
            shutil.rmtree(i.get_output_path())
        super(FileCleanupMixin, self).tearDown()

class ScriptFactoryMixin(object):
    def tearDown(self):
        for i in Script.objects.all():
            path = i.script_path.path
            utils.get_storage().delete(path)
            path += 'c' # handle pyc junk
            utils.get_storage().delete(path)
        super(ScriptFactoryMixin, self).tearDown()