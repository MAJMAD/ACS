from ACSLowLevel import *

ASTBitDesignators = {0:'#LEAD',3:'#DC',4:'#PEGREADY',5:'#MOVE',6: '#ACC',7:'#BUILDUP',8:'#VELLOCK',9:'#POSLOCK',
                    11:'#TRIGGER',16:'#NEWSEGM',17:'#STARV',18:'#ENCWARN',19:'#ENC2WARN',20:'#INRANGE',21:'#LCTICKLE',
                    22:'#LCMODUL',23:'#FOLLOWED',24:'#HOLD',25:'#INHOMING',26:'#DECOMPON',27:'#INSHAPE',29:'ENCPROC'}

def qAST(axis, bitdesignator):
    writeToACS(f'?AST({axis}).{bitdesignator}')
    status = recvall(1024)
    print(ASTBitDesignators[5])
    return status[9]

def qASTBitDesignator(bitdesignator):
    if


