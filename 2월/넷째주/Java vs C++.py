from sys import stdin

def find_c_java(temp):
    result =''
    if '_' in temp:
        temp = temp.split('_')
        if '' in temp:
            return 'Error!'

        else:
            for tp in temp:
                if tp.lower() != tp:
                    return 'Error!'

                else:
                    result += tp[0].upper() + tp[1:]

        return result[0].lower() + result[1:]


    else:

        for i, tp in enumerate(temp):
            if '_' in tp or ( i==0 and ord(tp) >=65 and ord(tp) <= 90):
                return 'Error!'


            elif (ord(tp) >= 65 and ord(tp) <= 90) and i != 0:
                result += '_' + tp.lower()

            else:
                result += tp


        return result

temp = stdin.readline().strip()
print(find_c_java(temp))