#say
class speakeasy:
    forward = {0:'zero'}
    forward[1] = 'one'
    forward[2] = 'two'
    forward[3] = 'three'
    forward[4] = 'four'
    forward[5] = 'five'
    forward[6] = 'six'
    forward[7] = 'seven'
    forward[8] = 'eight'
    forward[9] = 'nine'
    forward[10] = 'ten'
    forward[11] = 'eleven'
    forward[12] = 'twelve'
    forward[13] = 'thirteen'
    forward[14] = 'fourteen'
    forward[15] = 'fifteen'
    forward[16] = 'sixteen'
    forward[17] = 'seventeen'
    forward[18] = 'eighteen'
    forward[19] = 'ninteen'
    forward[20] = 'twenty'
    forward[30] = 'thirty'
    forward[40] = 'forty'
    forward[50] = 'fifty'
    forward[60] = 'sixty'
    forward[70] = 'seventy'
    forward[80] = 'eighty'
    forward[90] = 'ninety'
    def __init__(me):
        me.backward = {}
        for key in me.forward.keys():
            me.backward[me.forward[key]] = key
    def say(me, what):
        if what < 0 : return str(what)
        if what > 99: return str(what)
        if what < 21: return me.forward[what]
        digit = what %10
        tens = what - digit
        if digit == 0: return me.forward[tens]
        return me.forward[tens]+'-'+me.forward[digit]
    def unsay(me, what):
        x = what.split('-')
        s = 0
        for item in x:
            s += me.backward[item]
        return s
    def multiply_by_words( me, one, two):
        return(me.say(me.unsay(one)*me.unsay(two)))
    
