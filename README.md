# Prephouse Protobuf (ph-protos)

## Summary

The protocol buffers for our gRPCs are consolidated in this repository. Rather than run `protoc` directly,
we utilize [Buf][buf] to compile the protocol buffers in a simple and standardized manner. The corresponding
gRPC code (messages, stubs and so on) are generated in the [gen](gen) folder under the respective programming
language (e.g., gen/python would contain the Python implementation of the gRPC) and can then be used in
the appropriate subsystems including the backend server and the analyzer engine.

Our gRPC services are currently only generated and supported in Python.

## Instructions

### Setup

1. Download and install [Buf][buf] and [pre-commit][pre-commit]
2. Run `buf generate`

### Development

- Run `buf lint` to check the proto files against linter rules
- Run `buf breaking --against .git#branch=main` to check for any breaking changes between your .proto
  files and the current HEAD of the local main branch
- Run `./update_protos.sh` when you make changes to any .proto file in this repository

> The `./update_protos.sh` script compiles the protocol buffers and, unless the -d option is set, copies over the
> gRPC code blocks to the places where they're expected to be used.

[buf]: https://docs.buf.build/installation
[pre-commit]: https://pre-commit.com/

## Code Style

With some exceptions, we are mostly following the default [Buf Style Guide][style-guide] which builds upon the Google
Style Guide. The exceptions can be found in the [buf.yaml](buf.yaml) file. The `buf lint` command checks the .proto
files against the rules in this style guide and is configured to run on the pre-commit hook.

[style-guide]: https://docs.buf.build/best-practices/style-guide
