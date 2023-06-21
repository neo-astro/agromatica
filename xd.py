

# registro =  {
#             "_id": "648e5b3d46448fa5c63d3828",
#             "fecha": "2023-10-10",
#             "senHumedadAire": {"1": 40,"2":50 },
#             "senHumedadAgua": {"1": 40,"2":50 },
#             "senPh": {"1": 40,"2":50 },
#             "senCalidadAire": {"1": 40,"2":50 }
#         }

registro = {
        "data": [
             {
            "_id": "648e5b3d46448fa5c63d3828",
            "fecha": "2023-10-10",
            "senHumedadAire": {"1": 40,"2":50 },
            "senHumedadAgua": {"1": 40,"2":50 },
            "senPh": {"1": 40,"2":50 },
            "senCalidadAire": {"1": 40,"2":50 }
            }
          ]
        }

for dato in registro:
  for keyData in registro[dato][0]:
    if isinstance(registro[dato][0][keyData], dict):
      for valor in registro[dato][0][keyData]:
        print(registro[dato][0][keyData][valor] )
