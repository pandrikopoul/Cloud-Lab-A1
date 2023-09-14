import requests


requests_data = {
    "notification_type": "OutOfRange",
    "researcher": "d.landau@uu.nl",
    "measurement_id": "1234",
    "experiment_id": "5678",
    "cipher_data": "D5qnEHeIrTYmLwYX.hSZNb3xxQ9MtGhRP7E52yv2seWo4tUxYe28ATJVHUi0J++SFyfq5LQc0sTmiS4ILiM0/YsPHgp5fQKuRuuHLSyLA1WR9YIRS6nYrokZ68u4OLC4j26JW/QpiGmAydGKPIvV2ImD8t1NOUrejbnp/cmbMDUKO1hbXGPfD7oTvvk6JQVBAxSPVB96jDv7C4sGTmuEDZPoIpojcTBFP2xA"
}


response = requests.post("http://localhost:3000/api/notify", json=requests_data)

if response.status_code == 200:
   
    print("Response from notification-service:")
    print(response.json())

    
    volume_path = "/usr/src/data/save_file_nt" #sys.argv[-1]
    with open(volume_path, "w") as file:
        file.write(response.text)

    print(f"Response saved to {volume_path}")

    exit(0)
else:
    print(f"Request to {service_url} failed with status code {response.status_code}")
    exit(1)
