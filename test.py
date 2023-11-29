import requests
import json
import pandas as pd
# url = 'https://www.communitybenefitinsight.org/api/get_hospitals.php'
# data = requests.get(url).text
# hospital_data = json.loads(data)
# attribute_names = list(hospital_data[0].keys())
# data = {}
# for attribute in attribute_names:
#     data[attribute] = [item[attribute] for item in hospital_data]
# df = pd.DataFrame.from_dict(data)
# df.to_csv('lmao.csv', index=False)
# single_data = {}
# single_data['hospital_id'] = []
# for id in range(1, 3492):
#     # single_data['hospital_id'].append(id)
#     new_url = 'https://www.communitybenefitinsight.org/api/get_hospital_data.php?hospital_id=' + str(id)
#     new_data = requests.get(new_url).text
#     print('-------------------')
#     print(new_data)
#     json_data = json.loads(new_data)
#     try:
#         attribute = list(json_data[0].keys())
#         for name in attribute:
#             single_data[name] = json_data[-1][name]
#     except:
#         json_data = ''

# df = pd.DataFrame.from_dict(single_data)
# df.to_csv('test.csv', index=False)

# new_url = 'https://www.communitybenefitinsight.org/api/get_hospital_data.php?hospital_id=2171'
# response = requests.get(new_url).text
# response_data = json.loads(response)
# attribute = list(response_data[0].keys())
# lmao = response_data[-1]['hospital_data_id']
# print(lmao)
