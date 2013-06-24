from collective.grok import gs
from plonegovmy.policy import MessageFactory as _

@gs.importstep(
    name=u'plonegovmy.policy', 
    title=_('plonegovmy.policy import handler'),
    description=_(''))
def setupVarious(context):
    if context.readDataFile('plonegovmy.policy.marker.txt') is None:
        return
    portal = context.getSite()

    # do anything here
