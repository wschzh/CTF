import hashlib


def Get_Mi(m_list, M):  # 获取所有的Mi
    M_list = []
    for mi in m_list:
        M_list.append(M // mi)
    return M_list


def Get_ei_list(M_list, m_list):  # 取所有的Mi的逆元
    ei_list = []
    for i in range(len(M_list)):
        ei_list.append(Get_ei(M_list[i], m_list[i])[0])
    return ei_list


def Get_ei(a, b):
    # 计算ei

    if 0 == b:
        x = 1;
        y = 0;
        q = a
        return x, y, q
    xyq = Get_ei(b, a % b)
    x = xyq[0];
    y = xyq[1];
    q = xyq[2]
    temp = x;
    x = y;
    y = temp - a // b * y
    return x, y, q


def crt(a_list, m_list):
    # 计算中国剩余定理，返回计算结果，m_list是被除数，a_list是余数
    M = 1  # M是所有mi的乘积
    for mi in m_list:
        M *= mi
    Mi_list = Get_Mi(m_list, M)
    Mi_inverse = Get_ei_list(Mi_list, m_list)
    x = 0
    for i in range(len(a_list)):  # 开始计算x
        x += Mi_list[i] * Mi_inverse[i] * a_list[i]
        x %= M
    return x

if __name__ == '__main__':
    ms = [284461942441737992421992210219060544764, 218436209063777179204189567410606431578, 288673438109933649911276214358963643204, 239232622368515797881077917549177081575, 206264514127207567149705234795160750411, 338915547568169045185589241329271490503, 246545359356590592172327146579550739141, 219686182542160835171493232381209438048]
    cs = [273520784183505348818648859874365852523, 128223029008039086716133583343107528289, 5111091025406771271167772696866083419, 33462335595116820423587878784664448439, 145377705960376589843356778052388633917, 128158421725856807614557926615949143594, 230664008267846531848877293149791626711, 94549019966480959688919233343793910003]
    print(crt(cs,ms))
    x = crt(cs,ms)
    flag = "flag{" + hashlib.sha256(str(x).encode()).hexdigest() + "}"
    print(flag)

# 4b93deeb