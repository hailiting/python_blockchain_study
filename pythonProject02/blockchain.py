
from block import Block,InvalidBlock
from message import Message
from transaction import Transaction

class BlockCoin:
    def __init__(self):
        self.blocklist=[]
    def add_block(self, block):
        if len(self.blocklist)>0:
            # print("11----", block.hash, "0000", self.blocklist[-1].hash )
            block.pre_hash = self.blocklist[-1].hash
        # print(222)
        block.seal()
        block.validate()
        self.blocklist.append(block)
    def validate(self):
        print(len(self.blocklist))
        for i, block in enumerate(self.blocklist):
            print(str(block))
            try:
                block.validate()
            except InvalidBlock as e:
                raise  InvalidBlock("区块校验错误，区块索引{}".format(i))
    def __repr__(self):
        return "BlockCoin=====> {}".format(len(self.blocklist))

class InvalidBlockCoin(Exception):
    def __init__(self, *arg, **kargs):
        Exception.__init__(self, *arg, **kargs)

if __name__ == "__main__":
    try:
        t1 = Transaction("yincheng", "tanweinimei", 0.000001)
        t2 = Transaction("yincheng", "tanweinijie", 0.000002)
        t3 = Transaction("yincheng", "tanweinige", 0.000003)
        t4 = Transaction("yincheng", "tanweinidi", 0.000004)
        t5 = Transaction("yincheng", "tanweinidie", 0.000005)
        t6 = Transaction("yincheng", "tanweininiang", 0.000006)

        m1 = Message(t1)
        m2 = Message(t2)
        m3 = Message(t3)  # 交易记录
        m4 = Message(t4)  # 交易记录
        m5 = Message(t5)  # 交易记录
        m6 = Message(t6)  # 交易记录
        # 创建一个区块
        yin1 = Block(m1, m2)
        yin1.seal()

        yin2 = Block(m3, m4)
        yin2.seal()

        yin3 = Block(m5, m6)
        yin3.seal()


        # 创建一个区块链
        mydada = BlockCoin()  # 区块链
        mydada.add_block(yin1)  # 增加区块

        mydada.add_block(yin2)
        # print("line61: ----",yin2.pre_hash)
        mydada.add_block(yin3)
        # print("line63: ----",yin3.pre_hash)
        # 纂改区块
        # yin2.messagelist.append(m1)
        yin2.add_message(m1)
        # print("line66: ----", str(yin2))
        mydada.validate()  # 校验
        print(11111, mydada)
    except Exception as e:
        print(e)
