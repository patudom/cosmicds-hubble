from numpy import isnan
from echo import CallbackProperty


from ...utils import age_in_gyr_simple
from cosmicds.config import register_tool
from cosmicds.tools import LineFitTool

@register_tool
class HubbleLineFitTool(LineFitTool):

    tool_id = 'hubble:linefit'
    active = CallbackProperty(False)

    def label(self, layer, line):
        slope = line.slope.value
        age = age_in_gyr_simple(slope)
        return 'Age: %.0f Gyr' % (age) if not isnan(slope) else None

    def activate(self):
        super().activate()
    
    def deactivate(self):
        super()._clear_lines()
