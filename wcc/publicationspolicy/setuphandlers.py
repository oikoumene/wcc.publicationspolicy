from collective.grok import gs
from wcc.publicationspolicy import MessageFactory as _

@gs.importstep(
    name=u'wcc.publicationspolicy', 
    title=_('wcc.publicationspolicy import handler'),
    description=_(''))
def setupVarious(context):
    if context.readDataFile('wcc.publicationspolicy.marker.txt') is None:
        return
    portal = context.getSite()

    # do anything here
