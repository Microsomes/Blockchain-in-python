import hashlib
import time



 
class Miner:

    #verified all zeros
    def verifyZero(self,count,hash):
        torVeri=False
        for l in range(0,count):
            if(hash[l]=="0"):
                torVeri=True
            else:
                return False
        return torVeri

    def hashit(self,msg):
        e=  msg.encode(encoding='UTF-8',errors='strict')
        m= hashlib.sha256(e).hexdigest()
        return m
    def verifyNonce(self,nonce,data,hash):
        h= hashit(data+str(nonce))
        print("old:",h)
        if h==hash:
            return True
        else:
            return False


    def verifiy(self,msg,difficulty):
        starttime= time.time()
        running= True
        nonce= 1
        while running:
            h= self.hashit(str(msg)+str(nonce))
            print(h)
            nonce+=1
            if self.verifyZero(difficulty,h):
                running=False
                endtime=time.time()
                print("--------res took",endtime-starttime,"seconds")
                return {
                    "nonce":nonce-1,
                    "hash":h,
                    "starttime":starttime,
                    "endtime":endtime,
                    "timetaken":endtime-starttime
                }

     


