#!/usr/bin/env bash


#Hello world examples
curl http://localhost:5000/hello/ | jq .

curl http://localhost:5000/hello/Bob/ | jq .

# Relationship examples
curl http://localhost:5000/hello/?name=Bob | jq .

curl http://localhost:5000/related/Bob/ | jq .

# Full example
# Get All Posts
curl http://localhost:5000/api/post/ | jq .

# Create Post
curl -H "Content-Type: application/json" -X POST -d '{"username":"xyz","post_text":"xyz"}' http://localhost:5000/api/post/ | jq .

# Get Individual
curl http://localhost:5000/api/post/1/ | jq .

curl -H "Content-Type: application/json" -X POST -d '{"username":"xyz","comment_text":"This is my comment"}' http://localhost:5000/api/post/1/create_comment/ | jq .
