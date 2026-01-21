output "cluster_name" {
  value = aws_eks_cluster.eks.name
}

output "cluster_endpoint" {
  value = aws_eks_cluster.eks.endpoint
}

output "ecr_repository_url" {
  value = aws_ecr_repository.fastapi.repository_url
}

output "private_subnets" {
  value = aws_subnet.private[*].id
}
