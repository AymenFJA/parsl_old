#!/usr/bin/env python3

import radical.pilot as rp


# ------------------------------------------------------------------------------
#
class RPEX_MPIWorker(rp.raptor.MPIWorker):
    '''
    This class provides the required functionality to execute work requests.
    In this simple example, the worker only implements a single call: `hello`.
    '''

    # --------------------------------------------------------------------------
    #
    def __init__(self, cfg):

        rp.raptor.MPIWorker.__init__(self, cfg)


class RPEX_Worker(rp.raptor.DefaultWorker):
    '''
    This class provides the required functionality to execute work requests.
    In this simple example, the worker only implements a single call: `hello`.
    '''

    # --------------------------------------------------------------------------
    #
    def __init__(self, cfg):

        rp.raptor.DefaultWorker.__init__(self, cfg)
