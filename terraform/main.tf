terraform {
  required_providers {
    docker = {
      source  = "kreuzwerker/docker"
      version = "~> 3.0.0"
    }
  }
}

provider "docker" {
  host = "unix:///var/run/docker.sock"
}

resource "docker_image" "pyhack" {
  name         = "pyhack:latest"
   build {
     context    = "../"
     dockerfile = "Dockerfile"
   }
 }

resource "docker_container" "pyhack" {
  image = docker_image.pyhack.image_id
  name  = "pyhack"
  depends_on = [docker_image.pyhack]
  command = ["poetry", "run", "python", "src/nflai/app.py"]

  ports {
    internal = 5000
    external = 5000
  }
  env = [
    "PYTHONDONTWRITEBYTECODE=1",
    "COLORTERM=truecolor",
  ]
  volumes {
    host_path      = "/Users/andy/ws/projects/nflai/data"
    container_path = "/home/app/data"
  }
}
output "container_id" {
  value = docker_container.pyhack.id
}
