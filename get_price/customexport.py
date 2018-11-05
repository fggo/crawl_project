import os

from scrapy.extensions.feedexport import FileFeedStorage


class OverwriteFileFeedStorage(FileFeedStorage):
    """prevent scrapy from appending texts to output.json, instead it overwrites
    https://github.com/scrapy/scrapy/blob/master/scrapy/extensions/feedexport.py#L79
    """
    def open(self, spider):
        dirname = os.path.dirname(self.path)
        if dirname and not os.path.exists(dirname):
            os.makedirs(dirname)
        return open(self.path, 'wb')