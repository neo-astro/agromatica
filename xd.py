

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

# for dato in registro:
#   for keyData in registro[dato][0]:
#     if isinstance(registro[dato][0][keyData], dict):
#       for valor in registro[dato][0][keyData]:
#         print(registro[dato][0][keyData][valor] )


var = {
  "data": [
      {
          "_id": "648e5b3d46448fa5c63d3828",
          "fecha": "2023-10-10",
          "senHumedadAire": {"1": 40,"2":50 },
          "senHumedadAgua": {"1": 40,"2":50 },
          "senPh": {"1": 40,"2":50 },
          "senCalidadAire": {"1": 40,"2":50 }
      },
        {
          "_id": "648e5b3d46448fa5c63d3828",
          "fecha": "2023-10-12",
          "senHumedadAire": {"1": 40,"2":50 },
          "senHumedadAgua": {"1": 40,"2":50 },
          "senPh": {"1": 40,"2":50 },
          "senCalidadAire": {"1": 40,"2":50 }
      },
        {
          "_id": "648e5b3d46448fa5c63d3828",
          "fecha": "2023-10-11",
          "senHumedadAire": {"1": 40,"2":50 },
          "senHumedadAgua": {"1": 40,"2":50 },
          "senPh": {"1": 40,"2":50 },
          "senCalidadAire": {"1": 40,"2":50 }
      }
  ]
}

config = {
    'distancia': [3,7,11,15,19,23,27,31,35,39,43,47,51,55,59,63,67,71,75,79,83,87,91,95]  
}


var['data'].append(config)
print(var)