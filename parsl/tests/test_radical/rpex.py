import os
import sys
from parsl.config import Config
from parsl.executors import RadicalPilotExecutor

bulk_mode = False
cfg_file = 'rpex.cfg'

bulk = os.environ.get('RP_BULK', None)
mpi = os.environ.get('RP_MPI', None)

if bulk:
    bulk_mode = True
if mpi:
    cfg_file = 'rpex_mpi.cfg'

rpex_cfg = '{0}/{1}'.format(os.path.abspath(os.path.dirname(__file__)), cfg_file)

config = Config(
    executors=[RadicalPilotExecutor(rpex_cfg=rpex_cfg, bulk_mode=bulk_mode,
                                    resource='local.localhost', login_method='local',
                                    project='', partition='', walltime=30, managed=True, cores=16)])
