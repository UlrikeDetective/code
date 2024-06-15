import urllib.request

def get_public_ip():
    url = 'https://ipv4.icanhazip.com'
    try:
        with urllib.request.urlopen(url) as response:
            ip = response.read().decode('utf-8').strip()
        return ip
    except Exception as e:
        print(f"Error retrieving public IP: {e}")
        return None

if __name__ == "__main__":
    public_ip = get_public_ip()
    if public_ip:
        print("Password/Endpoint IP for localtunnel is:", public_ip)
    else:
        print("Could not retrieve public IP.")
