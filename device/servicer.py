#! /usr/bin/env python

"""servicer.py class that provides service to generated events.

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
import event


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
class Servicer(object):
    """ Service tasks stored in a queue.
    """

    #--------------------------------------------------------------------------
    def __init__(self, queue, engine):
        self.queue  = queue
        self.engine = engine
        self.busy   = False
        self.logger = loggerator.getLoggerator('SERVICER')
        self.stats  = {'waitTime': [], 'waitQueue': []}

    #--------------------------------------------------------------------------
    def _startService(self):
        if not self.busy and self.queue.size():
            task = self.queue.pop()
            task.pop(self.queue, self.engine)
            self._waitStats(task)
            ev = event.Event('task:%s' % (task.name, ), task.time, self._endService, task)
            self.engine.addEvent(ev)
            self.busy = True
            #self.logger.info('Servicer : START : task : %s for %s' % (task.name, task.time))

    #--------------------------------------------------------------------------
    def _endService(self, task):
        self.busy = False
        #self.logger.info('Servicer : END : task : %s for %s' % (task.name, task.time))
        self.update()

    #--------------------------------------------------------------------------
    def start(self):
        self.queue.registerPushCb(self.update)
        self.update()

    #--------------------------------------------------------------------------
    def update(self):
        self._startService()

    #--------------------------------------------------------------------------
    def _waitStats(self, task):
        self.stats['waitTime'].append(task.waitTime())
        self.stats['waitQueue'].append(task.waitQueue())

    #--------------------------------------------------------------------------
    def reportStats(self):
        avgTaskWaitTime  = sum(self.stats['waitTime'])/len(self.stats['waitTime'])
        avgTaskQueueSize = sum(self.stats['waitQueue'])/len(self.stats['waitQueue'])
        self.logger.info('Servicer task average wait time is %s' % (avgTaskWaitTime, ))
        self.logger.info('Servicer task average queue size is %s' % (avgTaskQueueSize, ))


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
