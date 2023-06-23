import os
from dotenv import load_dotenv
from azure.identity import DefaultAzureCredential
from azure.mgmt.compute import ComputeManagementClient
from azure.mgmt.network import NetworkManagementClient
from azure.mgmt.resource import ResourceManagementClient

def start_vm(VM,RG,compute_client):
    async_vm_start=compute_client.virtual_machines.begin_start(RG, VM)
    async_vm_start.wait()
    return '1'

def stop_vm(VM,RG,compute_client):
    async_vm_start=compute_client.virtual_machines.begin_deallocate(RG, VM)
    async_vm_start.wait()
    return '1'