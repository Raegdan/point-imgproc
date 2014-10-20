workers = 8

libs = ['/home/point/core/lib']

domain = 'point.im'

imgproc_socket = 'tcp://127.0.0.1:16379'
cache_socket = 'tcp://127.0.0.1:16380'

queue_timeout = 5

cache_expire_max = 86400

avatars_path = '/home/point/img/a'
avatars_root = 'http://i.point.im/a'
avatar_sizes = [24, 40, 80, 280]

thumbnail_path = '/home/point/img/t'
thumbnail_size = [400, 300]

media_path = '/home/point/img/m'
media_root = '://i.point.im/m'
media_size = [1920, 1080]

upload_dir = '/home/point/upload'

proctitle_prefix = 'point'

logger = 'imgproc'
logfile = '/home/point/log/imgproc.log'
loglevel = 'info'

debug = False

try:
    from settings_local import *
except ImportError:
    pass

