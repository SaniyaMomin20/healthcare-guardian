resource "aws_s3_bucket" "healthcare" {
  bucket = "healthcare-guardian-demo-12345"
  acl    = "public-read"
}
