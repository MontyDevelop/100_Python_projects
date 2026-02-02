import datetime
import time

end_time = datetime.datetime(2026,2,3)

block_website_url = ["www.w3schools.com", "www.facebook.com"]

host_path = "C:/Windows/System32/drivers/etc/hosts"

redirect = "127.0.0.1"

while True:
    if datetime.datetime.now() < end_time:
        print("Start blocking process..")
        with open(host_path,'r+') as host_file:
            data = host_file.read()
            for site in block_website_url:
                if site not in data:
                    data.write(f"{redirect} {site}\n")
                else:
                    pass
    else:
        with open(host_path,'r+') as host_file:
            data = host_file.readlines()
            host_file.seek(0) # To make pointer in starting
            for line in data:
                if not any(site in line for site in block_website_url):
                    host_file.write(line)
            host_file.truncate()
        time.sleep(5)



