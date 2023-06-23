from flask import Flask, request, jsonify
import logging
import os
from dotenv import load_dotenv
from azure.identity import DefaultAzureCredential
from azure.identity import EnvironmentCredential
from azure.identity import ClientSecretCredential
from azure.mgmt.compute import ComputeManagementClient
from azure.mgmt.network import NetworkManagementClient
from azure.mgmt.resource import ResourceManagementClient
from starvm import start_vm
from starvm import stop_vm
from gevent import pywsgi
from wol import wol
#region
# 创建日志记录器并设置日志级别
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

# 创建一个输出到控制台的处理程序
console_handler = logging.StreamHandler()
console_handler.setLevel(logging.INFO)

# 创建一个输出到文件的处理程序
file_handler = logging.FileHandler('/var/log/app.log')
file_handler.setLevel(logging.INFO)

# 创建日志格式
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
console_handler.setFormatter(formatter)
file_handler.setFormatter(formatter)

# 将处理程序添加到日志记录器
logger.addHandler(console_handler)
logger.addHandler(file_handler)
#endregion

subscription_id=os.environ.get('sub')
AZURE_CLIENT_ID=os.environ.get('client')
AZURE_TENANT_ID=os.environ.get('tenant')
AZURE_CLIENT_SECRET=os.environ.get('secret')

credential = ClientSecretCredential(AZURE_TENANT_ID, AZURE_CLIENT_ID, AZURE_CLIENT_SECRET)
compute_client = ComputeManagementClient(credential, subscription_id)

app = Flask(__name__)
app.logger.addHandler(file_handler)

auth = '/Love16by'
#POST区
@app.route(auth+'/startvm', methods=['POST'])
def process_start_post_request():
    if request.method == 'POST':
        json_data = request.json
        vm = json_data.get('VM')
        rg = json_data.get('RG')
#        data = request.get_data(as_text=True)   
    if start_vm(vm,rg,compute_client) == '1':
        response_data = {'message': 'Start VM successful'}
        return jsonify(response_data)
    else :
        response_data = {'message': 'Start VM failed'}
        return jsonify(response_data)
        
    
@app.route(auth+'/stopvm', methods=['POST'])
def process_stop_post_request():
    if request.method == 'POST':
        json_data = request.json
        vm = json_data.get('VM')
        rg = json_data.get('RG')
#        data = request.get_data(as_text=True)   
    if stop_vm(vm,rg,compute_client) == '1':
        response_data = {'message': 'stop VM successful'}
        return jsonify(response_data)
    else :
        response_data = {'message': 'stop VM failed'}
        return jsonify(response_data)

@app.route(auth+'/wol', methods=['POST'])
def process_wol_post_request():
    if request.method == 'POST':
        json_data = request.json
        mac = json_data.get('mac')
        return wol(mac)

@app.route(auth+'/sb', methods=['POST'])
def process_sb_post_request():
    if request.method == 'POST':
        json_data = request.json
        vm = json_data.get('VM')
        rg = json_data.get('RG')
        response_data = {'message': 'stop VM failed'}
        return jsonify(response_data)

#GET区

@app.route('/startvm/<param>', methods=['GET'])
def process_startvm_request(param):
    param_list = param.split('&')  # 将参数字符串拆分为列表
    vm = param_list[0]
    rg = param_list[1]
    return start_vm(vm,rg,compute_client)

@app.route('/stopvm/<param>', methods=['GET'])
def process_stop_request(param):
    param_list = param.split('&')  # 将参数字符串拆分为列表
    vm = param_list[0]
    rg = param_list[1]
    return stop_vm(vm,rg,compute_client)




    
if __name__ == '__main__':
    #app.run(host='0.0.0.0')
    server = pywsgi.WSGIServer(('0.0.0.0',9898),app)
    server.serve_forever()

