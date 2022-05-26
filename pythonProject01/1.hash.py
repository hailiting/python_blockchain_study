import hashlib
import datetime
class DaDaBlockCoin:
  def __init__(self, index, timestamp, data, next_hash):
      self.index=index
      self.timestamp=timestamp
      self.data=data
      self.next_hash=next_hash;
      self.selfhash=self.hash_DaDaBlockCoin(); # 自身hash

  def hash_DaDaBlockCoin(self):
    sha=hashlib.md5()
    datastr=str(self.index)+str(self.timestamp)+str(self.data)+str(self.next_hash) # 对数据整体加密
    sha.update(datastr.encode("utf-8"))
    return sha.hexdigest()

# 创世区块
def create_first_DaDaBlock():
  return DaDaBlockCoin(0, datetime.datetime.now(),"Lover Dar", "0123adf123")

def create_money_DaDaBlock(last_block):
  this_index = last_block.index+1
  this_timestamp = datetime.datetime.now()
  this_data = "this is data" + str(this_index)
  this_next_hash = last_block.selfhash
  return DaDaBlockCoin(this_index,this_timestamp,this_data, this_next_hash)

DaDaBlcokCoins =[create_first_DaDaBlock()]
nums=10
head_block=DaDaBlcokCoins[0];
print(head_block.index,head_block.timestamp,head_block.selfhash,head_block.next_hash)
for i in range(nums):
  dadaBlock_add = create_money_DaDaBlock(head_block)
  DaDaBlcokCoins.append(dadaBlock_add)
  head_block = dadaBlock_add
  print(dadaBlock_add.index,dadaBlock_add.timestamp,dadaBlock_add.selfhash,dadaBlock_add.next_hash)