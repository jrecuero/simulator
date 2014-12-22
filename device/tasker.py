#! /usr/bin/env python

"""tasker.py class keeps information for a task to be executed by a servicer.

:author:    Jose Carlos Recuero
:version:   0.1
:since:     12/09/2014

"""

__docformat__ = 'restructuredtext en'

###############################################################################
##  _                            _
## (_)_ __ ___  _ __   ___  _ __| |_ ___
## | | '_ ` _ \| '_ \ / _ \| '__| __/ __|
## | | | | | | | |_) | (_) | |  | |_\__ \
## |_|_| |_| |_| .__/ \___/|_|   \__|___/
##             |_|
###############################################################################
#
# import std python modules
#

#
# import engine python modules
#
import loggerator


###############################################################################
##
##   ___ ___  _ __  ___| |_ __ _ _ __ | |_ ___
##  / __/ _ \| '_ \/ __| __/ _` | '_ \| __/ __|
## | (_| (_) | | | \__ \ || (_| | | | | |_\__ \
##  \___\___/|_| |_|___/\__\__,_|_| |_|\__|___/
##
###############################################################################
#

###############################################################################
##            _                     _   _
##  ___ _   _| |__  _ __ ___  _   _| |_(_)_ __   ___  ___
## / __| | | | '_ \| '__/ _ \| | | | __| | '_ \ / _ \/ __|
## \__ \ |_| | |_) | | | (_) | |_| | |_| | | | |  __/\__ \
## |___/\__,_|_.__/|_|  \___/ \__,_|\__|_|_| |_|\___||___/
##
###############################################################################
#


###############################################################################
##       _                     _       __ _       _ _   _
##   ___| | __ _ ___ ___    __| | ___ / _(_)_ __ (_) |_(_) ___  _ __  ___
##  / __| |/ _` / __/ __|  / _` |/ _ \ |_| | '_ \| | __| |/ _ \| '_ \/ __|
## | (__| | (_| \__ \__ \ | (_| |  __/  _| | | | | | |_| | (_) | | | \__ \
##  \___|_|\__,_|___/___/  \__,_|\___|_| |_|_| |_|_|\__|_|\___/|_| |_|___/
##
###############################################################################
#

#
#------------------------------------------------------------------------------
class Tasker(object):
    """ Keeps information for a given task to be executed by a servicer.
    """

    #--------------------------------------------------------------------------
    def __init__(self, name, time):
        self.name = name
        self.time = time
        self.stats = {'pushedAt': None,
                      'popedAt': None,
                      'tasksAtPush': None,
                      'tasksAtPop': None}
        self.logger = loggerator.getLoggerator('TASKER')

    #--------------------------------------------------------------------------
    def push(self, queue, engine):
        self.stats['tasksAtPush'] = queue.size()
        self.stats['pushedAt']    = engine.getSimTime()
        #self.logger.info('task pushed at %s' % (self.stats['pushedAt'], ))

    #--------------------------------------------------------------------------
    def pop(self, queue, engine):
        self.stats['tasksAtPop'] = queue.size()
        self.stats['popedAt']    = engine.getSimTime()
        #self.logger.info('task poped at %s' % (self.stats['popedAt'], ))

    #--------------------------------------------------------------------------
    def waitTime(self):
        return self.stats['popedAt'] - self.stats['pushedAt']

    #--------------------------------------------------------------------------
    def waitQueue(self):
        return self.stats['tasksAtPop']


###############################################################################
##                  _
##  _ __ ___   __ _(_)_ __
## | '_ ` _ \ / _` | | '_ \
## | | | | | | (_| | | | | |
## |_| |_| |_|\__,_|_|_| |_|
##
###############################################################################
#
if __name__ == '__main__':
    import doctest
    doctest.testmod()
