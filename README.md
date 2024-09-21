# pytezos-crypto

This is a friendly fork of the `crypto` module from the [pytezos](https://github.com/baking-bad/pytezos) project, containing only the cryptographic utilities from the upstream repository, located at [pytezos/crypto](https://github.com/baking-bad/pytezos/tree/master/src/pytezos/crypto).

## Motivation

The purpose of this fork is to provide the cryptographic functionalities of `pytezos` while keeping dependencies to a minimum. The upstream project includes a large number of additional dependencies such as Jupyter Notebook which are unnecessary for those seeking only the cryptographic utilities. This fork extracts the core `crypto` functionality and eliminates non-essential dependencies.

## Approach

This project is not intended to diverge from the upstream. Please submit all proposed changes to the upstream project first, and only open Pull Requests here after those changes have been accepted upstream.

## Installation

```bash
pip install aleph-pytezos
```

## Dependencies

This fork only includes the essential cryptographic dependencies:

- `base58`
- `importlib-metadata`
- `mnemonic`
- `pynacl`
- `python-magic`
- `coincurve`
- `typing_extensions`
- `fastecdsa`
- `pysodium`

## Comparison with Upstream Dependencies

The upstream `pytezos` project has a much broader set of dependencies, supporting a variety of additional features beyond cryptography, including container management, CLI tools, and notebook integrations. Here is a breakdown of the differences:

### Dependencies in `pytezos-crypto` (this fork):
- `base58`
- `importlib-metadata`
- `mnemonic`
- `pynacl`
- `python-magic`
- `coincurve`
- `typing_extensions`
- `fastecdsa`
- `pysodium`

### Additional Dependencies in the Upstream Project:
- **Python version constraint**: `python >= 3.8.1`
- **CLI and utility dependencies**: 
  - `click`
  - `tqdm`
- **Development and container-related tools**: 
  - `docker`
  - `notebook`
  - `testcontainers`
- **Data manipulation and validation libraries**: 
  - `attrs`
  - `cattrs`
  - `jsonschema`
  - `simplejson`
  - `strict-rfc3339`
  - `tabulate`
- **Cryptography-related extensions**:
  - `cryptography`
  - `py-ecc`
  - `deprecation`
  - `ply`
- **Networking and API libraries**:
  - `requests`
  - `netstruct`
  - `python-dateutil`
- **Specialized serialization**:
  - `simple-bson`

The upstream project is suited for broader use cases such as Tezos contract management, testing, and development environments, which require additional dependencies. In contrast, `pytezos-crypto` focuses strictly on cryptographic functionalities, reducing complexity and improving performance for users needing only the core cryptographic tools.

## Usage

For usage details, refer to the [original pytezos documentation](https://github.com/baking-bad/pytezos). This fork maintains API compatibility for the `crypto` module while streamlining dependencies.

## License

This project follows the same license as the original `pytezos` project. See the [LICENSE](LICENSE) file for more details.
```
