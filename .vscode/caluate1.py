'''
纤维弹性模量计算
'''
def volum_fraction(r_1, s_0):
    v_0 = (r_1 ** 2 ) / (r_1 + s_0) ** 2

    return v_0 
i = 0
while True:
    S_00 = input('氧化层厚度')
    R_1 = 6.5#纤维半径
    S_0 = float(S_00)

    V_0 = volum_fraction(R_1, S_0)#纤维体积分数
    V_1 = 1 - V_0#基体体积分数
    
    E_00 = 245 * V_0 + 70 * V_1#弹性模量计算
    E_0 = str(E_00)
    
    print('氧化层厚度为' + S_00 + '的纤维弹性模量为' + E_0)
    
    i += 1

    if i >= 7:
        break

    


