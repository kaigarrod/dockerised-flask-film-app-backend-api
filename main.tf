terraform {
  required_providers {
    digitalocean = {
      source  = "digitalocean/digitalocean"
      version = "~> 2.0"
    }
  }
}


provider "digitalocean" {}

resource "digitalocean_droplet" "web" {
  image   = "ubuntu-22-04-x64"
  name    = "film-1"
  region  = "lon1"
  size    = "s-1vcpu-1gb"

  ssh_keys = ["3c:4b:c3:3f:eb:fb:a2:8a:f5:7d:80:3f:a5:a5:46:79"]

user_data = <<-EOF
#!/bin/bash
exec > /var/log/user-data.log 2>&1
apt update -y
apt install -y docker.io docker-compose-v2 git
systemctl start docker
systemctl enable docker
cd /root
git clone https://github.com/kaigarrod/dockerised-flask-film-app-backend-api.git
cd dockerised-flask-film-app-backend-api
docker compose up -d --build
EOF

}

output "ip-address" {
    value = digitalocean_droplet.web.ipv4_address
}