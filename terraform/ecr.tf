resource "aws_ecr_repository" "fastapi" {
  name = "fastapi-app"

  image_scanning_configuration {
    scan_on_push = true
  }
}
