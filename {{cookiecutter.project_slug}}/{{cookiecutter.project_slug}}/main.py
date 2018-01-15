import eel
import random
import pkg_resources

eel.init('web')


@eel.expose
def py_eel_version():
    return pkg_resources.get_distribution("eel").version


eel.start(
    'main.html',
    size=(640, 400),
    options={
        'mode': 'chrome-app',
        'host': 'localhost',
        'port': random.randint(49152, 65535),
        'chromeFlags': ['--incognito'],
    }
)
