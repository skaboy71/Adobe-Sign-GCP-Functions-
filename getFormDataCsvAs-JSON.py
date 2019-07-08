import requests
import pandas as pd
from io import StringIO as sio
import json

def get_csv_json(request):
    """
    This function uses the data passed in an HTTP post to the google function endpoint.
    Example JSON Body for POST:
    
    {
	
	"shard": "na2",
	"token": "3AAABLblqZhD7gPDMJ5vjNsKg*** Your API Token Here ***2WqAsaG1oYtllVLaHv9e",
	"ag_id": "CBJCHBCAAB*** Your V5 or V6 agreement ID here ***hgcVEyj-oI",
	"s_email": "senders-email@yourdomain.com"
	
    }
    
    It makes the call to the Adobe Sign API V6 using the python "requests" module to get the form data as CSV.
    It then converts the csv formatted string to JSON using the pandas and JSON libraries and returns it.
    This was initially done for use in Microsoft Flow, but it could be used anywhere that can ingest the form data as JSON.
    """
    request_json = request.get_json()
    if request.args and 'message' in request.args:
        return request.args.get('message')
    elif request_json and 'message' in request_json:
        return request_json['message']
    elif request_json and 'shard' and 'token' and 'ag_id' and 's_email' in request_json:
        _shard = request_json['shard']
        _token = request_json['token']
        _ag_id = request_json['ag_id']
        _s_email = request_json['s_email']
        # set base URL
        base_url = 'https://api.' + _shard + '.echosign.com/api/rest/v6'
        if _shard and _token and _ag_id and _s_email :
            base_url = 'https://api.' + _shard + '.echosign.com/api/rest/v6'
            fData_url = base_url + '/agreements/' + _ag_id + '/formData'
            headers = {
                "Authorization": "Bearer " + _token,
                "x-api-user": "email:" + _s_email,
                "Content-Type": "application/json"
                    }      
            response1 = requests.get(fData_url, headers=headers)
            csvData = sio(response1.text)
            record = pd.read_csv(csvData)
            jsonData = record.to_json(orient='records')
            jsonObject = json.loads(jsonData)
            prettyJson = json.dumps(jsonObject)
            
        return prettyJson
    else:
        return f"Where's all the data??"
