import paver
from paver.easy import *
import paver.setuputils
paver.setuputils.install_distutils_tasks()
import os, sys
import pkg_resources
from runestone.server import get_dburl
from sphinxcontrib import paverutils

sys.path.append(os.getcwd())

home_dir = os.getcwd()
master_url = 'http://127.0.0.1:8000'
master_app = 'runestone'
serving_dir = "./build/testpoll"
dest = "../../static"

options(
    sphinx = Bunch(docroot=".",),

    build = Bunch(
        builddir="./build/testpoll",
        sourcedir="_sources",
        outdir="./build/testpoll",
        confdir=".",
        project_name = "testpoll",
        template_args={'course_id': 'testpoll',
                       'login_required':'false',
                       'appname':master_app,
                       'loglevel': 0,
                       'course_url':master_url,
                       'use_services': 'false',
                       'python3': 'false',
                       'dburl': '', 'downloads_enabled': 'true', 'enable_chatcodes': 'false', 'allow_pairs': 'false',
                       'basecourse': 'testpoll'
                        }
    )
)
version = pkg_resources.require("runestone")[0].version
options.build.template_args['runestone_version'] = version

# If DBURL is in the environment override dburl
options.build.template_args['dburl'] = get_dburl(outer=locals())

from runestone import build  # build is called implicitly by the paver driver.
