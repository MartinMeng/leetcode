class Solution(object):
  def largestMultipleOfThree(self, d):
    """
    :type digits: List[int]
    :rtype: str
    """
    d1 = sorted([d[i] for i in range(0, len(d)) if d[i]%3==1])
    d2 = sorted([d[i] for i in range(0, len(d)) if d[i]%3==2])
    d3 = [d[i] for i in range(0, len(d)) if d[i]%3==0]
    tot = sum(d)
    if tot % 3 == 1:
        if len(d1) > 0:
            d = d1[1:]+d2+d3
        elif len(d2) > 1:
            d = d1+d2[2:]+d3
        else: return '0'
    if tot % 3 == 2:
        if len(d2) > 0:
            d = d1+d2[1:]+d3
        elif len(d1) > 1:
            d = d1[2:]+d2+d3
        else: return '0'
    if len(d) == 0: return ''
    if sum(d) == 0: return '0'

    d = sorted(d)[::-1]
    return ''.join(map(str, d))

