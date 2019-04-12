#!/usr/bin/env python
# coding=UTF-8
'''
@Description: COMP7405 Assignment 3
@Author: CJJ
@LastEditors: Cai Jiajun
@Date: 2019-04-02 17:12:19
@LastEditTime: 2019-04-11 16:43:12
'''

from flask import Flask, url_for, render_template
from flask import request, jsonify
from OptionCalculation import *

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('hello.html')

@app.route('/bs', methods=['POST','GET'])
def cal_bs():
    if request.method == 'POST':
        
        print("recevie data")
        
        s = float(request.form.get('bs_s'))
        print(s)
        vol = float(request.form.get('bs_vol'))
        print(vol)
        k = float(request.form.get('bs_k'))
        print(k)
        r = float(request.form.get('bs_r'))
        print(r)
        t = float(request.form.get('bs_t'))
        print(t)
        option_type = request.form.get('bs_type')
        print(option_type)
        #data = s+" "+vol+" "+k+" "+r+" "+t+" "+option_type

        data_para = {
            'S': s,
            'K': k,
            't': t,
            'r': r,
            'vol': vol,
            'type': option_type
        }

        OC = OptionCalculation()
        data = "%.4f"%float(OC.BSFormulas(other_para = data_para))

        print("return data")
        return data, 201
    
@app.route('/imp', methods=['POST','GET'])
def cal_imp():
    if request.method == 'POST':
        
        print("recevie data")
        
        s = float(request.form.get('imp_s'))
        print(s)
        q = float(request.form.get('imp_q'))
        print(q)
        value = float(request.form.get('imp_value'))
        print(value)
        k = float(request.form.get('imp_k'))
        print(k)
        r = float(request.form.get('imp_r'))
        print(r)
        t = float(request.form.get('imp_t'))
        print(t)
        option_type = request.form.get('imp_type')
        print(option_type)
        #data = s+" "+vol+" "+k+" "+r+" "+t+" "+option_type

        data_para = {
            'S': s,
            'K': k,
            'value':value,
            't': t,
            'r': r,
            'q': q,
            'type': option_type
        }

        OC = OptionCalculation()
        data = "%.4f"%float(OC.ImpVol(other_para = data_para))

        print("return data")
        return data, 201

@app.route('/cfs', methods=['POST','GET'])
def cfs_bs():
    if request.method == 'POST':
        
        print("recevie data")
        
        s = float(request.form.get('cfs_s'))
        print(s)
        vol = float(request.form.get('cfs_vol'))
        print(vol)
        N = float(request.form.get('cfs_N'))
        print(N)
        k = float(request.form.get('cfs_k'))
        print(k)
        r = float(request.form.get('cfs_r'))
        print(r)
        t = float(request.form.get('cfs_t'))
        print(t)
        option_type = request.form.get('cfs_type')
        print(option_type)
        #data = s+" "+vol+" "+k+" "+r+" "+t+" "+option_type

        data_para = {
            'S': s,
            'K': k,
            'T': t,
            'r': r,
            'sigma': vol,
            'n': N,
            'type': option_type
        }

        OC = OptionCalculation()
        data = "%.4f"%float(OC.ClosedFormFormulas(other_para = data_para))

        print("return data")
        return data, 201

@app.route('/cfb', methods=['POST','GET'])
def cfb_bs():
    if request.method == 'POST':
        
        print("recevie data")
        
        s1 = float(request.form.get('cfb_s1'))
        print(s1)
        s2 = float(request.form.get('cfb_s2'))
        print(s2)
        vol1 = float(request.form.get('cfb_vol1'))
        print(vol1)
        vol2 = float(request.form.get('cfb_vol2'))
        print(vol2)
        rho = float(request.form.get('cfb_rho'))
        print(rho)
        k = float(request.form.get('cfb_k'))
        print(k)
        r = float(request.form.get('cfb_r'))
        print(r)
        t = float(request.form.get('cfb_t'))
        print(t)
        option_type = request.form.get('cfb_type')
        print(option_type)
        #data = s+" "+vol+" "+k+" "+r+" "+t+" "+option_type

        data_para = {
            'K': k,
            'S': [s1,s2],
            't': t,
            'r': r,
            'sigma': [vol1,vol2],
            'rho': [rho],
            'type': option_type
        }

        OC = OptionCalculation()
        data = "%.4f"%float(OC.ClosedFormForBasketOption(other_para = data_para))

        print("return data")
        return data, 201

@app.route('/mca', methods=['POST','GET'])
def mca_bs():
    if request.method == 'POST':
        
        print("recevie data")
        
        s = float(request.form.get('mca_s'))
        print(s)
        vol = float(request.form.get('mca_vol'))
        print(vol)
        N = int(request.form.get('mca_N'))
        print(N)
        I = int(request.form.get('mca_I'))
        print(I)
        k = float(request.form.get('mca_k'))
        print(k)
        r = float(request.form.get('mca_r'))
        print(r)
        t = float(request.form.get('mca_t'))
        print(t)
        option_type = request.form.get('mca_type')
        print(option_type)
        c_v = request.form.get('mca_c_v')
        print(c_v)
        #data = s+" "+vol+" "+k+" "+r+" "+t+" "+option_type

        data_para = {
            'S': s,
            'K': k,
            'T': t,
            'r': r,
            'sigma': vol,
            'n': N,
            'type': option_type,
            'I': I,
            'c_v': c_v
        }

        OC = OptionCalculation()
        data = (OC.MonteCarloAsianOption(other_para = data_para))
        return_data = "[ Price ]: "+"%.4f    "%data['Price']+"[ 95% Confidence Interval ]: "+"%.4f"%data['95% Confidence Interval'][0]+"~"+"%.4f"%data['95% Confidence Interval'][1]

        print("return data")
        return return_data, 201

@app.route('/mcb', methods=['POST','GET'])
def mcb_bs():
    if request.method == 'POST':
        
        print("recevie data")
        
        s1 = float(request.form.get('mcb_s1'))
        print(s1)
        s2 = float(request.form.get('mcb_s2'))
        print(s2)
        vol1 = float(request.form.get('mcb_vol1'))
        print(vol1)
        vol2 = float(request.form.get('mcb_vol2'))
        print(vol2)
        I = int(request.form.get('mcb_I'))
        print(I)
        k = float(request.form.get('mcb_k'))
        print(k)
        r = float(request.form.get('mcb_r'))
        print(r)
        t = float(request.form.get('mcb_t'))
        print(t)
        rho = float(request.form.get('mcb_rho'))
        print(t)
        option_type = request.form.get('mcb_type')
        print(option_type)
        c_v = request.form.get('mcb_c_v')
        print(c_v)
        #data = s+" "+vol+" "+k+" "+r+" "+t+" "+option_type

        data_para = {
            'S': [s1,s2],
            'K': k,
            'T': t,
            'r': r,
            'sigma': [vol1,vol2],
            'rho': [rho],
            'type': option_type,
            'I': I,
            'c_v': c_v
        }

        OC = OptionCalculation()
        data = (OC.MonteCarloBasketOption(other_para = data_para))
        return_data = "[ Price ]: "+"%.4f    "%data['Arith_Price']+"[ 95% Confidence Interval ]: "+"%.4f"%data['95% Confidence Interval'][0]+"~"+"%.4f"%data['95% Confidence Interval'][1]

        print("return data")
        return return_data, 201



@app.route('/bt', methods=['POST','GET'])
def bt_bs():
    if request.method == 'POST':
        
        print("recevie data")
        
        s = float(request.form.get('bt_s'))
        print(s)
        vol = float(request.form.get('bt_vol'))
        print(vol)
        N = int(request.form.get('bt_N'))
        print(N)
        k = float(request.form.get('bt_k'))
        print(k)
        r = float(request.form.get('bt_r'))
        print(r)
        t = float(request.form.get('bt_t'))
        print(t)
        option_type = request.form.get('bt_type')
        print(option_type)
        #data = s+" "+vol+" "+k+" "+r+" "+t+" "+option_type

        data_para = {
            'S': s,
            'K': k,
            'T': t,
            'r': r,
            'vol': vol,
            'N': N,
            'type': option_type
        }

        OC = OptionCalculation()
        data = "%.4f"%float(OC.BinomialTreeAmericanOption(other_para = data_para))

        print("return data")
        return data, 201

if __name__ == "__main__":
    app.run()

