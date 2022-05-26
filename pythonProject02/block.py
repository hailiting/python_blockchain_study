import datetime
import hashlib
from message import  Message,InvalidMessage

class Block:
    def __init__(self, *args):
        self.messageList = []
        self.timestamp=None
        self.hash = None
        self.pre_hash=None
        if args:
            for arg in args:
                self.add_message(arg)
    def add_message(self, message):
        if len(self.messageList)>0:
            # print(self.messageList)
            message.link(self.messageList[-1])
        message.seal()
        message.validate()
        self.messageList.append(message)
    def link(self, block):
        self.pre_hash=block.hash
    def seal(self):
        self.timestamp=datetime.datetime.now()
        self.hash=self._hash_block()
    def _hash_block(self):
        return hashlib.sha256((str(self.pre_hash)+str(self.timestamp)+str(self.messageList[-1].hash)).encode("utf-8")).hexdigest()
    def validate(self):
        for i,message in enumerate(self.messageList):
            message.validate()
            if(i>0 and message.pre_hash != self.messageList[i-1].hash):
                print("sss---",i)
                raise  InvalidBlock("无效block, 第{}条交易记录已被修改".format(i)+str(self))
    def __repr__(self):
        return "block===>  hash: {}, pre_hash: {}, len:{}, timestamp:{},".format(self.hash, self.pre_hash, len(self.messageList), self.timestamp)

class InvalidBlock(Exception):
    def __init__(self, *args, **kargs):
        Exception.__init__(self, *args, **kargs)
if __name__ == "__main__":
    try:
        m1=Message("1")
        m2=Message("2")
        m3=Message("3")
        m4=Message("4")

        b1=Block(m1,m2,m3,m4)
        b1.seal()
        b1.validate()

        b2=Block(m4,m3)
        b2.link(b1)
        b2.seal()
        print(b2)
    except InvalidMessage as e:
        print(e)