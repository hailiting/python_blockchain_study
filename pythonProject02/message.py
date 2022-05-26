import datetime
import hashlib
class Message:
    def __init__(self, data):
        self.hash = None
        self.pre_hash = None
        self.timestamp=datetime.datetime.now()
        self.data = data
        self.payload_hash=self._hash_payload()

    def _hash_payload(self):
        return hashlib.sha256((str(self.timestamp)+str(self.data)).encode("utf-8")).hexdigest()
    def _hash_message(self):
        return hashlib.sha256((str(self.pre_hash)+str(self.payload_hash)).encode("utf-8")).hexdigest()
    def seal(self):
        self.hash = self._hash_message()
    def validate(self):
        # 0889e1150a97070ec55eb4e434999cb20e7d84a27fb6399fc8845a12a5b0e29f
        # 1bb1648ea6d35a4b665fadba6a2b44fd29cf82c164f8270b1dded068d33e1ec5
        if self.payload_hash != self._hash_payload():
            raise InvalidMessage("111 交易数据或时间被修改-----"+str(self))
        if self.hash != self._hash_message():
            raise InvalidMessage("2222 交易的哈希链接被修改-----"+str(self))
        return "数据正常"+str(self)
    def link(self, Message):
        self.pre_hash = Message.hash
    def __repr__(self):
        return "hash: {}, prev_hash: {}, data:{}, timestamp:{}".format(self.hash, self.pre_hash, self.data, self.timestamp)


class InvalidMessage(Exception):
    def __init__(self, *args, **kwargs):
        Exception.__init__(self, *args, **kwargs)

if __name__ == "__main__":
    try:
        m1=Message("DDD")
        m1.seal()

        m2=Message("aaa")
        m2.link(m1)
        m2.seal()

        m3 = Message("aaa")
        m3.link(m2)
        m3.seal()
        m3.validate()

        # m2.data="9999";
        m2 = Message("999")
        m2.link(m1)
        m2.seal()
        # m1.validate()
        m2.validate()
        # m3.validate()
    except InvalidMessage as e:
        print(e)
