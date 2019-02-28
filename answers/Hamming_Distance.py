class Solution:
  def hammingDistance(self, x, y):
    xBin = bin(int(str(x),10))[2:];
    yBin = bin(int(str(y),10))[2:];
    length = max(len(xBin),len(yBin));
    xBin = xBin.zfill(length);
    yBin = yBin.zfill(length);
    num = 0;
    for i in range(length):
      if(xBin[i]!=yBin[i]):
        num += 1;
    return num;

