#!/usr/bin/env bash

can_copy_grpc=true

display_help() {
  echo "
    usage: ./setup.sh [-d|-h]
    options:
      -d disable gRPC code from being copied to other repositories
      -h display help message
  "
}

while getopts ":dh" FLAG
do
  case $FLAG in
    d) can_copy_grpc=false;;
    h) display_help; exit 0;;
    \?) echo "ERROR: One or more options are not recognized by this script"; display_help; exit 1;;
  esac
done

buf generate prephouse
if [[ $can_copy_grpc = true ]]; then
  cp ./gen/python/prephouse_pb2_grpc.py ../backend/prephouse/prephouse_pb2_grpc.py
  cp ./gen/python/prephouse_pb2_grpc.py ../analyzer-engine/prephouse_pb2_grpc.py
  cp ./gen/python/prephouse_pb2.py ../backend/prephouse/prephouse_pb2.py
  cp ./gen/python/prephouse_pb2.py ../analyzer-engine/prephouse_pb2.py
fi
