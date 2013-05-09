# coding=utf-8

from ..packet import Packet
from ..proto import Proto
from ..flags import Flags

class Query(Packet):
    query = ""
    
    def getPayload(self):
        payload = bytearray()
        
        payload.extend(Proto.build_byte(Flags.COM_QUERY))
        payload.extend(Proto.build_eop_str(self.query))
        
        return payload
    
    @staticmethod
    def loadFromPacket(packet):
        obj = Query()
        proto = Proto(packet, 3)
        
        obj.sequenceId = proto.get_fixed_int(1)
        proto.get_filler(1)
        obj.query = proto.get_eop_str()
        
        return obj