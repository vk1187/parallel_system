import requests,json
from multiprocessing import Pool


app_url="api endpoint"
token= "xmdjndnndnnd"  #token
url = app_url + '/tx_Proposal_Document_Data/Harmonisation_Completed/'
files = requests.get(url, headers={'Authorization': 'Bearer '+token}, verify = False)
fileList = files.json()
json_obj = json.dumps(fileList, indent = 4)
with open('static/proposal-api-response.json', "w") as outfile:
    outfile.write(json_obj)
print("length of fileList : ",len(fileList))

jobs=[]

def apiInProposal():
    pass

pool = Pool(processes=40)

for x in fileList:
    result = pool.apply_async(apiInProposal, [x])
    jobs.append(result)

pool.close()
pool.join()
    
outputs = [j.get() for j in jobs]
return_dict,return_dict1, proposal_Processed = {},{}, []